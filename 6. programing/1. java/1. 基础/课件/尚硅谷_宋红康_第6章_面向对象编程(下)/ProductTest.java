package com.atguigu.java;

public class ProductTest {

	public static void main(String[] args) {
		TestProduct tp = new TestProduct();
		Product p = tp.getProduct();

		System.out.println(p.getName());
		System.out.println(p.getPrice());
		// ----------------------
		tp.showProduct(p);
		// ------------------------
		tp.showProduct(new Product() {// 创建了一个匿名类的对象。
			public int getPrice() {
				return 7899;
			}

			public String getName() {
				return "iphone5s-土豪金";
			}

		});
	}

	public Product getProduct() {
		// 创建了一个局部内部类的对象
		// class MyProduct implements Product{
		//
		// @Override
		// public int getPrice() {
		// // TODO Auto-generated method stub
		// return 3899;
		// }
		//
		// @Override
		// public String getName() {
		// // TODO Auto-generated method stub
		// return "ipad air";
		// }
		//
		// }
		// return new MyProduct();
		return new Product() {// 创建了一个匿名内部类的对象。
			public int getPrice() {
				return 7899;
			}

			public String getName() {
				return "iphone5s-土豪金";
			}

		};
	}

	public void showProduct(Product p) {
		System.out.println(p.getName());
		System.out.println(p.getPrice());
	}
}

interface Product {
	public abstract int getPrice();

	public abstract String getName();
}