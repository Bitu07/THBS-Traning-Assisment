package com.abhi.MongoDbDemo.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.stereotype.Repository;

import com.abhi.MongoDbDemo.model.Product;

@Repository
public interface ProductRepository extends MongoRepository<Product, String> {

	@Query("{name : '?0'}")
	Product findProductByName(String name);

	@Query(value = "{category : '?0'}")
	List<Product> findAll(String category);

	public long count();
}