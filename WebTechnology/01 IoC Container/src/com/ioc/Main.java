package com.ioc;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

class keys
{
	public void run(Engine b)
	{
//		Bike b = new Bike();
//		Car b = new Car();
		b.Start();
	}
}
public class Main {

	public static void main(String[] args) {
//		Bike b = new Bike();        // 1 method
//		keys k = new keys();
//		k.run(b);
		
//		new keys().run(new Bike());        // 2 method
//		new keys().run(new Car());
		
		
//		Engine key = new Car();        // 3 method
//		new keys().run(key);

		
		ApplicationContext ac = new ClassPathXmlApplicationContext("beans.xml");        // 4th using beans
		
		Engine key = (Engine)ac.getBean("engine");
		new keys().run(key);
		
	}

}
