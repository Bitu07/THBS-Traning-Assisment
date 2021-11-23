package com.DI;

public class Aeroplane {
	Engine engine;

	public Aeroplane(Engine engine) {
		this.engine = engine;
	}
	
	public void startEngine()
	{
		engine.start();
	}
}
