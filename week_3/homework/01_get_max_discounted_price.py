shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]
# 제일 할인을 받으려면 어떻게 해야 하는지


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)   # [1500000, 30000, 2000]
    coupons.sort(reverse=True)  # [40, 20]
    prices_index = 0
    coupons_index = 0
    max_price = 0

    while prices_index < len(prices) and coupons_index < len(coupons):
        max_price += prices[prices_index] * (100 - coupons[coupons_index]) // 100
        prices_index += 1
        coupons_index += 1
    while prices_index < len(prices):
        max_price += prices[prices_index]
        prices_index += 1

    return max_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.