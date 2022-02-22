#类的定义
class Person:
    #限制对象属性，如果这个作用的话，下面在类里添加属性就不用写了，这个作用在通过对象添加属性时，只能添加age属性
    #__slots__ = ["age"]
    
    #直接在类里添加属性
    age = 23
    gender = 'female'
    pets = ['None']
    
    #定义一个实例方法：默认第一个参数需要接收到一个实例
    def eat(self):
        print('这是一个实例方法')
        
    #定义一个类方法：默认第一个参数需要接收到一个类
    @classmethod
    def run(cls):
        print('这是一个类方法')
        
    #定义一个静态方法：第一个参数什么也不接收
    @staticmethod
    def jump():
        print('这是一个静态方法')
        
#根据这个类，创建一个对象（实例化）
p = Person()

#给对象添加属性
p.age = 18
p.gender = 'male'
p.pets = ['小花','小黑']

#给属性添加值
p.pets.append('小黄')

#删除属性
del p.age

c = Person()

#查看对象的所有属性
print(p.__dict__)
print(c.age, c.gender, c.pets) #这时不能通过 c.__dict__来查看

#修改属性
c.age = 35

print(c.age, c.gender, c.pets) 
print(c.__dict__)

#调用实例方法
c.eat() # 不能用Person.eat() 会报错

#调用类方法
c.run()

#调用静态方法
c.jump()

#-----------------------------------------------------------------------------------------------
#回到上面类方法的装饰器的作用：在保证原本函数不改变的前提下，直接给这个函数增加一些功能。静态方法也是如此
#例如下面使用A继承上面的Person类。
class A(Person):
    pass

A.run()
A.jump()

#-----------------------------------------------------------------------------------------------
#元类
#即创建类对象的一个类。首先要明白类也是对象，万物皆对象
Person.__class__ 

#-----------------------------------------------------------------------------------------------
#类的描述
class Person:
    '''
    关于这个类的描述，类的作用，类的构造函数等
    count: 人数
    '''
    count = 1
    
    def run(self, distance, step):
        '''
        这个方法的作用效果
        :param distance:参数的含义,类型，是否有默认值
        :param step:
        :return:返回值的含义，类型
        '''
        print('run')
        return distance / step
        
#-----------------------------------------------------------------------------------------------
#属性包含：私有化属性，只读属性，内置特殊属性
#---------------私有属性的概念-------------------
#python没有真正的私有化支持，但可以使用下划线完成伪私有的效果
# y代表公有属性 _y:代表受保护的属性 __y:代表私有属性  【同时适用于类属性和实例属性】
class Animal:
    __x = 10
    def test(self):
        print(Animal.__x)
        print(self.__x)
    pass
    
class Dog(Animal):
    def test2(self):
        print(Dog.__x)
        print(self.__x)
    pass

#测试3个区域的属性传递

#区域1  私有属性在区域1可以访问
a = Animal()
a.test()

#区域2  私有属性在区域2不能访问
b = Dog()
b.test2()

#区域3 受保护的属性在区域3被访问时会有警告，但还是可以访问  私有属性在区域3不能访问
print(Animal.__x)
print(Dog.__x)
print(a.__x)
print(b.__x)

#私有属性的目的：防止外界直接访问 防止被子类同名称属性覆盖
#私有属性的应用场景：数据保护  数据过滤
class Person:
    #当我们创建好一个实例对象之后，会自动的调用这个方法，来初始化这个对象
    def __init__(self):
        self.__age = 18
    
p = Person()
p.__age = 23 #外面写的__age是无意义的，只是普通的属性命名罢了

p.__dict__ # 会返回 {'_Person__age': 18, '__age': 23}

# 变量添加下划线的规范
# y_: 没啥作用，一般用来与系统内置的变量名做区分
# __y__:没啥作用，一般表示系统内置的写法。

#-----------------------------------------------------------------------------------------------
#----------只读属性的概念-------------
#一个属性，只能读取，不能写入。
#有些属性，只限在内部根据不同场景进行修改，对于外界不能修改，只能读取。比如电脑的网速属性，网络状态属性。

#通过一下两步完成只读属性的创建
#step1: 先建立私有属性
#step2: 部分公开
class Person:
    def __init__(self):
        self.__age = 18
    
    #修饰符的作用是可以以使用属性的方式来使用这个方法
    @property
    def getAge(self):
        return self.__age

p = Person()
print(p.getAge) #加完修饰符后，我们就可以把getAge这个实例当作属性来看待，不用再加括号。

#-----------------------------------------------------------------------------------------------
#-------property在经典类和新式类的使用------------
#经典类：没有继承至object,python2版本定义一个类时，默认不继承
#新式类：继承至object,python3版本定义一个类时，默认继承，建议使用新式类。可以通过 Person.__bases__看类是否继承至object

#新式类中的使用方法1
class Person(object):
    def __init__(self):
        self.__age = 18
        
    def get_age(self):
        return self.__age
    
    def set_age(self, value):
        self.__age = value
    
    age = property(get_age, set_age)
    
p = Person()
p.age = 16
print(p.age)
print(p.__dict__)

#新式类中的使用方法2
class Person(object):
    def __init__(self):
        self.__age = 18
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value
    
p = Person()
p.age
p.age = 20
print(p.age, p.__dict__)

#-----------------------------------------------------------------------------------------------
#-----------内置属性-------------
# 1 类属性
# __dict__: 类的属性
# __bases__: 类的所有父类构成元组
# __doc__: 类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块

# 2 实例属性
# __dict__: 实例的属性
# __class__: 实例对应的类

#-----------内置特殊方法---------------
# 1 信息格式化操作 __str__ 和 __repr__
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        
    def __str__(self): #或者 __repr__ ：repr和str的区别不再阐述
        return f'这个人的姓名是{self.name}，这个人的年龄是{self.age}'
    
p = Person('bob', 18)
print(p) # 输出 “这个人的姓名是bob，这个人的年龄是18”

# 2 调用操作 __call__:使得“对象”具备当作函数来调用的能力
class Person:
    def __call__(self, *args, **kwargs):
        print('xxx')
    pass

p = Person()
p() #调用p,输出 “xxx”

# 3 索引操作:可以对一个实例对象进行索引操作
class Person:
    def __init__(self):
        self.cache = {}
        
    def __setitem__(self, key, value):
        print('setitem', key, value)
        self.cache[key] = value
        
    def __getitem__(self, item):
        print('getitem', item)
        return self.cache[item]
    
    def __delitem__(self, key):
        print('delitem', key)
        del self.cache[key]
        
p = Person()
#通过set get del三者的组合，可以直接在实例部分进行属性的新建和赋值
p['name'] = 'bob' 
print(p['name'])
del p['name']
print(p.cache)

# 4 切片操作: 可以对一个实例对象进行切片操作
class Person:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]
    
    def __setitem__(self, key, value):
        self.items[key] = value
        
    def __getitem__(self, item):
        return self.items[item]
    
    def __delitem__(self, key):
        del self.items[key]
        
#通过set get del三者的组合，可以直接在实例部分进行列表的切分与赋值        
p = Person()
p[0:4:2] = ['a','b']
print(p.items) # 返回 ['a', 2, 'b', 4, 5]

# 5 比较操作：可以自定义对象“比较大小，相等以及真假”规则
class Person:
    def __init__(self, age, height):
        self.age = age
        self.height = height
    
    def __eq__(self, other): # 这里只是等于的，还有更多的内置的方法来表示 大于小于等等。
        print(other)
        return self.age == other.age #属性的判断标准
        
p1 = Person(18, 180)
p2 = Person(17, 190)
print(p1 == p2)

# 6 迭代器：怎样让我们自己创建的对象可以使用for循环或者使用next函数进行遍历或访问
# 6.1 for循环：可以通过__getitem__或者__iter__实现。 iter的优先级要高于getitem
# 通过 getitem 完成遍历
class Person:
    def __init__(self):
        self.result = 1
        
    def __getitem__(self, item):
        self.result += 1
        if self.result >= 6:
            raise StopIteration('停止遍历')
            
        return self.result
    pass

p = Person()

for i in p:
    print(i)
    
# 通过iter完成遍历    
class Person:
    def __init__(self):
        self.result = 1
            
    def __iter__(self):
        return self
    
    def __next__(self):
        self.result += 1
        if self.result >= 6:
            raise StopIteration('停止遍历')
        return self.result
    
    pass

p = Person()

for i in p:
    print(i)
    
#-----------------------------------------------------------------------------------------------
#---------使用类，实现装饰器-------------
class Check:
    def __init__(self, func):
        self.f = func
    
    def __call__(self, *args, **kwargs):
        print('登录验证') #在函数执行前要做的工作写在 self.f() 运行前就行了
        self.f()
        
@Check
def fashuoshuo():
    print('发说说')
    
fashuoshuo()

#-----------生命周期方法----------------
class Person():
    def __new__(cls, *args, **kwargs):
        print('新建了一个对象，但是被我拦截了')
    pass

p = Person()
print(p) # 返回None

class Person():
    def __init__(self):
        print('初始化方法')
        self.name = 'bob'
    
    #当一个对象被创建之后，会自动调用__del__。因此我们可以在这部分添加内存的释放工作。
    def __del__(self):
        print('这个对象被释放了')

p = Person()
print(p) 

#---------监听对象生命周期的方法-小案例-----------
# 打印一下，当前这个时刻由该类产生的实例个数
# 创建实例时，count + 1, 删除实例时，count - 1
class Person:
    __personCount = 0
    def __init__(self):
        global __personCount
        print('计数+1')
        Person.__personCount += 1
        
    def __del__(self):
        global __personCount
        print('计数-1')
        Person.__personCount -= 1
        
    @staticmethod    
    def log():
        print(f'人数为{Person.__personCount}个')
    pass
        
p = Person()   
p1 = Person()
del p
Person.log()

#--------直接引用计数器------------
import sys

class Person:
    pass

p1 = Person()
print(sys.getrefcount(p1))

#-----------------------------------------------------------------------------------------------
#---------------面向对象的三大特性---------------------
# 封装：将一些属性或相关方法封装在一个对象中，对外隐藏内部具体实现细节
# 其好处：使用起来更加方便，保证数据的安全，利于代码维护

# 继承：拥有和资源。
# “拥有”并不是资源的复制也不是变成双份资源，而是指资源的使用权。
# “资源”是指非私有的属性和方法。
# 单继承：仅继承了一个父类。多继承：继承了多个父类。

# 多态：一个类所延申的多种形态。或指调用时的多种形态。

#-------------综合案例-----------------
# 定义三个类：小狗，小猫，人
# 小狗：姓名，年龄，吃饭，玩，睡觉，看家
# 小猫：姓名，年龄，吃饭，玩，睡觉，捉老鼠
# 人：姓名，年龄，宠物，吃饭，玩，睡觉
# 养宠物：让所有的宠物吃饭，玩，睡觉
# 让宠物工作：让所有的宠物按自己的职责开始工作

class Dog:
    def __init__(self, name='un', age=1): #添加默认值
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self}在吃饭')
        
    def play(self):
        print(f'{self}在玩')
        
    def sleep(self):
        print(f'{self}在睡觉') 
        
    def work(self):
        print(f'{self}在看家')   
        
    def __str__(self):
        return f'名字是{self.name}，年龄是{self.age}的小狗'
    

class Cat:
    def __init__(self, name='an', age=1): #添加默认值
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self}在吃饭')
        
    def play(self):
        print(f'{self}在玩')
        
    def sleep(self):
        print(f'{self}在睡觉') 
        
    def work(self):
        print(f'{self}在捉老鼠')   
        
    def __str__(self):
        return f'名字是{self.name}，年龄是{self.age}的小猫'
    
    
class Person:
    def __init__(self, name, age, pets):
        self.name = name
        self.age = age
        self.pets = pets
        
    def eat(self):
        print(f'{self}在吃饭')
        
    def play(self):
        print(f'{self}在玩')
        
    def yangPets(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()
            
    def make_pets_work(self):
        for pet in self.pets:
            pet.work()
        
    def __str__(self):
        return f'名字是{self.name}，年龄是{self.age}的人'
    
d = Dog('小黑', 2)
c = Cat('小花', 4)
p = Person('大黄', 23, [d, c])
p.make_pets_work()

# 输出：
# 名字是小黑，年龄是2的小狗在看家
# 名字是小花，年龄是4的小猫在捉老鼠

#-----------综合案例--通过继承实现一种更简洁的方式--------------
#定义父类，父类中的属性和方法需要是公共的
class Animal:
    def __init__(self, name='an', age=1): #添加默认值
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self}在吃饭')
        
    def play(self):
        print(f'{self}在玩')
        
    def sleep(self):
        print(f'{self}在睡觉') 
        
    
class Person(Animal):
    #增加pets属性
    def __init__(self, name, age, pets):
        super(Person, self).__init__(name, age)
        self.pets = pets
    
    def yangPets(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()
            
    def make_pets_work(self):
        for pet in self.pets:
            pet.work()
        
    def __str__(self):
        return f'名字是{self.name}，年龄是{self.age}的人'
    
    
class Dog(Animal):
    def work(self):
        print(f'{self}在看家')   
        
    def __str__(self):
        return f'名字是{self.name}，年龄是{self.age}的小狗'
    
    
class Cat(Animal):
    def work(self):
        print(f'{self}在捉老鼠')   
        
    def __str__(self):
        return f'名字是{self.name}，年龄是{self.age}的小猫'
    
d = Dog('sa', 2)
c = Cat('er', 3)
p = Person('das', 23, [d,c])
p.make_pets_work()
# 输出：
# 名字是sa，年龄是2的小狗在看家
# 名字是er，年龄是3的小猫在捉老鼠

