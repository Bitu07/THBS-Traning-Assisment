package com.CI;

public class Address {
	private String city;
	private String state;
	private String Country;
	
	public Address(String city, String state, String country) {
		super();
		this.city = city;
		this.state = state;
		Country = country;
	}

	@Override
	public String toString() {
		return "Address [city=" + city + ", state=" + state + ", Country=" + Country + "]";
	}

}
