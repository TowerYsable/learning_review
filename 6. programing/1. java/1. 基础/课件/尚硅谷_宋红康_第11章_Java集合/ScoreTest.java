package com.atguigu.exer;

/*
 * 请把学生名与考试分数录入到Set中，并按分数显示前三名成绩学员的名字.怎么用Set实现?
 */
import java.util.TreeSet;
import java.util.Scanner;
import org.junit.Test;


public class ScoreTest {
	private Scanner scanner;

	@Test
	public void test1() {
		scanner = new Scanner(System.in);
		TreeSet<Student> treeSet = new TreeSet<>();
		System.out.println("请输入学生的姓名和成绩，当输入为负数时结束输入");
		for (int i = 1;; i++) {
			int score = 0;
			System.out.println("请输入第" + i + "位学生的姓名：");
			String name = scanner.next();
			System.out.println("请输入第" + i + "位学生的成绩：(输入负数，结束录入)");
			try {
				score = scanner.nextInt();
			} catch (ClassCastException e) {
				// TODO: handle exception
				System.out.println("您输入的分数有误");
			}

			if (score < 0) {
				break;
			} else {
				treeSet.add(new Student(name, score));
			}

		}
		System.out.println("您输入的成绩生成成绩单结果：");
		for (Student student : treeSet) {
			System.out.println(student.getName() + "--->" + student.getScore());
		}
		// 前三名学生的姓名
		System.out.println("前三名学生的姓名为：");
		int count = 0;
		for (Student student : treeSet) {
			if (count == 3) {
				break;
			} else {
				System.out.println(student.getName() + "--->"
						+ student.getScore());
				count++;
			}

		}
	}
}

class Student implements Comparable<Student> {
	private String name;
	private int score;

	public Student(String name, int score) {
		super();
		this.name = name;
		this.score = score;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getScore() {
		return score;
	}

	public void setScore(int score) {
		this.score = score;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		result = prime * result + score;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Student other = (Student) obj;
		if (name == null) {
			if (other.name != null)
				return false;
		} else if (!name.equals(other.name))
			return false;
		if (score != other.score)
			return false;
		return true;
	}

	@Override
	public int compareTo(Student o) {
		// TODO Auto-generated method stub
		int num = o.score - score;
		if (num != 0) {
			return num;
		} else {
			return this.name.compareTo(o.name);
		}
	}

}
