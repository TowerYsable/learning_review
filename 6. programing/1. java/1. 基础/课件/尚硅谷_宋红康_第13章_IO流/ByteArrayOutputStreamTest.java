package com.atguigu.java1;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

import org.junit.Test;

public class ByteArrayOutputStreamTest {

	@Test
	public void test1() throws Exception {
		FileInputStream fis = new FileInputStream("abc.txt");
		String info = readStringFromInputStream(fis);
		System.out.println(info);
	}

	private String readStringFromInputStream(FileInputStream fis) throws IOException {
		// 方式一：可能出现乱码
		// String content = "";
		// byte[] buffer = new byte[1024];
		// int len;
		// while((len = fis.read(buffer)) != -1){
		// content += new String(buffer);
		// }
		// return content;

		// 方式二：BufferedReader
		BufferedReader reader = new BufferedReader(new InputStreamReader(fis));
		char[] buf = new char[10];
		int len;
		String str = "";
		while ((len = reader.read(buf)) != -1) {
			str += new String(buf, 0, len);
		}
		return str;

		// 方式三：避免出现乱码
		// ByteArrayOutputStream baos = new ByteArrayOutputStream();
		// byte[] buffer = new byte[10];
		// int len;
		// while ((len = fis.read(buffer)) != -1) {
		// baos.write(buffer, 0, len);
		// }
		//
		// return baos.toString();
	}
}
