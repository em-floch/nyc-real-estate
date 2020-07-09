from src.zillow.scrape_zws import get_info


def test_get_info():
    address = "187 Kent Avenue"
    city_st = "Brooklyn, NY"
    zip = '11249'
    get_info(address, city_st, zip)
