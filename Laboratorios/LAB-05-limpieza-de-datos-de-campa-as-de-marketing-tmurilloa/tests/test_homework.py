# flake8: noqa: E501

"""Autograding script."""

import os

import pandas as pd  # type: ignore

from homework import homework


def test_homework():
    """Autograding the homework."""
    homework.clean_campaign_data()

    assert os.path.exists("files/output/campaign.csv")
    assert os.path.exists("files/output/client.csv")
    assert os.path.exists("files/output/economics.csv")

    #
    # Campaign
    #
    campaign = pd.read_csv("files/output/campaign.csv")

    assert campaign.shape == (41188, 7)
    for name in (
        "client_id,number_contacts,contact_duration,"
        "previous_campaign_contacts,previous_outcome,"
        "campaign_outcome,last_contact_date".split(",")
    ):
        assert name in campaign.columns

    assert (
        campaign[campaign["previous_outcome"].map(lambda x: x == 0)].shape[0] == 39815
    )
    assert (
        campaign[campaign["campaign_outcome"].map(lambda x: x == 0)].shape[0] == 36548
    )

    assert (
        campaign[campaign["last_contact_date"].map(lambda x: x == "2022-07-19")].shape[
            0
        ]
        == 234
    )

    assert (
        campaign[campaign["last_contact_date"].map(lambda x: x == "2022-07-25")].shape[
            0
        ]
        == 216
    )

    #
    # Economics
    #
    economics = pd.read_csv("files/output/economics.csv")

    assert economics.shape == (41188, 3)
    for name in "client_id,cons_price_idx,euribor_three_months".split(","):
        assert name in economics.columns

    #
    # Client
    #
    client = pd.read_csv("files/output/client.csv")
    # print(client.education.value_counts())

    assert client.shape == (41188, 7)
    for name in "client_id,age,job,marital,education,credit_default,mortgage".split(
        ","
    ):
        assert name in client.columns

    assert client[client["job"].map(lambda x: x == "admin")].shape[0] == 10422
    assert client[client["job"].map(lambda x: x == "blue_collar")].shape[0] == 9254
    assert client[client["job"].map(lambda x: x == "technician")].shape[0] == 6743
    assert client[client["job"].map(lambda x: x == "services")].shape[0] == 3969
    assert client[client["job"].map(lambda x: x == "entrepreneur")].shape[0] == 1456
    assert client[client["job"].map(lambda x: x == "housemaid")].shape[0] == 1060
    assert client[client["job"].map(lambda x: x == "management")].shape[0] == 2924
    assert client[client["job"].map(lambda x: x == "retired")].shape[0] == 1720

    assert (
        client[client["education"].map(lambda x: x == "university_degree")].shape[0]
        == 12168
    )
    assert (
        client[client["education"].map(lambda x: x == "high_school")].shape[0] == 9515
    )
    assert client[client["education"].map(lambda x: x == "basic_9y")].shape[0] == 6045
    assert (
        client[client["education"].map(lambda x: x == "professional_course")].shape[0]
        == 5243
    )
    assert client[client["education"].map(lambda x: x == "basic_4y")].shape[0] == 4176
    assert client[client["education"].map(lambda x: x == "basic_6y")].shape[0] == 2292
    assert client[client["education"].map(lambda x: x == "illiterate")].shape[0] == 18

    assert client[client["credit_default"].map(lambda x: x == 1)].shape[0] == 3
    assert client[client["mortgage"].map(lambda x: x == 1)].shape[0] == 21576
