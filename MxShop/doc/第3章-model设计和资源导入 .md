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
# 二、 xadmin后台管理系统配置
    * 将E:\study\python\coding-131\MxShop\extra_apps\xadmin拷贝到extra_apps下面
    * 在MxShop/settings.py里INSTALLED_APPS里面添加如下几句：
        'django.contrib.admin',
        'crispy_forms',
        'xadmin',
    * 将E:\study\python\coding-131\MxShop下面的goods, trade, user_operation, users里面的adminx.py拷贝到apps下面相应的表文件夹里
    * 安装xadmin依赖包： requirements.txt
        --------------------------------------------------------------------------------------------------
        E:\study\python\VueShop\MxShop\extra_apps\xadmin>pip install -r requirements.txt -i https://pypi.doubanio.com/simple/
        Looking in indexes: https://pypi.doubanio.com/simple/
        Requirement already satisfied: django>=2 in e:\study\python\workon\vueshop\lib\site-packages (from -r requirements.txt (line 1)) (2.0)
        Requirement already satisfied: django-crispy-forms>=1.6.0 in e:\study\python\workon\vueshop\lib\site-packages (from -r requirements.txt (line 2)) (1.8.1)
        Collecting django-import-export>=0.5.1
          Downloading https://pypi.doubanio.com/packages/ac/ab/dc240689d94099ce61df5b46b1ae3c1f24717cf1f19d34ac7425a6ff3aa7/django_import_export-2.0.1-py3-none-any.whl (82kB)
             |████████████████████████████████| 92kB 1.5MB/s
        Collecting django-reversion>=2.0.0
          Downloading https://pypi.doubanio.com/packages/e7/fe/b47df6c9540cd90c664b3ccd3a46f4db6ec15a675684f1ca3fbfd39d2d22/django_reversion-3.0.5-py2.py3-none-any.whl (80kB)
             |████████████████████████████████| 81kB 1.8MB/s
        Collecting django-formtools==2.1
          Downloading https://pypi.doubanio.com/packages/97/3f/b8e04c41c028d5cdad651393abea1f686d846c717d8ab5d5ebe2974f711c/django_formtools-2.1-py2.py3-none-any.whl (132kB)
             |████████████████████████████████| 133kB 2.2MB/s
        Collecting future==0.15.2
          Downloading https://pypi.doubanio.com/packages/5a/f4/99abde815842bc6e97d5a7806ad51236630da14ca2f3b1fce94c0bb94d3d/future-0.15.2.tar.gz (1.6MB)
             |████████████████████████████████| 1.6MB 2.2MB/s
        Collecting httplib2==0.9.2
          Downloading https://pypi.doubanio.com/packages/b1/e8/a49f534214a5c850faaad1678bea812991559d53bea49ecc7321f38a5757/httplib2-0.9.2.zip (210kB)
             |████████████████████████████████| 215kB 3.3MB/s
        Collecting six==1.10.0
          Downloading https://pypi.doubanio.com/packages/c8/0a/b6723e1bc4c516cb687841499455a8505b44607ab535be01091c0f24f079/six-1.10.0-py2.py3-none-any.whl
        Requirement already satisfied: pytz in e:\study\python\workon\vueshop\lib\site-packages (from django>=2->-r requirements.txt (line 1)) (2019.3)
        Collecting diff-match-patch
          Downloading https://pypi.doubanio.com/packages/f0/2a/5ba07def0e9107d935aba62cf632afbd0f7c723a98af47ccbcab753d2452/diff-match-patch-20181111.tar.gz (58kB)
             |████████████████████████████████| 61kB 4.1MB/s
        Collecting tablib<1.0.0
          Downloading https://pypi.doubanio.com/packages/7f/8d/665f895e4355f1ee95665e003b994512c8b670148a921aa9acec9d1607fb/tablib-0.14.0-py3-none-any.whl (65kB)
             |████████████████████████████████| 71kB 4.5MB/s
        Processing c:\users\lenovo\appdata\local\pip\cache\wheels\93\1b\9e\81e2e171818e99cccd906048e588b8888e1b607571c8f4254c\odfpy-1.4.0-py2.py3-none-any.whl
        Collecting markuppy
          Downloading https://pypi.doubanio.com/packages/4e/ca/f43541b41bd17fc945cfae7ea44f1661dc21ea65ecc944a6fa138eead94c/MarkupPy-1.14.tar.gz
        Collecting openpyxl>=2.4.0
          Downloading https://pypi.doubanio.com/packages/95/8c/83563c60489954e5b80f9e2596b93a68e1ac4e4a730deb1aae632066d704/openpyxl-3.0.3.tar.gz (172kB)
             |████████████████████████████████| 174kB 6.4MB/s
        Collecting pyyaml
          Downloading https://pypi.doubanio.com/packages/5e/17/512223ec8514cf9c5647dda4805c4dd051930ecb4d0fe744329061b00c00/PyYAML-5.3-cp36-cp36m-win32.whl (195kB)
             |████████████████████████████████| 204kB 3.3MB/s
        Collecting xlwt
          Downloading https://pypi.doubanio.com/packages/44/48/def306413b25c3d01753603b1a222a011b8621aed27cd7f89cbc27e6b0f4/xlwt-1.3.0-py2.py3-none-any.whl (99kB)
             |████████████████████████████████| 102kB 6.4MB/s
        Collecting xlrd
          Downloading https://pypi.doubanio.com/packages/b0/16/63576a1a001752e34bf8ea62e367997530dc553b689356b9879339cf45a4/xlrd-1.2.0-py2.py3-none-any.whl (103kB)
             |████████████████████████████████| 112kB 6.4MB/s
        Collecting defusedxml
          Downloading https://pypi.doubanio.com/packages/06/74/9b387472866358ebc08732de3da6dc48e44b0aacd2ddaa5cb85ab7e986a2/defusedxml-0.6.0-py2.py3-none-any.whl
        Collecting jdcal
          Downloading https://pypi.doubanio.com/packages/f0/da/572cbc0bc582390480bbd7c4e93d14dc46079778ed915b505dc494b37c57/jdcal-1.4.1-py2.py3-none-any.whl
        Collecting et_xmlfile
          Downloading https://pypi.doubanio.com/packages/22/28/a99c42aea746e18382ad9fb36f64c1c1f04216f41797f2f0fa567da11388/et_xmlfile-1.0.1.tar.gz
        Building wheels for collected packages: future, httplib2, diff-match-patch, markuppy, openpyxl, et-xmlfile
          Building wheel for future (setup.py) ... done
          Created wheel for future: filename=future-0.15.2-cp36-none-any.whl size=487094 sha256=5553edc0b3720cd9ad8c5c463d31829267574ad58294fd7698b882ac071028ce
          Stored in directory: C:\Users\Lenovo\AppData\Local\pip\Cache\wheels\11\5d\e5\383676505ad4b259e31059f59611cdecf7b7cf60c05c27ec17
          Building wheel for httplib2 (setup.py) ... done
          Created wheel for httplib2: filename=httplib2-0.9.2-cp36-none-any.whl size=84064 sha256=4b38b872d1f3f9eca8e04d3e6adee2fd8ffcf91e1b336113b1415e664d5b63f5
          Stored in directory: C:\Users\Lenovo\AppData\Local\pip\Cache\wheels\db\be\d4\44f191e38c9f4a73f4a488e831ce23990823b361208e5fba7e
          Building wheel for diff-match-patch (setup.py) ... done
          Created wheel for diff-match-patch: filename=diff_match_patch-20181111-cp36-none-any.whl size=58514 sha256=e4921fe8e2b5247996af543a32f6441a9218099b0e59cea9123ed0daa2a358b9
          Stored in directory: C:\Users\Lenovo\AppData\Local\pip\Cache\wheels\77\7f\da\dbf25d236a126ac9a0ea0be62510a12d5a7477fbcf23e61766
          Building wheel for markuppy (setup.py) ... done
          Created wheel for markuppy: filename=MarkupPy-1.14-cp36-none-any.whl size=7420 sha256=6c7c2a0f5cc20168d2ca985cafb15530ba0d837a0a8a0f9e77397ae1b253feb7
          Stored in directory: C:\Users\Lenovo\AppData\Local\pip\Cache\wheels\7b\29\72\f724cfc3eb15a5ebcaee6e8e660ab608da0f405c90c15e8eee
          Building wheel for openpyxl (setup.py) ... done
          Created wheel for openpyxl: filename=openpyxl-3.0.3-py2.py3-none-any.whl size=241267 sha256=eebe0f55679f908815f5361f5bbc3d38fec86ca8e9e1c3f192f0b6a131c983fa
          Stored in directory: C:\Users\Lenovo\AppData\Local\pip\Cache\wheels\d2\d8\e7\e195c0be178eb28bae777dcd21badbb67de007312ee2528998
          Building wheel for et-xmlfile (setup.py) ... done
          Created wheel for et-xmlfile: filename=et_xmlfile-1.0.1-cp36-none-any.whl size=8921 sha256=2013a1727c47d8a0a602ad4d52e50ccca7ecb04c405f26ca472ffddcfb0db87b
          Stored in directory: C:\Users\Lenovo\AppData\Local\pip\Cache\wheels\f3\9c\d1\7da7bea92fe95c9b8f52402c5b57bb418f949e49627fbb6f08
        Successfully built future httplib2 diff-match-patch markuppy openpyxl et-xmlfile
        Installing collected packages: diff-match-patch, defusedxml, odfpy, markuppy, jdcal, et-xmlfile, openpyxl, pyyaml, xlwt, xlrd, tablib, django-import-export, django-reversion, django-formtools, future, httplib2, six
        Successfully installed defusedxml-0.6.0 diff-match-patch-20181111 django-formtools-2.1 django-import-export-2.0.1 django-reversion-3.0.5 et-xmlfile-1.0.1 future-0.15.2 httplib2-0.9.2 jdcal-1.4.1 markuppy-1.14 odfpy-1.4.0 openpyxl-3.0.3 pyyaml-5.3 six-1.10.0 tablib-0.14.0 xlrd-1.2.0 xlwt-1.3.0

        (VueShop) E:\study\python\VueShop\MxShop\extra_apps\xadmin>
        --------------------------------------------------------------------------------------------------
    * 安装xadmin可选依赖包：xlwt xlsxwriter，这两个用于excel文件的导出
        --------------------------------------------------------------------------------------------------
        (VueShop) E:\study\python\VueShop\MxShop\extra_apps\xadmin>pip install xlwt xlsxwriter -i https://pypi.doubanio.com/simple/
        Looking in indexes: https://pypi.doubanio.com/simple/
        Requirement already satisfied: xlwt in e:\study\python\workon\vueshop\lib\site-packages (1.3.0)
        Collecting xlsxwriter
          Downloading https://pypi.doubanio.com/packages/0d/0c/4376ce9d0773c9969271419d4c843bf9b845d831a555f5abb6229e74ac1e/XlsxWriter-1.2.7-py2.py3-none-any.whl (141kB)
             |████████████████████████████████| 143kB 2.2MB/s
        Installing collected packages: xlsxwriter
        Successfully installed xlsxwriter-1.2.7
        --------------------------------------------------------------------------------------------------
    * 执行生成数据库三大步骤：
        * 运行Tools -> Run manage.py Task ->进入manage.py@MxShop
        * makemigrations
        * migrate
        然后，就可以在Navicat里mxshop数据库里面看到如下几个xadmin依赖的表：
            xadmin_bookmark
            xadmin_log
            xadmin_usersettings
            xadmin_userwidget
    * 配置xadmin: 打开MxShop/url.py，import xadmin，修改urlpatterns为如下配置：
        --------------------------------------------------------------------------------------------------
        import xadmin

        urlpatterns = [
            path('xadmin/', xadmin.site.urls),
        ]
        --------------------------------------------------------------------------------------------------
    * 创建超级管理用户：
        * 运行Tools -> Run manage.py Task ->进入manage.py@MxShop
        * createsuperuser
            --------------------------------------------------------------------------------------------------
            manage.py@MxShop > createsuperuser
            "D:\install\pycharm\PyCharm 2019.3\bin\runnerw64.exe" E:\study\python\workon\VueShop\Scripts\python.exe "D:\install\pycharm\PyCharm 2019.3\plugins\python\helpers\pycharm\django_manage.py" createsuperuser E:/study/python/VueShop/MxShop
            Tracking file by folder pattern:  migrations
            Username:  ptkang
            邮箱:  kpt205@163.com
            Warning: Password input may be echoed.
            Password:  linux123
            Warning: Password input may be echoed.
            Password (again):  linux123
            E:\study\python\workon\VueShop\lib\site-packages\django\db\models\fields\__init__.py:1423: RuntimeWarning: DateTimeField UserProfile.add_time received a naive datetime (2020-01-17 23:21:45.061078) while time zone support is active.
              RuntimeWarning)
            Superuser created successfully.

            Process finished with exit code 0
            --------------------------------------------------------------------------------------------------
        * 运行MxShop
        * 在浏览器打开：http://127.0.0.1:8000/xadmin/
            注意http://127.0.0.1:8000/后面一定要跟xadmin/
        * 设置英语到汉语显示：将原始的默认时区设置为北京时间
            * 原始默认:
                --------------------------------------------------------------------------------------------------
                LANGUAGE_CODE = 'en-us'

                TIME_ZONE = 'UTC'

                USE_I18N = True

                USE_L10N = True

                USE_TZ = True
                --------------------------------------------------------------------------------------------------
                * 设置为北京时区
                --------------------------------------------------------------------------------------------------
                \#设置时区
                LANGUAGE_CODE = 'zh-hans'  #中文支持，django1.8以后支持；1.8以前是zh-cn
                TIME_ZONE = 'Asia/Beijing'
                USE_I18N = True
                USE_L10N = True
                USE_TZ = False   #默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！
                --------------------------------------------------------------------------------------------------
            * 商品分类设置从英文设置为中文，即在每个app/设计表/migrations/apps.py里添加verbose_name，
                比如对用户表，添加如下：
                class UsersConfig(AppConfig):
                    name = 'apps.users'
                    verbose_name = '用户管理'

# 三、 导入商品类别数据和商品数据
    1. 从coding-131\MxShop\media里面的goods, brands, banner, message数据拷贝到VueShop\MxShop\media里面
    2. 配置MxShop\Settings.py里media相关的环境：
        MEDIA_URL = "/media/"
        MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    3. 配置MxShop\urls.py,将media添加到urlpattern里面
        from django.conf.urls import url, include
        from MxShop.settings import MEDIA_ROOT
        from django.views.static import serve
        url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
        注意要将urlpattern里面的path改为url，故需要注释到from django.urls import path，
        声明 from django.conf.urls import url, include
    3. 将从coding-131\MxShop\db_tools\data拷贝到VueShop\MxShop\db_tools里面
    4. 在db_tools下创建import_category_data.py和import_goods_data.py, 并编写导入数据库的脚本，
        或从coding-131\MxShop\db_tools\import_category_data.py和import_goods_data.py拷贝,
        并依次运行这两个py文件,运行完后可以到数据库里面查看是否有对应的数据，
        或从http://127.0.0.1:8000/xadmin/管理页面查看,
        注意：因goods外键依赖于category，所以要先执行import_category_data.py，再执行import_goods_data.py
