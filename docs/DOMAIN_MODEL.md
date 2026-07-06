# PrepFlow Domain Model

Version: 0.1  
Project Version: 0.6.2  
Sprint: 7 — Pack Standardization  

## Purpose

This document defines the core objects inside PrepFlow and how they relate to each other.

## Core Objects

### Question

A single standardized assessment item.

Owned by: PrepFlow  
Used by: Pack, Study Engine, Validator, Progress Tracker

### Pack

A collection of standardized Questions plus metadata.

Owned by: Compiler  
Used by: Study Engine, Validator, GUI

### Answer

The grading structure attached to a Question.

Owned by: Question  
Used by: Study Engine, Validator

### Origin

The source history of a Question.

Owned by: Question  
Used by: Compiler, Validator, Audit tools

### Classification

Concepts, tags, body systems, difficulty, and learning categories attached to a Question.

Owned by: Question  
Used by: Study Engine, Analytics, Adaptive Quiz Engine

### Session

A study run using one or more Packs.

Owned by: Study Engine  
Used by: Progress Tracker

### Attempt

One learner response to one Question.

Owned by: Session  
Used by: Progress Tracker, Analytics

### Progress Record

A learner’s history with a Question.

Owned by: Progress Tracker  
Used by: Study Engine, Analytics, Adaptive Quiz Engine

## Pipeline Objects

### Importer

Reads a source file and extracts raw content.

### Parser

Interprets raw content into structured question data.

### Compiler

Converts parsed data into canonical PrepFlow Questions and Packs.

### Validator

Checks Questions and Packs against PrepFlow rules.

## Relationship Summary

Source file → Importer → Parser → Compiler → Pack → Study Engine → Session → Attempts → Progress Records

## Sprint 7 Focus

Sprint 7 standardizes Question and Pack structure before adding new features.