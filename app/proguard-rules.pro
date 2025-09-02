proguard
# Proguard rules for Hotjar, ActiveX, and Shockwave/Sizzle (interpret with caution)

# Hotjar (Assuming this is for a library that interacts with Hotjar or similar analytics)
# If you are using a specific Hotjar SDK, refer to its documentation for specific Proguard rules.
# The following are generic examples and might need adjustment.
-keep class com.hotjar.** { *; }
-dontwarn com.hotjar.**

# ActiveX (Highly unlikely to be relevant for modern Android Proguard)
# ActiveX is a Microsoft technology primarily for Internet Explorer.
# If you have a very specific library trying to interface with something ActiveX-related
# via a WebView, you would need to identify the specific classes.
# This is a placeholder and likely not needed:
# -keep class com.example.activex.** { *; }
# -dontwarn com.example.activex.**

# Shockwave / Sizzle (Likely related to WebView content)
# If you are using Sizzle.js within a WebView and need to interface with it
# from Java/Kotlin, you might need rules for your JavaScriptInterface.
# The existing rule for com.google.swiper serves as an example of how to keep JavaScript interface classes.
# If Sizzle is used purely within the WebView's JavaScript context, Proguard rules for it are not directly applicable
# to the Sizzle library itself, but rather to any Android classes that might interact with it.

# Example: If you have a JavaScript interface for Sizzle interactions
# -keepclassmembers class com.example.SizzleInterface {
#    public *;
# }

# General keep rules for Javascript Interfaces if you're interacting with these technologies in a WebView
-keepattributes JavascriptInterface

# Keep any classes annotated with @Keep (often used by libraries to indicate they should not be obfuscated)
-keep @androidx.annotation.Keep class * {*;}
-keepclasseswithmembers class * {
    @androidx.annotation.Keep <fields>;
}
-keepclasseswithmembers class * {
    @androidx.annotation.Keep <methods>;
}
