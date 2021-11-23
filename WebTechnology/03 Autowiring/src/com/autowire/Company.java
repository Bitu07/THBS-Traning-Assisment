package com.autowire;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;

public class Company {
	
	@Autowired
	HRDept dept;
	
	public Company(HRDept dept)
	{
		this.dept = dept;
		System.out.println("cons...!!");
	}
	
	
	public void setDept(HRDept dept) {
		this.dept = dept;
		System.out.println("sett..!!");
	}


	public void companyWork()
	{
		if(dept == null)
		{
			System.out.println("No Client no Work");
		}
		else
		{
			dept.work();
		}
	}

}
