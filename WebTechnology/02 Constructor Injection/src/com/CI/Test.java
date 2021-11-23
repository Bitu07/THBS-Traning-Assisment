package com.CI;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test {

	public static void main(String[] args) {
			
		ApplicationContext ac = new ClassPathXmlApplicationContext("Spring.xml");
		Employee emp = (Employee) ac.getBean("emp");
		emp.show();
	}

}
