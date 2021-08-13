package com.atguigu.java;
interface USB{		// 
	public void start() ;
	public void stop() ;	
}
class Computer{
	public static void show(USB usb){	
		usb.start() ;
		System.out.println("=========== USB 设备工作 ========") ;
		usb.stop() ;
	}
};
class Flash implements USB{
	public void start(){	// 重写方法
		System.out.println("U盘开始工作。") ;
	}
	public void stop(){		// 重写方法
		System.out.println("U盘停止工作。") ;
	}
};
class Print implements USB{
	public void start(){	// 重写方法
		System.out.println("打印机开始工作。") ;
	}
	public void stop(){		// 重写方法
		System.out.println("打印机停止工作。") ;
	}
};
public class InterfaceDemo{
	public static void main(String args[]){
		Computer.show(new Flash()) ;
		Computer.show(new Print()) ;

		c.show(new USB(){
			public void start(){
				System.out.println("移动硬盘开始运行");
			}
			public void stop(){
				System.out.println("移动硬盘停止运行");
			}
		});
	}
};