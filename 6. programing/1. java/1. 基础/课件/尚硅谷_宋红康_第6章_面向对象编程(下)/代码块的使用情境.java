package com.atguigu.utils;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

import javax.sql.DataSource;

import org.apache.commons.dbcp.BasicDataSourceFactory;
import org.apache.commons.dbutils.DbUtils;

import com.atguigu.connection.DBCPTest;
import com.mchange.v2.c3p0.ComboPooledDataSource;


public class JDBCUtils {
	
	private static DataSource dataSource = null;
	static{
		InputStream is = null;
		try {
			is = DBCPTest.class.getClassLoader().getResourceAsStream("dbcp.properties");
			Properties pros = new Properties();
			pros.load(is);
			//调用BasicDataSourceFactory的静态方法，获取数据源。
			dataSource = BasicDataSourceFactory.createDataSource(pros);
		} catch (Exception e) {
			e.printStackTrace();
		}finally{
			if(is != null){
				try {
					is.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
				
			}
			
		}
		
	}
	//使用DBCP数据库连接池实现数据库的连接
	public static Connection getConnection2() throws SQLException{
		Connection conn = dataSource.getConnection();
		System.out.println(conn);
		return conn;
	}
	
}
