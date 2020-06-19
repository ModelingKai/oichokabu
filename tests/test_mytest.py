def test_my_tests():
    assert True


class Dealer(object):
    pass


class Deck(object):
    pass


def test_場札4に10点Betして決め札1でSTOPして役は5である():
    # 掛け点と掛けるプレイヤーは一緒にする
    dealer = Dealer(Deck)
    # 最初に場札4枚と、ディーラー用に場札1枚を配る
    bafuda1, bafuda2, bafuda3, bafuda4, bafuda_dealer = \
        dealer.initialDeal()

    bafuda1 = player.bet(bafuda, 賭け点(10))

    # 決め札を配る
    bafuda1 = dealer.deal()

    # 賭けたプレイヤーだけが決め札を見ることができる

    # 引く、引かないの判断をする

    # 引かない
    player.stop()

    # 役の確定

    # 役が5であることを確認する
    assert bafuda1.役 == 役.goke
