# 一、User Model设计
## 1. 分析有哪些实体，通过新建app来完成
* 商品类别信息
    * 商品列表页
        * 商品类别
        * 价格，排序，设置价格区间
        * 分页
    * 详情页
        * 商品标题
        * 轮播图
        * 价格、促销价格
        * 是否为免运费的商品
        * 商品详情
        * 热卖商品
        * 加入购物车
        * 收藏
* 登录
    * 账号
    * 密码
    * 会员中心
        * 用户信息
            * 出生日期
            * 性别
            * 电子邮件地址
            * 手机
        * 收藏
            * 删除
            * 可以点进商品的详情页
        * 我的留言
            * 留言类型
            * 留言内容
            * 上传文件
    * 订单中心
        * 我的订单
            * 订单号
                * 订单详情
                    * 立即支付
            * 取消订单
        * 收货地址
            * 增加收货地址
            * 修改收货地址
            * 删除收货地址
* 购物车            
    * 结算(进入支付页面)
    * 数量增改
    * 价格
    * 删除购物车商品
    * 添加配送地址
## 2. django设计思想-分类-首先定义app，然后才定义app里面的每一个model
* 设计app -> 分类思想
    * 归类
        * 商品想过 -> 商品 goods
        * 交易相关 -> 交易 -> trade
            * 支付相关 -> 购物车
            * 订单相关 -> 订单
        * 用户相关 -> 用户 users
        * 用户操作 -> 操作 user_operation
    * 运行Tools -> Run manage.py Task ->进入manage.py@MxShop >
        * 敲并运行命令：startapp goods, 将创建的goods拖入到apps下面
        * 敲并运行命令：startapp trade, 将创建的trade拖入到apps下面
        * 敲并运行命令：startapp user_operation, 将创建的user_operation拖入到apps下面
* 设计每个app下的model ->首先要弄清楚设计的model是什么
    * users:
        * 设计用户users的model ->在apps/users/migrations/models.py下设计
            * 设计model: 
                * 用户: UserProfile
                    * 姓名: name
                    * 出生年月: birthday
                    * 性别: gender
                    * 电话: mobile
                    * 邮箱: email
                    * 添加时间: add_time
                * 短信验证码: CodeVerify
                    * 验证码: code
                    * 电话: mobile
                    * 添加时间: add_time
        * 添加AUTH_USER_MODEL = 'users.UserProfile'到MxShop.settings.py下面，以替换系统用户
            * 可通过以下代码导入：
                from django.contrib.auth import get_user_model<br>
                User = get_user_model()
    * goods:
        * 设计用户goods的model ->在apps/goods/migrations/models.py下设计
            * 设计model: 
                * 商品类别: GoodsCategory， 从属关系通过外键来关联
                    * 类别名: name
                    * 类别code: code 
                    * 类别描述: desc
                    * 类目级别: category_type
                    * 父目录: parent_category
                    * 是否导航: is_tab 
                    * 添加时间: add_time
                * 品牌名: GoodsCategoryBrand
                    * 商品类目: category
                    * 品牌名: name
                    * 品牌描述: desc
                    * 图片：image
                    * 添加时间: add_time
                * 商品: Goods
                    * 商品类目: category
                    * 商品唯一货号: goods_sn
                    * 商品名: name
                    * 点击数: click_num
                    * 商品销售量: sold_num
                    * 收藏数: fav_num
                    * 库存数: goods_num
                    * 市场价格: market_price
                    * 本店价格: shop_price
                    * 商品简短描述: goods_brief
                    * 内容: goods_desc
                    * 是否承担运费: ship_free
                    * 封面图: goods_front_image
                    * 是否新品: is_new
                    * 是否热销: is_hot
                    * 添加时间: add_time
                * 首页商品类别广告: IndexAd
                    * 商品类目: category
                    * 商品: goods
                * 商品轮播图: GoodsImage
                    * 商品: goods
                    * 图片: image
                    * 添加时间: add_time
                * 轮播的商品: Banner
                    * 商品: goods
                    * 轮播图片: image
                    * 轮播顺序: index
                    * 添加时间: add_time
                * 热搜词: HotSearchWords
                    * 热搜词: keywords
                    * 排序: index
                    * 添加时间: add_time
    * trade: 购物车和支付
        * 设计用户trade的model ->在apps/trade/migrations/models.py下设计
            * 设计model: 
                * 购物车：ShoppingCart
                    * 用户: user
                    * 商品: goods
                    * 购买数量: nums
                    * 添加时间: add_time
                * 订单：OrderInfo
                    * 用户: user
                    * 订单号: order_sn
                    * 交易号: trade_no
                    * 订单状态: pay_status
                    * 订单留言: post_script
                    * 订单金额: order_mount
                    * 支付时间: pay_time
                    * 收货地址: address
                    * 签收人: signer_name
                    * 联系电话: singer_mobile
                    * 添加时间: add_time
                * 订单的商品详情: OrderGoods
                    * 订单信息: order
                    * 商品: goods
                    * 商品数量: goods_num
                    * 添加时间: add_time
    * user_operation: 用户操作
        * 设计用户user_operation的model ->在apps/user_operation/migrations/models.py下设计
            * 设计model: 
                * 用户收藏: UserFav
                    * 用户: user
                    * 商品: goods
                    * 添加时间: add_time
                * 用户留言: UserLeavingMessage
                    * 用户: user
                    * 留言类型: message_type
                    * 主题: subject
                    * 留言内容: message
                    * 上传的文件: file
                    * 添加时间: add_time
                * 用户收货地址: UserAddress
                    * 用户: user
                    * 省份: province
                    * 城市: city
                    * 区域: district
                    * 详细地址: address
                    * 签收人: signer_name
                    * 电话: signer_mobile
                    * 添加时间: add_time
## 3. 如何根据设计的表生成数据库，也就是django migrations的操作
    1. 在根据设计的表生成数据库之前，要将设计的app放到MxShop/settings.py里面的INSTALLED_APPS中去，记得加,
    2. 打开XAMPP，开启MySql
    3. 打开Navicat，连接好数据库127.0.0.1
    4. 运行Tools -> Run manage.py Task ->进入manage.py@MxShop >
        * 敲击命令：makemigrations, 生成每个app/设计表/migrations/0001_initial.py文件，正确运行的Log如下：
            ----------------------------------------------------
            manage.py@MxShop > makemigrations
            "D:\install\pycharm\PyCharm 2019.3\bin\runnerw64.exe" E:\study\python\workon\VueShop\Scripts\python.exe "D:\install\pycharm\PyCharm 2019.3\plugins\python\helpers\pycharm\django_manage.py" makemigrations E:/study/python/VueShop/MxShop
            Tracking file by folder pattern:  migrations
            Migrations for 'goods':
              apps\goods\migrations\0001_initial.py
                - Create model Banner
                - Create model Goods
                - Create model GoodsCategory
                - Create model GoodsCategoryBrand
                - Create model GoodsImage
                - Create model HotSearchWords
                - Create model IndexAd
                - Add field category to goods
                - Add field goods to banner
            Migrations for 'trade':
              apps\trade\migrations\0001_initial.py
                - Create model OrderGoods
                - Create model OrderInfo
                - Create model ShoppingCart
              apps\trade\migrations\0002_auto_20200116_2304.py
                - Add field user to shoppingcart
                - Add field user to orderinfo
                - Add field goods to ordergoods
                - Add field order to ordergoods
                - Alter unique_together for shoppingcart (1 constraint(s))
            Migrations for 'user_operation':
              apps\user_operation\migrations\0001_initial.py
                - Create model UserAddress
                - Create model UserFav
                - Create model UserLeavingMessage
              apps\user_operation\migrations\0002_auto_20200116_2304.py
                - Add field user to userleavingmessage
                - Add field goods to userfav
                - Add field user to userfav
                - Add field user to useraddress
                - Alter unique_together for userfav (1 constraint(s))
            Migrations for 'users':
              apps\users\migrations\0001_initial.py
                - Create model UserProfile
                - Create model VerifyCode

            Following files were affected 
             E:\study\python\VueShop\MxShop\apps\goods\migrations\0001_initial.py
            E:\study\python\VueShop\MxShop\apps\trade\migrations\0001_initial.py
            E:\study\python\VueShop\MxShop\apps\trade\migrations\0002_auto_20200116_2304.py
            E:\study\python\VueShop\MxShop\apps\users\migrations\0001_initial.py
            E:\study\python\VueShop\MxShop\apps\user_operation\migrations\0001_initial.py
            E:\study\python\VueShop\MxShop\apps\user_operation\migrations\0002_auto_20200116_2304.py
            Process finished with exit code 0
            ----------------------------------------------------
        * 敲击命令:migrate，实际是执行migrations下面的py文件生成数据库表, log如下：
            ----------------------------------------------------
            manage.py@MxShop > migrate
            "D:\install\pycharm\PyCharm 2019.3\bin\runnerw64.exe" E:\study\python\workon\VueShop\Scripts\python.exe "D:\install\pycharm\PyCharm 2019.3\plugins\python\helpers\pycharm\django_manage.py" migrate E:/study/python/VueShop/MxShop
            Tracking file by folder pattern:  migrations
            System check identified some issues:

            WARNINGS:
            ?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
                HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/2.0/ref/databases/#mysql-sql-mode
            Operations to perform:
              Apply all migrations: auth, contenttypes, goods, sessions, trade, user_operation, users
            Running migrations:
              Applying contenttypes.0001_initial... OK
              Applying contenttypes.0002_remove_content_type_name... OK
              Applying auth.0001_initial... OK
              Applying auth.0002_alter_permission_name_max_length... OK
              Applying auth.0003_alter_user_email_max_length... OK
              Applying auth.0004_alter_user_username_opts... OK
              Applying auth.0005_alter_user_last_login_null... OK
              Applying auth.0006_require_contenttypes_0002... OK
              Applying auth.0007_alter_validators_add_error_messages... OK
              Applying auth.0008_alter_user_username_max_length... OK
              Applying auth.0009_alter_user_last_name_max_length... OK
              Applying goods.0001_initial... OK
              Applying sessions.0001_initial... OK
              Applying users.0001_initial... OK
              Applying trade.0001_initial... OK
              Applying trade.0002_auto_20200116_2304... OK
              Applying user_operation.0001_initial... OK
              Applying user_operation.0002_auto_20200116_2304... OK

            Process finished with exit code 0
            ----------------------------------------------------
        * 到Navicat里查看mxshop数据库，会发现将设计的数据表里面的每一个类生成了数据库里面的数据表，并且新增了一些数据表
            * django_migrations表详细记录了已经运行了哪些app/设计表/migrations下面的哪些py文件，这样修改设计表后不至于
                只需要变更修改后的py文件
## 4. 需要避的坑
    * 修改apps下的设计表内容后，需要再一次执行生成数据库表的三步骤
        * 运行Tools -> Run manage.py Task ->进入manage.py@MxShop
        * makemigrations
        * migrate
    * 若觉得apps/设计表/migrations下面的py文件很乱，删除或重新整理了一下，那么需要先删除数据库django_migrations
        里面关于设计表的所有已运行的py文件，重新执行生成数据库表的三步骤
    * 修改数据库或数据库表时尽量用修改models.py的形式修改代码，通过执行生成数据库表的三步骤来修改数据库，不要直接修改
        数据库，不然会造成两种修改不统一，容易形成bug且不容易恢复
