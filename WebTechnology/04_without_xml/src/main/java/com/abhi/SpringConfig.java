package com.abhi;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import com.abhi.module.Address;
import com.abhi.module.Employee;

@Configuration
//@ComponentScan(basePackages = ("com.abhi"))
public class SpringConfig {
	
	@Bean
	public Address getAddress()
	{
		return new Address("Ankleshwar","Gujarat", "India");
	}
	
	@Bean
	public Employee getEmployee()
	{
		return new Employee(101,"Abhishek",getAddress());    // factory bean : A method that returns instance of a class 
	}
	
}
