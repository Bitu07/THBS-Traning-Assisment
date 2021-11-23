
package com.abhi;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import com.abhi.component.Laptop;

public class Test {
	public static void main(String[] args)
	{
		ApplicationContext ac = new AnnotationConfigApplicationContext(SpringConfig.class);
		Laptop lp = (Laptop) ac.getBean("laptop");
		lp.boot();
	}
}
