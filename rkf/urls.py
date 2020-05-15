"""rkf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from dashboardapp import views as d_views
from itemapp import views as i_views
from userapp import views as u_views
from codeapp import views as c_views
from salesmanapp import views as s_views
from stockapp import views as stock_views
from loginapp import views as l_views
from actionapp import views as a_views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Service Worker URL
    re_path(r'^service-worker.js', (TemplateView.as_view(template_name="service-worker.js", content_type='application/javascript', )), name='service-worker.js'),

    #Admin URL
    path('admin/', admin.site.urls),

    #Dashboard URL
    path('dashboard/', d_views.dash_views),
    path('lowstock/', d_views.lowitem_views),

    #Items URL
    path('items/', i_views.items_views),
    path('shop/', i_views.shop_views),
    path('search/', i_views.seacrh_views),
    path('items_submit/', i_views.items_submit_views),
    path('items_details/', i_views.item_detail_views),
    path('items_search/', i_views.search_item_views),
    path('restock/', i_views.restock_views),
    path('dumpstock/', i_views.dumpstock_views),
    path('ajax/get_item_info/', i_views.getItemsInfo, name="get_item_info"),

    #Stock URL
    path('stock/', stock_views.stockaudit_views),
    path('report/', stock_views.stock_report_views),
    path('report/render/pdf/', stock_views.Pdf.as_view()),

    #User URL
    path('users/', u_views.users_views, name="users"),
    path('user/update/<int:id>/', u_views.update_views),
    path('user/delete/<int:id>/', u_views.delete_views),
    path('search_users/', u_views.search_user_views, name="search_users"),
    path('sales_record/', u_views.sales_user_record_views, name="sales_record"),
    path('ajax/get_user_info', u_views.get_User_views, name = 'get_user_info'),

    #Barcode URL
    path('code/', c_views.code_views),
    path('code_submit/<int:id>', c_views.qrbar_views),

    #Sales URL
    path('salesman/', s_views.salesman_views),
    path('update/<int:id>', s_views.sale_udate_views),
    path('delete/<int:id>', s_views.sale_delete_views),
    path('salesearch/', s_views.sale_search_views),
    path('return/', s_views.return_search_views),
    path('salegraph/', s_views.sale_graph_views),
    path('ajax/get_item_name/', s_views.get_iname_views, name = 'get_item_name'),
    path('salesearch/pdf/', s_views.PdfSale.as_view()),

    #Login Logou URL
    path('login/', l_views.login_views, name="login"),
    path('logout/', l_views.logout_views),
    path('', l_views.login_page_views),

    #Action URL
    path('iupdate/<int:id>', a_views.item_update_views),
    path('iedit/', a_views.item_edit_views),
    path('idelete/<int:id>', a_views.item_delete_views),

    #Password Reset
    path('reset/password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset/password/sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')




]
