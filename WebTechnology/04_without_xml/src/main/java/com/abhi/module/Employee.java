package com.abhi.module;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import com.abhi.module.Address;

//@Component
public class Employee {

//	@Value("100")
	private int id;
	
//	@Value("Abhishek Yadav")
	private String name;
	@Autowired
	private Address address;
	
	public Employee() {	}	

	public Employee(int id, String name, Address address) {
		super();
		this.id = id;
		this.name = name;
		this.address = address;
	}



	public void display()
	{
		System.out.println("hello");
		System.out.println(id + " " + name);
		System.out.println(this.address);

	}

}
