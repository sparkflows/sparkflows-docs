Dataset API
============

The Dataset REST APIs, allow you to manage the Datasets.

Below are the various Dataset APIs available in Fire Insights. They should be executed after you have logged into Fire Insights.

GET List of Datasets
--------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/datasets
     - GET
     
An example response:

::   

   {
    "7fff0810-eb50-4b7e-8c9a-a55dcc2578f3": "Avazu",
    "e0775ee4-b0d6-498c-9dcc-957311281642": "Bike Sharing dataset",
    "a4ca862a-4127-449d-a7e0-c2fffd69fc14": "Cars",
    "1e404f69-a44f-4a76-be90-13cbffd06dfd": "Cars Dataset 2",
    "414c8cf7-6732-46ca-9887-3c0c55052474": "Customer Nested JSON",
    "b4a7dc88-5ce0-41d9-bac0-93caa08b98e7": "Date Time Sample",
    "753ffcfa-495b-496f-945c-345a4d20e492": "Dedup Error Dataset",
    "21687a6d-2e70-4374-ba90-9648e82b565e": "Dedup Master Dataset",
    "2c3b6f08-3c6c-4700-a0f0-6f5a1d9d17dd": "Episodes Avro",
    "9c96f8d9-44b9-4fe8-be58-35ba65953773": "Farmers Market",
    "9c96f8d9-44b9-4fe8-be58-35ba65953799": "Farmers Market",
    "2ff32692-9b3c-49de-91a7-401daf2590c1": "Flights Delay",
    "de0b65b3-9bc5-4d01-b4ca-7d189ef77b57": "General Payment Dataset",
    "a610f2d8-59f9-471f-8576-e3a2b49ab369": "HIVE sample_07",
    "acf80851-4d96-4d7a-91ef-dfa8fe8937ee": "Housing",
    "adf80851-4d96-4d7a-91ef-dfa8fe8937ee": "Housing",
    "ecf80851-4d96-4d7a-91ef-dfa8fe8937ee": "Housing",
    "1defab5a-93fa-410b-96f1-ef44e5332f94": "IRS 2013 AGI",
    "cc1aec58-3c26-4e7f-adab-10e2458ec185": "JetRail Test",
    "735ee5eb-b634-42f2-8b4e-386883be019f": "JetRail Train",
    "738ee5eb-b634-42f2-8b4e-386883be019f": "JetRail Train",
    "935ee5eb-b634-42f2-8b4e-386883be019f": "JetRail Train",
    "697b0419-9fd2-485b-b999-b8125c63e773": "Kidney Cdr Finding",
    "3d045ee1-7125-48b6-afeb-b26bae9cc47d": "Kidney Lab Results",
    "429086c5-3e60-4fa1-9b6d-93c9d093ee48": "Kindey Egfr Derived",
    "6fe6f5ec-5dca-453f-8f51-af33a96ebf63": "Loan Prediction Train",
    "d8a1a0b1-93b8-4096-ab95-8e3a02d65263": "Movie Lens Ratings",
    "bf506cf2-7f65-48cf-9e33-1411177c9bfd": "Music Recommendation",
    "452e77f9-2d70-4c2b-8673-41dd2e9aa668": "NYC Trip Data",
    "3c32dd3c-2464-4c60-8f1a-7bf3552aef04": "Omniture",
    "033a08ff-fc0c-44cf-b713-1f4be7465834": "Omniture Products",
    "51273c4b-a101-43b5-94ca-06a928a0ea97": "Omniture Users",
    "b57c52b1-064a-4899-a075-20286ae7dde6": "Parquet File",
    "663c2be6-d2c0-4461-b20e-13d8353d0b9e": "People Parquet",
    "9fb4dea1-daa3-4abc-ad92-0200d56fcead": "Retail Transation Datset",
    "3c92ca1d-7ac0-49c4-9b91-d94d1ff5bce8": "SMS Spam Collection",
    "6be87dab-55ab-4738-9fa6-97d8de4bd5f3": "Spam",
    "4e9387d5-6a14-4961-858e-15ec72787dfa": "Telco Churn Prediction",
    "8e9387d5-6a14-4961-858e-15ec72787dfa": "Telco Churn Prediction",
    "1e13ec2a-4094-405e-a6e7-ffed3bd027f7": "Test-dataset",
    "6fe6f5ec-5dca-453f-8f51-af31a96ebf63": "Titanic Data",
    "883dd363-f832-4c6a-8681-0dffc8ab638a": "Transaction Dataset",
    "883dd369-f832-4c6a-8681-0dffc8ab638a": "Transaction Dataset"
   },
