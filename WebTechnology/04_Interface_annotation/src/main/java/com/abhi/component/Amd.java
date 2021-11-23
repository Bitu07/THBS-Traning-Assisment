package com.abhi.component;

import org.springframework.stereotype.Component;

@Component("amd")

public class Amd implements Processor{

	@Override
	public void doprocessing() {
		System.out.println("Amd processor");
		
	}

}
