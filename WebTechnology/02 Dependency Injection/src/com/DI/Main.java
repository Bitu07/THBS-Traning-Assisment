package com.DI;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main {

	public static void main(String[] args) {
		ApplicationContext ac = new ClassPathXmlApplicationContext("beans.xml");
		
//		Bike bike = (Bike) ac.getBean("bike");
//		bike.showcolor();
		
//		Car car = (Car) ac.getBean("car");
//		car.showcolor();
		
		Aeroplane ae = ac.getBean("aeroplane",Aeroplane.class);
		ae.startEngine();
	
		
		Aeroplane1 ae1 = ac.getBean("aeroplane1",Aeroplane1.class);
		ae1.startEngine();
		

	}
	

}
