package com.DI;

public class Car {
	String color;
	
	Car(String color)
	{
		this.color = color;
	}

//	public void setColor(String color) {
//		this.color = color;
//	}
//	
	public void showcolor()
	{
		System.out.println("Car color: " + color);
	}
}
