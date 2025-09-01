import time
import random

# --- Mock Craigslist Posting Algorithm ---

class JobPosting:
    def __init__(self, title, company, location, description, keywords, post_date):
        self.id = random.randint(1000, 9999)
        self.title = title
        self.company = company
        self.location = location
        self.description = description
        self.keywords = set(k.lower() for k in keywords) # Store keywords in lowercase for easier matching
        self.post_date = post_date
        self.relevance_score = 0 # Will be calculated during search

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Title: {self.title}\n"
                f"Company: {self.company}\n"
                f"Location: {self.location}\n"
                f"Posted: {time.strftime('%Y-%m-%d', self.post_date)}\n"
                f"Description: {self.description[:100]}...\n" # Show a snippet
                f"Relevance: {self.relevance_score:.2f}\n"
                f"--------------------")

class CraigslistAggregator:
    def __init__(self):
        self.postings = []
        self._generate_mock_postings()

    def _generate_mock_postings(self):
        """Generates some sample job postings."""
        # More realistic posting times
        now = time.time()
        one_day_ago = now - (24 * 60 * 60)
        three_days_ago = now - (3 * 24 * 60 * 60)
        one_week_ago = now - (7 * 24 * 60 * 60)

        self.postings.extend([
            JobPosting("Software Engineer", "Tech Solutions Inc.", "San Francisco, CA", "Develop cutting-edge software applications.", ["python", "java", "backend", "developer"], time.gmtime(one_day_ago)),
            JobPosting("Data Analyst", "Analytics Corp.", "New York, NY", "Analyze large datasets to provide insights.", ["sql", "python", "data", "analysis"], time.gmtime(three_days_ago)),
            JobPosting("Web Developer", "Creative Designs LLC", "Remote", "Build responsive and user-friendly websites.", ["html", "css", "javascript", "frontend"], time.gmtime(now)),
            JobPosting("Marketing Specialist", "Growth Hackers Co.", "Austin, TX", "Develop and execute marketing campaigns.", ["marketing", "seo", "social media"], time.gmtime(one_week_ago)),
            JobPosting("Customer Support Representative", "HelpDesk Pro", "Chicago, IL", "Assist customers with inquiries and issues.", ["customer service", "support"], time.gmtime(one_day_ago)),
            JobPosting("Python Developer (Junior)", "Startup Innovate", "San Francisco, CA", "Join our team to build new features using Python.", ["python", "django", "junior"], time.gmtime(now)),
            JobPosting("Project Manager", "BuildIt Right", "New York, NY", "Lead and manage software development projects.", ["project management", "agile"], time.gmtime(three_days_ago)),
        ])

    def _calculate_relevance(self, posting, search_terms):
        """
        Mock algorithm for calculating relevance.
        - Keyword matches in title, description, and tags are important.
        - More recent posts are generally more relevant.
        """
        score = 0
        search_terms_lower = [term.lower() for term in search_terms]

        # Keyword matching in title (higher weight)
        for term in search_terms_lower:
            if term in posting.title.lower():
                score += 3
            if term in posting.keywords:
                score += 2
            if term in posting.description.lower():
                score += 1

        # Recency bonus (simple version)
        time_since_post = time.time() - time.mktime(posting.post_date)
        if time_since_post < (24 * 60 * 60): # Less than a day old
            score += 2
        elif time_since_post < (3 * 24 * 60 * 60): # Less than 3 days old
            score += 1

        posting.relevance_score = score
        return score

    def search_jobs(self, search_query):
        """Simulates searching for jobs based on a query."""
        search_terms = search_query.lower().split()
        print(f"\nSearching for jobs matching: '{search_query}'")
        print("Algorithm: Prioritizing keyword matches in title, tags, and description, with a bonus for recent posts.\n")

        # Calculate relevance for each posting
        for posting in self.postings:
            self._calculate_relevance(posting, search_terms)

        # Sort by relevance (descending) and then by post date (descending)
        # The primary sort is relevance, secondary is recency for tie-breaking
        # or when relevance scores are very close.
        sorted_postings = sorted(
            self.postings,
            key=lambda p: (p.relevance_score, time.mktime(p.post_date)),
            reverse=True
        )

        return [p for p in sorted_postings if p.relevance_score > 0] # Return only relevant postings

# --- Job Seeker Simulation ---

def job_seeker_experience(aggregator):
    print("Welcome, Job Seeker!")
    while True:
        search_query = input("Enter your job search query (e.g., 'python developer san francisco') or 'quit': ")
        if search_query.lower() == 'quit':
            print("Exiting job search. Good luck!")
            break

        results = aggregator.search_jobs(search_query)

        if results:
            print(f"Found {len(results)} relevant job postings:\n")
            for posting in results:
                print(posting)
        else:
            print("No job postings found matching your query. Try a different search.\n")

if __name__ == "__main__":
    craigslist_sim = CraigslistAggregator()
    job_seeker_experience(craigslist_sim)
