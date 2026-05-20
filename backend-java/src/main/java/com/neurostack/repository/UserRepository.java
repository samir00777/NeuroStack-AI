package com.neurostack.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.neurostack.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {}
