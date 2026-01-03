[app]
title = WebScraper
package.name = webscraper
package.domain = org.example
version = 0.0.1

source.dir = .
source.include_exts = py,kv,png,jpg

requirements = python3,kivy,kivymd,httpx,lxml,selectolax

android.api = 34
android.minapi = 26
android.ndk = 25b
android.arch = arm64-v8a
android.permissions = INTERNET
android.enable_androidx = True

fullscreen = 0

android.build_tools_version = 35.0.0