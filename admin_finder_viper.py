import requests
from concurrent.futures import ThreadPoolExecutor
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
import sys
import time

# List of common admin page paths
ADMIN_PATHS = [
    # Basic admin paths
    "admin", "admin/login", "adminpanel", "administrator", "wp-admin",
    "wp-login", "login", "dashboard", "controlpanel", "manager", "admin.php",
    "admin.aspx", "admin.html", "admin.cgi", "admin_area", "admin123",
    "admin_area/login", "admin_login", "admin1", "admin2", "admin3",
    "admin4", "admin5", "admin6", "admin7", "admin8", "admin9", "admin10",

    # Numbered admin paths
    "admin11", "admin12", "admin13", "admin14", "admin15", "admin16",
    "admin17", "admin18", "admin19", "admin20", "admin21", "admin22",
    "admin23", "admin24", "admin25", "admin26", "admin27", "admin28",
    "admin29", "admin30", "admin31", "admin32", "admin33", "admin34",
    "admin35", "admin36", "admin37", "admin38", "admin39", "admin40",
    "admin41", "admin42", "admin43", "admin44", "admin45", "admin46",
    "admin47", "admin48", "admin49", "admin50", "admin51", "admin52",
    "admin53", "admin54", "admin55", "admin56", "admin57", "admin58",
    "admin59", "admin60", "admin61", "admin62", "admin63", "admin64",
    "admin65", "admin66", "admin67", "admin68", "admin69", "admin70",
    "admin71", "admin72", "admin73", "admin74", "admin75", "admin76",
    "admin77", "admin78", "admin79", "admin80", "admin81", "admin82",
    "admin83", "admin84", "admin85", "admin86", "admin87", "admin88",
    "admin89", "admin90", "admin91", "admin92", "admin93", "admin94",
    "admin95", "admin96", "admin97", "admin98", "admin99", "admin100",

    # Backup and old admin paths
    "admin_backup", "admin_old", "admin_new", "admin_test", "admin_temp",
    "admin_dev", "admin_prod", "admin_live", "admin_staging", "admin_secure",
    "admin_private", "admin_public", "admin_archive", "admin_legacy", "admin_old1",
    "admin_old2", "admin_old3", "admin_old4", "admin_old5", "admin_old6",
    "admin_old7", "admin_old8", "admin_old9", "admin_old10",

    # Admin area paths
    "admin_area1", "admin_area2", "admin_area3", "admin_area4", "admin_area5",
    "admin_area6", "admin_area7", "admin_area8", "admin_area9", "admin_area10",
    "admin_area11", "admin_area12", "admin_area13", "admin_area14", "admin_area15",
    "admin_area16", "admin_area17", "admin_area18", "admin_area19", "admin_area20",
    "admin_area21", "admin_area22", "admin_area23", "admin_area24", "admin_area25",
    "admin_area26", "admin_area27", "admin_area28", "admin_area29", "admin_area30",
    "admin_area31", "admin_area32", "admin_area33", "admin_area34", "admin_area35",
    "admin_area36", "admin_area37", "admin_area38", "admin_area39", "admin_area40",
    "admin_area41", "admin_area42", "admin_area43", "admin_area44", "admin_area45",
    "admin_area46", "admin_area47", "admin_area48", "admin_area49", "admin_area50",
    "admin_area51", "admin_area52", "admin_area53", "admin_area54", "admin_area55",
    "admin_area56", "admin_area57", "admin_area58", "admin_area59", "admin_area60",
    "admin_area61", "admin_area62", "admin_area63", "admin_area64", "admin_area65",
    "admin_area66", "admin_area67", "admin_area68", "admin_area69", "admin_area70",
    "admin_area71", "admin_area72", "admin_area73", "admin_area74", "admin_area75",
    "admin_area76", "admin_area77", "admin_area78", "admin_area79", "admin_area80",
    "admin_area81", "admin_area82", "admin_area83", "admin_area84", "admin_area85",
    "admin_area86", "admin_area87", "admin_area88", "admin_area89", "admin_area90",
    "admin_area91", "admin_area92", "admin_area93", "admin_area94", "admin_area95",
    "admin_area96", "admin_area97", "admin_area98", "admin_area99", "admin_area100",

    # Admin area backup and old paths
    "admin_area_backup", "admin_area_old", "admin_area_new", "admin_area_test",
    "admin_area_temp", "admin_area_dev", "admin_area_prod", "admin_area_live",
    "admin_area_staging", "admin_area_secure", "admin_area_private", "admin_area_public",
    "admin_area_archive", "admin_area_legacy", "admin_area_old1", "admin_area_old2",
    "admin_area_old3", "admin_area_old4", "admin_area_old5", "admin_area_old6",
    "admin_area_old7", "admin_area_old8", "admin_area_old9", "admin_area_old10",

    # Admin login paths
    "admin/login", "admin_area/login", "adminpanel/login", "administrator/login",
    "wp-admin/login", "wp-login.php", "login/admin", "dashboard/login", "controlpanel/login",
    "manager/login", "admin1/login", "admin2/login", "admin3/login", "admin4/login",
    "admin5/login", "admin6/login", "admin7/login", "admin8/login", "admin9/login",
    "admin10/login", "admin11/login", "admin12/login", "admin13/login", "admin14/login",
    "admin15/login", "admin16/login", "admin17/login", "admin18/login", "admin19/login",
    "admin20/login", "admin21/login", "admin22/login", "admin23/login", "admin24/login",
    "admin25/login", "admin26/login", "admin27/login", "admin28/login", "admin29/login",
    "admin30/login", "admin31/login", "admin32/login", "admin33/login", "admin34/login",
    "admin35/login", "admin36/login", "admin37/login", "admin38/login", "admin39/login",
    "admin40/login", "admin41/login", "admin42/login", "admin43/login", "admin44/login",
    "admin45/login", "admin46/login", "admin47/login", "admin48/login", "admin49/login",
    "admin50/login", "admin51/login", "admin52/login", "admin53/login", "admin54/login",
    "admin55/login", "admin56/login", "admin57/login", "admin58/login", "admin59/login",
    "admin60/login", "admin61/login", "admin62/login", "admin63/login", "admin64/login",
    "admin65/login", "admin66/login", "admin67/login", "admin68/login", "admin69/login",
    "admin70/login", "admin71/login", "admin72/login", "admin73/login", "admin74/login",
    "admin75/login", "admin76/login", "admin77/login", "admin78/login", "admin79/login",
    "admin80/login", "admin81/login", "admin82/login", "admin83/login", "admin84/login",
    "admin85/login", "admin86/login", "admin87/login", "admin88/login", "admin89/login",
    "admin90/login", "admin91/login", "admin92/login", "admin93/login", "admin94/login",
    "admin95/login", "admin96/login", "admin97/login", "admin98/login", "admin99/login",
    "admin100/login", "admin_backup/login", "admin_old/login", "admin_new/login",
    "admin_test/login", "admin_temp/login", "admin_dev/login", "admin_prod/login",
    "admin_live/login", "admin_staging/login", "admin_secure/login", "admin_private/login",
    "admin_public/login", "admin_archive/login", "admin_legacy/login", "admin_old1/login",
    "admin_old2/login", "admin_old3/login", "admin_old4/login", "admin_old5/login",
    "admin_old6/login", "admin_old7/login", "admin_old8/login", "admin_old9/login",
    "admin_old10/login", "admin_area_backup/login", "admin_area_old/login",
    "admin_area_new/login", "admin_area_test/login", "admin_area_temp/login",
    "admin_area_dev/login", "admin_area_prod/login", "admin_area_live/login",
    "admin_area_staging/login", "admin_area_secure/login", "admin_area_private/login",
    "admin_area_public/login", "admin_area_archive/login", "admin_area_legacy/login",
    "admin_area_old1/login", "admin_area_old2/login", "admin_area_old3/login",
    "admin_area_old4/login", "admin_area_old5/login", "admin_area_old6/login",
    "admin_area_old7/login", "admin_area_old8/login", "admin_area_old9/login",
    "admin_area_old10/login",

    # Miscellaneous admin paths
    "cp", "cpanel", "webadmin", "sysadmin", "root", "superuser", "superadmin",
    "moderator", "mod", "staff", "support", "helpdesk", "operator", "operator/login",
    "operator/admin", "operator/panel", "operator/dashboard", "operator/cp",
    "operator/cpanel", "operator/webadmin", "operator/sysadmin", "operator/root",
    "operator/superuser", "operator/superadmin", "operator/moderator", "operator/mod",
    "operator/staff", "operator/support", "operator/helpdesk", "operator/operator",
    "operator/operator/login", "operator/operator/admin", "operator/operator/panel",
    "operator/operator/dashboard", "operator/operator/cp", "operator/operator/cpanel",
    "operator/operator/webadmin", "operator/operator/sysadmin", "operator/operator/root",
    "operator/operator/superuser", "operator/operator/superadmin", "operator/operator/moderator",
    "operator/operator/mod", "operator/operator/staff", "operator/operator/support",
    "operator/operator/helpdesk", "operator/operator/operator",

    # Additional admin paths
    "backend", "backend/login", "backend/admin", "backend/dashboard", "backend/controlpanel",
    "backend/manager", "backend/operator", "backend/superuser", "backend/superadmin",
    "backend/moderator", "backend/mod", "backend/staff", "backend/support", "backend/helpdesk",
    "backend/operator/login", "backend/operator/admin", "backend/operator/panel",
    "backend/operator/dashboard", "backend/operator/cp", "backend/operator/cpanel",
    "backend/operator/webadmin", "backend/operator/sysadmin", "backend/operator/root",
    "backend/operator/superuser", "backend/operator/superadmin", "backend/operator/moderator",
    "backend/operator/mod", "backend/operator/staff", "backend/operator/support",
    "backend/operator/helpdesk", "backend/operator/operator", "backend/operator/operator/login",
    "backend/operator/operator/admin", "backend/operator/operator/panel", "backend/operator/operator/dashboard",
    "backend/operator/operator/cp", "backend/operator/operator/cpanel", "backend/operator/operator/webadmin",
    "backend/operator/operator/sysadmin", "backend/operator/operator/root", "backend/operator/operator/superuser",
    "backend/operator/operator/superadmin", "backend/operator/operator/moderator", "backend/operator/operator/mod",
    "backend/operator/operator/staff", "backend/operator/operator/support", "backend/operator/operator/helpdesk",
    "backend/operator/operator/operator"
]


def check_admin_page(url, path):
    full_url = f"{url}/{path}"
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] Found: {full_url}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] Not found: {full_url}{Style.RESET_ALL}")
    except requests.RequestException as e:
        print(f"{Fore.YELLOW}[!] Error accessing {full_url}: {e}{Style.RESET_ALL}")

def scan_website(url):
    print(f"{Fore.CYAN}[*] Scanning {url} for admin pages...{Style.RESET_ALL}")
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_admin_page, url, path) for path in ADMIN_PATHS]
        for future in futures:
            future.result()
    print(f"{Fore.CYAN}[*] Scan completed.{Style.RESET_ALL}")

def hacker_interface():
    print(f"""
    {Fore.RED}██╗   ██╗██╗██████╗ ███████╗███████╗██████╗ 
    {Fore.RED}██║   ██║██║██╔══██╗██╔════╝██╔════╝██╔══██╗
    {Fore.RED}██║   ██║██║██████╔╝█████╗  █████╗  ██████╔╝
    {Fore.RED}██║   ██║██║██╔═══╝ ██╔══╝  ██╔══╝  ██╔══██╗
    {Fore.RED}╚██████╔╝██║██║     ███████╗███████╗██║  ██║
    {Fore.RED} ╚═════╝ ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝
    {Fore.GREEN}Powered by Viper Droid
    {Fore.YELLOW}Admin Page Finder - Ethical Use Only
    {Style.RESET_ALL}""")
    target = input(f"{Fore.CYAN}Enter the target website (e.g., http://example.com): {Style.RESET_ALL}").strip()
    if not target.startswith("http"):
        target = f"http://{target}"
    scan_website(target)

if __name__ == "__main__":
    hacker_interface()
