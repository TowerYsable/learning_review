package com.atguigu.java1;

import java.lang.annotation.Annotation;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

import org.junit.Test;

import com.atguigu.java.Person;

public class FieldMethodConstructorTest {

	@Test
	public void test1() {
//		showFields(Person.class);
		
		showMethods(Person.class);
	}

	// 注解
	// 权限修饰符 返回值类型 方法名(形参类型 变量名,....)throws 异常类型{}
	public void showMethods(Class clazz) {
		Method[] methods = clazz.getDeclaredMethods();
		for (Method m : methods) {
			// 1.注解
			Annotation[] annos = m.getAnnotations();
			for (Annotation a : annos) {
				System.out.println(a);
			}
			// 2.权限修饰符
			System.out.print(Modifier.toString(m.getModifiers()) + "\t");
			// 3. 返回值类型
			Class returnType = m.getReturnType();
			System.out.print(returnType.getName() + "\t");

			// 4.方法名
			System.out.print(m.getName() + "(");

			// 5.(形参类型 变量名,....)
			Class[] paras = m.getParameterTypes();
			for (int i = 0; i < paras.length; i++) {
				if (i == paras.length - 1) {
					System.out.print(paras[i].getName() + " args_" + i);
					break;
				}
				System.out.print(paras[i].getName() + " args_" + i + ",");
			}

			System.out.print(")");

			// 6. 异常类型
			Class[] exceptionTypes = m.getExceptionTypes();
			if (exceptionTypes != null && exceptionTypes.length != 0) {
				System.out.print(" throws ");
			}

			for (Class c : exceptionTypes) {
				System.out.print(c.getName() + "\t");
			}

			System.out.println();
		}
	}

	// 权限修饰符 类型 变量名
	public void showFields(Class clazz) {
		Field[] fields = clazz.getDeclaredFields();
		for (Field f : fields) {

			// 1.权限修饰符
			int modifier = f.getModifiers();
			System.out.print(Modifier.toString(modifier) + "\t");

			// 2.类型
			Class type = f.getType();
			System.out.print(type.getName() + "\t");

			// 3.变量名
			System.out.println(f.getName());
		}
	}

}
