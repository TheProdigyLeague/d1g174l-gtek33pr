import time
import random
import uuid # For generating mock API keys

# --- Mock Data ---

MOCK_DATABASES = {
    "Google LLC (Global HQ)": {
        "type": "Business",
        "hq_location": "Mountain View, CA, USA",
        "ip_address": "172.217.160.142", # Example public IP
        "mock_api_key": f"gapi_mock_{uuid.uuid4().hex[:20]}",
        "server_environment": {
            "web_server": "Google Web Server (GWS) - Simulated",
            "database_backend": "Spanner / Bigtable (Simulated)",
            "primary_language": "C++, Java, Python, Go",
            "ssl_cli_tool": "gcert (Simulated Google Internal Cert Tool)",
            "sql_tls_interface": "Cloud SQL Proxy with TLS (Simulated)"
        },
        "mock_api_endpoints": {
            "user_data_v1": "example.google.com/api/v1/users/profiles/...",
            "analytics_v3": "example.google.com/api/v3/analytics/reports/..."
        },
        "mock_users": {
            "user123": {"role": "Viewer", "password_hint": "common_pw_abc"},
            "admin_g": {"role": "Administrator", "password_hint": "complex_P@$$wOrd"},
            "service_acc_1": {"role": "Service", "password_hint": "auto_generated_token"}
        }
    },
    "Amazon Web Services (Global Infrastructure)": {
        "type": "Business",
        "hq_location": "Seattle, WA, USA",
        "ip_address": "52.95.110.1", # Example AWS IP
        "mock_api_key": f"aws_mock_{uuid.uuid4().hex[:20]}",
        "server_environment": {
            "web_server": "Nginx / Elastic Load Balancer (Simulated)",
            "database_backend": "Amazon RDS (PostgreSQL/MySQL), DynamoDB (Simulated)",
            "primary_language": "Java, Ruby, Python",
            "ssl_cli_tool": "AWS Certificate Manager CLI (Simulated)",
            "sql_tls_interface": "RDS IAM Auth + SSL (Simulated)"
        },
        "mock_api_endpoints": {
            "s3_objects_v2": "s3.amazonaws.com/your-bucket/objects/...",
            "ec2_instances_v1": "ec2.amazonaws.com/api/v1/instances/..."
        },
        "mock_users": {
            "dev_user_01": {"role": "Developer", "password_hint": "my_dev_pass"},
            "ops_manager": {"role": "Operator", "password_hint": "SecureOps!23"}
        }
    },
    "U.S. Census Bureau (Federal Agency)": {
        "type": "Government",
        "hq_location": "Suitland, MD, USA",
        "ip_address": "146.150.1.5", # Hypothetical
        "mock_api_key": f"uscbg_mock_{uuid.uuid4().hex[:20]}",
        "server_environment": {
            "web_server": "Apache Tomcat / IIS (Simulated)",
            "database_backend": "Oracle Database / SQL Server (Simulated)",
            "primary_language": "Java, .NET",
            "ssl_cli_tool": "OpenSSL CLI (Simulated)",
            "sql_tls_interface": "JDBC/ODBC with TLS (Simulated)"
        },
        "mock_api_endpoints": {
            "population_data_v1.2": "api.census.gov/data/2023/pep/population?get=...",
            "economic_indicators_v2": "api.census.gov/data/timeseries/eits/..."
        },
        "mock_users": {
            "researcher_smith": {"role": "Data Analyst", "password_hint": "statStrong"},
            "data_entry_clerk": {"role": "Clerk", "password_hint": "entryPass1"}
        }
    },
    "European Central Bank (Financial Institution)": {
        "type": "Government/Financial",
        "hq_location": "Frankfurt, Germany",
        "ip_address": "193.109.214.10", # Hypothetical
        "mock_api_key": f"ecb_mock_{uuid.uuid4().hex[:20]}",
        "server_environment": {
            "web_server": "SAP NetWeaver / JBoss (Simulated)",
            "database_backend": "SAP HANA / DB2 (Simulated)",
            "primary_language": "ABAP, Java",
            "ssl_cli_tool": "keytool (Java) / Sapgenpse (Simulated)",
            "sql_tls_interface": "Secure Network Communications (SNC) for SAP (Simulated)"
        },
        "mock_api_endpoints": {
            "exchange_rates_daily": "sdw-wsrest.ecb.europa.eu/service/data/EXR/D...",
            "monetary_policy_stats": "sdw-wsrest.ecb.europa.eu/service/data/BSI/..."
        },
        "mock_users": {
            "analyst_mueller": {"role": "Financial Analyst", "password_hint": "EuroSecure#24"},
            "audit_team_lead": {"role": "Auditor", "password_hint": "AuditPass!ECB"}
        }
    }
}

# --- Helper Functions ---

def display_title():
    print("=" * 60)
    print("      Mock Enterprise & Government Database Simulator")
    print("          (For Educational & Demonstration Purposes Only)")
    print("=" * 60)
    print()

def list_databases():
    print("Available Mock Datasets:")
    for i, name in enumerate(MOCK_DATABASES.keys()):
        db_type = MOCK_DATABASES[name]["type"]
        print(f"  {i+1}. {name} ({db_type}) - HQ: {MOCK_DATABASES[name]['hq_location']}")
    print()

def choose_database():
    while True:
        try:
            list_databases()
            choice = input("Enter the number of the dataset to load (or 'quit'): ")
            if choice.lower() == 'quit':
                return None
            choice_num = int(choice)
            if 1 <= choice_num <= len(MOCK_DATABASES):
                # Return the name of the chosen database
                return list(MOCK_DATABASES.keys())[choice_num - 1]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        print()

def display_db_info(db_name, db_data):
    print("-" * 40)
    print(f"Details for: {db_name}")
    print(f"  Type: {db_data['type']}")
    print(f"  HQ Location: {db_data['hq_location']}")
    print(f"  Simulated IP Address: {db_data['ip_address']}")
    print(f"  Mock API Key: {db_data['mock_api_key']}")
    print("  Simulated Server Environment:")
    for key, value in db_data['server_environment'].items():
        print(f"    {key.replace('_', ' ').title()}: {value}")
    print("-" * 40)
    print()

def simulate_api_interaction(db_name, db_data):
    print(f"\n--- Simulating API Interaction for {db_name} ---")
    if not db_data['mock_api_endpoints']:
        print("No mock API endpoints defined for this dataset.")
        return

    print("Available Mock API Endpoints:")
    endpoints = list(db_data['mock_api_endpoints'].items())
    for i, (name, path) in enumerate(endpoints):
        print(f"  {i+1}. {name} ({path})")

    while True:
        try:
            choice = input("Choose an API endpoint number to 'call' (or 'back'): ")
            if choice.lower() == 'back':
                return
            endpoint_num = int(choice)
            if 1 <= endpoint_num <= len(endpoints):
                chosen_endpoint_name, chosen_endpoint_path = endpoints[endpoint_num-1]
                print(f"\n  Mock 'calling' API: {chosen_endpoint_path}")
                print("  Simulating API request...")
                time.sleep(random.uniform(0.5, 1.5))
                print(f"  Mock Response from '{chosen_endpoint_name}':")

                # Simulate different types of responses based on endpoint name
                if "user" in chosen_endpoint_name.lower() or "profile" in chosen_endpoint_name.lower():
                    print("  {")
                    print("    \"status\": \"success\",")
                    print("    \"data\": [")
                    for user, details in list(db_data['mock_users'].items())[:2]: # Show a couple of users
                        print(f"      {{ \"username\": \"{user}\", \"role\": \"{details['role']}\", \"access_level\": \"mock_data_only\" }},")
                    print("      ...")
                    print("    ]")
                    print("  }")
                    print("  (Simulated: Database information such as user123 | admin | psswd would be part of a real, secured response)")

                    # Simulate login for a specific user
                    if db_data['mock_users']:
                        first_user = list(db_data['mock_users'].keys())[0]
                        login_choice = input(f"  Simulate login for '{first_user}'? (yes/no): ").lower()
                        if login_choice == 'yes':
                            print(f"  Attempting mock login for '{first_user}'...")
                            time.sleep(1)
                            print(f"  Password hint for '{first_user}': {db_data['mock_users'][first_user]['password_hint']}")
                            mock_pass = input(f"  Enter mock password for {first_user}: ")
                            if mock_pass == db_data['mock_users'][first_user]['password_hint']: # Simple check
                                print(f"  SUCCESS: Mock session started for '{first_user}'. You now have simulated '{db_data['mock_users'][first_user]['role']}' access.")
                            else:
                                print("  FAILURE: Mock login incorrect.")
                elif "analytic" in chosen_endpoint_name.lower() or "report" in chosen_endpoint_name.lower():
                    print("  {")
                    print("    \"report_id\": \"" + uuid.uuid4().hex[:12] + "\",")
                    print("    \"status\": \"completed\",")
                    print("    \"data_points\": " + str(random.randint(1000, 5000)) + ",")
                    print("    \"generated_at\": \"" + time.strftime("%Y-%m-%dT%H:%M:%SZ") + "\"")
                    print("  }")
                else:
                    print("  { \"message\": \"Mock data successfully retrieved.\", \"items_count\": " + str(random.randint(5,50)) + " }")
                print()
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        print()


def simulate_server_interaction(db_name, db_data):
    print(f"\n--- Simulating Server Interaction for {db_name} ---")
    ip = db_data['ip_address']
    env = db_data['server_environment']

    print(f"  Target IP: {ip}")
    print("  Simulated Server Interfaces:")
    print(f"    1. Web Server Interface ({env['web_server']})")
    print(f"    2. SSL/TLS CLI ({env['ssl_cli_tool']})")
    print(f"    3. SQL/Database TLS Interface ({env['database_backend']} via {env['sql_tls_interface']})")
    print()

    while True:
        choice = input("  Choose an interface to 'connect' to (1-3, or 'back'): ")
        if choice.lower() == 'back':
            return

        if choice == '1':
            print(f"\n  [{ip}]: Connecting to Web Server ({env['web_server']})...")
            time.sleep(1)
            print(f"  [{env['web_server']}]: Welcome! Mock HTTP/S session established.")
            print(f"  [{env['web_server']}]: Available simulated actions: 'status', 'logs', 'config'")
            while True:
                server_cmd = input(f"  [{env['web_server']}]> ").lower()
                if server_cmd == 'status':
                    print(f"  [{env['web_server']}]: Status: Running, CPU: {random.randint(10,70)}%, Memory: {random.randint(30,80)}% (Simulated)")
                elif server_cmd == 'logs':
                    print(f"  [{env['web_server']}]: Tailing mock logs...")
                    for i in range(3):
                        time.sleep(0.5)
                        print(f"  [{env['web_server']}]: {time.strftime('%H:%M:%S')} - Mock log entry {random.randint(100,999)}: Request from {random.randint(1,254)}.{random.randint(1,254)}...")
                elif server_cmd == 'config':
                    print(f"  [{env['web_server']}]: Displaying mock config: vHost: example.com, Port: 443, SSL: Enabled (Simulated)")
                elif server_cmd == 'exit':
                    print(f"  [{env['web_server']}]: Disconnecting from web server interface.")
                    break
                else:
                    print(f"  [{env['web_server']}]: Unknown command '{server_cmd}'. Try 'status', 'logs', 'config', or 'exit'.")
            break # Exit server choice loop
        elif choice == '2':
            print(f"\n  [{ip}]: Initiating SSL/TLS CLI ({env['ssl_cli_tool']})...")
            time.sleep(1)
            print(f"  [{env['ssl_cli_tool']}]: Mock SSL/TLS utility ready.")
            print(f"  [{env['ssl_cli_tool']}]: Example commands: 'list_certs', 'check_expiry example.com'")
            while True:
                ssl_cmd_full = input(f"  [{env['ssl_cli_tool']}]# ").lower()
                ssl_cmd_parts = ssl_cmd_full.split()
                ssl_cmd = ssl_cmd_parts[0] if ssl_cmd_parts else ""

                if ssl_cmd == 'list_certs':
                    print(f"  [{env['ssl_cli_tool']}]: Simulating certificate list:")
                    print(f"    - CN=*.{db_name.split()[0].lower()}.com, Expiry: {random.randint(2024, 2025)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}")
                    print(f"    - CN=internal.api.local, Expiry: {random.randint(2024, 2025)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}")
                elif ssl_cmd == 'check_expiry' and len(ssl_cmd_parts) > 1:
                    target_host = ssl_cmd_parts[1]
                    print(f"  [{env['ssl_cli_tool']}]: Checking mock SSL expiry for {target_host}... Valid until {random.randint(2024, 2025)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}.")
                elif ssl_cmd == 'exit':
                    print(f"  [{env['ssl_cli_tool']}]: Exiting SSL/TLS utility.")
                    break
                else:
                    print(f"  [{env['ssl_cli_tool']}]: Unknown command or invalid parameters. Try 'list_certs', 'check_expiry <hostname>', or 'exit'.")
            break # Exit server choice loop
        elif choice == '3':
            db_type = env['database_backend'].split()[0] # e.g., Spanner, MariaDB, Oracle
            print(f"\n  [{ip}]: Connecting to {db_type} via {env['sql_tls_interface']}...")
            time.sleep(1)
            print(f"  [{db_type}]: Mock secure SQL/NoSQL session established with TLS.")
            print(f"  [{db_type}]: Example queries: 'SELECT * FROM mock_users_table LIMIT 5;', 'SHOW DATABASES;'")
            print(f"  [{db_type}]: Simulating live user session view (read-only):")
            active_users = list(db_data['mock_users'].keys())
            if active_users:
                print(f"    Active mock user: '{random.choice(active_users)}' running 'SELECT query_id, query_text FROM information_schema.processlist WHERE user != \"system_user\" ' (Simulated)")
            else:
                print("    No active mock user sessions to display currently.")

            while True:
                sql_cmd = input(f"  [{db_type}_SQL_TLS]> ").strip()
                if sql_cmd.lower() == 'exit':
                    print(f"  [{db_type}]: Closing SQL/TLS session.")
                    break
                elif sql_cmd:
                    print(f"  [{db_type}]: Simulating execution of: {sql_cmd}")
                    time.sleep(0.5)
                    if "select" in sql_cmd.lower() and "mock_users_table" in sql_cmd.lower():
                        print("    username | role          | last_login_mock")
                        print("    ---------|---------------|------------------")
                        for user, details in list(db_data['mock_users'].items())[:3]:
                            print(f"    {user:<8} | {details['role']:<13} | {time.strftime('%Y-%m-%d %H:%M')}")
                    elif "show databases" in sql_cmd.lower():
                        print("    Database_Name_Mock")
                        print("    ------------------")
                        print("    main_app_db")
                        print("    user_profiles_db")
                        print("    audit_logs_db")
                    else:
                        print(f"  [{db_type}]: Mock query executed. (No actual data retrieved or changed)")
                else:
                    pass # Allow empty input to re-prompt
            break # Exit server choice loop
        else:
            print("  Invalid choice for server interface.")
        print()


# --- Main Program Logic ---
def main():
    display_title()

    while True:
        chosen_db_name = choose_database()

        if chosen_db_name is None: # User chose to quit from DB selection
            break

        db_data = MOCK_DATABASES[chosen_db_name]
        display_db_info(chosen_db_name, db_data)

        while True: # Loop for choosing vector
            print(f"Choose a vector to run against '{chosen_db_name}':")
            print("  1. Run API (Simulate API interaction and user login)")
            print("  2. Run Server (Simulate server/CLI interaction)")
            print("  3. Choose another dataset")
            print("  4. Quit")
            vector_choice = input("> ")
            print()

            if vector_choice == '1':
                simulate_api_interaction(chosen_db_name, db_data)
            elif vector_choice == '2':
                simulate_server_interaction(chosen_db_name, db_data)
            elif vector_choice == '3':
                break # Go back to database selection
            elif vector_choice == '4' or vector_choice.lower() == 'quit':
                print("Exiting program.")
                return # Exit main function, thus program
            else:
                print("Invalid vector choice. Please try again.")
            print() # Extra newline for readability

    print("Exiting program.")

if __name__ == "__main__":
    main()
