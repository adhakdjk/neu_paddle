
# 类是一个模板： 绑定属性和方法
# 注意缩进
# self是谁？
class Hero(object): 
    def __init__(self, name, init_health=100, init_attack=10, alive=True):
        # 构造函数/初始化方法 在创建对象时候执行
        self.name = name  # 为对象绑定属性
        self.health = init_health
        self.attack = init_attack
        self.alive = True
        
        self.birth()

    def attack_enemy(self, enemy):
        # 对象的方法 用本类创建的所有对象都有这个方法
        enemy.health -= self.attack
        if enemy.health <= 0:
            enemy.alive = False 
            enemy.health = 0
            print(f'{enemy.name} 死亡')

    def upgrade(self):
        self.attack *= 1.1
        self.health *= 1.1

    def birth(self):
        print(f'我,{self.name},出生了！')


# 实例化对象
hero1 = Hero('亚瑟', 1000, 100)