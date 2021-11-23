package com.abhi.SpringMVC.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.abhi.SpringMVC.model.Product;

@Repository
public interface ProductRepository extends JpaRepository<Product, Integer> {

}