# Dự Án E-Commerce Django

Đây là dự án e-commerce được xây dựng bằng Django với cấu trúc đa ứng dụng. Dự án bao gồm các ứng dụng chính sau:

- **customer**: Quản lý đăng ký, đăng nhập và thông tin khách hàng (sử dụng MySQL).
- **cart**: Quản lý giỏ hàng.
- **order**: Xử lý đơn hàng.
- **book**: Quản lý sản phẩm sách (sử dụng MongoDB).
- **main**: Ứng dụng chứa trang chủ và các template chung.

## Mục Lục

- [Cấu Trúc Dự Án](#cấu-trúc-dự-án)
- [Yêu Cầu](#yêu-cầu)
- [Cài Đặt và Cấu Hình](#cài-đặt-và-cấu-hình)
  - [1. Thiết lập môi trường](#1-thiết-lập-môi-trường)
  - [2. Cài đặt các gói phụ thuộc](#2-cài-đặt-các-gói-phụ-thuộc)
  - [3. Cấu hình cơ sở dữ liệu](#3-cấu-hình-cơ-sở-dữ-liệu)
    - [MySQL cho app customer](#mysql-cho-app-customer)
    - [MongoDB cho app book](#mongodb-cho-app-book)
  - [4. Chạy migration và collect static](#4-chạy-migration-và-collect-static)
- [Chạy Ứng Dụng](#chạy-ứng-dụng)
- [Tính Năng Chính](#tính-năng-chính)
- [Giao Diện và CSS](#giao-diện-và-css)
- [License](#license)

## Yêu Cầu

- **Python 3.10+**
- **Django 5.1.6**
- **MySQL** cho app **customer** (với gói `mysqlclient`)
- **MongoDB** cho app **book** (với gói `mongoengine`)
- Các gói phụ thuộc khác (xem file `requirements.txt`)
