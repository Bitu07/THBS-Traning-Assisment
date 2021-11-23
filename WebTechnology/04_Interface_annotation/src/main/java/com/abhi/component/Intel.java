package com.abhi.component;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

@Component("intel")
@Primary
public class Intel implements Processor {

	@Override
	public void doprocessing() {
		System.out.println("Intel i9th gen");
		
	}

}
