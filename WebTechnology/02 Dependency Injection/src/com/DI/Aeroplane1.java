package com.DI;

public class Aeroplane1 {
	
	Engine engine;

	public Aeroplane1(Engine engine) {
		this.engine = engine;
	}
	
	public void startEngine()
	{
		engine.start();
	}
}
