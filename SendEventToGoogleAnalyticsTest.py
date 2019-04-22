from PlusGoogleAnalyticsManager import HitClient

# Set your Google Analytics Tracking Id here
GA_ID = "UA-116081388-1"

def run():


    hit_client = HitClient(GA_ID)

    try:

        # Test with required params only
        r = hit_client.send_hit(
            "event",
            event_category="orange",
            event_action="want",
        )

        print(str(r))

    except (Exception) as ex:

        print(ex)

    # # Test with optional params included
    # r = hit_client.send_hit(
    #         "event",
    #         event_category="Users",
    #         event_action="New Registration w Value",
    #         user_id="uy6rafdye7",
    #         event_label="JP",
    #         event_value="7",
    #         )
    #
    #
    # # Test with optional params included
    # r = hit_client.send_hit(
    #         "transaction",
    #         revenue="2160",
    #         currency="JPY",
    #         user_id="uy6Rafdye7",
    #         shipping="500",
    #         tax="160",
    #         affiliation="Test Category",
    #         transaction_id="XXXtesttransid01",
    #         )
    #
    # # Test with required params only
    # r = hit_client.send_hit(
    #     "transaction",
    #     revenue="999",
    #     currency="MYR",
    # )


if __name__ == "__main__":
    run()
