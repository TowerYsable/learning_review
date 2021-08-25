package com.atguigu.interview;

import java.util.concurrent.locks.ReentrantLock;

class Window implements Runnable{
	int ticket = 100;
	private final ReentrantLock lock = new ReentrantLock();
	public void run(){
		
		while(true){
			try{
				lock.lock();
				if(ticket > 0){
					try {
						Thread.sleep(10);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
					System.out.println(ticket--);
				}else{
					break;
				}
			}finally{
				lock.unlock();
			}
		}
	}
}

public class ThreadLock {
	public static void main(String[] args) {
		Window t = new Window();
		Thread t1 = new Thread(t);
		Thread t2 = new Thread(t);
		
		t1.start();
		t2.start();
	}
}
