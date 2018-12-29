class GameInstance:
    def __init__(self, hd, ad, hk, ak, b, d):
        self.hd = hd
        self.ad = ad
        self.hk = hk
        self.ak = ak
        self.b = b
        self.d = d
        self.turn = 0
        
        self.attack = None
        self.buff = None
        self.cure = None
        self.debuff = None


    def min_turns(self):
        return 0


    def is_lose_state(self):
        return self.hd <= 0


    def is_win_state(self):
        return self.hk <= 0


    def attack(self):
        self.attack = GameInstance(hd - ak, ad, hk - ad, b, d)
        self.attack.set_turn(self.turn + 1)


    def hd(self):
        return self.hd
    

    def ad(self):
        return self.ad


    def hk(self):
        return self.hk


    def ak(self):
        return self.ak


    def b(self):
        return self.b


    def d(self):
        return self.d


    def turn(self):
        return self.turn

    
    def set_turn(turn_number):
        self.turn = turn_number
