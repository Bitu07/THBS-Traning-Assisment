package com.abhi;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import com.abhi.module.Address;
import com.abhi.module.Employee;

@Configuration
//@ComponentScan(basePackages = "com.abhi")
public class SpringConfig {
	
	@Bean
	public Address getAddress()
	{
		Address a = new Address();
		
		a.setCity("Ankleshwar");
		a.setState("Gujarat");
		a.setCountry("India");
		
		return a;
	}
	
//	@Bean
	@Bean(name = {"emp"})
	public Employee getEmployee()
	{
		Employee e = new Employee();
		
		e.setId(101);
		e.setName("Abhi");
		e.setAddress(getAddress());
		
		return e;
	}

}
