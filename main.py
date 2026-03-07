import requests
import time
from concurrent.futures import ThreadPoolExecutor

targets = [
    "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "ns2", "ns3",
    "web", "cpanel", "whm", "autodiscover", "autoconfig", "admin", "administrator",
    "dev", "development", "stage", "staging", "test", "testing", "qa", "uat",
    "prod", "production", "sandbox", "beta", "alpha", "demo", "old", "new",
    "api", "api-v1", "api-v2", "api-v3", "rest", "graphql", "gw", "gateway",
    "blog", "shop", "store", "forum", "support", "help", "docs", "portal",
    "login", "secure", "auth", "sso", "vpn", "remote", "ssh", "connect",
    "int", "internal", "intranet", "corp", "hr", "it", "staff", "employee", "admin-panel",
    "db", "sql", "mysql", "oracle", "redis", "elastic", "kibana", "grafana",
    "monitor", "monitoring", "metrics", "stats", "status", "logs", "syslog",
    "cdn", "static", "assets", "media", "img", "images", "video", "s3", "cloud",
    "m", "mobile", "app", "ios", "android", "tv", "ws", "chat", "msg",
    "git", "gitlab", "github", "svn", "hg", "jira", "confluence", "wiki",
    "backup", "backups", "archive", "storage", "files", "download", "downloads",
    "billing", "pay", "payment", "checkout", "cart", "invoice", "finance",
    "marketing", "sales", "crm", "erp", "partner", "partners", "affiliate",
    "mail2", "mx", "mx1", "mx2", "pop3", "imap", "newsletter", "campaign",
    "vpn1", "vpn2", "fw", "firewall", "router", "switch", "pbx", "voip", "sip",
    "calendar", "events", "meet", "video", "conference", "booking", "reservations",
    "go", "link", "url", "short", "track", "tracking", "click", "analytics"
]
found = []
website = input("Enter domain (example.com): ")

start = time.perf_counter()

def scan_directory(path):
    url = "https://" + path + "." + website
    try:
        response = requests.get(url)
        found.append(url)
    except:
        pass

with ThreadPoolExecutor(max_workers=150) as executor:
    executor.map(scan_directory, targets)

end = time.perf_counter()

if len(found)>0:
    print("Total subdomains found:", len(found))

if len(found)>0:
    print("Scanned", len(targets),"subdomains in", round(end-start,3), "seconds")