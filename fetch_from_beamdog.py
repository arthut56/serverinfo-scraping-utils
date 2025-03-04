from playwright.sync_api import sync_playwright
import datetime

##You must specify the exact server name as beamdog.net has it
def find_no_players_at(server_name = "ES) Puerta de Baldur 5E"):

    try:
        with sync_playwright() as p:

            print(datetime.datetime.now())
            print(f"Fetching number of players at {server_name}")

            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("https://nwn.beamdog.net/", timeout=15000)
            page.wait_for_selector("table#serverlist")

            tbody = page.query_selector("table#serverlist > tbody")
            data = str(tbody.inner_html())

            #Busy-waiting loop checks that data has loaded into the table
            #Take a snapshot of the table data as HTML
            while "Loading" in data:
                tbody = page.query_selector("table#serverlist > tbody")
                data = str(tbody.inner_html())


            #Find the server position and "sorting_1" tag, where the no. players is located
            server_pos = data.find(server_name)
            people_in_server_pos = data.find("sorting_1", server_pos) + 11
            people_in_server = data[people_in_server_pos: data.find("</td>", people_in_server_pos) ]

            print(f"There are currently {people_in_server} players in {server_name}.")


            browser.close()

    except Exception as e:
        print(e)

find_no_players_at()