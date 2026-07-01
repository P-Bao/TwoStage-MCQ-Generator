## Object-Oriented and Classical Software Engineering

Eighth Edition 

Stephen R. Schach 

# Object-Oriented and Classical Software Engineering

Eighth Edition 

Stephen R. Schach Vanderbilt University 

## OBJECT-ORIENTED AND CLASSICAL SOFTWARE ENGINEERING, EIGHTH EDITION

Published by McGraw-Hill, a business unit of The McGraw-Hill Companies, Inc., 1221 Avenue of the Americas, New York, NY 10020. Copyright © 2011 by The McGraw-Hill Companies, Inc. All rights reserved. Previous editions © 2007, 2005, and 2002. No part of this publication may be reproduced or distributed in any form or by any means, or stored in a database or retrieval system, without the prior written consent of The McGraw-Hil Companies, Inc., including, but not limited to, in any network or other electronic storage or transmission, or broadcast for distance learning. 

Some ancillaries, including electronic and print components, may not be available to customers outside the United States. 

This book is printed on acid-free paper. 

1 2 3 4 5 6 7 8 9 0 DOC/DOC 1 0 9 8 7 6 5 4 3 2 1 0 

ISBN 978-0-07-337618-9 MHID 0-07-337618-3 

Vice President & Editor-in-Chief: Marty Lange Publisher: Raghothaman Srinivasan Vice President EDP & Central Publishing Services: Kimberly Meriwether David Development Editor: Lora Neyens Senior Marketing Manager: Curt Reynolds Project Manager: Melissa M. Leick Buyer: Kara Kudronowicz Design Coordinator: Brenda A. Rolwes Cover Designer: Studio Montage, St. Louis, Missour Cover Image: © Photodisc/Getty Images Compositor: Glyph International Typeface: 10/12 Times Roman Printer: R. R. Donnelley 

All credits appearing on page or at the end of the book are considered to be an extension of the copyright page. 

Library of Congress Cataloging-in-Publication Data 

Schach, Stephen R. Object-oriented and classical software engineering / Stephen R. Schach. — 8th ed. p. cm. ISBN-13: 978-0-07-337618-9 (alk. paper) ISBN-10: 0-07-337618-3 (alk. paper) 1. Software engineering. 2. Object-oriented programming (Computer science) 3. UML (Computer science) 4. C++ (Computer program language) I. Title. QA76.758.S318 2010 005.1’17—dc22 

2010020995 

To Jackson and Mikaela 

The following are registered trademarks: 

<table><tr><td>ADF</td><td>Jackpot Source Code Metrics</td><td>Rational</td></tr><tr><td>Analyst/Designer</td><td>Java</td><td>Requisite Pro</td></tr><tr><td>Ant</td><td>JBuilder</td><td>Rhapsody</td></tr><tr><td>Apache</td><td>JUnit</td><td>Rose</td></tr><tr><td>Apple</td><td>Linux</td><td>SBC Communications</td></tr><tr><td>AS/400</td><td>Lotus 1-2-3</td><td>SilkTest</td></tr><tr><td>AT&amp;T</td><td>Lucent Technologies</td><td>SLAM</td></tr><tr><td>Bachman Product Set</td><td>MacApp</td><td>Software through Pictures</td></tr><tr><td>Bell Laboratories</td><td>Macintosh</td><td>Solaris</td></tr><tr><td>Borland</td><td>Macintosh Toolbox</td><td>SourceSafe</td></tr><tr><td>Bugzilla</td><td>MacProject</td><td>SPARCstation</td></tr><tr><td>Capability Maturity Model</td><td>Microsoft</td><td>Sun</td></tr><tr><td>Chrome</td><td>Motif</td><td>Sun Enterprise</td></tr><tr><td>ClearCase</td><td>MS-DOS</td><td>Sun Microsystems</td></tr><tr><td>ClearQuest</td><td>MVS/360</td><td>Sun ONE Studio</td></tr><tr><td>CMM</td><td>Natural</td><td>System Architect</td></tr><tr><td>Cocoa</td><td>Netscape</td><td>Together</td></tr><tr><td>Coca-Cola</td><td>New York Times</td><td>UNIX</td></tr><tr><td>CORBA</td><td>Object C</td><td>VAX</td></tr><tr><td>CppUnit</td><td>Objective-C</td><td>Visual Component Library</td></tr><tr><td>CVS</td><td>ObjectWindows Library</td><td>Visual C++</td></tr><tr><td>DB2</td><td>1-800-flowers.com</td><td>Visual J++</td></tr><tr><td>Eclipse</td><td>Oracle</td><td>VM/370</td></tr><tr><td>e-Components</td><td>Oracle Developer Suite</td><td>VMS</td></tr><tr><td>Emeraude</td><td>OS/360</td><td>Wall Street Journal</td></tr><tr><td>Enterprise JavaBeans</td><td>OS/370</td><td>WebSphere</td></tr><tr><td>eServer</td><td>OS/VS2</td><td>Win32</td></tr><tr><td>Excel</td><td>Palm Pilot</td><td>Windows 95</td></tr><tr><td>Firefox</td><td>Parasoft</td><td>Windows 2000</td></tr><tr><td>Focus</td><td>Post-It Note</td><td>Windows NT</td></tr><tr><td>Ford</td><td>PowerBuilder</td><td>Word</td></tr><tr><td>Foundation Class Library</td><td>PREfix</td><td>X11</td></tr><tr><td>FoxBASE</td><td>PREfast</td><td>Xrunner</td></tr><tr><td>GCC</td><td>Project</td><td>XUnit</td></tr><tr><td>Hewlett-Packard</td><td>PureCoverage</td><td>Zip disk</td></tr><tr><td>IBM</td><td>PVCS</td><td>ZIP Code</td></tr><tr><td>IMS/360</td><td>QARun</td><td>z10</td></tr></table>

## Contents

Preface xiii
Chapter 1
The Scope of Software Engineering 1
Learning Objectives 1
Historical Aspects 2
Economic Aspects 5
Maintenance Aspects 6
Classical and Modern Views of Maintenance 9
The Importance of Postdelivery Maintenance 10
Requirements, Analysis, and Design Aspects 12
Team Development Aspects 15
Why There Is No Planning Phase 16
Why There Is No Testing Phase 16
Why There Is No Documentation Phase 17
The Object-Oriented Paradigm 18
The Object-Oriented Paradigm in Perspective 22
Terminology 23
Ethical Issues 26
Chapter Review 27
For Further Reading 27
Key Terms 28
Problems 29
References 30
PART A
SOFTWARE ENGINEERING CONCEPTS 35
Chapter 2
Software Life-Cycle Models 37
Learning Objectives 37
Software Development in Theory 37
Winburg Mini Case Study 38
Lessons of the Winburg Mini Case Study 42
Teal Tractors Mini Case Study 42
Iteration and Incrementation 43
Winburg Mini Case Study Revisited 47
Risks and Other Aspects of Iteration and Incrementation 48
Managing Iteration and Incrementation 51
Other Life-Cycle Models 52
Code-and-Fix Life-Cycle Model 52
Waterfall Life-Cycle Model 53
Rapid-Prototyping Life-Cycle Model 55
Open-Source Life-Cycle Model 56
Agile Processes 59
Synchronize-and-Stabilize Life-Cycle Model 62
Spiral Life-Cycle Model 62
Comparison of Life-Cycle Models 66
Chapter Review 67
For Further Reading 68
Key Terms 69
Problems 69
References 70
Chapter 3
The Software Process 74
Learning Objectives 74
The Unified Process 76
Iteration and Incrementation within the Object-Oriented Paradigm 76
The Requirements Workflow 78
The Analysis Workflow 80
The Design Workflow 82
The Implementation Workflow 83
The Test Workflow 84
3.7.1 Requirements Artifacts 84
3.7.2 Analysis Artifacts 84
3.7.3 Design Artifacts 85
3.7.4 Implementation Artifacts 85
Postdelivery Maintenance 87 

3.9 Retirement 88 3.10 The Phases of the Unifi ed Process 88 3.10.1 The Inception Phase 89 3.10.2 The Elaboration Phase 91 3.10.3 The Construction Phase 92 3.10.4 The Transition Phase 92 3.11 One- versus Two-Dimensional Life-Cycle Models 92 3.12 Improving the Software Process 94 3.13 Capability Maturity Models 95 3.14 Other Software Process Improvement Initiatives 98 3.15 Costs and Benefi ts of Software Process Improvement 99 Chapter Review 101 For Further Reading 102 Key Terms 102 Problems 103 References 104 

## Chapter 4

## Teams 107

Learning Objectives 107 4.1 Team Organization 107 4.2 Democratic Team Approach 109 4.2.1 Analysis of the Democratic Team Approach 110 4.3 Classical Chief Programmer Team Approach 110 4.3.1 The New York Times Project 112 4.3.2 Impracticality of the Classical Chief Programmer Team Approach 113 4.4 Beyond Chief Programmer and Democratic Teams 113 4.5 Synchronize-and-Stabilize Teams 117 4.6 Teams for Agile Processes 118 4.7 Open-Source Programming Teams 118 4.8 People Capability Maturity Model 119 4.9 Choosing an Appropriate Team Organization 120 Chapter Review 121 For Further Reading 121 Key Terms 122 Problems 122 References 122 

## Chapter 5

The Tools of the Trade 124 Learning Objectives 124 5.1 Stepwise Refi nement 124 5.1.1 Stepwise Refi nement Mini Case Study 125 5.2 Cost–Benefi t Analysis 130 5.3 Divide-and-Conquer 132 5.4 Separation of Concerns 132 5.5 Software Metrics 133 5.6 CASE 134 5.7 Taxonomy of CASE 135 5.8 Scope of CASE 137 5.9 Software Versions 141 5.9.1 Revisions 141 5.9.2 Variations 142 5.10 Confi guration Control 143 5.10.1 Confi guration Control during Postdelivery Maintenance 145 5.10.2 Baselines 145 5.10.3 Confi guration Control during Development 146 5.11 Build Tools 146 5.12 Productivity Gains with CASE Technology 147 Chapter Review 149 For Further Reading 149 Key Terms 150 Problems 150 References 151 

## Chapter 6

## Testing 154

Learning Objectives 154 6.1 Quality Issues 155 6.1.1 Software Quality Assurance 156 6.1.2 Managerial Independence 156 6.2 Non-Execution-Based Testing 157 6.2.1 Walkthroughs 158 6.2.2 Managing Walkthroughs 158 6.2.3 Inspections 159 6.2.4 Comparison of Inspections and Walkthroughs 161 

6.2.5 Strengths and Weaknesses of Reviews 162 6.2.6 Metrics for Inspections 162 6.3 Execution-Based Testing 162 6.4 What Should Be Tested? 163 6.4.1 Utility 164 6.4.2 Reliability 164 6.4.3 Robustness 165 6.4.4 Performance 165 6.4.5 Correctness 166 6.5 Testing versus Correctness Proofs 167 6.5.1 Example of a Correctness Proof 167 6.5.2 Correctness Proof Mini Case Study 171 6.5.3 Correctness Proofs and Software Engineering 172 6.6 Who Should Perform Execution-Based Testing? 175 6.7 When Testing Stops 176 Chapter Review 176 For Further Reading 177 Key Terms 177 Problems 178 References 179 

## Chapter 7

From Modules to Objects 183 Learning Objectives 183 7.1 What Is a Module? 183 7.2 Cohesion 187 7.2.1 Coincidental Cohesion 187 7.2.2 Logical Cohesion 188 7.2.3 Temporal Cohesion 189 7.2.4 Procedural Cohesion 189 7.2.5 Communicational Cohesion 190 7.2.6 Functional Cohesion 190 7.2.7 Informational Cohesion 191 7.2.8 Cohesion Example 191 7.3 Coupling 192 7.3.1 Content Coupling 192 7.3.2 Common Coupling 193 7.3.3 Control Coupling 195 7.3.4 Stamp Coupling 195 7.3.5 Data Coupling 196 7.3.6 Coupling Example 197 7.3.7 The Importance of Coupling 198 

7.4 Data Encapsulation 199 7.4.1 Data Encapsulation and Development 201 7.4.2 Data Encapsulation and Maintenance 202 7.5 Abstract Data Types 207 7.6 Information Hiding 209 7.7 Objects 211 7.8 Inheritance, Polymorphism, and Dynamic Binding 215 7.9 The Object-Oriented Paradigm 217 Chapter Review 220 For Further Reading 221 Key Terms 221 Problems 221 References 222 

## Chapter 8

## Reusability and Portability 225 Reusability and Portability 225

Learning Objectives 225 8.1 Reuse Concepts 226 8.2 Impediments to Reuse 228 8.3 Reuse Case Studies 229 8.3.1 Raytheon Missile Systems Division 230 8.3.2 European Space Agency 231 8.4 Objects and Reuse 232 8.5 Reuse during Design and Implementation 232 8.5.1 Design Reuse 232 8.5.2 Application Frameworks 234 8.5.3 Design Patterns 235 8.5.4 Software Architecture 236 8.5.5 Component-Based Software Engineering 237 8.6 More on Design Patterns 237 8.6.1 FLIC Mini Case Study 238 8.6.2 Adapter Design Pattern 239 8.6.3 Bridge Design Pattern 240 8.6.4 Iterator Design Pattern 241 8.6.5 Abstract Factory Design Pattern 241 8.7 Categories of Design Patterns 245 8.8 Strengths and Weaknesses of Design Patterns 247 8.9 Reuse and the World Wide Web 248 

8.10 Reuse and Postdelivery Maintenance 249 8.11 Portability 250 8.11.1 Hardware Incompatibilities 250 8.11.2 Operating System Incompatibilities 251 8.11.3 Numerical Software Incompatibilities 251 8.11.4 Compiler Incompatibilities 253 8.12 Why Portability? 255 8.13 Techniques for Achieving Portability 256 8.13.1 Portable System Software 257 8.13.2 Portable Application Software 257 8.13.3 Portable Data 258 8.13.4 Model-Driven Architecture 259 Chapter Review 259 For Further Reading 260 Key Terms 261 Problems 261 References 263 

## CHAPTER 9

## Planning and Estimating 268

Learning Objectives 268 9.1 Planning and the Software Process 268 9.2 Estimating Duration and Cost 270 9.2.1 Metrics for the Size of a Product 272 9.2.2 Techniques of Cost Estimation 275 9.2.3 Intermediate COCOMO 278 9.2.4 COCOMO II 281 9.2.5 Tracking Duration and Cost Estimates 282 9.3 Components of a Software Project Management Plan 282 9.4 Software Project Management Plan Framework 284 9.5 IEEE Software Project Management Plan 286 9.6 Planning Testing 288 9.7 Planning Object-Oriented Projects 289 9.8 Training Requirements 290 9.9 Documentation Standards 291 9.10 CASE Tools for Planning and Estimating 292 9.11 Testing the Software Project Management Plan 292 

Chapter Review 292 For Further Reading 292 Key Terms 293 Problems 294 References 295 

## PART B

SOFTWARE LIFE CYCLE 299 

## Chapter 10

Learning Objective 301 10.1 Software Development: Theory versus Practice 301 10.2 Iteration and Incrementation 302 10.3 The Unifi ed Process 306 10.4 Workfl ow Overview 307 10.5 Teams 307 10.6 Cost–Benefi t Analysis 308 10.7 Metrics 308 10.8 CASE 308 10.9 Versions and Confi gurations 309 10.10 Testing Terminology 309 10.11 Execution-Based and Non-Execution-Based Testing 309 10.12 Modularity 310 10.13 Reuse 310 10.14 Software Project Management Plan 310 Chapter Review 311 Key Terms 311 Problems 312 

## Chapter 11 Requirements 313

Learning Objectives 313 11.1 Determining What the Client Needs 313 11.2 Overview of the Requirements Workfl ow 314 11.3 Understanding the Domain 315 11.4 The Business Model 316 11.4.1 Interviewing 316 11.4.2 Other Techniques 317 11.4.3 Use Cases 318 

11.5 Initial Requirements 319 11.6 Initial Understanding of the Domain: The MSG Foundation Case Study 320 11.7 Initial Business Model: The MSG Foundation Case Study 322 11.8 Initial Requirements: The MSG Foundation Case Study 326 11.9 Continuing the Requirements Workfl ow: The MSG Foundation Case Study 328 11.10 Revising the Requirements: The MSG Foundation Case Study 330 11.11 The Test Workflow: The MSG Foundation Case Study 338 11.12 The Classical Requirements Phase 347 11.13 Rapid Prototyping 348 11.14 Human Factors 349 11.15 Reusing the Rapid Prototype 351 11.16 CASE Tools for the Requirements Workfl ow 353 11.17 Metrics for the Requirements Workfl ow 353 11.18 Challenges of the Requirements Workfl ow 354 Chapter Review 355 For Further Reading 356 Key Terms 357 Case Study Key Terms 357 Problems 357 References 358 

## Chapter 12 Chapter 12

Classical Analysis 360 Learning Objectives 360 12.1 The Specifi cation Document 360 12.2 Informal Specifi cations 362 12.2.1 Correctness Proof Mini Case Study Redux 363 12.3 Structured Systems Analysis 364 12.3.1 Sally’s Software Shop Mini Case Study 364 12.4 Structured Systems Analysis: The MSG Foundation Case Study 372 12.5 Other Semiformal Techniques 373 12.6 Entity-Relationship Modeling 374 

12.7 Finite State Machines 376 12.7.1 Finite State Machines: The Elevator Problem Case Study 378 12.8 Petri Nets 382 12.8.1 Petri Nets: The Elevator Problem Case Study 385 12.9 Z 387 12.9.1 Z: The Elevator Problem Case Study 388 12.9.2 Analysis of Z 390 12.10 Other Formal Techniques 392 12.11 Comparison of Classical Analysis Techniques 392 12.12 Testing during Classical Analysis 393 12.13 CASE Tools for Classical Analysis 394 12.14 Metrics for Classical Analysis 395 12.15 Software Project Management Plan: The MSG Foundation Case Study 395 12.16 Challenges of Classical Analysis 396 Chapter Review 396 For Further Reading 397 Key Terms 398 Case Study Key Terms 398 Problems 398 References 400 

Chapter 13 Object-Oriented Analysis 404 Learning Objectives 404 13.1 The Analysis Workfl ow 405 13.2 Extracting the Entity Classes 406 13.3 Object-Oriented Analysis: The Elevator Problem Case Study 407 13.4 Functional Modeling: The Elevator Problem Case Study 407 13.5 Entity Class Modeling: The Elevator Problem Case Study 410 13.5.1 Noun Extraction 411 13.5.2 CRC Cards 413 13.6 Dynamic Modeling: The Elevator Problem Case Study 414 13.7 The Test Workfl ow: Object-Oriented Analysis 417 13.8 Extracting the Boundary and Control Classes 424 

13.9 The Initial Functional Model: The MSG Foundation Case Study 425
13.10 The Initial Class Diagram: The MSG Foundation Case Study 428
13.11 The Initial Dynamic Model: The MSG Foundation Case Study 430
13.12 Revising the Entity Classes: The MSG Foundation Case Study 432
13.13 Extracting the Boundary Classes: The MSG Foundation Case Study 434
13.14 Extracting the Control Classes: The MSG Foundation Case Study 435
13.15 Use-Case Realization: The MSG Foundation Case Study 435
13.15.1 Estimate Funds Available for Week Use Case 436
13.15.2 Manage an Asset Use Case 442
13.15.3 Update Estimated Annual Operating Expenses Use Case 446
13.15.4 Produce a Report Use Case 449
13.16 Incrementing the Class Diagram: The MSG Foundation Case Study 454
13.17 The Test Workflow: The MSG Foundation Case Study 456
13.18 The Specification Document in the Unified Process 456
13.19 More on Actors and Use Cases 457
13.20 CASE Tools for the Object-Oriented Analysis Workflow 458
13.21 Metrics for the Object-Oriented Analysis Workflow 459
13.22 Challenges of the Object-Oriented Analysis Workflow 459
Chapter Review 460
For Further Reading 461
Key Terms 462
Problems 462
References 463

Chapter 14
Design 465

Learning Objectives 465
Design and Abstraction 466
Operation-Oriented Design 466

14.3 Data Flow Analysis 467
14.3.1 Mini Case Study Word Counting 468
14.3.2 Data Flow Analysis Extensions 473
14.4 Transaction Analysis 473
14.5 Data-Oriented Design 475
14.6 Object-Oriented Design 476
14.7 Object-Oriented Design: The Elevator Problem Case Study 477
14.8 Object-Oriented Design: The MSG Foundation Case Study 481
14.9 The Design Workflow 483
14.10 The Test Workflow: Design 487
14.11 The Test Workflow: The MSG Foundation Case Study 488
14.12 Formal Techniques for Detailed Design 488
14.13 Real-Time Design Techniques 488
14.14 CASE Tools for Design 490
14.15 Metrics for Design 490
14.16 Challenges of the Design Workflow 491 Chapter Review 492 For Further Reading 493 Key Terms 493 Problems 494 References 495

Chapter 15
Implementation 498

Learning Objectives 498
Choice of Programming Language 498
Fourth-Generation Languages 501 Good Programming Practice 504
15.1 Choice of Programming Language 498
15.2 Fourth-Generation Languages 501
15.3 Good Programming Practice 504
15.3.1 Use of Consistent and Meaningful Variable Names 504
15.3.2 The Issue of Self-Documenting Code 505
15.3.3 Use of Parameters 507
15.3.4 Code Layout for Increased Readability 507
15.3.5 Nested if Statements 507

Coding Standards 509
Code Reuse 510
Integration 510

Learning Objectives 465
Design and Abstraction 466
Operation-Oriented Design 466 

15.6.4 Integration of Object-Oriented Products 514 15.6.5 Management of Integration 515 15.7 The Implementation Workfl ow 516 15.8 The Implementation Workfl ow: The MSG Foundation Case Study 516 15.9 The Test Workfl ow: Implementation 516 15.10 Test Case Selection 517 15.10.1 Testing to Specifi cations versus Testing to Code 517 15.10.2 Feasibility of Testing to Specifi cations 517 15.10.3 Feasibility of Testing to Code 518 15.11 Black-Box Unit-Testing Techniques 520 15.11.1 Equivalence Testing and Boundary Value Analysis 521 15.11.2 Functional Testing 522 15.12 Black-Box Test Cases: The MSG Foundation Case Study 523 15.13 Glass-Box Unit-Testing Techniques 525 15.13.1 Structural Testing: Statement, Branch, and Path Coverage 526 15.13.2 Complexity Metrics 527 15.14 Code Walkthroughs and Inspections 528 15.15 Comparison of Unit-Testing Techniques 528 15.16 Cleanroom 529 15.17 Potential Problems When Testing Objects 530 15.18 Management Aspects of Unit Testing 533 15.19 When to Reimplement Rather than Debug a Code Artifact 533 15.20 Integration Testing 535 15.21 Product Testing 535 15.22 Acceptance Testing 536 15.23 The Test Workflow: The MSG Foundation Case Study 537 15.24 CASE Tools for Implementation 537 15.24.1 CASE Tools for the Complete Software Process 538 15.24.2 Integrated Development Environments 538 15.24.3 Environments for Business Applications 539 15.24.4 Public Tool Infrastructures 540 15.24.5 Potential Problems with Environments 540 

15.25 CASE Tools for the Test Workfl ow 540 15.26 Metrics for the Implementation Workfl ow 541 15.27 Challenges of the Implementation Workfl ow 542 Chapter Review 542 For Further Reading 543 Key Terms 544 Problems 545 References 547 

## Chapter 16

Postdelivery Maintenance 551 Learning Objectives 551 16.1 Development and Maintenance 551 16.2 Why Postdelivery Maintenance Is Necessary 553 16.3 What Is Required of Postdelivery Maintenance Programmers? 553 16.4 Postdelivery Maintenance Mini Case Study 555 16.5 Management of Postdelivery Maintenance 557 16.5.1 Defect Reports 557 16.5.2 Authorizing Changes to the Product 558 16.5.3 Ensuring Maintainability 559 16.5.4 Problem of Repeated Maintenance 559 16.6 Maintenance of Object-Oriented Software 560 16.7 Postdelivery Maintenance Skills versus Development Skills 563 16.8 Reverse Engineering 563 16.9 Testing during Postdelivery Maintenance 564 16.10 CASE Tools for Postdelivery Maintenance 565 16.11 Metrics for Postdelivery Maintenance 566 16.12 Postdelivery Maintenance: The MSG Foundation Case Study 566 16.13 Challenges of Postdelivery Maintenance 566 Chapter Review 566 For Further Reading 567 

Key Terms 567 Problems 567 References 568 

Chapter 17 More on UML 571 Learning Objectives 571 17.1 UML Is Not a Methodology 571 17.2 Class Diagrams 572 17.2.1 Aggregation 573 17.2.2 Multiplicity 574 17.2.3 Composition 575 17.2.4 Generalization 576 17.2.5 Association 576 17.3 Notes 577 17.4 Use-Case Diagrams 577 17.5 Stereotypes 577 17.6 Interaction Diagrams 579 17.7 Statecharts 581 17.8 Activity Diagrams 583 17.9 Packages 585 17.10 Component Diagrams 586 17.11 Deployment Diagrams 586 17.12 Review of UML Diagrams 587 17.13 UML and Iteration 587 Chapter Review 587 For Further Reading 588 Key Terms 588 Problems 588 References 589 

Chapter 18 Emerging Technologies 590 Learning Objectives 590 18.1 Aspect-Oriented Technology 591 18.2 Model-Driven Technology 593 18.3 Component-Based Technology 594 18.4 Service-Oriented Technology 594 18.5 Comparison of Service-Oriented and Component-Based Technology 595 18.6 Social Computing 596 18.7 Web Engineering 596 

18.8 Cloud Technology 597 18.9 Web 3.0 598 18.10 Computer Security 598 18.11 Model Checking 598 18.12 Present and Future 599 Chapter Review 599 For Further Reading 599 Key Terms 599 References 600 

Bibliography 601 Appendix A Term Project: Chocoholics Anonymous 627 Appendix B Software Engineering Resources 630 Appendix C Requirements Workflow: The MSG Foundation Case Study 632 Appendix D Structured Systems Analysis: The MSG Foundation Case Study 633 Appendix E Analysis Workflow: The MSG Foundation Case Study 636 Appendix F Software Project Management Plan: The MSG Foundation Case Study 637 Appendix G Design Workflow: The MSG Foundation Case Study 642 Appendix H Implementation Workflow: The MSG Foundation Case Study (C++ Version) 647 Appendix I Implementation Workflow: The MSG Foundation Case Study (Java Version) 648 Appendix J Test Workflow: The MSG Foundation Case Study 649 

Author Index 651 

Subject Index 654 

Almost every computer science and computer engineering curriculum now includes a required team-based software development project. In some cases, the project is only one semester or quarter in length, but a year-long team-based software development project is fast becoming the norm. 

In an ideal world, every student would complete a course in software engineering before starting his or her team-based project (“two-stage curriculum”). In practice, however, many students have to start their projects partway through their software engineering course, or even at the beginning of the course (“parallel curriculum”). 

As explained in the next section, this book is organized in such a way that it can be used for both curricula. 

## How the Eighth Edition Is Organized


The book comprises two main parts: Part B teaches the students how to develop a software product; Part A provides the necessary theoretical background for Part B. The 18 chapters are organized as follows:


<table><tr><td></td><td>Chapter 1</td><td>Introduction to software engineering</td></tr><tr><td>Part A</td><td>Chapters 2 through 9</td><td>Software engineering concepts</td></tr><tr><td>Part B</td><td>Chapters 10 through 17</td><td>Software engineering techniques</td></tr><tr><td></td><td>Chapter 18</td><td>Emerging technologies</td></tr></table>

Chapter 10 is new. It contains a summary of the key material of Part A. When the two-stage curriculum is followed, the instructor teaches fi rst Part A and then Part B (omitting Chapter 10, because the material of Chapter 10 will have been covered in depth in Part A). For the parallel curriculum, the instructor fi rst teaches Part B (so that the students can start their projects as soon as possible), and then Part A. The material of Chapter 10 enables the students to understand Part B without fi rst covering Part A. 

This latter approach seems counterintuitive: Surely theory should always be taught before practice. In fact, curricular issues have forced many of the instructors who have used the seventh edition of this book to teach the material of Part B before Part A. Surprisingly, they have been most satisfi ed with the outcome. They report that their students have a greater appreciation of the theoretical material of Part A as a consequence of their project work. That is, team-based project work makes students more receptive to and understanding of the theoretical concepts that underlie software engineering. 

In more detail, the material of the eighth edition may be taught in the following two ways: 

## 1. Two-Stage Curriculum

<table><tr><td></td><td>Chapter 1 (Introduction to software engineering)</td></tr><tr><td>Part A</td><td>Chapters 2 through 9 (Software engineering concepts)</td></tr><tr><td rowspan="3">Part B</td><td>Chapters 11 through 17 (Software engineering techniques)</td></tr><tr><td>Chapter 18 (Emerging technologies)</td></tr><tr><td>The students then commence their team-based projects in the following semester or quarter.</td></tr></table>

## 2. Parallel Curriculum

<table><tr><td rowspan="3"></td><td>Chapter 1 (Introduction to software engineering)</td></tr><tr><td>Chapter 10 (Key material from Part A)</td></tr><tr><td>The students now commence their team-based projects, in parallel with studying the material of Part B.</td></tr><tr><td>Part B</td><td>Chapters 11 through 17 (Software engineering techniques)</td></tr><tr><td rowspan="2">Part A</td><td>Chapters 2 through 9 (Software engineering concepts)</td></tr><tr><td>Chapter 18 (Emerging technologies)</td></tr></table>

## New Features of the Eighth Edition

• The book has been updated throughout. 

• I have added two new chapters. As previously explained, Chapter 10, a summary of key points of Part A, has been included so that this book can be used when students start their team-based term projects in parallel with their software engineering course. The other new chapter, Chapter 18, gives an overview of 10 emerging technologies, including 

• Aspect-oriented technology 

• Model-driven technology 

• Component-based technology 

• Service-oriented technology 

• Social computing 

• Web engineering 

• Cloud technology 

• Web 3.0 

• Computer security 

• Model checking 

• I have considerably expanded the material on design patterns in Chapter 8, including a new mini case study. 

• Two theoretical tools have been added to Chapter 5: divide-and-conquer, and separation of concerns. 

• The object-oriented analysis of the elevator problem of Chapter 13 now refl ects a modern distributed, decentralized architecture. 

• The references have been extensively updated, with an emphasis on current research. 

• There are well over 100 new problems. 

• There are new Just in Case You Wanted to Know boxes. 

## Features Retained from the Seventh Edition

• The Unifi ed Process is still largely the methodology of choice for object-oriented software development. Throughout this book, the student is therefore exposed to both the theory and the practice of the Unifi ed Process. 

• In Chapter 1, the strengths of the object-oriented paradigm are analyzed in depth. 

• The iterative-and-incremental life-cycle model has been introduced as early as possible, namely, in Chapter 2. Furthermore, as with all previous editions, numerous other life-cycle models are presented, compared, and contrasted. Particular attention is paid to agile processes. 

• In Chapter 3 (“The Software Process”), the workfl ows (activities) and processes of the Unifi ed Process are introduced, and the need for two-dimensional life-cycle models is explained. 

• A wide variety of ways of organizing software teams are presented in Chapter 4 (“Teams”), including teams for agile processes and for open-source software development. 

• Chapter 5 (“The Tools of the Trade”) includes information on important classes of CASE tools. 

• The importance of continual testing is stressed in Chapter 6 (“Testing”). 

• Objects continue to be the focus of attention in Chapter 7 (“From Modules to Objects”). 

• Design patterns remain a central focus of Chapter 8 (“Reusability and Portability”). 

• The IEEE standard for software project management plans is again presented in Chapter 9 (“Planning and Estimating”). 

• Chapter 11 (“Requirements”), Chapter 13 (“Object-Oriented Analysis”), and Chapter 14 (“Design”) are largely devoted to the workfl ows (activities) of the Unifi ed Process. For obvious reasons, Chapter 12 (“Classical Analysis”) is largely unchanged. 

• The material in Chapter 15 (“Implementation”) clearly distinguishes between implementation and integration. 

• The importance of postdelivery maintenance is stressed in Chapter 16. 

• Chapter 17 provides additional material on UML to prepare the student thoroughly for employment in the software industry. This chapter is of particular use to instructors who utilize this book for the two-semester software engineering course sequence. In the second semester, in addition to developing the team-based term project or a capstone project, the student can acquire additional knowledge of UML, beyond what is needed for this book. 

• As before, there are two running case studies. The MSG Foundation case study and the Elevator Problem case study have been developed using the Unifi ed Process. As usual, Java and C++ implementations are available online at www.mhhe.com/schach. 

• In addition to the two running case studies that are used to illustrate the complete life cycle, eight mini case studies highlight specifi c topics, such as the moving target prob lem, stepwise refi nement, design patterns, and postdelivery maintenance. 

• In all the previous editions, I have stressed the importance of documentation, maintenance, reuse, portability, testing, and CASE tools. In this edition, all these concepts are stressed equally fi rmly. It is no use teaching students the latest ideas unless they appreciate the importance of the basics of software engineering. 

As in the seventh edition, particular attention is paid to object-oriented life-cycle models, object-oriented analysis, object-oriented design, management implications of the object-oriented paradigm, and the testing and maintenance of object-oriented software. Metrics for the object-oriented paradigm also are included. In addition, many briefer references are made to objects, a paragraph or even only a sentence in length. The reason is that the object-oriented paradigm is not just concerned with how the various phases are performed but rather permeates the way we think about software engineering. Object technology again pervades this book. 

• The software process is still the concept that underlies the book as a whole. To control the process, we have to be able to measure what is happening to the project. Accordingly, the emphasis on metrics continues. With regard to process improvement, the material on the capability maturity model (CMM), ISO/IEC 15504 (SPICE), and ISO/IEC 12207 has been retained. 

• The book is still language independent. The few code examples are presented in C++ and Java, and I have made every effort to smooth over language-dependent details and ensure that the code examples are equally clear to C++ and Java users. For example, instead of using cout for C++ output and System.out.println for Java output, I have utilized the pseudocode instruction print . (The one exception is the new case study, where complete implementation details are given in both C++ and Java, as before.) 

• As in the seventh edition, this book contains over 600 references. I have selected current research papers as well as classic articles and books whose message remains fresh and relevant. There is no question that software engineering is a rapidly moving fi eld, and students therefore need to know the latest results and where in the literature to fi nd them. At the same time, today’s cutting-edge research is based on yesterday’s truths, and I see no reason to exclude an older reference if its ideas are as applicable today as they originally were. 

• With regard to prerequisites, it is assumed that the reader is familiar with a high-level programming language such as C, C#, C++, or Java. In addition, the reader is expected to have taken a course in data structures. 

## Why the Classical Paradigm Is Still Included

There is now almost unanimous agreement that the object-oriented paradigm is superior to the classical paradigm. Accordingly, many instructors who adopted the seventh edition of Object-Oriented and Classical Software Engineering chose to teach only the objectoriented material in that book. However, when asked, instructors indicated that they prefer to adopt a text that includes the classical paradigm. 

The reason is that, even though more and more instructors teach only the object-oriented paradigm, they still refer to the classical paradigm in class; many object-oriented techniques are hard for the student to understand unless that student has some idea of the classical techniques from which those object-oriented techniques are derived. For example, understanding entityclass modeling is easier for the student who has been introduced, even superfi cially, to entityrelationship modeling. Similarly, a brief introduction to fi nite state machines makes it easier for the instructor to teach statecharts. Accordingly, I have retained classical material in the eighth edition, so that instructors have classical material available for pedagogical purposes. 

## The Problem Sets

As in the seventh edition, this book has fi ve types of problems. First, there are running object-oriented analysis and design projects at the end of Chapters 11, 13, and 14. These have been included because the only way to learn how to perform the requirements, analysis, and design workfl ows is from extensive hands-on experience. 

Second, the end of each chapter contains a number of exercises intended to highlight key points. These exercises are self-contained; the technical information for all the exercises can be found in this book. 

Third, there is a software term project. It is designed to be solved by students working in teams of three, the smallest number of team members that cannot confer over a standard telephone. The term project comprises 15 separate components, each tied to the relevant chapter. For example, design is the topic of Chapter 14, so in that chapter the component of the term project is concerned with software design. By breaking a large project into smaller, well-defi ned pieces, the instructor can monitor the progress of the class more closely. The structure of the term project is such that an instructor may freely apply the 15 components to any other project that he or she chooses. 

Because this book has been written for use by graduate students as well as upper-class undergraduates, the fourth type of problem is based on research papers in the software engineering literature. In each chapter, an important paper has been chosen; wherever possible, a paper related to object-oriented software engineering has been selected. The student is asked to read the paper and answer a question relating to its contents. Of course, the instructor is free to assign any other research paper; the For Further Reading section at the end of each chapter includes a wide variety of relevant papers. 

The fi fth type of problem relates to the case study. This type of problem was fi rst introduced in the third edition in response to a number of instructors who felt that their students learn more by modifying an existing product than by developing a new product from scratch. Many senior software engineers in the industry agree with that viewpoint. Accordingly, each chapter in which the case study is presented has problems that require the student to modify the case study in some way. For example, in one chapter the student is asked to redesign the case study using a different design technique from the one used for the case study. In another chapter, the student is asked what the effect would have been of performing the steps of the object-oriented analysis in a different order. To make it easy to modify the source code of the case study, it is available on the Web at www.mhhe.com/schach. 

The website also has material for instructors, including a complete set of PowerPoint lecture notes and detailed solutions to all the exercises as well as to the term project. 

## Material on UML

This book makes substantial use of UML (Unifi ed Modeling Language). If the students do not have previous knowledge of UML, this material may be taught in two ways. I prefer to teach UML on a just-in-time basis; that is, each UML concept is introduced just before it is needed. The following table describes where the UML constructs used in this book are introduced 

<table><tr><td>Construct</td><td>Section in Which the Corresponding UML Diagram Is Introduced</td></tr><tr><td>Class diagram, note, inheritance (generalization), aggregation, association, navigation triangle</td><td>Section 7.7</td></tr><tr><td>Use case</td><td>Section 11.4.3</td></tr><tr><td>Use-case diagram, use-case description</td><td>Section 11.7</td></tr><tr><td>Stereotype</td><td>Section 13.1</td></tr><tr><td>Statechart</td><td>Section 13.6</td></tr><tr><td>Interaction diagram (sequence diagram, communication diagram)</td><td>Section 13.15</td></tr></table>

Alternatively, Chapter 17 contains an introduction to UML, including material above and beyond what is needed for this book. Chapter 17 may be taught at any time; it does not depend on material in the fi rst 16 chapters. The topics covered in Chapter 17 are as follows: 

<table><tr><td>Construct</td><td>Section in Which the Corresponding UML Diagram Is Introduced</td></tr><tr><td>Class diagram, aggregation, multiplicity, composition, generalization, association</td><td>Section 17.2</td></tr><tr><td>Note</td><td>Section 17.3</td></tr><tr><td>Use-case diagram</td><td>Section 17.4</td></tr><tr><td>Stereotype</td><td>Section 17.5</td></tr><tr><td>Interaction diagram</td><td>Section 17.6</td></tr><tr><td>Statechart</td><td>Section 17.7</td></tr><tr><td>Activity diagram</td><td>Section 17.8</td></tr><tr><td>Package</td><td>Section 17.9</td></tr><tr><td>Component diagram</td><td>Section 17.10</td></tr><tr><td>Deployment diagram</td><td>Section 17.11</td></tr></table>

## Online Resources

A website to accompany the text is available at www.mhhe.com/schach. The website features Java and C++ implementations as well as source code for the MSG case study for students. For instructors, lecture PowerPoints, detailed solutions to all exercises and the term project, and an image library are available. For details, contact your sales representative. 

## Electronic Textbook Options

E-books are an innovative way for students to save money and create a greener environment at the same time. An e-book can save students about half the cost of a traditional textbook and offers unique features like a powerful search engine, highlighting, and the ability to share notes with classmates using e-books. 

McGraw-Hill offers this text as an e-book. To talk about the e-book options, contact your McGraw-Hill sales representative or visit the site www.coursesmart.com to learn more. 

## Acknowledgments

I greatly appreciate the constructive criticisms and many helpful suggestions of the reviewers of the seven previous editions. Special thanks go to the reviewers of this edition, including 

Ramzi Bualuan 

Mike McCracken 

University of Notre Dame 

Georgia Institute of Technology 

Ruth Dameron 

Nenad Medvidovic 

University of Colorado, Boulder 

University of Southern California 

Werner Krandick 

Saeed Monemi 

Drexel University 

California Polytechnic University, Pomona 

California State University, Northridge 

Jie Wei 

City University of New York—City College 

With regard to my publishers, McGraw-Hill, I am most grateful to copyeditor Kevin Camp bell and designer Brenda Rolwes. A special word of thanks goes to Melissa Welch of Studio Montage, who transformed a photograph of Sydney Harbour Bridge at night into the stunning cover. 

Special thanks also go to Jean Naudé (Vaal University of Technology, Secunda Campus) for co-authoring the Instructor’s Solution Manual. In particular, Jean provided a complete solution for the term project, including implementing it in both Java and C++. In the course of working on the ISM, Jean made numerous constructive suggestions for improving this book. I am most grateful to Jean. 

Finally, as always, I thank my wife, Sharon, for her continual support and encouragement. As with all my previous books, I did my utmost to ensure that family commitments took precedence over writing. However, when deadlines loomed, this was not always possible. At such times, Sharon always understood, and for this I am most grateful. 

It is my privilege to dedicate my fi fteenth book to my grandchildren, Jackson and Mikaela, with love. 

Stephen R. Schach 

This page intentionally left blank 

# The Scope of Software Engineering

Learning Objectives 

After studying this chapter, you should be able to 

• Defi ne what is meant by software engineering. 

• Describe the classical software engineering life-cycle model. 

• Explain why the object-oriented paradigm is now so widely accepted. 

• Discuss the implications of the various aspects of software engineering. 

• Distinguish between the classical and modern views of maintenance. 

• Discuss the importance of continual planning, testing, and documentation. 

• Appreciate the importance of adhering to a code of ethics. 

A well-known story tells of an executive who received a computer-generated bill for $0.00. After having a good laugh with friends about “idiot computers,” the executive tossed the bill away. A month later, a similar bill arrived, this time marked 30 days. Then came the third bill. The fourth bill arrived a month later, accompanied by a message hinting at possible legal action if the bill for $0.00 was not paid at once. 

The fi fth bill, marked 120 days, did not hint at anything—the message was rude and forthright, threatening all manner of legal actions if the bill was not immediately paid. Fearful of his organization’s credit rating in the hands of this maniacal machine, the executive called an acquaintance who was a software engineer and related the whole sorry story. Trying not to laugh, the software engineer told the executive to mail a check for $0.00. This had the desired effect, and a receipt for $0.00 was received a few days later. The executive meticulously fi led it away in case at some future date the computer might allege that $0.00 was still owed. 

This well-known story has a less well-known sequel. A few days later, the executive was summoned by his bank manager. The banker held up a check and asked, “Is this your check?” 

The executive agreed that it was. 

“Would you mind telling me why you wrote a check for $0.00?” asked the banker. 

So the whole story was retold. When the executive had fi nished, the banker turned to him and she quietly asked, “Have you any idea what your check for $0.00 did to our computer system?” 

A computer professional can laugh at this story, albeit somewhat nervously. After all, every one of us has designed or implemented a product that, in its original form, would have resulted in the equivalent of sending dunning letters for $0.00. Up to now, we have always caught this sort of fault during testing. But our laughter has a hollow ring to it, because at the back of our minds is the fear that someday we will not detect the fault before the product is delivered to the customer. 

A decidedly less humorous software fault was detected on November 9, 1979. The Strategic Air Command had an alert scramble when the worldwide military command and control system (WWMCCS) computer network reported that the Soviet Union had launched missiles aimed toward the United States [Neumann, 1980]. What actually happened was that a simulated attack was interpreted as the real thing, just as in the movie WarGames some 5 years later. Although the U.S. Department of Defense understandably has not given details about the precise mechanism by which test data were taken for actual data, it seems reasonable to ascribe the problem to a software fault. Either the system as a whole was not designed to differentiate between simulations and reality or the user interface did not include the necessary checks for ensuring that end users of the system would be able to distinguish fact from fiction. In other words, a software fault, if indeed the problem was caused by software, could have brought civilization as we know it to an unpleasant and abrupt end. (See Just in Case You Wanted to Know Box 1.1 for information on disasters caused by other software faults.) 

Whether we are dealing with billing or air defense, much of our software is delivered late, over budget, and with residual faults, and does not meet the client’s needs. Software engineering is an attempt to solve these problems. In other words, software engineering is a discipline whose aim is the production of fault-free software, delivered on time and within budget, that satisfi es the client’s needs. Furthermore, the software must be easy to modify when the user’s needs change. 

The scope of software engineering is extremely broad. Some aspects of software engineering can be categorized as mathematics or computer science; other aspects fall into the areas of economics, management, or psychology. To display the wide-reaching realm of software engineering, we now examine fi ve different aspects. 

## 1.1 Historical Aspects

It is a fact that electric power generators fail, but far less frequently than payroll products. Bridges sometimes collapse but considerably less often than operating systems. In the belief that software design, implementation, and maintenance could be put on the same 

In the case of the WWMCCS network, disaster was averted at the last minute. However, the consequences of other software faults have been fatal. For example, between 1985 and 1987, at least two patients died as a consequence of severe overdoses of radiation delivered by the Therac-25 medical linear accelerator [Leveson and Turner, 1993]. The cause was a fault in the control software. 

Also, during the 1991 Gulf War, a Scud missile penetrated the Patriot antimissile shield and struck a barracks near Dhahran, Saudi Arabia. In all, 28 Americans were killed and 98 wounded. The software for the Patriot missile contained a cumulative timing fault. The Patriot was designed to operate for only a few hours at a time, after which the clock was reset. As a result, the fault never had a signifi cant effect and therefore was not detected. In the Gulf War, however, the Patriot missile battery at Dhahran ran continuously for over 100 hours. This caused the accumulated time discrepancy to become large enough to render the system inaccurate. 

During the Gulf War, the United States shipped Patriot missiles to Israel for protection against the Scuds. Israeli forces detected the timing problem after only 8 hours and immediately reported it to the manufacturer in the United States. The manufacturer corrected the fault as quickly as it could, but tragically, the new software arrived the day after the direct hit by the Scud [Mellor, 1994]. 

Fortunately, it is extremely rare for death or serious injury to be caused by a software fault. However, one fault can cause major problems for thousands and thousands of people. For example, in February 2003, a software fault resulted in the U.S. Treasury Department mailing 50,000 Social Security checks that had been printed without the name of the benefi ciary, so the checks could not be deposited or cashed [St. Petersburg Times Online, 2003]. In April 2003, borrowers were informed by SLM Corp. (commonly known as Sallie Mae) that the interest on their student loans had been miscalculated as a consequence of a software fault from 1992 but detected only at the end of 2002. Nearly 1 million borrowers were told that they would have to pay more, either in the form of higher monthly payments or extra interest payments on loans extending beyond their original 10-year terms [GJSentinel.com, 2003]. Both faults were quickly corrected, but together they resulted in nontrivial fi nancial consequences for about a million people. 

The Belgian government overestimated its 2007 budget by <sup>€</sup>883,000,000 (more than $1,100,000,000 at time of writing). This mistake was caused by a software fault compounded by the manual overriding of an error-detection mechanism [La Libre Online, 2007a; 2007b]. The Belgian tax authorities used scanners and optical character recognition software to process tax returns. If the software encountered an unreadable return, it recorded the taxpayer’s income as <sup>€</sup>99,999,999.99 (over $125,000,000). Presumably, the “magic number” <sup>€</sup>99,999,999.99 was chosen to be quickly detected by employees of the data processing department, so that the return in question would then be processed manually. This worked fi ne when the tax returns were analyzed for tax assessment purposes, but not when the tax returns were reanalyzed for budgetary purposes. Ironically, the software product did have fi lters to detect this sort of problem, but the fi lters were manually bypassed to speed up processing. 

There were at least two faults in the software. First, the software engineers assumed that there would always be adequate manual scrutiny before further processing of the data. Second, the software allowed the fi lters to be manually overridden. 

As stated in Section 1.1, the aim of the Garmisch conference was to make software development as successful as traditional engineering. But by no means are all traditional engineering projects successful. For example, consider bridge building. 

In July 1940, construction of a suspension bridge over the Tacoma Narrows, in Washington State, was completed. Soon after, it was discovered that the bridge swayed and buckled dangerously in windy conditions. Approaching cars would alternately disappear into valleys and then reappear as that part of the bridge rose again. From this behavior, the bridge was given the nickname “Galloping Gertie.” Finally, on November 7, 1940, the bridge collapsed in a 42 mile per hour wind; fortunately, the bridge had been closed to all traffi c some hours earlier. The last 15 minutes of its life were captured on fi lm, now stored in the U.S. National Film Registry. 

A somewhat more humorous bridge construction failure was observed in January 2004. A new bridge was being built over the Upper Rhine River near the German town of Laufenberg, to connect Germany and Switzerland. The German half of the bridge was designed and constructed by a team of German engineers; the Swiss half by a Swiss team. When the two parts were connected, it immediately became apparent that the German half was some 21 inches (54 centimeters) higher than the Swiss half. Major reconstruction was needed to correct the problem, which was caused by wrongly correcting for the fact that “sea level” is taken by Swiss engineers to be the average level of the Mediterranean Sea, whereas German engineers use the North Sea. To compensate for the difference in sea levels, the Swiss side should have been raised 10.5 inches. Instead, it was lowered 10.5 inches, resulting in the gap of 21 inches [Spiegel Online, 2004]. 

footing as traditional engineering disciplines, a NATO study group in 1967 coined the term software engineering . The claim that building software is similar to other engineering tasks was endorsed by the 1968 NATO Software Engineering Conference held in Garmisch, Germany [Naur, Randell, and Buxton, 1976]. This endorsement is not too surprising; the very name of the conference refl ected the belief that software production should be an engineering-like activity (but see Just in Case You Wanted to Know Box 1.2). A conclusion of the conferees was that software engineering should use the philosophies and paradigms of established engineering disciplines to solve what they termed the software crisis, namely, that the quality of software generally was unacceptably low and that deadlines and budgets were not being met. 

Despite many software success stories, an unacceptably large proportion of software products still are being delivered late, over budget, and with residual faults. For example, the Standish Group is a research fi rm that analyzes software development projects. Their study of development projects completed in 2006 is summarized in Figure 1.1 [Rubenstein, 2007]. Only 35 percent of the projects were successfully completed, whereas 19 percent were canceled before completion or were never implemented. The remaining 46 percent of the projects were completed and installed on the client’s computer. However, those projects were over budget, late, or had fewer features and functionality than initially specifi ed. In other words, during 2006, just over one in three software development projects was successful; almost half the projects displayed one or more symptoms of the software crisis. 

FIGURE 1.1 The outcomes of over 9,000 development projects completed in 2006 [Rubenstein, 2007]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/6e198cb4abf9a51dfbdac86eebb3b7c205f28aa53827e82974e1130e86c3123c.jpg)


The fi nancial implications of the software crisis are horrendous. In a survey conducted by the Cutter Consortium [2002], the following was reported: 

• An astounding 78 percent of information technology organizations have been involved in disputes that ended in litigation. 

• In 67 percent of those cases, the functionality or performance of the software products as delivered did not measure up to the claims of the software developers. 

• In 56 percent of those cases, the promised delivery date slipped several times 

• In 45 percent of those cases, the faults were so severe that the software product was unusable. 

It is clear that far too little software is delivered on time, within budget, fault free, and meeting its client’s needs. To achieve these goals, a software engineer has to acquire a broad range of skills, both technical and managerial. These skills have to be applied not just to programming but to every step of software production, from requirements to postdelivery maintenance. 

That the software crisis still is with us, some 40 years later, tells us two things. First, the software process , that is, the way we produce software, has its own unique properties and problems, even though it resembles traditional engineering in many respects. Second, the software crisis perhaps should be renamed the software depression , in view of its long duration and poor prognosis. 

We now consider economic aspects of software engineering. 

## 1.2 Economic Aspects

A software organization currently using coding technique $\mathrm { C T _ { o l d } }$ discovers that new coding technique $\mathrm { C T } _ { \mathrm { n e w } }$ would result in code being produced in only nine-tenths of the time needed by $\mathrm { C T _ { o l d } }$ and, hence, at nine-tenths the cost. Common sense seems to dictate that $\mathrm { C T } _ { \mathrm { n e w } }$ is the appropriate technique to use. In fact, although common sense certainly dictates that the faster technique is the technique of choice, the economics of software engineering may imply the opposite. 

• One reason is the cost of introducing new technology into an organization. The fact that coding is 10 percent faster when technique $\mathrm { C T } _ { \mathrm { n e w } }$ is used may be less important than the costs incurred in introducing $\mathrm { C T } _ { \mathrm { n e w } }$ into the organization. It may be necessary to complete two or three projects before recouping the cost of training. Also, while attending courses on $\mathrm { C T } _ { \mathrm { n e w } }$ software personnel are unable to do productive work. Even when they return, a steep learning curve may be involved; it may take many months of practice with $\mathrm { C T } _ { \mathrm { n e w } }$ before software professionals become as profi cient with $\mathrm { C T } _ { \mathrm { n e w } }$ as they currently are with $\mathrm { C T } _ { \mathrm { o l d } } .$ . Therefore, initial projects using $\mathrm { C T } _ { \mathrm { n e w } }$ may take far longer to complete than if the organization had continued to use $\mathrm { C T } _ { \mathrm { o l d } } .$ All these costs need to be taken into account when deciding whether to change to $\mathrm { C T } _ { \mathrm { n e w } } .$ 

• A second reason why the economics of software engineering may dictate that $\mathrm { C T _ { o l d } }$ be retained is the maintenance consequence. Coding technique $\mathrm { C T } _ { \mathrm { n e w } }$ indeed may be 10 percent faster than $\mathrm { C T _ { o l d } } ,$ and the resulting code may be of comparable quality from the viewpoint of satisfying the client’s current needs. But the use of technique $\mathrm { C T } _ { \mathrm { n e w } }$ may result in code that is diffi cult to maintain, making the cost of $\mathrm { C T } _ { \mathrm { n e w } }$ higher over the life of the product. Of course, if the software developer is not responsible for any postdelivery maintenance, then, from the viewpoint of just that developer, $\mathrm { C T } _ { \mathrm { n e w } }$ is a more attractive proposition. After all, the use of $\mathrm { C T } _ { \mathrm { n e w } }$ would cost 10 percent less. The client should insist that technique $\mathrm { C T _ { o l d } }$ be used and pay the higher initial costs with the expectation that the total lifetime cost of the software will be lower. Unfortunately, often the sole aim of both the client and the software provider is to produce code as quickly as possible. The long-term effects of using a particular technique generally are ignored in the interests of short-term gain. Applying economic principles to software engineering requires the client to choose techniques that reduce long-term costs. 

This example deals with coding, which constitutes less than 10 percent of the software development effort. The economic principles, however, apply to all other aspects of software production as well. 

We now consider the importance of maintenance. 

## 1.3 Maintenance Aspects

In this section, we describe maintenance within the context of the software life cycle. A life-cycle model is a description of the steps that should be performed when building a software product. Many different life-cycle models have been proposed; several of them are described in Chapter 2 . Because it is almost always easier to perform a sequence of smaller tasks than one large task, the overall life-cycle model is broken into a series of smaller steps, called phases . The number of phases varies from model to model—from as few as four to as many as eight. In contrast to a life-cycle model, which is a theoretical description of what should be done, the actual series of steps performed on a specifi c software product, from concept exploration through fi nal retirement, is termed the life cycle of that product. In practice, the phases of the life cycle of a software product may not be carried out exactly as specifi ed in the life-cycle model, especially when time and cost overruns 

FIGURE 1.2 The six phases of the classical life-cycle model. 

1. Requirements phase 

2. Analysis (specification) phase 

3. Design phase 

4. Implementation phase 

5. Postdelivery maintenance 

6. Retirement 

are encountered. It has been claimed that more software projects have gone wrong for lack of time than for all other reasons combined [Brooks, 1975]. 

Until the end of the 1970s, most organizations were producing software using as their life-cycle model what now is termed the waterfall model . There are many variations of this model, but by and large, a product developed using this classical life-cycle model goes through the six phases shown in Figure 1.2 . These phases probably do not correspond exactly to the phases of any one particular organization, but they are suffi ciently close to most practices for the purposes of this book. Similarly, the precise name of each phase varies from organization to organization. The names used here for the various phases have been chosen to be as general as possible in the hope that the reader will feel comfortable with them. 

1. Requirements phase. During the requirements phase , the concept is explored and refi ned, and the client’s requirements are elicited. 

2. Analysis (specifi cation) phase. The client’s requirements are analyzed and presented in the form of the specifi cation document , “what the product is supposed to do.” The analysis phase sometimes is called the specifi cation phase. At the end of this phase, a plan is drawn up, the software project management plan , describing the proposed software development in full detail. 

3. Design phase . The specifi cations undergo two consecutive design procedures during the design phase . First comes architectural design , in which the product as a whole is broken down into components, called modules . Then, each module is designed; this procedure is termed detailed design . The two resulting design documents describe “how the product does it.” 

4. Implementation phase . The various components undergo coding and testing ( unit testing ) separately. Then, the components of the product are combined and tested as a whole; this is termed integration . When the developers are satisfi ed that the product functions correctly, it is tested by the client ( acceptance testing ). The implementation phase ends when the product is accepted by the client and installed on the client’s computer. (We see in Chapter 15 that coding and integration should be performed in parallel.) 

5. Postdelivery maintenance. The product is used to perform the tasks for which it was developed. During this time, it is maintained. Postdelivery maintenance includes all changes to the product once the product has been delivered and installed on the client’s computer and passes its acceptance test. Postdelivery maintenance 

One of the most widely quoted results in software engineering is that 17.4 percent of the postdelivery maintenance effort is corrective in nature; 18.2 percent is adaptive; 60.3 percent is perfective; and 4.1 percent can be categorized as “other.” This result is taken from a paper published in 1978 [Lientz, Swanson, and Tompkins, 1978]. 

However, the result in that paper was not derived from measurements on maintenance data. Instead, the authors conducted a survey of maintenance managers who were asked to estimate how much time was devoted to each category within their organization as a whole and to state how confi dent they felt about their estimate. More specifi cally, the participating software maintenance managers were asked whether their response was based on reasonably accurate data, minimal data, or no data; 49.3 percent stated that their answer was based on reasonably accurate data, 37.7 percent on minimal data, and 8.7 percent on no data. 

In fact, one should seriously question whether any respondents had “reasonably accurate data” regarding the percentage of time devoted to the categories of maintenance included in the survey; most of them probably did not have even “minimal data.” In that survey, participants were asked to state what percentage of maintenance consisted of items like “emergency fi xes” or “routine debugging”; from this raw information, the percentage of adaptive, corrective, and perfective maintenance was deduced. Software engineering was just starting to emerge as a discipline in 1978, and it was the exception for software maintenance managers to collect the detailed information needed to respond to such a survey. Indeed, in modern terminology, in 1978 virtually every organization was still at CMM level 1 (see Section 3.13). 

Hence, we have strong grounds for questioning whether the actual distribution of postdelivery maintenance activities back in 1978 was anything like the estimates of the managers who took part in the survey. The distribution of maintenance activities is certainly nothing like that today. For example, results on actual maintenance data for the Linux kernel [Schach et al., 2002] and the gcc compiler [Schach et al., 2003] show that at least 50 percent of postdelivery maintenance is corrective, as opposed to the 17.4 percent fi gure claimed in the survey. 

includes corrective maintenance (or software repair ), which consists of the removal of residual faults while leaving the specifications unchanged, as well as enhancement (or software update), which consists of changes to the specifications and the implementation of those changes. There are, in turn, two types of enhancement. The first is perfective maintenance , changes that the client thinks will improve the effectiveness of the product, such as additional functionality or decreased response time. The second is adaptive maintenance , changes made in response to changes in the environment in which the product operates, such as a new hardware/operating system or new government regulations. (For an insight into the three types of postdelivery maintenance, see Just in Case You Wanted to Know Box 1.3.) 

6. Retirement . Retirement occurs when the product is removed from service. This occurs when the functionality provided by the product no longer is of any use to the client organization. 

Now we examine the defi nition of maintenance in greater detail. 

## 1.3.1 Classical and Modern Views of Maintenance

In the 1970s, software production was viewed as consisting of two distinct activities performed sequentially: development followed by maintenance . Starting from scratch, the software product was developed, and then installed on the client’s computer. Any change to the software after installation on the client’s computer and acceptance by the client, whether to fi x a residual fault or extend the functionality, constituted classical maintenance [IEEE 610.12, 1990]. Hence, the way that software was developed classically can be described as the development-then-maintenance model . 

This is a temporal defi nition ; that is, an activity is classifi ed as development or maintenance depending on when it is performed. Suppose that a fault in the software is detected and corrected a day after the software has been installed. By defi nition, this constitutes classical maintenance. But if the identical fault is detected and corrected the day before the software is installed, in terms of the defi nition, this constitutes classical development. Now suppose that a software product has just been installed but the client wants to increase the functionality of the software product. Classically, that would be described as perfective maintenance. However, if the client wants the same change to be made just before the software product is installed, this would be classical development. Again, there is no difference whatsoever between the nature of the two activities, but classically one is considered development, the other perfective maintenance. 

In addition to such inconsistencies, two other reasons explain why the developmentthen-maintenance model is unrealistic today: 

1. Nowadays, it is certainly not unusual for construction of a product to take a year or more. During this time, the client’s requirements may well change. For example, the client might insist that the product now be implemented on a faster processor, which has just become available. Alternatively, the client organization may have expanded into Belgium while development was under way, and the product now has to be modifi ed so it can also handle sales in Belgium. To see how a change in requirements can affect the software life cycle, suppose that the client’s requirements change while the design is being developed. The software engineering team has to suspend development and modify the specifi cation document to refl ect the changed requirements. Furthermore, it then may be necessary to modify the design as well, if the changes to the specifi cations necessitate corresponding changes to those portions of the design already completed. Only when these changes have been made can development proceed. In other words, developers have to perform “maintenance” long before the product is installed. 

2. A second problem with the classical development-then-maintenance model arose as a result of the way in which we now construct software. In classical software engineering, a characteristic of development was that the development team built the target product starting from scratch. In contrast, as a consequence of the high cost of software production today, wherever possible developers try to reuse parts of existing software products in the software product to be constructed (reuse is discussed in detail in Chapter 8 ). Therefore, the development-then-maintenance model is inappropriate today because reuse is so widespread. 

A more realistic way of looking at maintenance is that given in the standard for lifecycle processes published by the International Organization for Standardization (ISO) 

The International Organization for Standardization (ISO) is a network of the national standards institutes of 147 countries, with a central secretariat based in Geneva, Switzerland. ISO has published over 13,500 internationally accepted standards, ranging from standards for photographic fi lm speed (“ISO number”) to many of the standards presented in this book. For example, ISO 9000 is discussed in Chapter 3 . 

ISO is not an acronym. It is derived from the Greek word , meaning equal, the root of the English prefi x iso- found in words such as isotope, isobar, and isosceles. The International Organization for Standardization chose ISO as the short form of its name to avoid having multiple acronyms arising from the translation of the name “International Organization for Standardization” into the languages of the different member countries. Instead, to achieve international standardization, a universal short form of its name was chosen. 

and the International Electrotechnical Commission (IEC). That is, maintenance is the process that occurs when “software undergoes modifi cations to code and associated documentation due to a problem or the need for improvement or adaptation” [ISO/IEC 12207, 1995]. In terms of this operational defi nition , maintenance occurs whenever a fault is fi xed or the requirements change, irrespective of whether this takes place before or after installation of the product. The Institute for Electrical and Electronics Engineers (IEEE) and the Electronic Industries Alliance (EIA) subsequently adopted this defi nition [IEEE/EIA 12207.0-1996, 1998] when IEEE standards were modifi ed to comply with ISO/IEC 12207. (See Just in Case You Wanted to Know Box 1.4 for more on ISO.) 

In this book, the term postdelivery maintenance refers to the 1990 IEEE defi nition of maintenance as any change to the software after it has been delivered and installed on the client’s computer, and modern maintenance or just maintenance refers to the 1995 ISO/IEC defi nition of corrective, perfective, or adaptive activities performed at any time. Postdelivery maintenance is therefore a subset of (modern) maintenance. 

## 1.3.2 The Importance of Postdelivery Maintenance

It is sometimes said that only bad software products undergo postdelivery maintenance. In fact, the opposite is true: Bad products are thrown away, whereas good products are repaired and enhanced, for 10, 15, or even 20 years. Furthermore, a software product is a model of the real world, and the real world is perpetually changing. As a consequence, software has to be maintained constantly for it to remain an accurate reflection of the real world. 

For instance, if the sales tax rate changes from 6 to 7 percent, almost every software product that deals with buying or selling has to be changed. Suppose the product contains the C++ statement 

$$
\text { const   float   salesTax } = 6. 0;
$$

or the equivalent Java statement 

$$
\text { public   static   final   float   salesTax } = (\text { float }) 6. 0;
$$

declaring that salesTax is a fl oating-point constant initialized to the value 6.0. In this case, maintenance is relatively simple. With the aid of a text editor the value 6.0 is replaced by 7.0 and the code is recompiled and relinked. However, if instead of using the name salesTax, the actual value 6.0 has been used in the product wherever the value of the sales tax is invoked, then such a product is extremely diffi cult to modify. For example, there may be occurrences of the value 6.0 in the source code that should be changed to 7.0 but are overlooked, or instances of 6.0 that do not refer to sales tax but are incorrectly changed to 7.0. Finding these faults almost always is diffi cult and time consuming. In fact, with some software, it might be less expensive in the long run to throw away the product and recode it rather than try to determine which of the many constants need to be changed and how to make the modifi cations. 

The real-time real world also is constantly changing. The missiles with which a jet fi ghter is armed may be replaced by a new model, requiring a change to the weapons control component of the associated avionics system. A six-cylinder engine is to be offered as an option in a popular four-cylinder automobile; this implies changing the onboard computers that control the fuel injection system, timing, and so on. 

But just how much time (= money) is devoted to postdelivery maintenance? The pie chart in Figure 1.3(a) shows that, some 40 years ago, approximately two-thirds of total software costs went to postdelivery maintenance; the data were obtained by averaging information from various sources, including [Elshoff, 1976], [Daly, 1977], [Zelkowitz, Shaw, and Gannon, 1979], and [Boehm, 1981]. Newer data show that an even larger proportion is devoted to postdelivery maintenance. Many organizations devote 70–80 percent or more of their software budget to postdelivery maintenance [Yourdon, 1992; Hatton, 1998], as shown in Figure 1.3(b) . 

Surprisingly, the average cost percentages of the classical development phases have hardly changed. This is shown in Figure 1.4 , which compares the data used to derive Figure 1.3(a) with more recent data on 132 Hewlett-Packard projects [Grady, 1994]. 

FIGURE 1.3 Approximate average cost percentages of development and postdelivery maintenance (a) between 1976 and 1981 and (b) between 1992 and 1998. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/8a53c80399f62d957e7f083845846ce354968b71a617b9153fe41b130035dd9d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/baf5fea25a3259a1f227a747e8ecc4e79f9971749fd5a53c57479e68d9b079d1.jpg)



FIGURE 1.4 A comparison of the approximate average cost percentages of the classical development phases for various projects between 1976 and 1981 and for 132 more recent Hewlett-Packard projects.


<table><tr><td></td><td>Various Projects between 1976 and 1981</td><td>132 More Recent Hewlett-Packard Projects</td></tr><tr><td>Requirements and analysis (specification) phases</td><td>21%</td><td>18%</td></tr><tr><td>Design phase</td><td>18</td><td>19</td></tr><tr><td>Implementation phase</td><td></td><td></td></tr><tr><td>Coding (including unit testing)</td><td>36</td><td>34</td></tr><tr><td>Integration</td><td>24</td><td>29</td></tr></table>

Now consider again the software organization currently using coding technique $\mathrm { C T _ { o l d } }$ that learns that $\mathrm { C T } _ { \mathrm { n e w } }$ will reduce coding time by 10 percent. Even if $\mathrm { C T } _ { \mathrm { n e w } }$ has no adverse effect on maintenance, an astute software manager will think twice before changing coding practices. The entire staff has to be retrained, new software development tools purchased, and perhaps additional staff members hired who are experienced in the new technique. All this expense and disruption has to be endured for a decrease of at most 0.85 percent in software costs because, as shown in Figures 1.3(b) and 1.4 , coding together with unit testing constitutes on average only 34 percent of 25 percent or 8.5 percent of total software costs. 

Now suppose a new technique that reduces postdelivery maintenance costs by 10 percent is developed. This probably should be introduced at once, because on average, it will reduce overall costs by 7.5 percent. The overhead involved in changing to this technique is a small price to pay for such large overall savings. 

Because postdelivery maintenance is so important, a major aspect of software engineering consists of those techniques, tools, and practices that lead to a reduction in postdelivery maintenance costs. 

## 1.4 Requirements, Analysis, and Design Aspects

Software professionals are human and therefore sometimes make a mistake while developing a product. As a result, there will be a fault in the software. If the mistake is made while eliciting the requirements, the resulting fault will probably also appear in the specifi cations, the design, and the code. Clearly, the earlier we correct a fault, the better. 

The relative costs of fi xing a fault at various phases in the classical software life cycle are shown in Figure 1.5 [Boehm, 1981]. The fi gure refl ects data from IBM [Fagan, 1974], GTE [Daly, 1977], the Safeguard project [Stephenson, 1976], and some smaller TRW projects [Boehm, 1980]. The solid line in Figure 1.5 is the best fi t for the data relating to the larger projects, and the dashed line is the best fi t for the smaller projects. For each of the phases of the classical software life cycle, the corresponding relative cost to detect and correct a fault is depicted in Figure 1.6 . Each step on the solid line in Figure 1.6 is constructed by taking the corresponding point on the solid straight line of Figure 1.5 and plotting the data on a linear scale. 


FIGURE 1.5 The relative cost of fi xing a fault at each phase of the classical software life cycle. The solid line is the best fi t for the data relating to the larger software projects, and the dashed line is the best fi t for the smaller software projects. (Barry Boehm, Software Engineering Economics, © 1981, p. 40. Adapted by permission of Prentice Hall, Inc., Englewood Cliffs, NJ.)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/9a987576f00d7a352287bf7168ba0971f724e814039c7a5bb48013a5391d2570.jpg)



Phase in which fault was detected and corrected


Suppose it costs $40 to detect and correct a specific fault during the design phase. From the solid line in Figure 1.6 (projects between 1974 and 1980), that same fault would cost only about $30 to fix during the analysis phase. But during postdelivery maintenance, that fault would cost around $2000 to detect and correct. Newer data show that now it is even more important to detect faults early. The dashed line in Figure 1.6 shows the cost of detecting and correcting a fault during the development of system software for the IBM AS/400 [Kan et al., 1994]. On average, the same fault would have cost $3680 to fix during postdelivery maintenance of the AS/400 software. 

The reason that the cost of correcting a fault increases so steeply is related to what has to be done to correct a fault. Early in the development life cycle, the product essentially exists only on paper, and correcting a fault may simply mean making a change to a document. The other extreme is a product already delivered to a client. At the very least, correcting a fault at that time means editing the code, recompiling and relinking it, and then carefully testing that the problem is solved. Next, it is critical to check that making the change has not created a new problem elsewhere in the product. All the relevant documentation, including manuals, needs to be updated. Finally, the corrected product must be delivered and reinstalled. The moral of the story is this: We must fi nd faults early or else it will cost us money. We therefore should employ techniques for detecting faults during the requirements and analysis (specifi cation) phases. 


FIGURE 1.6 The solid line depicts the points on the solid line of Figure 1.5 plotted on a linear scale. The dashed line depicts newer data.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/e8ed83530d4c60fd796c1da2f9cda8d48983aa3ffa8c97612b118431e285b19e.jpg)


There is a further need for such techniques. Studies have shown [Boehm, 1979] that between 60 and 70 percent of all faults detected in large projects are requirements, analysis, or design faults. Newer results from inspections bear out this preponderance of requirements, analysis, or design faults (an inspection is a meticulous examination of a document by a team, as described in Section 6.2.3). During 203 inspections of Jet Propulsion Laboratory software for the NASA unmanned interplanetary space program, on average, about 1.9 faults were detected per page of a specifi cation document, 0.9 faults per page of a design, but only 0.3 faults per page of code [Kelly, Sherif, and Hops, 1992]. 

Therefore it is important that we improve our requirements, analysis, and design techniques, not only so that faults can be found as early as possible but also because requirements, analysis, and design faults constitute such a large proportion of all faults. Just as the example in Section 1.3 showed that reducing postdelivery maintenance costs by 10 percent reduces overall costs by about 7.5 percent, reducing requirements, analysis, and design faults by 10 percent reduces the overall number of faults by 6–7 percent. 

That so many faults are introduced early in the software life cycle highlights another important aspect of software engineering: techniques that yield better requirements, specifi cations, and designs. 

Most software is produced by a team of software engineers rather than by a single individual responsible for every aspect of the development and maintenance life cycle. We now consider the implications of this. 

## 1.5 Team Development Aspects

The cost of hardware continues to decrease rapidly. A mainframe computer of the 1950s that cost in excess of a million preinfl ation dollars was considerably less powerful in every way than a laptop computer of today costing less than $1000. As a result, organizations easily can afford hardware that can run large products, that is, products too large (or too complex) to be implemented by one person within the allowed time constraints. For example, if a product has to be delivered within 18 months but would take a single software professional 15 years to complete, then the product must be developed by a team. However, team development leads to interfacing problems among code components and communication problems among team members. 

For example, Jeff and Juliet code modules p and q, respectively, where module p calls module q. When Jeff codes p, he inserts a call to q with fi ve arguments in the argument list. Juliet codes q with fi ve arguments, but in a different order from those of Jeff. Some software tools, such as the Java interpreter and loader, or lint for C (Section 8.11.4), detect such a type violation but only if the interchanged arguments are of different types; if they are of the same type, then the problem may not be detected for a long period of time. It may be debated that this is a design problem, and if the modules had been more carefully designed, this problem would not have happened. That may be true, but in practice a design often is changed after coding commences, and notifi cation of a change may not be distributed to all members of the development team. Therefore, when a design that affects two or more programmers has been changed, poor communication can lead to the interface problems Jeff and Juliet experienced. This sort of problem is less likely to occur when only one individual is responsible for every aspect of the product, as was the case before powerful computers that can run huge products became affordable. 

But interfacing problems are merely the tip of the iceberg when it comes to problems that can arise when software is developed by teams. Unless the team is properly organized, an inordinate amount of time can be wasted in conferences between team members. Suppose that a product takes a single programmer 1 year to complete. If the same task is assigned to a team of six programmers, the time for completing the task frequently is closer to 1 year than the expected 2 months, and the quality of the resulting code may well be lower than if the entire task had been assigned to one individual (see Section 4.1). Because a considerable proportion of today’s software is developed and maintained by teams, the scope of software engineering must include techniques for ensuring that teams are properly organized and managed. 

As has been shown in the preceding sections, the scope of software engineering is extremely broad. It includes every step of the software life cycle, from requirements to postdelivery retirement. It also includes human aspects, such as team organization; economic aspects; and legal aspects, such as copyright law. All these aspects implicitly are incorporated in the defi nition of software engineering given at the beginning of this chapter, that software engineering is a discipline whose aim is the production of fault-free soft ware delivered on time, within budget, and satisfying the user’s needs. 

We return to the classical phases of Figure 1.2 to ask why there is no planning, testing, or documentation phase. 

## 1.6 Why There Is No Planning Phase

Clearly it is impossible to develop a software product without a plan. Accordingly, it appears to be essential to have a planning phase at the very beginning of the project. 

The key point is that, until it is known exactly what is to be developed, there is no way an accurate, detailed plan can be drawn up. Therefore, three types of planning activities take place when a software product is developed using the classical paradigm: 

1. At the beginning of the project, preliminary planning takes place for managing the requirements and analysis phases. 

2. Once what is going to be developed is known precisely, the software project management plan (SPMP) is drawn up. This includes the budget, staffi ng requirements, and detailed schedule. The earliest we can draw up the project management plan is when the specifi cation document has been approved by the client, that is, at the end of the analysis phase. Until that time, planning has to be preliminary and partial. 

3. All through the project, management needs to monitor the SPMP and be on the watch for any deviation from the plan. 

For example, suppose that the SPMP for a specifi c project states that the project as a whole will take 16 months and that the design phase will take 4 of those months. After a year, management notices that the project as a whole seems to be progressing much more slowly than anticipated. A detailed investigation shows that, so far, 8 months have been devoted to the design phase, which is still far from complete. The project almost certainly will have to be abandoned, and the funds spent to date are wasted. Instead, management should have tracked progress by phase, and noticed, after at most 2 months, a serious problem in the design phase. At that time, a decision could have been made how best to proceed. The usual initial step in such a situation is to call in a consultant to determine if the project is feasible and to determine whether the design team is competent to carry out the task or the risk of proceeding is too great. Based on the report of the consultant, various alternatives are now considered, including reducing the scope of the target product, and then designing and implementing a less ambitious one. Only if all other alternatives are considered unworkable does the project have to be canceled. In the case of the specifi c project, this cancellation would have taken place some 6 months earlier if management had monitored the plan closely, saving a considerable sum of money. 

In conclusion, there is no separate planning phase. Instead, planning activities are carried out all through the life cycle. However, there are times when planning activities predominate. These include the beginning of the project (preliminary planning) and directly after the specifi cation document has been signed off on by the client (software project management plan). 

## 1.7 Why There Is No Testing Phase

It is essential to check a software product meticulously after it has been developed. Accordingly, it is reasonable to ask why there is no testing phase after the product has been implemented. 

Unfortunately, checking a software product once it is ready to be delivered to the client is far too late. For instance, if there is a fault in the specifi cation document, this fault will have been carried forward into the design and implementation. There are times in the software process when testing is carried out almost to the total exclusion of other activities. This occurs toward the end of each phase ( verifi cation ) and is especially true before the product is handed over to the client ( validation ). Although there are times when testing predominates, there should never be times when no testing is being performed. If testing is treated as a separate ( testing ) phase , then there is a very real danger that testing will not be carried out constantly throughout every phase of the product development and maintenance process. 

But even this is not enough. What is needed is continual checking of a software product. Meticulous checking should automatically accompany every software development and maintenance activity. A separate testing phase is incompatible with the goal of ensuring that a software product is as fault free as possible at all times. 

Every software development organization should contain an independent group whose primary responsibility is to ensure that the delivered product is what the client needs and that the product has been built correctly in every way. This group is called the software quality assurance (SQA) group. The quality of software is the extent to which it meets its specifi cations. Quality and software quality assurance are described in more detail in Chapter 6 , as is the role of SQA in setting and enforcing standards. 

## 1.8 Why There Is No Documentation Phase

Just as there should never be a separate planning phase or testing phase, there also should never be a separate documentation phase . On the contrary, at all times, the documentation of a software product must be complete, correct, and up to date. For instance, during the analysis phase, the specifi cation document must refl ect the current version of the specifi cations, and this is also true for the other phases. 

1. One reason why it is essential to ensure that the documentation is always up to date is the large turnover in personnel in the software industry. For example, suppose that the design documentation has not been kept current and the chief designer leaves to take another job. It is now extremely hard to update the design document to refl ect all the changes made while the system was being designed. 

2. It is almost impossible to perform the steps of a specifi c phase unless the documentation of the previous phase is complete, correct, and up to date. For instance, an incomplete specifi cation document must inevitably result in an incomplete design and then in an incomplete implementation. 

3. It is virtually impossible to test whether a software product is working correctly unless documents are available that state how that software product is supposed to behave. 

4. Maintenance is almost impossible unless there is a complete and correct set of documentation that describes precisely what the current version of the product does. 

Therefore, just as there is no separate planning phase or testing phase, there is no separate documentation phase. Instead, planning, testing, and documentation should be activities that accompany all other activities while a software product is being constructed. 

Now we examine the object-oriented paradigm. 

## 1.9 The Object-Oriented Paradigm

Before 1975, most software organizations used no specifi c techniques; each individual worked his or her own way. Major breakthroughs were made between approximately 1975 and 1985, with the development of the so-called structured or classical paradigm . The techniques constituting the classical paradigm include structured systems analysis (Section 12.3), data fl ow analysis (Section 14.3), structured programming, and structured testing (Section 15.13.2). These techniques seemed extremely promising when fi rst used. However, as time passed, they proved to be somewhat less successful in two respects: 

1. The techniques sometimes were unable to cope with the increasing size of software products. That is, the classical techniques were adequate when dealing with small-scale products (typically 5000 lines of code) or even medium-scale products of 50,000 lines of code. Today, however, large-scale products of 500,000 lines of code are relatively common; even products of 5 million or more lines of code are not considered unusual. However, the classical techniques frequently could not scale up suffi ciently to handle the development of today’s larger products. 

2. The classical paradigm did not live up to earlier expectations during postdelivery maintenance. A major driving force behind the development of the classical paradigm some 40 years ago was that, on average, two-thirds of the software budget was being devoted to postdelivery maintenance (see Figure 1.3 ). Unfortunately, the classical paradigm has not solved this problem; as pointed out in Section 1.3.2, many organizations still spend 70–80 percent or more of their time and effort on postdelivery maintenance [Yourdon, 1992; Hatton, 1998]. 

A major reason for the limited success of the classical paradigm is that classical techniques are either operation oriented or attribute (data) oriented but not both. The basic components of a software product are the operations of the product and the attributes on which those operations operate. For example, determine_average_height <sup>1</sup> is an operation that operates on a collection of heights (attributes) and returns the average of those heights (attribute). Some classical techniques, such as data fl ow analysis (Section 14.3), are operation oriented. That is, such techniques concentrate on the operations of the product; the attributes are of secondary importance. Conversely, techniques such as Jackson system development (Section 14.5) are attribute oriented. The emphasis here is on the attributes; the operations that operate on the attributes are less signifi cant. 

In contrast, the object-oriented paradigm considers both attributes and operations to be equally important. A simplistic way of looking at an object is as a unifi ed software artifact that incorporates both the attributes and the operations performed on the attributes (an artifact is a component of a software product, such as a specifi cation document, a code module, or a manual). This defi nition of an object is incomplete and is fl eshed out later in the book, once inheritance has been defi ned (Section 7.8). Nevertheless, the defi nition captures much of the essence of an object. 


FIGURE 1.7 A comparison of implementations of a bank account using (a) the classical paradigm and (b) the object oriented paradigm. The solid black line surrounding the object denotes that details as to how accountBalance i implemented are not known outside the object


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/227009ed7cdb48b3a9dff8b4002de7391f81ad1cdf43e51bd0e78f90f1c8e737.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/42182e729c252d0276344d68a200073e253128aafe8ed11bc50194e0cbb308b7.jpg)



(b)


A bank account is one example of an object (see Figure 1.7 ). The attribute component of the object is the accountBalance. The operations that can be performed on that account balance include deposit money in the account, withdraw money from the account, and determineBalance. The bank account object combines an attribute with the three operations performed on that attribute in a single artifact. From the viewpoint of the classical paradigm, a product that deals with banking would have to incorporate an attribute, the account_balance, and three operations, deposit, withdraw, and determine_balance. 

Up to now, there seems to be little difference between the two approaches. However, a key point is the way in which an object is implemented. Specifi cally, details as to how the attributes of an object are stored are not known from outside the object. This is an instance of “information hiding,” discussed in more detail in Section 7.6. In the case of the bank account object shown in Figure 1.7(b) , the rest of the software product is aware that there is such a thing as a balance within a bank account object, but it has no idea as to the format of accountBalance. That is, there is no knowledge outside the object as to whether the account balance is implemented as an integer or a fl oating-point number or a fi eld (component) of some larger structure. This information barrier surrounding the object is denoted by the solid black line in Figure 1.7(b) , which depicts an implementation using the object-oriented paradigm. In contrast, a dashed line surrounds account_balance in Figure 1.7(a) , because all the details of account_balance are known to the modules in the implementation using the classical paradigm, and the value of account_balance therefore can be changed by any of them. 

Returning to Figure 1.7(b) , the object-oriented implementation, if a customer deposits $10 in an account, then a message is sent to the deposit method of the relevant object telling it to increment the accountBalance attribute by $10 (a method is an implementation of an operation). The deposit method is within the bank account object and knows how the accountBalance is implemented; this is denoted by the dashed circular line inside the object. But no entity external to the object needs this knowledge. That the three methods in Figure 1.7(b) shield accountBalance from the rest of the product symbolizes this localization of knowledge. The fact that implementation details are local to an object illustrates the fi rst of the many strengths of the object-oriented paradigm: 

1. Consider postdelivery maintenance. Suppose that the banking product has been constructed using the classical paradigm. If the way an account_balance is represented is changed from (say) an integer to a fi eld of a structure, then every part of that product that has anything to do with an account_balance has to be changed, and these changes have to be made consistently. In contrast, if the object-oriented paradigm is used, then changes need be made only within the bank account object itself. No other part of the product has knowledge of how an accountBalance is implemented, so no other part can have access to an accountBalance. Consequently, no other part of the banking product needs to be changed. Accordingly, the object-oriented paradigm makes maintenance quicker and easier, and the chance of introducing a regression fault (that is, a fault inadvertently introduced into one part of a product as a consequence of making an apparently unrelated change to another part of the product) is greatly reduced. 

2. In addition to maintenance, the object-oriented paradigm also makes development easier. In many instances, an object has a physical counterpart. For example, a bank account object in the bank product corresponds to an actual bank account in the bank for which this product is being implemented. As will be shown in Part B, modeling plays a major role in the object-oriented paradigm. The close correspondence between the objects in a product and their counterparts in the real world should lead to better-quality software. 

3. Well-designed objects are independent units. As has been explained, an object consists of both attributes and the operations performed on the attributes. If all the operations performed on the attributes of an object are included in that object, then the object can be considered a conceptually independent entity. Everything in the product that relates to the portion of the real world modeled by that object can be found in the object itself. This conceptual independence sometimes is termed encapsulation (Section 7.4). But there is an additional form of independence, physical independence. In a well-designed object, information hiding ensures that implementation details are hidden from everything outside that object. The only allowable form of communication is sending a message to the object to carry out a specifi c operation. The way that the operation is carried out is entirely the responsibility of the object itself. For this reason, object-oriented design sometimes is referred to as responsibility-driven design [Wirfs-Brock, Wilkerson, and Wiener, 1990] or design by contract [Meyer, 1992]. (For another view of responsibility-driven design, see Just in Case You Wanted to Know Box 1.5, derived from an example in [Budd, 2002].) Another way of looking at both encapsulation and information hiding is as instances of separation of concerns (Section 5.4). 

4. A product built using the classical paradigm is implemented as a set of modules, but conceptually it is essentially a single unit. This is one reason why the classical paradigm has been less successful when applied to larger products. In contrast, when the objectoriented paradigm is used correctly, the resulting product consists of a number of smaller, largely independent units. The object-oriented paradigm reduces the level of complexity of a software product and hence simplifi es both development and maintenance. 

# Just in Case You Wanted to Know

Suppose that you live in New Orleans, and you want to send a Mother’s Day bouquet to your mother in Chicago. One strategy would be to consult the Chicago yellow pages (on the World Wide Web), determine which fl orist is located closest to your mother’s apartment, and place your order with that fl orist. A more convenient way is to order the fl owers at 1-800-fl owers.com, leaving the total responsibility for delivering the fl owers to that company. It is irrelevant where 1-800-fl owers.com is physically located or which fl orist is given your order to deliver. In any event, the company does not divulge that information, an instance of information hiding. 

In exactly the same way, when a message is sent to an object, not only is it entirely irrelevant how the request is carried out, but the unit that sends the message is not even allowed to know the internal structure of the object. The object itself is entirely responsible for every detail of carrying out the message. 

5. The object-oriented paradigm promotes reuse; because objects are independent entities, they can generally be utilized in future products (but see Problem 1.17). This reuse of objects reduces the time and cost of both development and maintenance, as explained in Chapter 8. 

When the object-oriented paradigm is utilized, the classical software life cycle of Figure 1.2 has to be modifi ed. Figure 1.8 compares the life-cycle model of the classical paradigm with that of the object-oriented paradigm. 

The fi rst difference appears to be purely terminological; the word phase is used for the classical paradigm, whereas workfl ow is used for the object-oriented paradigm. In fact, as will be explained in detail in Chapter 2 , there is no correspondence between a phase and a workfl ow. On the contrary, the two terms are totally distinct, and this distinction epitomizes the differences between the life-cycle models that underlie the two paradigms. 

In this chapter, we consider another difference between the two paradigms, the role played by modules (in the classical paradigm) versus that played by objects (in the objectoriented paradigm). First consider the design phase of the classical paradigm. As stated in Section 1.3, this phase is divided into two subphases: architectural design followed by detailed design. In the architectural design subphase, the product is decomposed into components, called modules . Then, during the detailed design subphase, the data structures and algorithms of each module are designed in turn. Finally, during the implementation phase, these modules are implemented. 

If the object-oriented paradigm is used instead, one of the steps of the objectoriented analysis workfl ow is to determine the classes. Because a class is a kind of module, architectural design is performed during the object-oriented analysis workfl ow. 

<table><tr><td>Classical Paradigm</td><td>Object-Oriented Paradigm</td></tr><tr><td>1. Requirements phase</td><td>1. Requirements workflow</td></tr><tr><td>2. Analysis (specification) phase</td><td>2'. Object-oriented analysis workflow</td></tr><tr><td>3. Design phase</td><td>3'. Object-oriented design workflow</td></tr><tr><td>4. Implementation phase</td><td>4'. Object-oriented implementation workflow</td></tr><tr><td>5. Postdelivery maintenance</td><td>5. Postdelivery maintenance</td></tr><tr><td>6. Retirement</td><td>6. Retirement</td></tr><tr><td>2. Analysis (specification) phase• Determine what the product is to do</td><td>2'. Object-oriented analysis workflow• Determine what the product is to do• Extract the classes</td></tr><tr><td>3. Design phase• Architectural design (extract the modules)• Detailed design</td><td>3'. Object-oriented design workflow• Detailed design</td></tr><tr><td>4. Implementation phase• Code the modules in an appropriate programming language• Integrate</td><td>4'. Object-oriented implementation workflow• Code the classes in an appropriate object-oriented programming language• Integrate</td></tr></table>

Consequently, object-oriented analysis goes further than the corresponding analysis (specifi cation) phase of the classical paradigm. This is shown in Figure 1.9 . 

This difference between the two paradigms has major consequences. When the classical paradigm is used, there almost always is a sharp transition between the analysis phase and the design phase. After all, the aim of the analysis phase is to determine what the product is to do, whereas the purpose of the design phase is to decide how to do it. In contrast, when object-oriented analysis is used, objects enter the life cycle from the very beginning. The objects are extracted in the analysis workfl ow, designed in the design workfl ow, and coded in the implementation workfl ow. The object-oriented paradigm is therefore an integrated approach; the transition from workfl ow to workfl ow is far smoother than with the classical paradigm, reducing the number of faults introduced during development. 

As already mentioned, it is inadequate to defi ne an object merely as a software artifact that encapsulates both attributes and operations and implements the principle of information hiding. A more complete defi nition is given in Chapter 7 , where objects are examined in depth. 

## 1.10 The Object-Oriented Paradigm in Perspective

Figure 1.1 is evidence of the many shortcomings of the classical (structured) paradigm. However, the object-oriented paradigm is by no means a panacea for all ills: 

• Like all approaches to software production, the object-oriented paradigm has to be used correctly; it is just as easy to misuse the object-oriented paradigm as any other paradigm. 

• When correctly applied, the object-oriented paradigm can solve some (but not all) of the problems of the classical paradigm. 

• The object-oriented paradigm has some problems of its own, as described in Section 7.9. 

• The object-oriented paradigm is the best approach available today. However, like all technologies, it is certain to be superseded by a superior technology in the future. 

In this book, strengths and weaknesses of both the classical and the object-oriented paradigm are pointed out within the context of the specifi c topic under discussion. Consequently, the comparison of the two paradigms does not appear in one single place but is spread over the entire book. 

We now defi ne a number of software engineering terms. 

## 1.11 Terminology

The client is the individual who wants a product to be built (developed). The developers are the members of a team responsible for building that product. The developers may be responsible for every aspect of the software process, from the requirements onward, or they may be responsible for only the implementation of an already designed product. 

Both the client and developers may be part of the same organization. For example, the client may be the head actuary of an insurance company and the developers a team headed by the vice-president for software development of that insurance company. This is termed internal software development . On the other hand, with contract software the client and developers are members of totally independent organizations. For instance, the client may be a senior offi cial in the Department of Defense and the developers employees of a major defense contractor specializing in software for weapons systems. On a much smaller scale, the client may be an accountant in a one-person practice and the developer a student who earns income by developing software on a part-time basis. 

The third party involved in software production is the user . The user is the person or persons on whose behalf the client has commissioned the product and who will utilize the software. In the insurance company example, the users may be insurance agents, who will use the software to select the most appropriate policies. In some instances, the client and the user are the same person (for example, the accountant discussed previously). 

As opposed to expensive custom software developed for one client, multiple copies of software, such as word processors or spreadsheets, are sold at much lower prices to a large numbers of buyers. That is, the manufacturers of such software (such as Microsoft or Borland) recover the cost of developing a product by volume selling. This type of software usually is called commercial off-the-shelf (COTS) software . The earlier term for this type of software was shrink-wrapped software because the box containing the CD or diskettes, the manuals, and the license agreement almost always was shrink-wrapped. Nowadays, COTS software often is downloaded over the World Wide Web—there is no box to shrink-wrap. For this reason, COTS software nowadays sometimes is referred to as clickware . COTS software is developed for “the market”; that is, the software is not targeted to a specifi c client or users until it has been developed and is available for purchase. 

Open-source software is becoming extremely popular. An open-source software product is developed and maintained by a team of volunteers and may be downloaded and used free of charge by anyone. Widely used open-source products include the Linux operating system, the Firefox Web browser, and the Apache Web server. The term open source refers to the availability of the source code to all, unlike most commercial products where only the executable version is sold. Because any user of an open-source product can scrutinize the source code and report faults to the developers, many open-source software products are of high quality. The expected consequence of the public nature of faults in open-source software was formalized by Raymond in The Cathedral and the Bazaar as Linus’s Law , named after Linus Torvalds, the creator of Linux [Raymond, 2000]. Linus’s Law states that “given enough eyeballs, all bugs are shallow.” In other words, if enough individuals scrutinize the source code of an open-source software product, someone should be able to locate that fault and suggest how to fi x it (but see Just in Case You Wanted to Know Box 1.6). A related principle is “Release early. Release often” [Raymond, 2000]. 

It is self-evident that the more people who carefully examine a piece of code, the more likely it is that someone will be able to fi nd and fi x a fault in that code. Accordingly, Linus’s Law should perhaps be called “Torvalds’s Truism.” 

That is, open-source developers tend to spend less time on testing than closed-source developers, preferring to release a new version of a product virtually as soon as it is fi nished, leaving much of the responsibility for testing to users. 

A word used on almost every page of this book is software . Software consists of not just code in machine-readable form but also all the documentation that is an intrinsic component of every project. Software includes the specifi cation document, the design document, legal and accounting documents of all kinds, the software project management plan, and other management documents as well as all types of manuals. 

Since the 1970s, the difference between a program and a system has become blurred. In the “good old days,” the distinction was clear. A program was an autonomous piece of code, generally in the form of a deck of punched cards that could be executed. A system was a related collection of programs. A system might consist of programs P, Q, R, and S. Magnetic tape ${ \sf T } _ { 1 }$ was mounted, and then program P was run. It caused a deck of data cards to be read in and produced as output tapes ${ \sf T } _ { 2 }$ and ${ \sf T } _ { 3 } .$ . Tape $\mathsf { T } _ { 2 }$ then was rewound, and program Q was run, producing tape ${ \sf T } _ { 4 }$ as output. Program R now merged tapes ${ \sf T } _ { 3 }$ and ${ \sf T } _ { 4 }$ into tape $\mathsf { T } _ { 5 } ; \mathsf { T } _ { 5 }$ served as input for program S, which printed a series of reports. 

Compare that situation with a product, running on a machine with a front-end communications processor and a back-end database manager, that performs real-time control of a steel mill. The single piece of software controlling the steel mill does far more than the old-fashioned system, but in terms of the classic defi nitions of program and system, this software undoubtedly is a program. To add to the confusion, the term system now is also used to denote the hardware–software combination. For example, the fl ight control system in an aircraft consists of both the in-fl ight computers and the software running on them. Depending on who is using the term, the fl ight control system also may include the controls, such as the joystick, that send commands to the computer and the parts of the aircraft, such as the wing fl aps, controlled by the computer. Furthermore, within the context of traditional software development, the term systems analysis refers to the fi rst two phases (requirements and analysis phases) and systems design refers to the third phase (design phase). 

To minimize confusion, this book uses the term product to denote a nontrivial piece of software. There are two reasons for this convention. The fi rst is simply to obviate the program versus system confusion by using a third term. The second reason is more important. This book deals with the process of software production, that is, the way we produce software, and the end result of a process is termed a product . Finally, the term system is used in its modern sense, that is, the combined hardware and software, or as part of universally accepted phrases, such as operating system and management information system. 

Two words widely used within the context of software engineering are methodology and paradigm . In the 1970s, the word methodology began to be used in the sense of “a way of developing a software product”; the word actually means the “science of methods.” Then, in the 1980s, the word paradigm became a major buzzword of the business world, as in the phrase, “It’s a whole new paradigm.” The software industry soon 

# Just in Case You Wanted to Know

The fi rst use of the word bug to denote a fault is attributed to the late Rear Admiral Grace Murray Hopper, one of the designers of COBOL. On September 9, 1945, a moth fl ew into the Mark II computer that Hopper and her colleagues used at Harvard and lodged between the contact plates of a relay. Accordingly, there was actually a bug in the system. Hopper taped the bug to the logbook and wrote, “First actual case of bug being found.” The logbook, with moth still attached, is in the Naval Museum at the Naval Surface Weapons Center, in Dahlgren, Virginia. 

Although this may have been the fi rst use of bug in a computer context, the word was used in engineering slang in the 19th century [Shapiro, 1994]. For example, Thomas Alva Edison wrote on November 18, 1878, “This thing gives out and then that—‘Bugs’—as such little faults and diffi culties are called . . .” [Josephson, 1992]. One of the defi nitions of bug in the 1934 edition of Webster’s New English Dictionary is, “A defect in apparatus or its operation.” It is clear from Hopper’s remark that she, too, was familiar with the use of the word in that context; otherwise, she would have explained what she meant. 

started using the word paradigm in the phrases object-oriented paradigm and classical (or traditional ) paradigm to mean “a style of software development.” This was another unfortunate choice of terminology, because a paradigm is a model or a pattern. Erudite readers offended by this corruption of the English language are warmly invited to take up the cudgels of linguistic accuracy on the author’s behalf; he is tired of tilting at windmills. 

A methodology or a paradigm is a component of the software process as a whole. In contrast, a technique is a component of a portion of the software process. Examples include coding techniques, documentation techniques, and planning techniques. 

When a programmer makes a mistake , the consequence of that mistake is a fault in the code. Executing the software product then results in a failure , that is, the observed incorrect behavior of the product as a consequence of the fault. An error is the amount by which a result is incorrect. The terms mistake , fault , failure , and error are defi ned in IEEE Standard 610.12, “A Glossary of Software Engineering Terminology” [IEEE 610.12, 1990], reaffi rmed in 2002 [IEEE Standards, 2003]. The word defect is a generic term that refers to a fault, failure, or error. In the interests of precision, in this book we therefore minimize use of the umbrella term defect. 

One term that is avoided as far as possible is bug (the history of this word is in Just in Case You Wanted to Know Box 1.7). The term bug nowadays is simply a euphemism for a fault . Although there generally is no real harm in using euphemisms, the word bug has overtones that are not conducive to good software production. Specifi cally, instead of saying, “I made a mistake,” a programmer will say, “A bug crept into the code” (not my code but the code), thereby transferring responsibility for the mistake from the programmer to the bug. No one blames a programmer for coming down with a case of infl uenza, because the fl u is caused by the fl u bug. Referring to a mistake as a bug is a way of casting off responsibility. In contrast, the programmer who says, “I made a mistake,” is a computer professional who takes responsibility for his or her actions. 

Considerable confusion surrounds object-oriented terminology. For example, in addition to the term attribute for a data component of an object, the term state variable sometimes is used in the object-oriented literature. In Java, the term is instance variable . In C++ the term fi eld is used, and in Visual Basic .NET, the term is property . With regard to the implementation of the operations of an object, the term method usually is used; in 

C++, however, the term is member function . In C++, a member of an object refers to either an attribute (“fi eld”) or a method. In Java, the term fi eld is used to denote either an attribute (“instance variable”) or a method. To avoid confusion, wherever possible, the generic terms attribute and method are used in this book. 

Fortunately, some terminology is widely accepted. For example, when a method within an object is invoked, this almost universally is termed sending a message to the object. 

## 1.12 Ethical Issues

We conclude this chapter on a cautionary note. Software products are developed and maintained by humans. If those individuals are hard working, intelligent, sensible, up to date, and above all, ethical , then the chances are good that the way that the software products they develop and maintain will be satisfactory. Unfortunately, the converse is equally true. 

Most societies for professionals have a code of ethics to which all its members must adhere. The two major societies for computer professionals, the Association for Computing Machinery (ACM) and the Computer Society of the Institute of Electrical and Electronics Engineers (IEEE-CS) jointly approved a Software Engineering Code of Ethics and Professional Practice as the standard for teaching and practicing software engineering [IEEE/ ACM, 1999]. It is lengthy, so a short version, consisting of a preamble and eight principles, was also produced. Here is the short version: 

Software Engineering Code of Ethics and Professional Practice <sup>2</sup> (Version 5.2) 

## as recommended by the IEEE-CS/ACM Joint Task Force on Software Engineering Ethics and Professional Practices Short Version Preamble

The short version of the code summarizes aspirations at a high level of abstraction; th clauses that are included in the full version give examples and details of how these aspirations change the way we act as software engineering professionals. Without the aspirations, the details can become legalistic and tedious; without the details, the aspirations can become high sounding but empty; together, the aspirations and the details form a cohesive code. 

Software engineers shall commit themselves to making the analysis, specifi cation, design, development, testing and maintenance of software a benefi cial and respected profession. In accordance with their commitment to the health, safety and welfare of the public, softwar engineers shall adhere to the following Eight Principles: 

1. Public —Software engineers shall act consistently with the public interest. 

2. Client and Employer— Software engineers shall act in a manner that is in the best interests of their client and employer consistent with the public interest. 

3. Product —Software engineers shall ensure that their products and related modifi cations meet the highest professional standards possible. 

4. Judgment —Software engineers shall maintain integrity and independence in their profes sional judgment. 

5. Management —Software engineering managers and leaders shall subscribe to and promote an ethical approach to the management of software development and maintenance. 

6. Profession —Software engineers shall advance the integrity and reputation of the profes sion consistent with the public interest. 

7. Colleagues —Software engineers shall be fair to and supportive of their colleagues. 

8. Self— Software engineers shall participate in lifelong learning regarding the practice of their profession and shall promote an ethical approach to the practice of the profession 

The codes of ethics of other societies for computer professionals express similar senti ments. It is vital for the future of our profession that we adhere rigorously to such codes of ethics. 

In Chapter 2 , we examine various life-cycle models to shed further light on the differences between the classical and the object-oriented paradigm. 

## Chapter Review

Software engineering is defi ned (Section 1.1) as a discipline whose aim is the production of fault-free software that satisfi es the user’s needs and is delivered on time and within budget. To achieve this goal, appropriate techniques have to be used throughout software production, including when performing analysis (specifi cation) and design (Section 1.4) and postdelivery maintenance (Section 1.3). Software engineering addresses all the steps of the software life cycle and incorporates aspects of many different areas of human knowledge, including economics (Section 1.2) and the social sciences (Section 1.5). There is no separate planning phase (Section 1.6), no testing phase (Section 1.7), and no documentation phase (Section 1.8). In Section 1.9, objects are introduced, and a comparison between the classical and object-oriented paradigms is made. Then the object-oriented paradigm is evaluated (Section 1.10). Next, in Section 1.11, the terminology used in this book is explained. Finally, ethical issues are discussed in Section 1.12. 

## For Further Reading

The earliest source of information on the scope of software engineering is [Boehm, 1976]. The future of software engineering is discussed in [Finkelstein, 2000]. The current state of the practice of software engineering is described in a variety of articles in the November–December 2003 issue of IEEE Soft ware. An investigation of the factors leading to successful software development appears in [Procaccino, Verner, and Lorenzet, 2006]. 

For a view on the importance of postdelivery maintenance in software engineering and how to plan for it, see [Parnas, 1994]. Software development for COTS-based products is the subject of [Brownsword, Oberndorf, and Sledge, 2000]. Acquiring COTS components is described in [Ulkuniemi and Seppanen, 2004] and in [Keil and Tiwana, 2005]. Risk management when software is developed using COTS components is described in [Li et al., 2008]. The July–August 2005 issue of IEEE Software contains six articles on integrating COTS components into software products, including [Donzelli et al., 2005] and [Yang, Bhuta, Boehm, and Port, 2005]. A reassessment of risk management appears in [Bannerman, 2008]. 

Risks in enterprise systems are described in [Scott and Vessey, 2002] and in information systems in general in [Longstaff, Chittister, Pethia, and Haimes, 2000]. Zvegintzov [1998] explains just how little accurate data on software engineering practice actually are available. 

The fact that mathematics underpins software engineering is stressed in [Devlin, 2001]. The importance of economics in software engineering is discussed in [Boehm and Huang, 2003]. The November–December 2002 issue of IEEE Software contains a number of articles on software engineering economics. 

Two classic books on the social sciences and software engineering are [Weinberg, 1971] and [Shneiderman, 1980]. Neither book requires prior knowledge of psychology or the behavioral sciences in general. 

Brooks’s [1975] timeless work, The Mythical Man-Month , is a highly recommended introduction to the realities of software engineering. The book includes material on all the topics mentioned in this chapter. 

An excellent introduction to open-source software is [Raymond, 2000]. Paulsen, Succi, and Eberlein [2004] present an empirical study comparing open- and closed-source software products. Reuse of open-source components is described in [Madanmohan and De’, 2004]. A variety of articles on open-source software appears in the January/February 2004 issue of IEEE Software and in issue No. 2, 2005, of IBM Systems Journal . The issue of whether open-source software leads to increased security is discussed in [Hoepman and Jacobs, 2007]. The interplay between business and open-source software is the subject of [Watson et al., 2008], [Ven, Verelst, and Mannaert, 2008], and [Wesselius, 2008]. 

An excellent introduction to the object-oriented paradigm is [Budd, 2002]. Three successful projects carried out using the object-oriented paradigm are described in [Capper, Colgate, Hunter, and James, 1994], with a detailed analysis. A survey of the attitudes of 150 experienced software developers toward the object-oriented paradigm is reported in [Johnson, 2000]. With regard to ethics, an ethical code common to both business and software professionals is presented in [Payne and Landry, 2006]. 

## Key Terms

acceptance testing 7 adaptive maintenance 8 analysis phase 7 architectural design 7 artifact 18 attribute 25 bug 25 classical paradigm 18 clickware 23 client 23 coding 7 commercial-off-the-shelf (COTS) software 23 contract software 23 corrective maintenance 8 defect 25 design by contract 20 design document 7 design phase 7 detailed design 7 

developer 23 development-thenmaintenance model 9 documentation phase 17 encapsulation 20 enhancement 8 error 25 ethics 26 failure 25 fault 25 fi eld 25 implementation phase 7 instance variable 25 integration 7 internal software development 23 life cycle 6 life-cycle model 6 Linus's Law 23 maintenance 10 

message 19 member function 26 method 19 methodology 24 mistake 25 module 7 object-oriented paradigm 25 open-source software 23 operational defi nition (of maintenance) 10 paradigm 24 perfective maintenance 8 phase 6 planning phase 16 postdelivery maintenance 7 process 5 product 24 program 24 property 25 

<table><tr><td>quality 17</td><td>software engineering 2</td><td>technique 25</td></tr><tr><td>regression fault 20</td><td>software project management</td><td>temporal definition</td></tr><tr><td>requirements phase 7</td><td>plan 7</td><td>(of maintenance) 9</td></tr><tr><td>responsibility-driven design 20</td><td>software repair 8</td><td>testing phase 17</td></tr><tr><td>retirement 8</td><td>specification document 7</td><td>traditional paradigm 25</td></tr><tr><td>send a message 26</td><td>specification phase 7</td><td>unit testing 7</td></tr><tr><td>shrink-wrapped</td><td>state variable 25</td><td>user 23</td></tr><tr><td>software 23</td><td>structured paradigm 18</td><td>validation 17</td></tr><tr><td>software 24</td><td>system 24</td><td>verification 17</td></tr><tr><td>software crisis 4</td><td>systems analysis 24</td><td>waterfall model 7</td></tr><tr><td>software depression 5</td><td>systems design 24</td><td></td></tr></table>

## Problems

1.1 You are in charge of automating a multi-site architectural practice. The cost of developing the software has been estimated to be $530,000. Approximately how much additional money will be needed for postdelivery maintenance of the software? 

1.2 Is there a way of reconciling the classical temporal defi nition of maintenance with the operational defi nition we now use? Explain your answer. 

1.3 You are a software-engineering consultant. The chief information offi cer of a regional gasoline distribution corporation wants you to develop a software product that will carry out all the accounting functions of the company and provide online information to the head offi ce staff regarding orders and inventory in the various company storage tanks. Computers are required for 21 accounting clerks, 15 order clerks, and 37 storage tank clerks. In addition, 14 managers need access to the data. The company is willing to pay $30,000 for the hardware and the software together and wants the complete software product in 4 weeks. What do you tell him? Bear in mind that your company wants his corporation’s business, no matter how unreasonable his request. 

1.4 You are a vice-admiral in the Velorian Navy. It has been decided to call in a software development organization to develop the control software for a new generation of ship-to-ship missiles. You are in charge of supervising the project. To protect the government of Veloria, what clauses do you include in the contract with the software developers? 

1.5 You are a software engineer whose job is to supervise the development of the software in Problem 1.4. List ways your company can fail to satisfy the contract with the navy. What are the probable causes of such failures? 

1.6 Nine months after delivery, a fault is detected in the software of a product that analyzes mRNA using the Stein–Röntgen reagent. The cost of fi xing the fault is $18,900. The cause of the fault is an ambiguous sentence in the specifi cation document. Approximately how much would it have cost to correct the fault during the analysis phase? 

1.7 Suppose that the fault in Problem 1.6 had been detected during the implementation phase. Approximately how much would it have cost to fi x then? 

1.8 You are the president of an organization that builds large-scale software. You show Figure 1.6 to your employees, urging them to fi nd faults early in the software life cycle. Someone responds that it is unreasonable to expect anyone to remove faults before they have entered the product. For example, how can anyone remove a fault while the design is being produced if the fault in question is a coding fault? What do you reply? 

1.9 Describe a situation in which the client, developer, and user are the same person. 

1.10 What problems can arise if the client, developer, and user are the same person? How can these problems be solved? 



1.11 What potential advantages accrue if the client, developer, and user are the same person? 



1.12 Look up the word system in a dictionary. How many different defi nitions are there? Write down those defi nitions that are applicable within the context of software engineering. 

1.13 It is your fi rst day at your fi rst job. Your manager hands you a program listing and says, “See if you can fi nd the bug.” What do you reply? 

1.14 You are in charge of developing the product in Problem 1.1. Will you use the object-oriented paradigm or the classical paradigm? Give reasons for your answer. 

1.15 Instead of implementing component c9 of a software product, the developers decide to buy a COTS component with the same specifi cations as component c9. What are the advantages and disadvantages of this approach? 

1.16 Instead of implementing component c37 of a software product, the developers decide to utilize an open-source component with the same specifi cations as component c37. What are the advantages and disadvantages of this approach? 

1.17 Object P invokes method m1 of object Q. Suppose we wish to reuse object P in a new software product. Can P be reused without reusing Q as well? What does this say about objects as “independent entities” (as stated in Section 1.9)? 

1.18 Is it correct to state that, as a consequence of Linus’s Law, all open-source software is of high quality? 

1.19 (Term Project) Suppose that the product for Chocoholics Anonymous of Appendix A has been implemented exactly as described. Now the product has to be modifi ed to include endocrinologists as providers. In what ways will the existing product have to be changed? Would it be better to discard everything and start again from scratch? 

1.20 (Readings in Software Engineering) Your instructor will distribute copies of Schach et al. [2003]. What is your opinion of the relative merits of results based on managers’ estimates compared to results computed from actual data? 

## References



[Bannerman, 2008] P. L. BANNERMAN, “Risk and Risk Management in Software Projects: A Reassessment,” Journal of Systems and Software 81 (December 2008), pp. 2118–33. 





[Boehm, 1976] B. W. BOEHM, “Software Engineering,” IEEE Transactions on Computers C-25 (December 1976), pp. 1226–41. 





[Boehm, 1979] B. W. BOEHM, “Software Engineering, R & D Trends and Defense Needs,” in: Research Directions in Software Technology , P. Wegner (Editor), The MIT Press, Cambridge, MA, 1979. 





[Boehm, 1980] B. W. BOEHM, “Developing Small-Scale Application Software Products: Some Experimental Results,” Proceedings of the Eighth IFIP World Computer Congress, October 1980, IFIP, pp. 321–26. 





[Boehm, 1981] B. W. BOEHM, Software Engineering Economics, Prentice Hall, Englewood Cliffs, NJ, 1981. 





[Boehm and Huang, 2003] B. BOEHM AND L. G. HUANG, “Value-Based Software Engineering: A Case Study,” IEEE Computer 36 (March 2003), pp. 33–41. 





[Brooks, 1975] F. P. BROOKS, JR., The Mythical Man-Month: Essays on Software Engineering, Addison-Wesley, Reading, MA, 1975; Twentieth Anniversary Edition, Addison-Wesley, Reading, MA, 1995. 





[Brownsword, Oberndorf, and Sledge, 2000] L. BROWNSWORD, T. OBERNDORF, AND C. A. SLEDGE, “Developing New Process for COTS-Based Systems,” IEEE Software 17 (July–August 2000), pp. 40–47. 





[Budd, 2002] T. A. BUDD, An Introduction to Object-Oriented Programming , 3rd ed., Addison-Wesley, Reading, MA, 2002. 





[Capper, Colgate, Hunter, and James, 1994] N. P. CAPPER, R. J. COLGATE, J. C. HUNTER, AND M. F. JAMES, “The Impact of Object-Oriented Technology on Software Quality: Three Case Histories,” IBM Systems Journal 33 (No. 1, 1994), pp. 131–57. 





[Cutter Consortium, 2002] Cutter Consortium, “78% of IT Organizations Have Litigated,” The Cutter Edge , www.cutter.com/research/2002/edge020409.html,<sup>3</sup> April 09, 2002. 





[Daly, 1977] E. B. DALY, “Management of Software Development,” IEEE Transactions on Software Engineering SE-3 (May 1977), pp. 229–42. 





[Devlin, 2001] K. DEVLIN, “The Real Reason Why Software Engineers Need Math,” Communications of the ACM 44 (October 2001), pp. 21–22. 





[Donzelli et al., 2005] P. DONZELLI, M. ZELKOWITZ, V. BASILI, D. ALLARD, AND K. N. MEYER, “Evaluating COTS Component Dependability in Context,” IEEE Software 22 (July–August 2005), pp. 46–53. 





[Elshoff, 1976] J. L. ELSHOFF, “An Analysis of Some Commercial PL/I Programs,” IEEE Transactions on Software Engineering SE-2 (June 1976), pp. 113–20. 





[Fagan, 1974] M. E. FAGAN, “Design and Code Inspections and Process Control in the Development of Programs,” Technical Report IBM-SSD TR 21.572, IBM Corporation, December 1974. 





[Finkelstein, 2000] A. FINKELSTEIN (Editor), The Future of Software Engineering , IEEE Computer Society Press, Los Alamitos, CA, 2000. 





[GJSentinel.com, 2003] “Sallie Mae’s Errors Double Some Bills,” www.gjsentinel.com/news/ content/coxnet/headlines/0522_salliemae.html, May 22, 2003. 





[Grady, 1994] R. B. GRADY, “Successfully Applying Software Metrics,” IEEE Computer 27 (September 1994), pp. 18–25. 





[Hatton, 1998] L. HATTON, “Does OO Sync with How We Think?” IEEE Software 15 (May–June 1998), pp. 46–54. 





[Hoepman and Jacobs, 2007] J.-H. HOEPMAN AND B. JACOBS, “Increased Security through Open Source,” Communications of the ACM 50 (January 2007), pp. 79–83. 





[IEEE 610.12, 1990] “A Glossary of Software Engineering Terminology,” IEEE 610.12-1990, Institute of Electrical and Electronic Engineers, Inc., 1990. 





[IEEE Standards, 2003] “Products and Projects Status Report,” standards.ieee.org/db/status/ status.txt, June 3, 2003. 





[IEEE/ACM, 1999] “Software Engineering Code of Ethics and Professional Practice, Version 5.2, as Recommended by the IEEE-CS/ACM Joint Task Force on Software Engineering Ethics and Professional Practice,” www.computer.org/tab/seprof/code.htm, 1999. 





[IEEE/EIA 12207.0-1996, 1998] “IEEE/EIA 12207.0-1996 Industry Implementation of International Standard ISO/IEC 12207:1995,” Institute of Electrical and Electronic Engineers, Electronic Industries Alliance, New York, 1998. 





[ISO/IEC 12207, 1995] “ISO/IEC 12207:1995, Information Technology—Software Life-Cycle Processes,” International Organization for Standardization, International Electrotechnical Commission, Geneva, 1995. 





[Johnson, 2000] R. A. JOHNSON, “The Ups and Downs of Object-Oriented System Development,” Communications of the ACM 43 (October 2000), pp. 69–73. 





[Josephson, 1992] M. JOSEPHSON, Edison, A Biography , John Wiley and Sons, New York, 1992. 





[Kan et al., 1994] S. H. KAN, S. D. DULL, D. N. AMUNDSON, R. J. LINDNER, AND R. J. HEDGER, “AS/400 Software Quality Management,” IBM Systems Journal 33 (No. 1, 1994), pp. 62–88. 





[Keil and Tiwana, 2005] M. KEIL AND A. TIWANA, “Beyond Cost: The Drivers of COTS Application Value,” IEEE Software 22 (May–June 2005), pp. 64–69. 





[Kelly, Sherif, and Hops, 1992] J. C. KELLY, J. S. SHERIF, AND J. HOPS, “An Analysis of Defect Densities Found during Software Inspections,” Journal of Systems and Software 17 (January 1992), pp. 111–17. 





[La Libre Online, 2007a] “Lalibre.be—Une erreur à 883 millions d’euros,” www.lalibre.be/index. php?view=article&art_id=305607. 





[La Libre Online, 2007b] “Lalibre.be—C’est la faute à l’informatique,” www.lalibre.be/index. php?view=article&art_id=307021. 





[Leveson and Turner, 1993] N. G. LEVESON AND C. S. TURNER, “An Investigation of the Therac-25 Accidents,” IEEE Computer 26 (July 1993), pp. 18–41. 





[Li et al., 2008] J. LI, O. P. N. SLYNGSTAD, M. TORCHIANO, M. MORISIO, AND C. BUNSE, “A State-ofthe-Practice Survey of Risk Management in Development with Off-the-Shelf Software Components,” IEEE Transactions on Software Engineering 34 (March–April 2008), pp. 271–86. 





[Lientz, Swanson, and Tompkins, 1978] B. P. LIENTZ, E. B. SWANSON, AND G. E. TOMPKINS, “Characteristics of Application Software Maintenance,” Communications of the ACM 21 (June 1978), pp. 466–71. 





[Longstaff, Chittister, Pethia, and Haimes, 2000] T. A. LONGSTAFF, C. CHITTISTER, R. PETHIA, AND Y. Y. HAIMES, “Are We Forgetting the Risks of Information Technology?” IEEE Computer 33 (December 2000), pp. 43–51. 





[Madanmohan and De’, 2004] T. R. MADANMOHAN AND R. DE’, “Open Source Reuse in Commercial Firms,” IEEE Software 21 (November–December 2004), pp. 62–69. 





[Mellor, 1994] P. MELLOR, “CAD: Computer-Aided Disaster,” Technical Report, Centre for Software Reliability, City University, London, July 1994. 





[Meyer, 1992] B. MEYER, “Applying ‘Design by Contract’,” IEEE Computer 25 (October 1992), pp. 40–51. 





[Naur, Randell, and Buxton, 1976] P. NAUR, B. RANDELL, AND J. N. BUXTON (Editors), Software Engineering: Concepts and Techniques: Proceedings of the NATO Conferences , Petrocelli-Charter, New York, 1976. 





[Neumann, 1980] P. G. NEUMANN, Letter from the Editor, ACM SIGSOFT Software Engineering Notes 5 (July 1980), p. 2. 





[Parnas, 1994] D. L. PARNAS, “Software Aging,” Proceedings of the 16th International Conference on Software Engineering , Sorrento, Italy, May 1994, IEEE, pp. 279–87. 





[Paulson, Succi, and Eberlein, 2004] J. W. PAULSON, G. SUCCI, AND A. EBERLEIN, “An Empirical Study of Open-Source and Closed-Source Software Products,” IEEE Transactions on Software Engineering 30 (April 2004), pp. 246–56. 





[Payne and Landry, 2006] D. PAYNE AND B. J. L. LANDRY, “A Uniform Code of Ethics: Business and IT Professional Ethics,” Communications of the ACM 49 (November 2006), pp. 81–84. 





[Procaccino, Verner, and Lorenzet, 2006] J. D. PROCACCINO, J. M. VERNER, AND S. J. LORENZET, “Defi ning and Contributing to Software Development Success,” Communications of the ACM (August 2006), pp. 79–83. 





[Raymond, 2000] E. S. RAYMOND, The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary , O’Reilly & Associates, Sebastopol, CA, 2000; also available at www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/. 





[Rubenstein, 2007] D. RUBENSTEIN, “Standish Group Report: There’s Less Development Chaos Today,” www.sdtimes.com/content/article.aspx?ArticleID=30247, March 1, 2007. 





[Schach et al., 2002] S. R. SCHACH, B. JIN, D. R. WRIGHT, G. Z. HELLER, AND A. J. OFFUTT, “Maintainability of the Linux Kernel,” IEE Proceedings—Software 149 (February 2002), pp. 18–23. 





[Schach et al., 2003] S. R. SCHACH, B. JIN, G. Z. HELLER, L. YU, AND J. OFFUTT, “Determining the Distribution of Maintenance Categories: Survey versus Measurement,” Empirical Software Engineering 8 (December 2003), pp. 351–66. 





[Scott and Vessey, 2002] J. E. SCOTT AND I. VESSEY, “Managing Risks in Enterprise Systems Implementations,” Communications of the ACM 45 (April 2002), pp. 74–81. 





[Shapiro, 1994] F. R. SHAPIRO, “The First Bug,” Byte 19 (April 1994), p. 308. 





[Shneiderman, 1980] B. SHNEIDERMAN, Software Psychology: Human Factors in Computer and Information Systems , Winthrop Publishers, Cambridge, MA, 1980. 





[Spiegel Online, 2004] “Rheinbrücke mit Treppe—54 Zentimeter Höhenunterschied,” www.spiegel. de/panorama/0,1518,281837,00.html. 





[St. Petersburg Times Online, 2003] “Thousands of Federal Checks Uncashable,” www.sptimes. com/2003/02/07/Worldandnation/Thousands_of_federal_.shtml, February 07, 2003. 





[Stephenson, 1976] W. E. STEPHENSON, “An Analysis of the Resources Used in Safeguard System Software Development,” Bell Laboratories, Draft Paper, August 1976. 





[Ulkuniemi and Seppanen, 2004] P. ULKUNIEMI, AND V. SEPPANEN, “COTS Component Acquisition in an Emerging Market,” IEEE Software 21 (November–December 2004), pp. 76–82. 





[Ven, Verelst, and Mannaert, 2008] K. VEN, I. VERELST, AND H. MANNAERT, “Should You Adopt Open Source Software?” IEEE Software 25 (May–June 2008), pp. 54–59. 





[Watson et al., 2008] R. T. WATSON, M.-C. BOUDREAU, P. T. YORK, M. E. GREINER, AND D. WYNN, “The Business of Open Source,” Communications of the ACM 51 (April 2008), pp. 41–46. 





[Weinberg, 1971] G. M. WEINBERG, The Psychology of Computer Programming , Van Nostrand Reinhold, New York, 1971. 





[Wesselius, 2008] J. WESSELIUS, “The Bazaar inside the Cathedral: Business Models for Internal Markets,” IEEE Software 25 (May–June 2008), pp. 60–66. 





[Wirfs-Brock, Wilkerson, and Wiener, 1990] R. WIRFS-BROCK, B. WILKERSON, AND L. WIENER, Designing Object-Oriented Software , Prentice Hall, Englewood Cliffs, NJ, 1990. 





[Yang, Bhuta, Boehm, and Port, 2005] Y. YANG, J. BHUTA, B. BOEHM, AND D. N. PORT, “Value-Based Processes for COTS-Based Applications,” IEEE Software 22 (July–August 2005), pp. 54–62. 





[Yourdon, 1992] E. YOURDON, The Decline and Fall of the American Programmer , Yourdon Press, Upper Saddle River, NJ, 1992. 





[Zelkowitz, Shaw, and Gannon, 1979] M. V. ZELKOWITZ, A. C. SHAW, AND J. D. GANNON, Principles of Software Engineering and Design, Prentice Hall, Englewood Cliffs, NJ, 1979. 





[Zvegintzov, 1998] N. ZVEGINTZOV, “Frequently Begged Questions and How to Answer Them,” IEEE Software 15 (January/February 1998), pp. 93–96. 



This page intentionally left blank 

# Software Engineering Concepts

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/c97a85343f7694ba790b83705fa15296a3f8bfc070228f29a6f953f688395e8a.jpg)


Chapters 2 through 9 of this book play a dual role: They introduce the reader to the software process, and they provide the foundation for the material in the second half of the book, where the workfl ows (activities) of software development are described. 

The software process is the way we produce software. It starts with concept exploration and ends when the product is fi nally decommissioned. During this period, the product goes through a series of steps such as requirements, analysis (specifi cation), design, implementation, integration, postdelivery maintenance, and ultimately, retirement. The software process includes the tools and techniques we use to develop and maintain software as well as the software professionals involved. 

A variety of different software life-cycle models are discussed in detail in Chapter 2 , “Software Life-Cycle Models.” These include the evolution-tree model, the waterfall model, the rapid-prototyping model, the synchronize-and-stabilize model, the opensource model, the agile process model, the spiral model, and most important of all, the iterative-and-incremental model. To enable the reader to decide on an appropriate life-cycle model for a specifi c project, the various life-cycle models are compared and contrasted. 

“The Software Process” is the title of Chapter 3 . The emphasis in this chapter is on the Unifi ed Process, currently the most promising way of developing software. Agile processes, an alternative approach to software development gaining in popularity, are also treated in detail. The chapter concludes with material on software process improvement. 

Chapter 4 is entitled “Teams.” Today’s projects are too large to be completed by a single individual within the given time constraints. Instead, a team of software professionals collaborate on the project. The major topic of this chapter is how teams should be organized so that team members work together productively. Various ways of organizing teams are discussed, including democratic teams, chief programmer teams, synchronize-and-stabilize teams, open-source teams, and agile process teams. 

A software engineer needs to be able to use a number of different tools, both analytical and practical. In Chapter 5 , “The Tools of the Trade,” the reader is introduced to a variety of software engineering tools. One such tool is stepwise refi nement, a technique for decomposing a large problem into smaller, more tractable problems. Another tool is cost– benefi t analysis, a technique for determining whether a software project is fi nancially feasible. Then, computer-aided software engineering (CASE) tools are described. A CASE tool is a software product that helps software engineers to develop and maintain software. Finally, to manage the software process, it is necessary to measure various quantities to determine whether the project is on track. These measures (metrics) are critical to the success of a project. 

The last two topics of Chapter 5 , CASE tools and metrics, are treated in detail in Chapters 11 through 16, which describe the specifi c workfl ows of the software life cycle. There is a discussion of the CASE tools that support each workfl ow, as well as a description of the metrics needed to manage that workfl ow adequately. 

Chapter 6 , “Testing,” discusses the concepts underlying testing. The consideration of testing techniques specifi c to each workfl ow of the software life cycle is deferred until Chapters 11 through 16. 

Chapter 7 , “From Modules to Objects,” gives a detailed explanation of classes and objects and why the object-oriented paradigm is proving more successful than the classical paradigm. The concepts of this chapter are utilized in the rest of the book, particularly Chapter 11 , “Requirements”; Chapter 13 , “Object-Oriented Analysis”; and Chapter 14 , “Design,” in which object-oriented design is presented. 

The ideas of Chapter 7 are extended in Chapter 8 , “Reusability and Portability.” It is important to be able to implement reusable software that can be ported to a variety of different hardware. The fi rst part of the chapter is devoted to reuse; the topics include a variety of reuse case studies as well as reuse strategies such as object-oriented patterns and frameworks. Portability is the second major topic; portability strategies are presented in some depth. A recurring theme of this chapter is the role of objects in achieving reusability and portability. 

The last chapter in Part A is Chapter 9 , “Planning and Estimating.” Before starting a software project, it is essential to plan the entire operation in detail. Once the projec begins, management must closely monitor progress, noting deviations from the plan and taking corrective action where necessary. Also, it is vital that the client be provided accurate estimates of how long the project will take and how much it will cost. Different estimation techniques are presented, including function points and COCOMO II. A detailed description of a software project management plan is given. The material of this chapter is utilized in Chapters 12 and 13 . When the classical paradigm is used, major planning and estimating activities take place at the end of the classical analysis phase, as explained in Chapter 12 . When software is developed using the object-oriented paradigm, this planning takes place at the end of the object-oriented analysis workfl ow ( Chapter 13 ) 

# Software Life-Cycle Models

## Learning Objectives

After studying this chapter, you should be able to 

• Describe how software products are developed in practice 

• Understand the evolution-tree life-cycle model. 

• Appreciate the negative impact of change on software products. 

• Utilize the iterative-and-incremental life-cycle model. 

• Comprehend the impact of Miller’s Law on software production. 

• Describe the strengths of the iterative-and-incremental life-cycle model. 

• Realize the importance of mitigating risks early. 

• Describe agile processes, including extreme programming. 

• Compare and contrast a variety of other life-cycle models. 

Chapter 1 describes how software products would be developed in an ideal world. The theme of this chapter is what happens in practice. As will be explained, there are vast differences between theory and practice. 

## 2.1 Software Development in Theory

In an ideal world, a software product is developed as described in Chapter 1 . As depicted schematically in Figure 2.1, the system is developed from scratch; - denotes the empty set. (See Just in Case You Wanted to Know Box 2.1 if you want to know the origin of the term from scratch .) First the client’s Requirements are determined, and then the Analysis 

# Just in Case You Wanted to Know

The term from scratch, meaning “starting with nothing,” comes from 19th century sports terminology. Before roads (and running tracks) were paved, races had to be held on open ground. In many cases, the starting line was a scratch in the sand. A runner who had no advantage or handicap had to start from that line, that is, “from [the] scratch.” 

The term scratch has a different sporting connotation nowadays. A “scratch golfer” is one whose golfi ng handicap is zero. 

FIGURE 2.1 Idealized software development. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/361e43c89ba334dc66be6654bd229b910f5360c5d34f970b89e6fb0d22849023.jpg)



Development


is performed. When the analysis artifacts are complete, the Design is produced. This is followed by the Implementation of the complete software product, which is then installed on the client’s computer. 

However, software development is considerably different in practice for two reasons. First, software professionals are human and therefore make mistakes. Second, the client’s requirements can change while the software is being developed. In this chapter, both these issues are discussed in some depth, but fi rst we present a mini case study, based on the case study in [Tomer and Schach, 2000], that illustrates the issues involved. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/d05fa5af2237f4c505c378b0404f4052e34c87806b1cecb224cd6ffdb33ef8c1.jpg)


## 2.22.2

## Winburg Mini Case Study

To reduce traffi c congestion in downtown Winburg, Indiana, the mayor convinces the city to set up a public transportation system. Bus-only lanes are to be established, and commuters will be encouraged to “park and ride”; that is, to park their cars in suburban parking lots and then take buses from there to work and back at a cost of one dollar per ride. Each bus is to have a fare machine that accepts only dollar bills. Passengers insert a bill into the slot as they enter the bus. Sensors inside the fare machine scan the bill, and the software in the machine uses an image recognition algorithm to decide whether the passenger has indeed inserted a valid dollar bill into the slot. It is important that the fare machine be accurate because, once the news gets out that any piece of paper will do the trick, fare income will plummet to effectively zero. Conversely, if the machine regularly rejects valid dollar bills, passengers will be reluctant to use the buses. In addition, the fare machine must be rapid. Passengers will be equally reluctant to use the buses if the machine spends 15 seconds coming to a decision regarding the validity of a dollar bill—it would take even a relatively small number of passengers many minutes to board a bus. Therefore, the requirements for the fare machine software include an average response time of less than 1 second and an average accuracy of at least 98 percent. 

Episode 1 The fi rst version of the software is implemented. 

Episode 2 Tests show that the required constraint of an average response time of 1 second for deciding on the validity of a dollar bill is not achieved. In fact, on average, it takes 10 seconds to get a response. Senior management discovers the cause. It seems that, to get the required 98 percent accuracy, a programmer has been instructed by her manager to use double-precision numbers for all mathematical calculations. As a result, every operation takes at least twice as long as it would with the usual single-precision numbers. The result is that the program is much slower than it should be, resulting in the long response time. Calculations then show that, despite what the manager told the programmer, the stipulated 98 percent accuracy can be at tained even if single-precision numbers are used. The programmer starts to make the necessary changes to the implementation. 

Episode 3 Before the programmer can complete her work, further tests of the sys tem show that, even if the indicated changes to the implementation were made, the system would still have an average response time of over 4.5 seconds, nowhere near the stipulated 1 second. The problem is the complex image recognition algorithm. Fortunately, a faster algorithm has just been discovered, so the fare machine software is redesigned and reimplemented using the new algorithm. This results in the average response time being successfully achieved. 

Episode 4 By now, the project is considerably behind schedule and way over budget. The mayor, a successful entrepreneur, has the bright idea of asking the software development team to try to increase the accuracy of the dollar bill recognition component of the system as much as possible, to sell the resulting package to vending machine companies. To meet this new requirement, a new design is adopted that improves the average accuracy to over 99.5 percent. Management decides to install that version of the software in the fare machines. At this point, development of the software is complete. The city is later able to sell its system to two small vending machine companies, defraying about one-third of the cost overrun. 

Epilogue A few years later, the sensors inside the fare machine become obsolete and need to be replaced by a newer model. Management suggests taking advantage of the change to upgrade the hardware at the same time. The software professionals point out that changing the hardware means that new software also is needed. They suggest reimplementing the software in a different programming language. At the 

FIGURE 2.2 The evolution-tree life-cycle model for the Winburg mini case study. (The rectangle drawn with a dotted line denotes the implementation that was not completed.) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/20ff17b36f5649a92232e30ae6999467934a2be28a5e77cdb435ea192ea2a025.jpg)


time of writing, the project is 6 months behind schedule and 25 percent over budget. However, everyone involved is confi dent that the new system will be more reliable and of higher quality, despite “minor discrepancies” in meeting its response time and accuracy requirements. 

Figure 2.2 depicts the evolution-tree life-cycle model of the mini case study. The leftmost boxes represent Episode 1. As shown in the fi gure, the system was developed from scratch (-). The requirements $( \mathsf { R e q u i r e m e n t s } _ { 1 } )$ , analysis $( \mathsf { A n a l y s i s } _ { 1 } )$ , design $( \mathsf { D e s i g n } _ { 1 } )$ , and implementation (Implementation  ) followed in turn. Next, as previously described, trials of the fi rst version of the software showed that the average response time of 1 second could not be achieved and the implementation had to be modifi ed. The modifi ed implementation appears in Figure 2.2 as Implementation . However, Implementation  was never completed. That is why the rectangle representing Implementation  is drawn with a dotted line. 

In Episode 3, the design had to be changed. Specifi cally, a faster image recognition algorithm was used. The modifi ed design $( { \mathsf { D e s i g n } } _ { 3 } )$ resulted in a modifi ed implementation (Implementation  ). 

Finally, in Episode 4, the requirements were changed (Requirements  ) to increase the accuracy. This resulted in modifi ed specifi cations $( \mathsf { A n a l y s i s } _ { 4 } )$ , modifi ed design $( \mathsf { D e s i g n } _ { 4 } )$ , and modifi ed implementation (Implementation  ). 

In Figure 2.2 , the solid arrows denote development and the dashed arrows denote maintenance. For example, when the design is changed in Episode 3, $\mathsf { D e s i g n } _ { 3 }$ replaced $\mathsf { D e s i g n } _ { 1 }$ as the design of $\mathsf { A n a l y s i s } _ { 1 }$ 

The evolution-tree model is an example of a life-cycle model (or model, for short), that is, the series of steps to be performed while the software product is developed and maintained. Another life-cycle model that can be used for the mini 

FIGURE 2.3 A simplifi ed version of the waterfall lifecycle model. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/43d7bf21afe94dbe254bfc21ce110c692a2b9d9cd5225cf4593fd450c2358fd8.jpg)


case study is the waterfall life-cycle model [Royce, 1970]; a simplifi ed version of the waterfall model is depicted in Figure 2.3 . This classical life-cycle model can be viewed as the linear model of Figure 2.1 with feedback loops. Then, if a fault is found during the design that was caused by a fault in the requirements, following the dashed upward arrows, the software developers can backtrack from the design up to the analysis and hence to the requirements and make the necessary corrections there. Then, they move down to the analysis, correct the specifi cation document to refl ect the corrections to the requirements, and in turn, correct the design document. Design activities can now resume where they were suspended when the fault was discovered. Again, the solid arrows denote development; the dashed arrows, maintenance. 

The waterfall model can certainly be used to represent the Winburg mini case study, but, unlike the evolution-tree model of Figure 2.2 , it cannot show the order of events. The evolution-tree model has a further advantage over the waterfall model. At the end of each episode we have a baseline , that is, a complete set of artifacts (recall that an artifact is a constituent component of a software product). There are four baselines in Figure 2.2 . They are 

At the end of Episode 1: Requirements , Analysis , Design , Implementation 

At the end of Episode 2: Requirements , Analysis , Design , Implementation 

At the end of Episode 3: Requirements , Analysis , Design , Implementation 

At the end of Episode 4: Requirements , Analysis , Design , Implementation 

The fi rst baseline is the initial set of artifacts; the second baseline refl ects the modifi ed (but never completed) Implementation  of Episode 2, together with the unchanged requirements, analysis, and design of Episode 1. The third baseline is the same as the fi rst baseline but with the design and implementation changed. The fourth baseline is the complete set of new artifacts shown in Figure 2.2 . We revisit the concept of a baseline in Chapters 5 and 16 . 

## 2.3 Lessons of the Winburg Mini Case Study

The Winburg mini case study depicts the development of a software product that goes awry for a number of unrelated causes, such as a poor implementation strategy (the unnecessary use of double-precision numbers) and the decision to use an algorithm that was too slow. In the end, the project was a success. However, the obvious question is, Is software development really as chaotic in practice? In fact, the mini case study is far less traumatic than many, if not the majority of, software projects. In the Winburg mini case study, there were only two new versions of the software because of faults (the inappropriate use of doubleprecision numbers; the utilization of an algorithm that could not meet the response time requirement), and only one new version because of a change made by the client (the need for increased accuracy). 

Why are so many changes to a software product needed? First, as previously stated, software professionals are human and therefore make mistakes. Second, a software product is a model of the real world, and the real world is continually changing. This issue is discussed at greater length in Section 2.4. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/188ae705e774136a15170e4989b5562bdf3cbbe6d694558b7a40ca9144636464.jpg)


## Teal Tractors Mini Case Study

Teal Tractors, Inc., sells tractors in most areas of the United States. The company has asked its software division to develop a new product that can handle all aspects of its business. For example, the product must be able to handle sales, inventory, and commissions paid to the sales staff, as well as providing all necessary accounting functions. While this software product is being implemented, Teal Tractors buys a Canadian tractor company. The management of Teal Tractors decides that, to save money, the Canadian operations are to be integrated into the U.S. operations. That means that the software has to be changed before it is completed: 

1. It must be modifi ed to handle additional sales regions. 

2. It must be extended to handle those aspects of the business that are handled differently in Canada, such as taxes. 

3. It must be extended to handle two different currencies, U.S. dollars and Canadian dollars. 

Teal Tractors is a rapidly growing company with excellent future prospects. The takeover of the Canadian tractor company is a positive development, one that may well lead to even greater profi ts in future years. But, from the viewpoint of the software division, the purchase of the Canadian company could be disastrous. Unless the requirements, analysis, and design have been performed with a view to incorporating possible future extensions, the work involved in adding the Canadian sales regions may be so great that it might be more effective to discard everything done to date and start from scratch. The reason is that changing the product at this stage is similar to trying to fi x a software product late in its life cycle (see Figure 1.6 ). Extending the software to handle aspects specifi c to the Canadian market, as well as Canadian currency, may be equally hard. 

Even if the software has been well thought out and the original design is indeed extensible, the design of the resulting patched-together product cannot be as cohesive as it would have been if it had been developed from the very beginning to cater to both the United States and Canada. This can have severe implications for future maintenance. 

The software division of Teal Tractors is a victim of the moving-target problem. That is, while the software is being developed, the requirements change. It does not matter that the reason for the change is otherwise extremely worthwhile. The fact is that the takeover of the Canadian company could well be detrimental to the quality of the software being developed. 

In some cases, the reason for the moving target is less benign. Sometimes a powerful senior manager within an organization keeps changing his or her mind regarding the functionality of a software product being developed. In other cases, there is feature creep , a succession of small, almost trivial, additions to the requirements. But whatever the reason may be, frequent changes, no matter how minor they may seem, are harmful to the health of a software product. It is important that a software product be designed as a set of components that are as independent as possible, so that a change to one part of the software does not induce a fault in an apparently unrelated part of the code, a so-called regression fault . When numerous changes are made, the effect is to induce dependencies within the code. Finally, there are so many dependencies that virtually any change induces one or more regression faults. At that time, the only thing that can be done is to redesign the entire software product and reimplement it. 

Unfortunately, there is no known solution to the moving-target problem. With regard to positive changes to requirements, growing companies are always going to change, and these changes have to be refl ected in the mission-critical software products of the company. As for negative changes, if the individual calling for those changes has suffi cient clout, nothing can be done to prevent the changes being implemented, to the detriment of the further maintainability of the software product. 

## 2.5 Iteration and Incrementation

As a consequence of both the moving-target problem and the need to correct the inevitable mistakes made while a software product is being developed, the life cycle of actual software products resembles the evolution-tree model of Figure 2.2 or the waterfall model of Figure 2.3 , rather than the idealized chain of Figure 2.1 . One consequence of this reality is that it does not make much sense to talk about (say) “ the analysis phase.” Instead, the operations of the analysis phase are spread out over the life cycle. Similarly, Figure 2.2 shows four different versions of the implementation, one of which (Implementation  ) was never completed because of the moving-target problem. 

Consider successive versions of an artifact, for example, the specifi cation document or a code module. From this viewpoint, the basic process is iterative. That is, we produce the fi rst version of the artifact, then we revise it and produce the second version, and so on. Our intent is that each version is closer to our target than its predecessor and fi nally we construct a version that is satisfactory. Iteration is an intrinsic aspect of software engineering, and iterative life-cycle models have been used for over 30 years [Larman and Basili, 2003]. For example, the waterfall model, which was fi rst put forward in 1970, is iterative (but not incremental). 

A second aspect of developing real-world software is the restriction imposed on us by Miller’s Law . In 1956, George Miller, a professor of psychology, showed that, at any one time, we humans are capable of concentrating on only approximately seven chunks (units of information) [Miller, 1956]. However, a typical software artifact has far more than seven chunks. For example, a code artifact is likely to have considerably more than seven variables, and a requirements document is likely to have many more than seven requirements. One way we humans handle this restriction on the amount of information we can handle at any one time is to use stepwise refi nement . That is, we concentrate on those aspects that are currently the most important and postpone until later those aspects that are currently less critical. In other words, every aspect is eventually handled but in order of current importance. This means that we start off by constructing an artifact that solves only a small part of what we are trying to achieve. Then, we consider further aspects of the problem and add the resulting new pieces to the existing artifact. For example, we might construct a requirements document by considering the seven requirements we consider the most important. Then, we would consider the seven next most important requirements, and so on. This is an incremental process. Incrementation is also an intrinsic aspect of software engineering; incremental software development is over 45 years old [Larman and Basili, 2003]. 

In practice, iteration and incrementation are used in conjunction with one another. That is, an artifact is constructed piece by piece (incrementation), and each increment goes through multiple versions (iteration). These ideas are illustrated in Figure 2.2 , which represents the life cycle for the Winburg mini case study (Sections 2.2 and 2.3). As shown in that fi gure, there is no single “requirements phase” as such. Instead, the client’s requirements are extracted and analyzed twice, yielding the original requirements (Requirements  ) and the modifi ed requirements (Requirements  ). Similarly, there is no single “implementation phase,” but rather four separate episodes in which the code is produced and then modifi ed. 

These ideas are generalized in Figure 2.4 , which refl ects the basic concepts underlying the iterative-and-incremental life-cycle model [Jacobson, Booch, and Rumbaugh, 1999]. The fi gure shows the development of a software product in four increments, labeled Increment A, Increment B, Increment C, and Increment D. The horizontal axis is time, and the vertical axis is person-hours (one person-hour is the amount of work that one person can do in 1 hour), so the shaded area under each curve is the total effort for that increment. 

It is important to appreciate that Figure 2.4 depicts just one possible way a software product can be decomposed into increments. Another software product may be constructed in just 2 increments, whereas a third may require 14. Furthermore, the fi gure is not intended to be an accurate representation of precisely how a software product is developed. Instead, it shows how the emphasis changes from iteration to iteration. 

The sequential phases of Figure 2.1 are artifi cial constructs. Instead, as explicitly refl ected in Figure 2.4 , we must acknowledge that different workfl ows (activities) are performed over the entire life cycle. There are fi ve core workfl ows , the requirements workfl ow , analysis workfl ow , design workfl ow , implementation workfl ow , and test workfl ow , and, as stated in the previous sentence, all fi ve are performed over the life cycle of a software product. However, there are times when one workfl ow predominates over the other four. 


FIGURE 2.4 The construction of a software product in four increments.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/240859a2ad4042219f05c1b477ffec6bc9ea2f1f51b51e589479a443d53e682e.jpg)


For example, at the beginning of the life cycle, the software developers extract an initial set of requirements. In other words, at the beginning of the iterative-and-incremental life cycle, the requirements workfl ow predominates. These requirements artifacts are extended and modifi ed during the remainder of the life cycle. During that time, the other four workfl ows (analysis, design, implementation, and test) predominate. In other words, the requirements workfl ow is the major workfl ow at the beginning of the life cycle, but its relative importance decreases thereafter. Conversely, the implementation and test workfl ows occupy far more of the time of the members of the software development team toward the end of the life cycle than they do at the beginning. 

Planning and documentation activities are performed throughout the iterative-and incremental life cycle. Furthermore, testing is a major activity during each iteration, and particularly at the end of each iteration. In addition, the software as a whole is thoroughly tested once it has been completed; at that time, testing and then modifying the implementation in the light of the outcome of the various tests is virtually the sole activity of the software team. This is refl ected in the test workfl ow of Figure 2.4. 

Figure 2.4 shows four increments. Consider Increment A, depicted by the column on the left. At the beginning of this increment, the requirements team members determine the client’s requirements. Once most of the requirements have been determined, the fi rst version of part of the analysis can be started. When suffi cient progress has been made with the analysis, the fi rst version of the design can be started. Even some coding is often done during this fi rst increment, perhaps in the form of a proof-of-concept prototype to test the feasibility of part of the proposed software product. Finally, as previously mentioned, 

FIGURE 2.5 The three iterations of Increment B of the iterativeand-incremental life-cycle model of Figure 2.4 . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/275d9189e5e1591a5c3b010d0051c30a1372e39b91fdb179e6df866f06d7cb75.jpg)


planning, testing, and documentation activities start on Day One and continue from then on, until the software product is fi nally delivered to the client. 

Similarly, the primary concentration during Increment B is on the requirements and analysis workfl ows, and then on the design workfl ow. The emphasis during Increment C is fi rst on the design workfl ow, and then on the implementation workfl ow and test workfl ow. Finally, during Increment D, the implementation workfl ow and test workfl ow dominate. 

As refl ected in Figure 1.4 , about one-fi fth of the total effort is devoted to the requirements and analysis workfl ows (together), another one-fi fth to the design workfl ow, and about three-fi fths to the implementation workfl ow. The relative total sizes of the shaded areas in Figure 2.4 refl ect these values. 

There is iteration during each increment of Figure 2.4 . This is shown in Figure 2.5 , which depicts three iterations during Increment B. ( Figure 2.5 is an enlarged view of the second column of Figure 2.4 .) As shown in Figure 2.5 , each iteration involves all fi ve workfl ows but again in varying proportions. 

Again, it must be stressed that Figure 2.5 is not intended to show that every increment involves exactly three iterations. The number of iterations varies from increment to increment. The purpose of Figure 2.5 is to show the iteration within each increment and repeat that all fi ve workfl ows (requirements, analysis, design, implementation, and testing, together with planning and documentation) are carried out during almost every iteration, although in varying proportions each time. 

As previously explained, Figure 2.4 refl ects the incrementation intrinsic to the development of every software product. Figure 2.5 explicitly displays the iteration that under lies incrementation. Specifi cally, Figure 2.5 depicts three consecutive iterative steps, as opposed to one large incrementation. In more detail, Iteration B.1 consists of requirements, analysis, design, implementation, and test workfl ows, represented by the leftmost dashed rectangle with rounded corners. The iteration continues until the artifacts of each of the fi ve workfl ows are satisfactory. 

Next, all fi ve sets of artifacts are iterated in Iteration B.2. This second iteration is similar in nature to the fi rst. That is, the requirements artifacts are improved, which in turn triggers improvements to the analysis artifacts, and so on, as refl ected in the second iteration of Figure 2.5 , and similarly for the third iteration. 

The process of iteration and incrementation starts at the beginning of Increment A and continues until the end of Increment D. The completed software product is then installed on the client’s computer. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/15f8e0bf2ba8ffee6520c8b8a9ba9549ee305dd73cd2bc37fff8444f99b2cbb6.jpg)


## Winburg Mini Case Study Revisited

Figure 2.6 shows the evolution-tree model of the Winburg mini case study ( Figure 2.2 ) superimposed on the iterative-and-incremental model (the test workfl ow is not shown because the evolution-tree model assumes continual testing, explained in Section 1.7). Figure 2.6 sheds additional light on the nature of incrementation: 

• Increment A corresponds to Episode 1, Increment B corresponds to Episode 2, and so on. 


FIGURE 2.6 The evolution-tree life-cycle model for the Winburg mini case study ( Figure 2.2 ) superimposed on the iterative-and-incremental life-cycle model.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/fa2d3fcb9f70c2376496e204909e6043e3e08bb1d5a2514d1676e61a4bee7825.jpg)


From the viewpoint of the iterative-and-incremental model, two of the increments do not include all four workfl ows. In more detail, Increment B (Episode 2) includes only the implementation workfl ow, and Increment C (Episode 3) includes only the design workfl ow and the implementation workfl ow. The iterative-and incremental model does not require that every workfl ow be performed during every increment. 

Furthermore, in Figure 2.4 most of the requirements workfl ow is performed in Increment A and Increment B, whereas in Figure 2.6 it is performed in Increment A and Increment D. Also, in Figure 2.4 most of the analysis is performed in Increment B, whereas in Figure 2.6 the analysis workfl ow is performed in Increment A and Increment D. This indicates that neither Figure 2.4 nor Figure 2.6 represents the way every software product is built. Instead, each fi gure shows the way that one particular software product is built, highlighting the under lying iteration and incrementation. 

• The small size and abrupt termination of the implementation workfl ow during Increment B (Episode 2) of Figure 2.6 shows that Implementation  was not completed. The gray piece refl ects the part of the implementation workfl ow that was not performed. 

The three dashed arrows of the evolution-tree model show that each increment constitutes maintenance of the previous increment. In this example, the second and third increments are instances of corrective maintenance. That is, each increment corrects faults in the previous increment. As previously explained, Increment B (Episode 2) corrects the implementation workfl ow by replacing double-precision variables with the usual single-precision variables. Increment C (Episode 3) corrects the design workfl ow by using a faster image recognition algorithm, thereby enabling the response time requirement to be met. Corresponding changes then have to be made to the implementation workfl ow. Finally, in Increment D (Episode 4) the requirements are changed to stipulate improved overall accuracy, an instance of perfective maintenance. Corresponding changes are then made to the analysis workfl ow, design workfl ow, and implementation workfl ow. 

## 2.7 Risks and Other Aspects of Iteration and Incrementation

Another way of looking at iteration and incrementation is that the project as a whole is divided into smaller mini projects (or increments). Each mini project extends the requirements, analysis, design, implementation, and testing artifacts. Finally, the resulting set of artifacts constitutes the complete software product. 

In fact, each mini project consists of more than just extending the artifacts. It is essential to check that each artifact is correct (the test workfl ow) and make any necessary changes to the relevant artifacts. This process of checking and modifying, then rechecking and remodifying, and so on, is clearly iterative in nature. It continues until the members of the development team are satisfi ed with all the artifacts of the current mini project (or increment). When that happens, they proceed to the next increment. 

Comparing Figure 2.3 (the waterfall model) with Figure 2.5 (view of the iterations within Increment B) shows that each iteration can be viewed as a small but complete waterfall model. That is, during each iteration the members of the development team go through the classical requirements, analysis, design, and implementation phases on a specifi c portion of the software product. From this viewpoint, the iterative-and-incremental model of Figures 2.4 and 2.5 can be viewed as a consecutive series of waterfall models. 

The iterative-and-incremental model has many strengths: 

1. Multiple opportunities are offered for checking that the software product is correct. Every iteration incorporates the test workfl ow, so every iteration is another chance to check all the artifacts developed up to this point. The later faults are detected and corrected, the higher is the cost, as shown in Figure 1.6 . Unlike the classical waterfall model, each of the many iterations of the iterative-and-incremental model offers a further opportunity to fi nd faults and correct them, thereby saving money. 

2. The robustness of the underlying architecture can be determined relatively early in the life cycle. The architecture of a software product includes the various component artifacts and how they fit together. An analogy is the architecture of a cathedral, which might be described as Romanesque, Gothic, or Baroque, among other possibilities. Similarly, the architecture of a software product might be described as object-oriented ( Chapter 7 ), pipes and filters (UNIX or Linux components), or client–server (with a central server providing file storage for a network of client computers). The architecture of a software product developed using the iterativeand-incremental model must have the property that it can be extended continually (and, if necessary, easily changed) to incorporate the next increment. Being able to handle such extensions and changes without falling apart is called robustness . Robustness is an important quality during development of a software product; it is vital during postdelivery maintenance. So, if a software product is to last through the usual 12, 15, or more years of postdelivery maintenance, the underlying architecture has to be robust. When an iterative-and-incremental model is used, it soon becomes apparent whether or not the architecture is robust. If, in the course of incorporating (say) the third increment, it is clear that the software developed to date has to be drastically reorganized and large parts reimplemented, then it is clear that the architecture is not sufficiently robust. The client must decide whether to abandon the project or start again from scratch. Another possibility is to redesign the architecture to be more robust, and then reuse as much of the current artifacts as possible before proceeding to the next increment. Another reason why a robust architecture is so important is the moving-target problem (Section 2.4). It is all but certain that the client’s requirements will change, either because of growth within the client’s organization or because the client keeps changing his or her mind as to what the target software has to do. The more robust the architecture, the more resilient to change the software will be. It is not possible to design an architecture that can cope with too many drastic changes. But, if the required changes are reasonable in scope, a robust architecture should be capable of incorporating those changes without having to be drastically restructured. 

3. The iterative-and-incremental model enables us to mitigate risks early. Risks are invariably involved in software development and maintenance. In the Winburg mini case study, for example, the original image recognition algorithm was not fast enough; there is an everpresent risk that a completed software product will not meet its time constraints. Developing a software product incrementally enables us to mitigate such risks early in the life cycle. For example, suppose a new local area network (LAN) is being developed and there is concern that the current network hardware is inadequate for the new software product. Then, the fi rst one or two iterations are directed toward constructing those parts of the software that interface with the network hardware. If it turns out that, contrary to the developers’ fears, the network has the necessary capability, the developers can proceed with the project, confi dent that this risk has been mitigated. On the other hand, if the network indeed cannot cope with the additional traffi c that the new LAN generates, this is reported to the client early in the life cycle, when only a small proportion of the budget has been spent. The client can now decide whether to cancel the project, extend the capabilities of the existing network, buy a new and more powerful network, or take some other action. 

4. We always have a working version of the software. Suppose a software product is developed using the classical life-cycle model of Figure 2.1 . Only at the very end of the project is there a working version of the software product. In contrast, when the iterative-and-incremental life-cycle model is used, at the end of each iteration, there is a working version of part of the overall target software product. The client and the intended users can experiment with that version and determine what changes are needed to ensure that the future complete implementation meets their needs. These changes can be made to a subsequent increment, and the client and users can then determine if further changes are needed. A variation on this is to deliver partial versions of the software product, not only for experimentation but also to smooth the introduction of the new software product in the client organization. Change is almost always perceived as a threat. All too often, users fear that the introduction of a new software product within the workplace will result in them losing their jobs to a computer. However, introducing a software product gradually can have two benefi ts. First, the understandable fear of being replaced by a computer is diminished. Second, it is generally easier to learn the functionality of a complex software product if that functionality is introduced stepwise over a period of months, rather than as a whole. 

5. There is empirical evidence that the iterative-and-incremental life cycle works. The pie chart of Figure 1.1 shows the results of the report from the Standish Group on projects completed in 2006 [Rubenstein, 2007]. In fact, this report (the so-called CHAOS Report— see Just in Case You Wanted to Know Box 2.2) is produced every 2 years. Figure 2.7 shows the results for 1994 through 2006. The percentage of successful products increased steadily from 16 percent in 1994 to 34 percent in 2002, but then decreased to 29 percent in 2004. In both the 2002 [Softwaremag.com, 2004] and 2004 [Hayes, 2004] reports, one of the factors associated with the successful projects was the use of an iterative process. (The reasons given for the decrease in the percentage of successful projects in 2004 included: more large projects than in 2002, use of the waterfall model, lack of user involvement, and lack of support from senior executives [Hayes, 2004].) Then, the percentage of successful projects increased again in the 2006 study to 35 percent. The president of the Standish Group, Jim Johnson, attributed this increase to three factors: better project management, the emerging Web infrastructure, and (again) iterative development [Rubenstein, 2007]. 

The term CHAOS is an acronym. For some unknown reason, the Standish Group keeps the acronym top secret. They state [Standish, 2003]: 

Only a few people at The Standish Group, and any one of the 360 people who received and saved the T-shirts we gave out after they completed the fi rst survey in 1994, know what the CHAOS letters represent. 

FIGURE 2.7 Results of the Standish Group CHAOS Report from 1994 to 2006. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/2a4b63389af60e90a26c21e9bbfd967b111062e2beecf2c4de7cc276f6581656.jpg)


## 2.8 Managing Iteration and Incrementation

At fi rst glance, the iterative-and-incremental model of Figures 2.4 and 2.5 looks totally chaotic. Instead of the orderly progression from requirements to implementation of the waterfall model ( Figure 2.3 ), it appears that developers do whatever they like, perhaps some coding in the morning, an hour or two of design after lunch, and then half an hour of specifying before going home. That is not the case. On the contrary, the iterative-and-incremental model is as regimented as the waterfall model, because as previously pointed out, developing a software product using the iterative-and-incremental model is nothing more or less than developing a series of smaller software products, all using the waterfall model. 

In more detail, as shown in Figure 2.3 , developing a software product using the waterfall model means successively performing the requirements, analysis, design, and implementation phases (in that order) on the software product as a whole. If a problem is encountered, the feedback loops of Figure 2.3 (dashed arrows) are followed; that is, iteration (maintenance) is performed. However, if the same software product is developed using the iterative-and-incremental model, the software product is treated as a set of increments. For each increment in turn, the requirements, analysis, design, and implementation phases (in that order) are repeatedly performed on that increment until it is clear that no further iteration is needed. In other words, the project as a whole is broken up into a series of waterfall mini projects. During each mini project, iteration is performed as needed, as shown in Figure 2.5 . Therefore, the reason the previous paragraph stated that the iterative-and-incremental model is as regimented as the waterfall model is because the iterative-and-incremental model is the waterfall model, applied successively. 

## 2.9 Other Life-Cycle Models

We now consider a number of other life-cycle models, including the spiral model and the synchronize-and-stabilize model. We begin with the infamous code-and-fi x model. 

## 2.9.1 Code-and-Fix Life-Cycle Model

It is unfortunate that so many products are developed using what might be termed the code-and-fix life-cycle model . The product is implemented without requirements or specifications, or any attempt at design. Instead, the developers simply throw code together and rework it as many times as necessary to satisfy the client. This approach is shown in Figure 2.8 , which clearly displays the absence of requirements, specifi cations, and design. Although this approach may work well on short programming exercises 100 or 200 lines long, the code-and-fi x model is totally unsatisfactory for products of any reasonable size. Figure 1.6 shows that the cost of changing a software product is relatively small if the 

FIGURE 2.8 The code-andfi x life-cycle model. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/cfe54248e2cca009e01c9dacbce1ba6c1ca825c4bdc121f1ef73cbdb4cdbc347.jpg)


change is made during the requirements, analysis, or design phases but grows unacceptably large if changes are made after the product has been coded or, worse, if it has already been delivered and installed on the client’s computer. Hence, the cost of the code-and-fi x approach is actually far greater than the cost of a properly specifi ed and meticulously designed product. In addition, maintenance of a product can be extremely diffi cult without specifi cation or design documents, and the chances of a regression fault occurring are considerably greater. Instead of the code-and-fi x approach, it is essential that, before development of a product begins, an appropriate life-cycle model be chosen. 

Regrettably, all too many projects use the code-and-fi x model. The problem is particularly acute in organizations that measure progress solely in terms of lines of code, so members of the software development team are pressured into churning out as many lines of code as possible, starting on Day One of the project. The code-and-fi x model is the easiest way to develop software—and by far the worst way. 

A simplifi ed version of the waterfall model was presented in Section 2.2. We now consider that model in more detail. 

## 2.9.2 Waterfall Life-Cycle Model

The waterfall life-cycle model was fi rst put forward by Royce [1970]. Figure 2.9 shows the feedback loops for maintenance while the product is being developed, as refl ected in Figure 2.3 , the simplifi ed waterfall model. Figure 2.9 also shows the feedback loops for postdelivery maintenance. 

A critical point regarding the waterfall model is that no phase is complete until the documentation for that phase has been completed and the products of that phase have been approved by the software quality assurance (SQA) group. This carries over into modifi cations; if the products of an earlier phase have to be changed as a consequence of following 

FIGURE 2.9 The full waterfall lifecycle model. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/a3542f849f7773d77e85c21da6bf0471395242d2536939e0e028250fd38a32b4.jpg)


a feedback loop, that earlier phase is deemed to be complete only when the documentation for the phase has been modifi ed and the modifi cations have been checked by the SQA group. Inherent in every phase of the waterfall model is testing. Testing is not a separate phase to be performed only after the product has been constructed, nor is it to be performed only at the end of each phase. Instead, as stated in Section 1.7, testing should proceed continually throughout the software process. In particular, during maintenance, it is necessary to ensure not only that the modifi ed version of the product still does what the previous version did—and still does it correctly (regression testing)—but that it also satisfi es any new requirements imposed by the client. 

The waterfall model has many strengths, including the enforced disciplined approach—the stipulation that documentation be provided at each phase and the requirement that all the products of each phase (including the documentation) be meticulously checked by SQA. However, the fact that the waterfall model is documentation driven can also be a weakness. To see this, consider the following two somewhat bizarre scenarios. 

First, Joe and Jane Johnson decide to build a house. They consult with an architect. Instead of showing them sketches, plans, and perhaps a scale model, the architect gives them a 20-page single-spaced typed document describing the house in highly technical terms. Even though both Joe and Jane have no previous architectural experience and hardly understand the document, they enthusiastically sign it and say, “Go right ahead, build the house!” 

Another scenario is as follows: Mark Marberry buys his suits by mail order. Instead of mailing him pictures of their suits and samples of available cloths, the company sends Mark a written description of the cut and the cloth of their products. Mark then orders a suit solely on the basis of a written description. 

The preceding two scenarios are highly unlikely. Nevertheless, they typify precisely the way software is often constructed using the waterfall model. The process begins with the specifi cations. In general, specifi cation documents are long, detailed, and, quite frankly, boring to read. The client is usually inexperienced in the reading of software specifi cations, and this diffi culty is compounded by the fact that specifi cation documents are usually written in a style with which the client is unfamiliar. The diffi culty is even worse when the specifi cations are written in a formal specifi cation language like Z [Spivey, 1992] (Section 12.9). Nevertheless, the client proceeds to sign off on the specifi cation document, whether properly understood or not. In many ways there is little difference between Joe and Jane Johnson contracting to have a house built from a written description that they only partially comprehend and clients approving a software product described in terms of a specifi cation document that they only partially understand. 

Mark Marberry and his mail-order suits may seem bizarre in the extreme, but that is precisely what happens when the waterfall model is used in software development. The fi rst time that the client sees a working product is only after the entire product has been coded. Small wonder that software developers live in fear of the sentence, “I know this is what I asked for, but it isn’t really what I wanted.” 

What has gone wrong? There is a considerable difference between the way a client understands a product as described by the specifi cation document and the actual product. The specifi cations exist only on paper; the client therefore cannot really understand what the product itself will be like. The waterfall model, depending as it does so crucially on written specifi cations, can lead to the construction of products that simply do not meet the client’s real needs. 

In fairness it should be pointed out that, just as an architect can help a client understand what is to be built by providing scale models, sketches, and plans, so the software engineer can use graphical techniques, such as data fl ow diagrams (Section 12.3) or UML diagrams ( Chapter 17 ) to communicate with the client. The problem is that these graphical aids do not describe how the fi nished product will work. For example, there is a considerable difference between a fl owchart (a diagrammatic description of a product) and the working product itself. In this book, two solutions are put forward for solving the problem that the specifi cation document generally does not describe a product in a way that enables the client to determine whether the proposed product meets his or her needs. The object-oriented solution is described in Chapters 11 and 13 . The classical solution is the rapid-prototyping model, described in Section 2.9.3. 

## 2.9.3 Rapid-Prototyping Life-Cycle Model

A rapid prototype is a working model that is functionally equivalent to a subset of the product. For example, if the target product is to handle accounts payable, accounts receivable, and warehousing, then the rapid prototype might consist of a product that performs the screen handling for data capture and prints the reports, but does no fi le updating or error handling. A rapid prototype for a target product that is to determine the concentration of an enzyme in a solution might perform the calculation and display the answer, but without doing any validation or reasonableness checking of the input data. 

The fi rst step in the rapid-prototyping life-cycle model depicted in Figure 2.10 is to build a rapid prototype and let the client and future users interact and experiment with the rapid prototype. Once the client is satisfi ed that the rapid prototype indeed does most of 

FIGURE 2.10 The rapidprototyping lifecycle model. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/982ef45c2f575a1f1a61880c4a834c994903a510feb10700afa5db0c6ca620e6.jpg)


what is required, the developers can draw up the specifi cation document with some assurance that the product meets the client’s real needs. 

Having produced the rapid prototype, the software process continues as shown in Figure 2.10 . A major strength of the rapid-prototyping model is that the development of the product is essentially linear, proceeding from the rapid prototype to the delivered product; the feedback loops of the waterfall model ( Figure 2.9 ) are less likely to be needed in the rapid-prototyping model. There are a number of reasons for this. First, the members of the development team use the rapid prototype to construct the specifi cation document. Because the working rapid prototype has been validated through interaction with the client, it is reasonable to expect that the resulting specifi cation document will be correct. Second, consider the design. Even though the rapid prototype has (quite rightly) been hurriedly assembled, the design team can gain insight from it—at worst it will be of the “how not to do it” variety. Again, the feedback loops of the waterfall model are less likely to be needed here. 

Implementation comes next. In the waterfall model, implementation of the design sometimes leads to design faults coming to light. In the rapid-prototyping model, the fact that a preliminary working version of the software product has already been built tends to lessen the need to repair the design during or after implementation. The prototype has given some insights to the design team, even though it may refl ect only partial functionality of the complete target product. 

Once the product has been accepted by the client and installed, postdelivery maintenance begins. Depending on the specifi c maintenance task that has to be performed, the cycle is reentered either at the requirements, analysis, design, or implementation phase. 

An essential aspect of a rapid prototype is embodied in the word rapid . The developers should endeavor to construct the rapid prototype as rapidly as possible to speed up the software development process. After all, the sole use of the rapid prototype is to determine what the client’s real needs are; once this has been determined, the rapid prototype implementation is discarded but the lessons learned are retained and used in subsequent development phases. For this reason, the internal structure of the rapid prototype is not relevant. What is important is that the prototype be built rapidly and modifi ed rapidly to refl ect the client’s needs. Therefore, speed is of the essence. 

Rapid prototyping is discussed in greater detail in Chapter 11. 

## 2.9.4 Open-Source Life-Cycle Model

Almost all successful open-source software projects go through two informal phases. First, a single individual has an idea for a program, such as an operating system (Linux), a Net browser (Firefox), or a Web server (Apache). He or she builds an initial version, which is then made available for distribution free of charge to anyone who would like a copy; nowadays, this is done via the Internet, at sites like SourceForge.net and FreshMeat.net. If someone downloads a copy of the initial version and thinks that the program fulfi lls a need, he or she will start to use that program. 

If there is suffi cient interest in the program, the project moves gradually into informal phase two. Users become co-developers, in that some users report defects and others suggest ways of fi xing those defects. Some users put forward ideas for extending the program, 

FIGURE 2.11 The opensource life-cycle model. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/c3e5cba4100869e5a7f8341c9b2238e8593c66c314fc4468084f68ec2b0c9557.jpg)


and others implement those ideas. As the program expands in functionality, yet other users port the program so that it can run on additional operating system/hardware combinations. A key aspect is that individuals usually work on an open-source project in their spare time on a voluntary basis; they are not paid to participate. 

Now look more closely at the three activities of the second informal phase: 

1. Reporting and correcting defects is corrective maintenance. 

2. Adding additional functionality is perfective maintenance. 

3. Porting the program to a new environment is adaptive maintenance. 

In other words, the second informal phase of the open-source life-cycle model consists solely of postdelivery maintenance, as shown in Figure 2.11 . In fact, the term co-developers in the second paragraph of this section should rather be co-maintainers. 

There are a number of key differences between closed-source and open-source software life-cycle models: 

• Closed-source software is maintained and tested by teams of employees of the organization that owns the software. Users sometimes submit defect reports. However, these are restricted to failure reports (reports of observed incorrect behavior); users have no access to the source code, so they cannot possibly submit fault reports (reports that describe where the source code is incorrect and how to correct it). 

In contrast, open-source software is generally maintained by unpaid volunteers. Users are strongly encouraged to submit defect reports. Although all users have access to the source code, only the minority have the inclination and the time, as well as the necessary skills, to peruse the source code and submit fault reports (“fi xes”); most defect reports are therefore failure reports. There is generally a core group of dedicated maintainers who take responsibility for managing the open-source project. Some members of the peripheral group , that is, the users who are not members of the core group, choose to submit defect reports from time to time. The members of the core group are responsible for ensuring that these defects are corrected. In more detail, when a fault report is submitted, a core group member checks that the fi x indeed solves the problem and modifi es the source code appropriately. When a failure report is submitted, a member of the core group will either personally determine the fi x or assign that task to another volunteer, often a member of the peripheral group who is eager to become more involved in the open-source project. Again, the power to install the fi x in the software is restricted to members of the core group. 

• New versions of closed-source software are typically released roughly once a year. Each new version is carefully checked by the software quality assurance group before release; a wide variety of test cases are run. 

In contrast, a dictum of the open-source movement is “Release early. Release often” [Raymond, 2000]. That is, the core group releases a new version of an open-source product as soon as it is ready, which may be a month or even only a day after the previous version was released. This new version is released after minimal testing; it is assumed that more extensive testing will be performed by the members of the peripheral group. A new version may be installed by literally hundreds of thousands of users within a day or two of its release. These users do not run test cases as such. However, in the course of utilizing the new version on their computer, they encounter failures, which they report via e-mail. In this way, faults in the new version (as well as deeper faults in previous versions) come to light and are corrected. 

Comparing Figures 2.8 , 2.10 , and 2.11 , we see that the open-source life-cycle model has features in common with both the code-and-fi x model and the rapid-prototyping model. In all three life-cycle models, an initial working version is produced. In the case of the rapid-prototyping model, this initial version is discarded, and the target product is then specifi ed and designed before being coded. In both the code-and-fi x and opensource life-cycle models, the initial version is reworked until it becomes the target product. Accordingly, in an open-source project, there are generally no specifi cations or design. 

Bearing in mind the great importance of having specifi cations and designs, how have some open-source projects been so successful? In the closed-source world, some software professionals are more skilled and some are less skilled (see Section 9.2). The challenge of producing open-source software has attracted some of the fi nest software experts. In other words, an open-source project can be successful, despite the lack of specifi cations or design, if the skills of the individuals who work on that project are so superb that they can function effectively without specifi cations or design. 

The open-source life-cycle model is restricted in its applicability. On the one hand, the open-source model has been exceedingly successfully used for certain infrastructure software projects, such as operating systems (Linux, OpenBSD, Mach, Darwin), Web browsers (Firefox, Netscape), compilers (gcc), Web servers (Apache), or database management systems (MySQL). On the other hand, it is hard to conceive of open-source development of a software product to be used only in one commercial organization. A key to open-source software development is that the members of both the core group and the periphery are users of the software being developed. Consequently, the open-source life-cycle model is inapplicable unless the target product is viewed by a wide range of users as useful to them. 

At the time of writing, there are about 350,000 open-source projects at SourceForge. net and FreshMeat.net. About half them have never even attracted a team to work on the project. Of those where work has started, the overwhelming preponderance have never been completed and are unlikely to ever progress much further. But when the open-source model has worked, it has sometimes been incredibly successful. The open-source products listed in parentheses in the previous paragraph are widely used; most of them are utilized on a regular basis by literally millions of users. 

Explanations for the success of the open-source life-cycle model are presented in Chapter 4 within the context of team organizational aspects of open-source software projects. 

## 2.9.5 Agile Processes

Extreme programming [Beck, 2000] is a somewhat controversial new approach to software development based on the iterative-and-incremental model. The fi rst step is that the software development team determines the various features ( stories ) the client would like the product to support. For each such feature, the team informs the client how long it will take to implement that feature and how much it will cost. This fi rst step corresponds to the requirements and analysis workfl ows of the iterative-and-incremental model ( Figure 2.4 ). 

The client selects the features to be included in each successive build using cost– benefi t analysis (Section 5.2), that is, on the basis of the duration and the cost estimates provided by the development team as well as the potential benefi ts of the feature to his or her business. The proposed build is broken down into smaller pieces termed tasks . A programmer first draws up test cases for a task; this is termed test-driven development (TDD). Two programmers work together on one computer ( pair programming ) [Williams, Kessler, Cunningham, and Jeffries, 2000], implementing the task and ensuring that all the test cases work correctly. The two programmers alternate typing every 15 or 20 minutes; the programmer who is not typing carefully checks the code while it is being entered by his or her partner. The task is then integrated into the current version of the product. Ideally, implementing and integrating a task should take no more than a few hours. In general, a number of pairs will implement tasks in parallel, so integration is essentially continuous. Team members change coding partners daily, if possible; learning from the other team members increases everyone’s skill level. The TDD test cases used for the task are retained and utilized in all further integration testing. 

Some drawbacks to pair programming have been observed in practice [Drobka, Noftz, and Raghu, 2004]. For example, pair programming requires large blocks of uninterrupted time, and software professionals can have diffi culty in fi nding 3- to 4-hour blocks of time. In addition, pair programming does not always work well with shy or overbearing individuals, or with two inexperienced programmers. 

A number of features of extreme programming (XP) are somewhat different from the way in which software is usually developed: 

• The computers of the XP team are set up in the center of a large room lined with small cubicles. 

• A client representative works with the XP team at all times. 

• No individual can work overtime for two successive weeks. 

• There is no specialization. Instead, all members of the XP team work on requirements, analysis, design, code, and testing. 

• There is no overall design step before the various builds are constructed. Instead, the design is modified while the product is being built. This procedure is termed refactoring. Whenever a test case will not run, the code is reorganized until the team is satisfi ed that the design is simple, straightforward, and runs all the test cases satisfactorily. 

Two acronyms now associated with extreme programming are YAGNI (you aren’t gonna need it) and DTSTTCPW (do the simplest thing that could possibly work). In other words, a principle of extreme programming is to minimize the number of features; there is no need to build a product that does any more than what the client actually needs. 

Extreme programming is one of a number of new paradigms that are collectively referred to as agile processes . Seventeen software developers (later dubbed the Agile Alliance) met at a Utah ski resort for two days in February 2001 and produced the Manifesto for Agile Software Development [Beck et al., 2001]. Many of the participants had previously authored their own software development methodologies, including Extreme Programming [Beck, 2000], Crystal [Cockburn, 2001], and Scrum [Schwaber, 2001]. Consequently, the Agile Alliance did not prescribe a specifi c life-cycle model, but rather laid out a group of underlying principles that were common to their individual approaches to software development. 

Agile processes are characterized by considerably less emphasis on analysis and design than in almost all other modern life-cycle models. Implementation starts much earlier in the life cycle because working software is considered more important than detailed documentation. Responsiveness to changes in requirements is another major goal of agile processes, and so is the importance of collaborating with the client. 

One of the principles in the Manifesto is to deliver working software frequently, ideally every 2 or 3 weeks. One way of achieving this is to use timeboxing [Jalote, Palit, Kurien, and Peethamber, 2004], which has been used for many years as a time management technique. A specifi c amount of time is set aside for a task, and the team members then do the best job they can during that time. Within the context of agile processes, typically 3 weeks are set aside for each iteration. On the one hand, it gives the client confi dence to know that a new version with additional functionality will arrive every 3 weeks. On the other hand, the developers know that they will have 3 weeks (but no more) to deliver a new iteration without client interference of any kind; once the client has chosen the work for an iteration, it cannot be changed or increased. However, if it is impossible to complete the entire task in the timebox, the work may be reduced (“descoped”). In other words, agile processes demand fi xed time, not fi xed features. 

Another common feature of agile processes is to have a short meeting at a regular time each day. All team members have to attend the meeting. Making all the participants stand in a circle, rather than sit around a table, helps to ensure that the meeting lasts no more than the stipulated 15 minutes. Each team member in turn answers fi ve questions: 

• What have I done since yesterday’s meeting? 

• What am I working on today? 

• What problems are preventing me from achieving this? 

• What have we forgotten? 

• What did I learn that I would like to share with the team? 

The aim of the stand-up meeting is to raise problems, not solve them; solutions are found at follow-up meetings, preferably held directly after the stand-up meeting. Like timeboxing, stand-up meetings are a successful management technique now utilized within the context of agile processes. Both timeboxed iterations and stand-up meetings are instances of two basic principles that underlie all agile methods: communication and satisfying the client’s needs as quickly as possible. 

Agile processes have been successfully used on a number of small-scale projects. However, agile processes have not yet been used widely enough to determine whether this approach will fulfi ll its early promise. Furthermore, even if agile processes turn out to be good for small-scale software products, that does not necessarily mean that they can be used for medium- or large-scale software products, as will now be explained 

To appreciate why many software professionals have expressed doubts about agile processes within the context of medium- and especially large-scale software products [Reifer, Maurer, and Erdogmus, 2003], consider the following analogy by Grady Booch [2000]. Anyone can successfully hammer together a few planks to build a doghouse, but it would be foolhardy to build a three-bedroom home without detailed plans. In addition, skills in plumbing, wiring, and roofi ng are needed to build a three-bedroom home, and inspections are essential. (That is, being able to build small-scale software products does not necessarily mean that one has the skills for building medium-scale software products.) Furthermore, the fact that a skyscraper is the height of 1000 doghouses does not mean that one can build a skyscraper by piling 1000 doghouses on top of one another. In other words, building large-scale software products requires even more specialized and sophisticated skills than those needed to cobble together small-scale software products. 

A key determinant in deciding whether agile processes are indeed a major breakthrough in software engineering will be the cost of future postdelivery maintenance (Section 1.3.2). That is, if the use of agile processes results in a reduction in the cost of postdelivery maintenance, XP and other agile processes will become widely adopted. On the other hand, refactoring is an intrinsic component of agile processes. As previously explained, the product is not designed as a whole; instead, the design is developed incrementally, and the code is reorganized whenever the current design is unsatisfactory for any reason. This refactoring then continues during postdelivery maintenance. If the design of a product when it passes its acceptance test is openended and fl exible, then perfective maintenance should be easy to achieve at a low cost. However, if the design has to be refactored whenever additional functionality is added, then the cost of postdelivery maintenance of that product will be unacceptably high. As a consequence of the newness of the approach, there are still essentially no data on the maintenance of software developed using agile processes. However, preliminary maintenance data indicate that refactoring can consume a large percentage of the overall cost [Li and Alshayeb, 2002]. 

Experiments have shown that certain features of agile processes can work well. For example, Williams, Kessler, Cunningham, and Jeffries [2000] showed that pair programming leads to the development of higher-quality code in a shorter time, with greater job satisfaction. However, an extensive experiment to evaluate pair programming within the context of software maintenance described in Section 4.6 [Arisholm, Gallis, Dybå, and Sjøberg, 2007] came to the same conclusion as an analysis of 15 published studies comparing the effectiveness of individual and pair programming [Dybå et al., 2007]: It depends on both the programmer’s expertise and the complexity of the software product and the tasks to be solved. 

The Manifesto for Agile Software Development essentially claims that agile processes are superior to more disciplined processes like the Unifi ed Process ( Chapter 3 ). Skeptics respond that proponents of agile processes are little more than hackers. However, there is a middle ground. The two approaches are not incompatible; it is possible to incorporate proven features of agile processes within the framework of disciplined processes. This integration of the two approaches is described in books such as the one by Boehm and Turner [2003]. 

In conclusion, agile processes appear to be a useful approach to building small-scale software products when the client’s requirements are vague. In addition, some of the features of agile processes can be effectively utilized within the context of other life-cycle models. 

## 2.9.6 Synchronize-and-Stabilize Life-Cycle Model

Microsoft, Inc., is the world’s largest manufacturer of COTS software. The majority of its packages are built using a version of the iterative-and-incremental model that has been termed the synchronize-and-stabilize life-cycle model [Cusumano and Selby, 1997]. 

The requirements analysis phase is conducted by interviewing numerous potential clients for the package and extracting a list of features of highest priority to the clients. A specifi cation document is now drawn up. Next, the work is divided into three or four builds. The fi rst build consists of the most critical features, the second build consists of the next most critical features, and so on. Each build is carried out by a number of small teams working in parallel. At the end of each day, all the teams synchronize ; that is, they put the partially completed components together and test and debug the resulting product. Stabilization is performed at the end of each of the builds. Any remaining faults that have been detected so far are fi xed, and they now freeze the build; that is, no further changes will be made to the specifi cations. 

The repeated synchronization step ensures that the various components always work together. Another advantage of this regular execution of the partially constructed product is that the developers obtain early insight into the operation of the product and can modify the requirements if necessary during the course of a build. The life-cycle model can be used even if the initial specifi cation is incomplete. The synchronize-and-stabilize model is considered further in Section 4.5, where team organizational details are discussed. 

The spiral model has been left to last because it incorporates aspects of all the other models described in Section 2.9. 

## 2.9.7 Spiral Life-Cycle Model

As stated in Section 2.5, an element of risk is always involved in the development of software. For example, key personnel can resign before the product has been adequately documented. The manufacturer of hardware on which the product is critically dependent can go bankrupt. Too much, or too little, can be invested in testing and quality assurance. After spending hundreds of thousands of dollars on developing a major software product, technological breakthroughs can render the entire product worthless. An organization may research and develop a database management system, but before the product can be marketed, a lower-priced, functionally equivalent package is announced by a competitor. The components of a product may not fi t together when integration is performed. For obvious reasons, software developers try to minimize such risks wherever possible. 

One way of minimizing certain types of risk is to construct a prototype. As described in Section 2.9.3, one approach to reducing the risk that the delivered product will not satisfy the client’s real needs is to construct a rapid prototype during the requirements phase. During subsequent phases, other sorts of prototypes may be appropriate. For example, a telephone company may devise a new, apparently highly effective algorithm for routing calls through a long-distance network. If the product is implemented but does not work as expected, the telephone company will have wasted the cost of developing the product. In addition, angry or inconvenienced customers may take their business elsewhere. This outcome can be avoided by constructing a proof-of-concept prototype to handle only the routing of calls and testing it on a simulator. In this way, the actual system is not disturbed; and for the cost of implementing just the routing algorithm, the telephone company can determine whether it is worthwhile to develop an entire network controller incorporating the new algorithm. 

A proof-of-concept prototype is not a rapid prototype constructed to be certain that the requirements have been accurately determined, as described in Section 2.9.3. Instead, it is more like an engineering prototype, that is, a scale model constructed to test the feasibility of construction. If the development team is concerned whether a particular part of the proposed software product can be constructed, a proof-of-concept prototype is constructed. For example, the developers may be concerned whether a particular computation can be performed quickly enough. In that case, they build a prototype to test the timing of just that computation. Or they may be worried that the font they intend to use for all screens will be too small for the average user to read without eyestrain. In this instance, they construct a prototype to display a number of different screens and determine by experiment whether the users fi nd the font uncomfortably small. 

The idea of minimizing risk via the use of prototypes and other means is the idea underlying the spiral life-cycle model [Boehm, 1988]. A simplifi ed way of looking at this lifecycle model is as a waterfall model with each phase preceded by risk analysis, as shown in Figure 2.12 . Before commencing each phase, an attempt is made to mitigate (control) the risks. If it is impossible to mitigate all the signifi cant risks at that stage, then the project is immediately terminated 

FIGURE 2.12 A simplifi ed version of the spiral life-cycle model. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/eeb1a24d18c3779c7969384bd231eb816765a9877dc2a5ede330e1d7ead38b61.jpg)


Prototypes can be used effectively to provide information about certain classes of risk. For example, timing constraints can generally be tested by constructing a prototype and measuring whether the prototype can achieve the necessary performance. If the prototype is an accurate functional representation of the relevant features of the product, then measurements made on the prototype should give the developers a good idea as to whether the timing constraints can be achieved. 

Other areas of risk are less amenable to prototyping, for example, the risk that the software personnel necessary to build the product cannot be hired or that key personnel may resign before the project is complete. Another potential risk is that a particular team may not be competent enough to develop a specifi c large-scale product. A successful contractor who builds single-family homes would probably not be able to build a highrise offi ce complex. In the same way, there are essential differences between small-scale and large-scale software, and prototyping is of little use. This risk cannot be mitigated by testing team performance on a much smaller prototype, in which team organizational issues specifi c to large-scale software cannot arise. Another area of risk for which prototyping cannot be employed is evaluating the delivery promises of a hardware supplier. A strategy the developer can adopt is to determine how well previous clients of the supplier have been treated, but past performance is by no means a certain predictor of future performance. A penalty clause in the delivery contract is one way of trying to ensure that essential hardware is delivered on time, but what if the supplier refuses to sign an agreement that includes such a clause? Even with a penalty clause, late delivery may occur and eventually lead to legal action that can drag on for years. In the meantime, the software developer may have gone bankrupt because nondelivery of the promised hardware caused nondelivery of the promised software. In short, whereas prototyping helps reduce risk in some areas, in other areas it is at best a partial answer, and in still others it is no answer at all. 

The full spiral model is shown in Figure 2.13 . The radial dimension represents cumulative cost to date, and the angular dimension represents progress through the spiral. Each cycle of the spiral corresponds to a phase. A phase begins (in the top left quadrant) by determining objectives of that phase, alternatives for achieving those objectives, and constraints imposed on those alternatives. This process results in a strategy for achieving those objectives. Next, that strategy is analyzed from the viewpoint of risk. Attempts are made to mitigate every potential risk, in some cases by building a prototype. If certain risks cannot be mitigated, the project may be terminated immediately; under some circumstances, however, a decision could be made to continue the project but on a signifi cantly smaller scale. If all risks are successfully mitigated, the next development step is started (bottom right quadrant). This quadrant of the spiral model corresponds to the classical waterfall model. Finally, the results of that phase are evaluated and the next phase is planned. 

The spiral model has been used successfully to develop a wide variety of products. In one set of 25 projects in which the spiral model was used in conjunction with other means of increasing productivity, the productivity of every project increased by at least 50 percent over previous productivity levels and by 100 percent in most of the projects [Boehm, 1988]. To be able to decide whether the spiral model should be used for a given project, the strengths and weaknesses of the spiral model are now assessed. 

The spiral model has a number of strengths. The emphasis on alternatives and con straints supports the reuse of existing software (Section 8.1) and the incorporation of software quality as a specifi c objective. In addition, a common problem in software development is determining when the products of a specifi c phase have been adequately tested. Spending too much time on testing is a waste of money, and delivery of the product may be unduly delayed. Conversely, if too little testing is performed, then the delivered software may contain residual faults, resulting in unpleasant consequences for the developers. The spiral model answers this question in terms of the risks that would be incurred by not doing enough testing or by doing too much testing. Perhaps most important, within the structure of the spiral model, postdelivery maintenance is simply another cycle of the spiral; there is essentially no distinction between postdelivery maintenance and development. Therefore, the problem that postdelivery maintenance is sometimes maligned by ignorant software professionals does not arise, because postdelivery maintenance is treated the same way as development. 


FIGURE 2.13 Full spiral life-cycle model [Boehm, 1988]. (© 1988 IEEE.)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/1c06ba6cfd0bda7cd6b7cbb54808df9a934e01427dd2f555412792bd04883268.jpg)


There are restrictions on the applicability of the spiral model. Specifi cally, in its present form, the model is intended exclusively for internal development of large-scale software [Boehm, 1988]. Consider an internal project, that is, one where the developers and client are members of the same organization. If risk analysis leads to the conclusion that the project should be terminated, then in-house software personnel can simply be reassigned to a different project. However, once a contract has been signed between a development organization and an external client, an attempt by either side to terminate that contract can lead to a breach-of-contract lawsuit. Therefore, in the case of contract software, all risk analysis must be performed by both client and developers before the contract is signed, not as in the spiral model. 

A second restriction on the spiral model relates to the size of the project. Specifi cally, the spiral model is applicable to only large-scale software. It makes no sense to perform risk analysis if the cost of performing the risk analysis is comparable to the cost of the project as a whole, or if performing the risk analysis would signifi cantly affect the profi t potential. Instead, the developers should fi rst decide how much is at risk and then how much risk analysis, if any, to perform. 

A major strength of the spiral model is that it is risk driven, but this can also be a weakness. Unless the software developers are skilled at pinpointing the possible risks and analyzing the risks accurately, there is a real danger that the team may believe that all is well at a time when the project, in fact, is headed for disaster. Only if the members of the development team are competent risk analysts should management decide to use the spiral model. 

Overall, however, the major weakness of the spiral model, as well as the waterfall model and the rapid-prototyping model, is that it assumes that software is developed in discrete phases. In reality, however, software development is iterative and incremental, as refl ected in the evolution-tree model (Section 2.2) or the iterative-and-incremental model (Section 2.5) 

## 2.10 Comparison of Life-Cycle Models

Nine different software life-cycle models have been examined with special attention paid to some of their strengths and weaknesses. The code-and-fi x model (Section 2.9.1) should be avoided. The waterfall model (Section 2.9.2) is a known quantity. Its strengths are understood, and so are its weaknesses. The rapid-prototyping model (Section 2.9.3) was developed as a reaction to a specifi c perceived weakness in the waterfall model, namely, that the delivered product may not be what the client really needs. However, there is still insuffi cient evidence that this approach is superior to the waterfall model in other respects. The open-source lifecycle model has been incredibly successful in a small number of cases when used to construct infrastructure software (Section 2.9.4). Agile processes (Section 2.9.5) are a set of controversial new approaches that, so far, appear to work, but for only small-scale software. The synchronize-and-stabilize model (Section 2.9.6) has been used with great success by Microsoft, but as yet there is no evidence of comparable success in other corporate cultures. Yet another alternative is to use the spiral model (Section 2.9.7), but only if the developers are adequately trained in risk analysis and risk resolution. The evolution-tree model (Section 2.2) and the iterative-and-incremental model (Section 2.5) are closest to the way that software is produced in the real world. An overall comparison appears in Figure 2.14 . 

Each software development organization should decide on a life-cycle model that is appropriate for that organization, its management, its employees, and its software process 

FIGURE 2.14 Comparison of life-cycle models described in this chapter, including the section in which each is defi ned. 

<table><tr><td>Life-Cycle Model</td><td>Strengths</td><td>Weaknesses</td></tr><tr><td>Evolution-tree model (Section 2.2)</td><td>Closely models real-world software productionEquivalent to the iterative-and-incremental model</td><td></td></tr><tr><td>Iterative-and-incremental life-cycle model (Section 2.5)</td><td>Closely models real-world software productionUnderlies the Unified Process</td><td></td></tr><tr><td>Code-and-fix life-cycle model (Section 2.9.1)</td><td>Fine for short programs that require no maintenance</td><td>Totally unsatisfactory for nontrivial programs</td></tr><tr><td>Waterfall life-cycle model (Section 2.9.2)</td><td>Disciplined approachDocument driven</td><td>Delivered product may not meet client&#x27;s needs</td></tr><tr><td>Rapid-prototyping life-cycle model (Section 2.9.3)</td><td>Ensures that the delivered product meets the client&#x27;s needs</td><td>Not yet proven beyond all doubt</td></tr><tr><td>Open-source life-cycle model (Section 2.9.4)</td><td>Has worked extremely well in a small number of instances</td><td>Limited applicability</td></tr><tr><td>Agile processes (Section 2.9.5)</td><td>Work well when the client&#x27;s requirements are vague</td><td>Usually does not work</td></tr><tr><td>Synchronize-and-stabilize life-cycle model (Section 2.9.6)</td><td>Future users&#x27; needs are metEnsures that components can be successfully integrated</td><td>Appear to work on only small-scale projectsHas not been widely used other than at Microsoft</td></tr><tr><td>Spiral life-cycle model (Section 2.9.7)</td><td>Risk driven</td><td>Can be used for only large-scale, in-house productsDevelopers have to be competent in risk analysis and risk resolution</td></tr></table>

and should vary the life-cycle model depending on the features of the specifi c product currently under development. Such a model incorporates appropriate aspects of the various life-cycle models, utilizing their strengths and minimizing their weaknesses. 

Chapter There are signifi cant differences between the way that software is developed in theory (Section 2.1) and the Review way it is developed in practice. The Winburg mini case study is used to introduce the evolution-tree model (Section 2.2). Lessons of this mini case study, especially that requirements change, are presented in Section 2.3. Change is discussed in greater detail in Section 2.4, where the moving-target problem is presented using the Teal Tractors mini case study. In Section 2.5, the importance of iteration and incrementation in real-world software engineering is stressed, and the iterative-and-incremental model is presented. Th Winburg mini case study is then re-examined in Section 2.6 to illustrate the equivalence of the evolutiontree model and the iterative-and-incremental model. In Section 2.7, the strengths of the iterative-and incremental model are presented, particularly that it enables us to resolve risks early. Management of the iterative-and-incremental model is discussed in Section 2.8. A number of different life-cycle models are now described, including the code-and-fi x life-cycle model (Section 2.9.1), waterfall life-cycle mode (Section 2.9.2), rapid-prototyping life-cycle model (Section 2.9.3), open-source life-cycle model (Section 2.9.4), agile processes (Section 2.9.5), synchronize-and-stabilize life-cycle model (Section 2.9.6), and spi ral life-cycle model (Section 2.9.7). In Section 2.10, these life-cycle models are compared and suggestions are made regarding the choice of a life-cycle model for a specifi c project 

The waterfall model was fi rst put forward in [Royce, 1970]. An analysis of the waterfall model is given in the fi rst chapter of [Royce, 1998]. 

The synchronize-and-stabilize model is outlined in [Cusumano and Selby, 1997] and described in detail in [Cusumano and Selby, 1995]. The spiral model is explained in [Boehm, 1988], and its application to the TRW Software Productivity System appears in [Boehm et al., 1984]. 

Extreme programming is described in [Beck, 2000]; refactoring is the subject of [Fowler et al., 1999]. The Manifesto for Agile Software Development may be found at [Beck et al., 2001]. Books have been published on a variety of agile methods, including [Cockburn, 2001] and [Schwaber, 2001]. Agile methods are advocated in [Highsmith and Cockburn, 2001], [Boehm, 2002], [DeMarco and Boehm, 2002], and [Boehm and Turner, 2003], whereas the case against agile methods is presented in [Stephens and Rosenberg, 2003]. Refactoring is surveyed in [Mens and Tourwe, 2004]. The use of XP in four mission-critical projects is described in [Drobka, Noftz, and Raghu, 2004]. Issues that can arise when introducing agile processes within an organization that currently is using traditional methodologies are discussed in [Nerur, Mahapatra, and Mangalaraj, 2005] and in [Boehm and Turner, 2005]. 

A number of papers on extreme programming appear in the May–June 2003 issue of IEEE Soft ware , including [Murru, Deias, and Mugheddu, 2003] and [Rasmusson, 2003], both of which describe successful projects developed using extreme programming. The June 2003 issue of IEEE Computer contains several articles on agile processes. The May–June 2005 issue of IEEE Software has four articles on agile processes, especially [Ceschi, Sillitti, Succi, and De Panfi lis, 2005] and [Karlström and Runeson, 2005]. The extent to which agile methods are used in the software industry is analyzed in [Hansson, Dittrich, Gustafsson, and Zarnak, 2006]. A survey of the critical success factors in agile software products is presented in [Chow and Cao, 2008]. Approaches to assist in the transition to agile methods are given in [Qumer and Henderson-Sellers, 2008]. Refactoring poses problems for software confi guration management tools; a solution is put forward in [Dig, Manzoor, Johnson, and Nguyen, 2008]. 

Agile testing of a large-scale software product is described in [Talby, Keren, Hazzan, and Dubinsky, 2006]. The effectiveness of test-driven development is discussed in [Erdogmus, Morisio, and Torchiano, 2005]. The May–June 2007 issue of IEEE Software has a variety of articles on test-driven development, including [Martin, 2007] 

Risk analysis is described in [Ropponen and Lyttinen, 2000], [Longstaff, Chittister, Pethia, and Haimes, 2000], and [Scott and Vessey, 2002]. Managing risks in offshore software development is presented in [Sakthivel, 2007] and in [Iacovou and Nakatsu, 2008]. Risk management when software is developed using COTS components is described in [Li et al., 2008]. 

A major iterative-and-incremental model is described in detail in [Jacobson, Booch, and Rumbaugh, 1999]. However, many other iterative-and-incremental models have been put forward over the past 30 years, as recounted in [Larman and Basili, 2003]. The use of an incremental model to build an airtraffi c control system is discussed in [Goth, 2000]. An iterative approach to re-engineering legacy systems is given in [Bianchi, Caivano, Marengo, and Visaggio, 2003]. A tool for supporting incremental software development while ensuring that the artifacts evolve consistently is described in [Reiss, 2006]. 

Many other life-cycle models have been put forward. For example, Rajlich and Bennett [2000] describe a maintenance-oriented life-cycle model. The July–August 2000 issue of IEEE Software has a variety of papers on software life-cycle models, including [Williams, Kessler, Cunningham, and Jeffries, 2000] which describes an experiment on pair programming, one component of agile methods. 

Rajlich [2006] goes further and suggests that many of the topics of this chapter have led us to a new paradigm for software engineering 

The proceedings of the International Software Process Workshops are a useful source of information on life-cycle models. [ISO/IEC 12207, 1995] is a widely accepted standard for software lifecycle processes. 

## Key Terms

agile process 60 incrementation 44 requirements workfl ow 44 analysis workfl ow 44 iteration 44 risk 50 architecture 49 iterative-and-incremental robustness 49 artifact 41 life-cycle model 44 spiral life-cycle model 63 baseline 41 life-cycle model 40 stabilize 62 code-and-fi x life-cycle Miller’s Law 44 stand-up meeting 60 model 52 mitigate risk 63 stepwise refi nement 44 core group 57 model 40 story 59 core workfl ow 44 moving-target problem 43 synchronize 62 design workfl ow 44 open-source software 56 synchronize-and-stabilize evolution-tree life-cycle pair programming 59 life-cycle model 62 model 40 peripheral group 57 task 59 extreme programming 59 proof-of-concept prototype 63 test-driven development 59 failure report 57 rapid prototype 55 test workfl ow 44 fault report 57 rapid-prototyping life-cycle timeboxing 60 feature creep 43 model 55 waterfall life-cycle model 41 freeze 62 refactoring 60 workfl ow 44 implementation workfl ow 44 regression fault 43 

## Problems

2.1 Represent the Winburg mini case study of Sections 2.2 and 2.3 using the waterfall model. Is this more or less effective than the evolution-tree model? Explain your answer. 

2.2 Assume that the programmer in the Winburg mini case study had used single-precision numbers from the beginning. Draw the resulting evolution tree. 

2.3 What is the connection between Miller’s Law and stepwise refi nement? 

2.4 Does stepwise refi nement correspond to iteration or incrementation? 

2.5 How are a workfl ow, an artifact, and a baseline related? 

2.6 What is the connection between the waterfall model and the iterative-and-incremental model? 

2.7 Suppose you have to build a product to determine the cube root of 9384.2034 to four decimal places. Once the product has been implemented and tested, it will be thrown away. Which life-cycle model would you use? Give reasons for your answer. 

2.8 You are a software engineering consultant and have been called in by the vice-president for fi nance of a corporation that manufactures tires and sells them via its large chain of retail outlets. She wants your organization to build a product that will monitor the company’s stock, starting with the purchasing of the raw materials and keeping track of the tires as they are manufactured, distributed to the individual stores, and sold to customers. What criteria would you use in selecting a life-cycle model for the project? 

2.9 List the risks involved in developing the software of Problem 2.8. How would you attempt to mitigate each risk? 

2.10 Your development of the stock control product for the tire company is so successful that your organization decides that it must be reimplemented as a package to be sold to a variety of different organizations that manufacture and sell products via their own retailers. The new product must therefore be portable and easily adapted to new hardware and/or operating systems. How would the criteria you use in selecting a life-cycle model for this project differ from those in your answer to Problem 2.8? 

2.11 Describe the sort of product that would be an ideal application for open-source software development. 



2.12 Now describe the type of situation where open-source software development is inappropriate. 





2.13 Describe the sort of product that would be an ideal application for an agile process. 





2.14 Now describe the type of situation where an agile process is inappropriate. 





2.15 Describe the sort of product that would be an ideal application for the spiral life-cycle model. 





2.16 Now describe the type of situation where the spiral life-cycle model is inappropriate. 





2.17 Describe a risk inherent in using the waterfall life-cycle model. 





2.18 Describe a risk inherent in using the code-and-fi x life-cycle model. 





2.19 Describe a risk inherent in using the open-source life-cycle model. 





2.20 Describe a risk inherent in using agile processes. 





2.21 Describe a risk inherent in using the spiral life-cycle model. 





2.22 (Term Project) Which software life-cycle model would you use for the Chocoholics Anonymous product described in Appendix A? Give reasons for your answer. 





2.23 (Readings in Software Engineering) Your instructor will distribute copies of [Rajlich, 2006]. Do you agree that software engineering has embarked on a new paradigm? Explain your answer. 



## References



[Arisholm, Gallis, Dybå, and Sjøberg, 2007] E. ARISHOLM, H. GALLIS, T. DYBÅ, AND D. I. K. SJØBERG, “Evaluating Pair Programming with Respect to System Complexity and Programmer Expertise,” IEEE Transactions on Software Engineering 33 (February 2007), pp. 65–86. 





[Beck, 2000] K. BECK, Extreme Programming Explained: Embrace Change, Addison-Wesley Longman, Reading, MA, 2000. 





[Beck et al., 2001] K. BECK, M. BEEDLE, A. COCKBURN, W. CUNNINGHAM, M. FOWLER, J. GRENNING, J. HIGHSMITH, A. HUNT, R. JEFFRIES, J. KERN, B. MARICK, R. C. MARTIN, S. MELLOR, K. SCHWABER, J. SUTHERLAND, D. THOMAS, AND A. VAN BENNEKUM, Manifesto for Agile Software Development , agilemanifesto.org, 2001. 





[Bianchi, Caivano, Marengo, and Visaggio, 2003] A. BIANCHI, D. CAIVANO, V. MARENGO, AND G. VISAGGIO, “Iterative Reengineering of Legacy Systems,” IEEE Transactions on Software Engineering 29 (March 2003), pp. 225–41. 





[Boehm, 1988] B. W. BOEHM, “A Spiral Model of Software Development and Enhancement,” IEEE Computer 21 (May 1988), pp. 61–72. 





[Boehm, 2002] B. W. BOEHM, “Get Ready for Agile Methods, with Care,” IEEE Computer 35 (January 2002), pp. 64–69. 





[Boehm and Turner, 2003] B. BOEHM AND R. TURNER, Balancing Agility and Discipline: A Guide for the Perplexed , Addison-Wesley Professional, Boston, MA, 2003. 





[Boehm and Turner, 2005] B. BOEHM AND R. TURNER, “Management Challenges to Implementing Agile Processes in Traditional Development Organizations,” IEEE Software 22 (September– October 2005), pp. 30–39. 





[Boehm et al., 1984] B. W. BOEHM, M. H. PENEDO, E. D. STUCKLE, R. D. WILLIAMS, AND A. B. PYSTER, “A Software Development Environment for Improving Productivity,” IEEE Computer 17 (June 1984), pp. 30–44. 





[Booch, 2000] G. BOOCH, “The Future of Software Engineering,” keynote address, International Conference on Software Engineering, Limerick, Ireland, May 2000. 





[Ceschi, Sillitti, Succi, and De Panfi lis, 2005] M. CESCHI, A. SILLITTI, G. SUCCI, AND S. DE PANFILIS, “Project Management in Plan-Based and Agile Companies,” IEEE Software 22 (May–June 2005), pp. 21–27. 





[Chow and Cao, 2008] T. CHOW AND D.-B. CAO, “A Survey Study of Critical Success Factors in Agile Software Projects,” Journal of Systems and Software 81 (June 2008), pp. 961–71. 





[Cockburn, 2001] A. COCKBURN, Agile Software Development , Addison-Wesley Professional, Reading, MA, 2001. 





[Cusumano and Selby, 1995] M. A. CUSUMANO AND R. W. SELBY, Microsoft Secrets: How the World’s Most Powerful Software Company Creates Technology, Shapes Markets, and Manages People , The Free Press/Simon and Schuster, New York, 1995. 





[Cusumano and Selby, 1997] M. A. CUSUMANO AND R. W. SELBY, “How Microsoft Builds Software,” Communications of the ACM 40 (June 1997), pp. 53–61. 





[DeMarco and Boehm, 2002] T. DEMARCO AND B. BOEHM, “The Agile Methods Fray,” IEEE Computer 35 (June 2002), pp. 90–92. 





[Dig, Manzoor, Johnson, and Nguyen, 2008] D. DIG, K. MANZOOR, R. E. JOHNSON, AND T. N. NGUYEN, “Effective Software Merging in the Presence of Object-Oriented Refactorings,” IEEE Transactions on Software Engineering 34 (May–June 2008), pp. 321–35. 





[Drobka, Noftz, and Raghu, 2004] J. DROBKA, D. NOFTZ, AND R. RAGHU, “Piloting XP on Four Mission-Critical Projects,” IEEE Software 21 (November–December 2004), pp. 70–75. 





[Dybå et al., 2007] T. DYBÅ, E. ARISHOLM, D. I. K. SJØBERG, J. E. HANNAY, AND F. SHULL, “Are Two Heads Better than One? On the Effectiveness of Pair Programming,” IEEE Software 24 (November–December 2007), pp. 12–15. 





[Erdogmus, Morisio, and Torchiano, 2005] H. ERDOGMUS, M. MORISIO, AND M. TORCHIANO, “On the Effectiveness of the Test-First Approach to Programming,” IEEE Transactions on Software Engineering 31 (March 2005), pp. 226–37. 





[Fowler et al., 1999] M. FOWLER wITH K. BECK, J. BRANT, W. OPDYKE, AND D. ROBERTS, Refactoring: Improving the Design of Existing Code , Addison-Wesley, Reading, MA, 1999. 





[Goth, 2000] G. GOTH, “New Air Traffi c Control Software Takes an Incremental Approach,” IEEE Software 17 (July–August 2000), pp. 108–11. 





[Hansson, Dittrich, Gustafsson, and Zarnak, 2006] C. HANSSON, Y. DITTRICH, B. GUSTAFSSON, AND S. ZARNAK, “How Agile Are Industrial Software Development Practices?” Journal of Systems and Software 79 (September 2006), pp. 1217–58. 





[Hayes, 2004] F. HAYES, “Chaos Is Back,” Computerworld , www.computerworld.com/ managementtopics/management/project/story/0,10801,97283,00.html, November 8, 2004. 





[Highsmith and Cockburn, 2001] J. HIGHSMITH AND A. COCKBURN, “Agile Software Development: The Business of Innovation,” IEEE Computer 34 (September 2001), pp. 120–22. 





[Iacovou and Nakatsu, 2008] C. L. IACOVOU AND R. NAKATSU, “A Risk Profi le of Offshore-Outsourced Development Projects,” Communications of the ACM 51 (June 2008) pp. 89–94. 





[ISO/IEC 12207, 1995] “ISO/IEC 12207:1995, Information Technology—Software Life-Cycle Processes,” International Organization for Standardization, International Electrotechnical Commission, Geneva, 1995. 





[Jacobson, Booch, and Rumbaugh, 1999] I. J , G. B ,  J. R , The Unifi ed Software Development Process , Addison-Wesley, Reading, MA, 1999. 





[Jalote, Palit, Kurien, and Peethamber, 2004] P. JALOTE, A. PALIT, P. KURIEN, AND V. T. PEETHAMBER, “ Timeboxing: A Process Model for Iterative Software Development,” Journal of Systems and Software 70 (February 2004), pp. 117–27. 





[Karlström and Runeson, 2005] D. KARLSTRÖM AND P. RUNESON, “Combining Agile Methods with Stage-Gate Project Management,” IEEE Software 22 (May–June 2005), pp. 43–49. 





[Larman and Basili, 2003] C. LARMAN AND V. R. BASILI, “Iterative and Incremental Development: A Brief History,” IEEE Computer 36 (June 2003), pp. 47–56. 





[Li and Alshayeb, 2002] W. LI AND M. ALSHAYEB, “An Empirical Study of XP Effort,” Proceedings of the 17th International Forum on COCOMO and Software Cost Modeling , Los Angeles, October 2002, IEEE. 





[Li et al., 2008] J. LI, O. P. N. SLYNGSTAD, M. TORCHIANO, M. MORISIO, AND C. BUNSE, “A State-ofthe-Practice Survey of Risk Management in Development with Off-the-Shelf Software Components,” IEEE Transactions on Software Engineering 34 (March–April 2008), pp. 271–86. 





[Longstaff, Chittister, Pethia, and Haimes, 2000] T. A. LONGSTAFF, C. CHITTISTER, R. PETHIA, AND Y. Y. HAIMES, “Are We Forgetting the Risks of Information Technology?” IEEE Computer 33 (December 2000), pp. 43–51. 





[Martin, 2007] R. C. MARTIN, “Professionalism and Test-Driven Development,” IEEE Software 24 (May–June 2007), pp. 32–36. 





[Mens and Tourwe, 2004] T. MENS AND T. TOURWE, “A Survey of Software Refactoring,” IEEE Transactions on Software Engineering 30 (February 2004), pp. 126–39. 





[Miller, 1956] G. A. MILLER, “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,” The Psychological Review 63 (March 1956), pp. 81–97; reprinted in: www.well.com/user/smalin/miller.html. 





[Murru, Deias, and Mugheddu, 2003] O. MURRU, R. DEIAS, AND G. MUGHEDDU, “Assessing XP at a European Internet Company,” IEEE Software 20 (May–June, 2003), pp. 37–43. 





[Nerur, Mahapatra, and Mangalaraj, 2005] S. NERUR, R. MAHAPATRA, AND G. MANGALARAJ, “Challenges of Migrating to Agile Methodologies,” Communications of the ACM 48 (May 2005), pp. 72–78. 





[Qumer and Henderson-Sellers, 2008] A. QUMER AND B. HENDERSON-SELLERS, “A Framework to Support the Evaluation, Adoption and Improvement of Agile Methods in Practice,” Journal of Systems and Software 81 (November 2008), pp. 1899–1919. 





[Rajlich, 2006] V. RAJLICH, “Changing the Paradigm of Software Engineering,” Communications of the ACM 49 (August 2006), pp. 67–70. 





[Rajlich and Bennett, 2000] V. RAJLICH AND K. H. BENNETT, “A Staged Model for the Software Life Cycle,” IEEE Computer 33 (July 2000), pp. 66–71. 





[Rasmusson, 2003] J. RASMUSSON, “Introducing XP into Greenfi eld Projects: Lessons Learned,” IEEE Software 20 (May–June, 2003), pp. 21–29. 





[Raymond, 2000] E. S. RAYMOND, The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary , O’Reilly & Associates, Sebastopol, CA, 2000; also available at www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/. 





[Reifer, Maurer, and Erdogmus, 2003] D. REIFER, F. MAURER, AND H. ERDOGMUS, “Scaling Agile Methods,” IEEE Software 20 (July–August 2004), pp. 12–14. 





[Reiss, 2006] S. P. REISS, “Incremental Maintenance of Software Artifacts,” IEEE Transactions on Software Engineering 32 (September 2006), pp. 682–97. 





[Ropponen and Lyttinen, 2000] J. ROPPONEN AND K. LYTTINEN, “Components of Software Development Risk: How to Address Them? A Project Manager Survey,” IEEE Transactions on Software Engineering 26 (February 2000), pp. 96–111. 





[Royce, 1970] W. W. ROYCE, “Managing the Development of Large Software Systems: Concepts and Techniques,” 1970 WESCON Technical Papers, Western Electronic Show and Convention , Los Angeles, August 1970, pp. A/1-1–A/1-9; reprinted in: Proceedings of the 11th International Conference on Software Engineering , Pittsburgh, May 1989, IEEE, pp. 328–38. 





[Royce, 1998] W. ROYCE, Software Project Management: A Unifi ed Framework , Addison-Wesley, Reading, MA, 1998. 





[Rubenstein, 2007] D. RUBENSTEIN, “Standish Group Report: There’s Less Development Chaos Today,” www.sdtimes.com/content/article.aspx?ArticleID=30247, March 1, 2007. 





[Sakthivel, 2007] S. SAKTHIVEL, “Managing Risk in Offshore Systems Development,” Communications of the ACM 50 (April 2007), pp. 69–75. 





[Schwaber, 2001] K. SCHWABER, Agile Software Development with Scrum , Prentice Hall, Upper Saddle River, NJ, 2001. 





[Scott and Vessey, 2002] J. E. SCOTT AND I. VESSEY, “Managing Risks in Enterprise Systems Implementations,” Communications of the ACM 45 (April 2002), pp. 74–81. 





[Softwaremag.com, 2004] “Standish: Project Success Rates Improved over 10 Years,” www. softwaremag.com/L.cfm?Doc=newsletter/2004-01-15/Standish, January 15, 2004. 





[Spivey, 1992] J. M. SPIVEY, The Z Notation: A Reference Manual , Prentice Hall, New York, 1992. 





[Standish, 2003] STANDISH GROUP INTERNATIONAL, “Introduction,” www.standishgroup.com/ chaos/introduction.pdf, 2003. 





[Stephens and Rosenberg, 2003] M. STEPHENS AND D. ROSENBERG, Extreme Programming Refactored: The Case against XP , Apress, Berkeley, CA, 2003. 





[Talby, Keren, Hazzan, and Dubinsky, 2006] D. TALBY, A. KEREN, O. HAZZAN, AND Y. DUBINSKY, “Agile Software Testing in a Large-Scale Project,” IEEE Software 23 (July–August 2006), pp. 30–37. 





[Tomer and Schach, 2000] A. TOMER AND S. R. SCHACH, “The Evolution Tree: A Maintenance-Oriented Software Development Model,” in: Proceedings of the Fourth European Conference on Software Maintenance and Reengineering (CSMR 2000) , Zürich, Switzerland, February/March 2000, ACM, pp. 209–14. 





[Williams, Kessler, Cunningham, and Jeffries, 2000] L. WILLIAMS, R. R. KESSLER, W. CUNNINGHAM, AND R. JEFFRIES, “Strengthening the Case for Pair Programming,” IEEE Software 17 (July–August 2000), pp. 19–25. 



# The Software Process

Learning Objectives 

After studying this chapter, you should be able to 

• Explain why two-dimensional life-cycle models are important. 

• Describe the fi ve core workfl ows of the Unifi ed Process. 

• List the artifacts tested in the test workfl ow. 

• Describe the four phases of the Unifi ed Process. 

• Explain the difference between the workfl ows and the phases of the Unifi ed Process. 

• Appreciate the importance of software process improvement. 

• Describe the capability maturity model (CMM). 

The software process is the way we produce software. It incorporates the methodology (Section 1.11) with its underlying software life-cycle model ( Chapter 2 ) and techniques, the tools we use (Sections 5.6 through 5.12), and most important of all, the individuals building the software. 

Different organizations have different software processes. For example, consider the issue of documentation. Some organizations consider the software they produce to be selfdocumenting; that is, the product can be understood simply by reading the source code. Other organizations, however, are documentation intensive. They punctiliously draw up specifi cations and check them methodically. Then they perform design activities painstakingly, check and recheck their designs before coding commences, and give extensive descriptions of each code artifact to the programmers. Test cases are preplanned, the result of each test run is logged, and the test data are meticulously fi led away. Once the product has been delivered and installed on the client’s computer, any suggested change must be proposed in writing, with detailed reasons for making the change. The proposed change can be made only with written authorization, and the modifi cation is not integrated into the product until the documentation has been updated and the changes to the documentation approved. 

Why does the software process vary so drastically from organization to organization? A major reason is lack of software engineering skills. All too many software professionals simply do not keep up to date. They continue to develop software Ye Olde Fashioned Way, because they know no other way. 

Another reason for differences in the software process is that many software managers are excellent managers but know precious little about software development or maintenance. Their lack of technical knowledge can result in the project slipping so badly behind schedule that there is no point in continuing. This frequently is the reason why many software projects are never completed. 

Yet another reason for differences among processes is management outlook. For example, one organization may decide that it is better to deliver a product on time, even if it is not adequately tested. Given the identical circumstances, a different organization might conclude that the risk of delivering that product without comprehensive testing would be far greater than taking the time to test the product thoroughly and consequently delivering it late. 

Intensity of testing is another measure by which organizations can be compared. Some organizations devote up to half their software budgets to testing software, whereas others feel that only the user can thoroughly test a product. Consequently, some companies devote minimal time and effort to testing the product but spend a considerable amount of time fi xing problems reported by users. 

Postdelivery maintenance is a major preoccupation of many software organizations. Software that is 10, 15, or even 20 years old is continually enhanced to meet changing needs; in addition, residual faults continue to appear, even after the software has been successfully maintained for many years. Almost all organizations move their software to newer hardware every 3 to 5 years; this, too, constitutes postdelivery maintenance. 

In contrast, yet other organizations essentially are concerned with research, leaving development—let alone maintenance—to others. This applies particularly to university computer science departments, where graduate students build software to prove that a particular design or technique is feasible. The commercial exploitation of the validated concept is left to other organizations. (See Just in Case You Wanted to Know Box 3.1 regarding the wide variation in the ways different organizations develop software.) 

However, regardless of the exact procedure, the software development process is structured around the fi ve workfl ows of Figure 2.4 : requirements, analysis (specifi - cation), design, implementation, and testing. In this chapter, these workfl ows are described, together with potential challenges that may arise during each workfl ow. Solutions to the challenges associated with the production of software usually are nontrivial, and the rest of this book is devoted to describing suitable techniques. In the fi rst part of this chapter, only the challenges are highlighted, but the reader is guided to the relevant sections or chapters for solutions. Accordingly, this part of the chapter not only is an overview of the software process, but a guide to much of the rest of the book. The chapter concludes with national and international initiatives to improve the software process. 

We now examine the Unifi ed Process. 

## 3.1 The Unifi ed Process

As stated at the beginning of this chapter, methodology is one component of a software process. The primary object-oriented methodology today is the Unifi ed Process . As explained in Just in Case You Wanted to Know Box 3.2, the Unifi ed “Process” is actually a methodology, but the name Unifi ed Methodology already had been used as the name of the fi rst version of the Unified Modeling Language (UML). The three precursors of the Unifi ed Process (OMT, Booch’s method, and Objectory) are no longer supported, and the other object-oriented methodologies have had little or no following. As a result, the Unifi ed Process is usually the primary choice today for object-oriented software production. Fortunately, as will be demonstrated in Part B of this book, the Unifi ed Process is an excellent object-oriented methodology in almost every way. 

The Unifi ed Process is not a specifi c series of steps that, if followed, will result in the construction of a software product. In fact, no such single “one size fi ts all” methodology could exist because of the wide variety of types of software products. For example, there are many different application domains, such as insurance, aerospace, and manufacturing. Also, a methodology for rushing a COTS package to market ahead of its competitors is different from one used to construct a high-security electronic funds transfer network. In addition, the skills of software professionals can vary widely. 

Instead, the Unifi ed Process should be viewed as an adaptable methodology. That is, it is modifi ed for the specifi c software product to be developed. As will be seen in Part B, some features of the Unifi ed Process are inapplicable to small- and even medium-scale software. However, much of the Unifi ed Process is used for software products of all sizes. The emphasis in this book is on this common subset of the Unifi ed Process, but aspects of the Unifi ed Process applicable to only large-scale software also are discussed, to ensure that the issues that need to be addressed when larger software products are constructed are thoroughly appreciated. 

## 3.2 Iteration and Incrementation within the Object-Oriented Paradigm

The object-oriented paradigm uses modeling throughout. A model is a set of UML diagrams that represent one or more aspects of the software product to be developed. (UML diagrams are introduced in Chapter 7 .) Recall that UML stands for Unifi ed Modeling Language. That is, UML is the tool that we use to represent (model) the target software product. A major reason for using a graphical representation like UML is best expressed by the old proverb, a picture is worth a thousand words. UML diagrams enable software professionals to communicate with one another more quickly and more accurately than if only verbal descriptions were used. 

The object-oriented paradigm is an iterative-and-incremental methodology. Each workfl ow consists of a number of steps, and to carry out that workfl ow, the steps of the workfl ow are repeatedly performed until the members of the development team are satisfi ed that they have an accurate UML model of the software product they want to develop. That is, even the most experienced software professionals iterate and reiterate until they are fi nally satisfi ed that the UML diagrams are correct. The implication is that software engineers, no 

Until recently, the most popular object-oriented software development methodologies were object modeling technique (OMT) [Rumbaugh et al., 1991] and Grady Booch’s method [Booch, 1994]. OMT was developed by Jim Rumbaugh and his team at the General Electric Research and Development Center in Schenectady, New York, whereas Grady Booch developed his method at Rational, Inc., in Santa Clara, California. All object-oriented software development methodologies essentially are equivalent, so the differences between OMT and Booch’s method are small. Nevertheless, there always was a friendly rivalry between the supporters of the two camps. 

This changed in October 1994, when Rumbaugh joined Booch at Rational. The two methodologists immediately began to work together to develop a methodology that would combine OMT and Booch’s method. When a preliminary version of their work was published, it was pointed out that they had not developed a methodology but merely a notation for representing an object-oriented software product. The name Unifi ed Methodology was quickly changed to Unifi ed Modeling Language (UML). In 1995, they were joined at Rational by Ivar Jacobson, author of the Objectory methodology. Booch, Jacobson, and Rumbaugh, affectionately called the “Three Amigos” (after the 1986 John Landis movie Three Amigos! with Chevy Chase and Steve Martin), then worked together. Version 1.0 of UML, published in 1997, took the software engineering world by storm. Until then, there had been no universally accepted notation for the development of a software product. Almost overnight UML was used all over the world. The Object Management Group (OMG), an association of the world’s leading companies in object technology, took the responsibility for organizing an international standard for UML, so that every software professional would use the same version of UML, thereby promoting communication among individuals within an organization as well as companies worldwide. UML [Booch, Rumbaugh, and Jacobson, 1999] is today the unquestioned international standard notation for representing object-oriented software products. 

An orchestral score shows which musical instruments are needed to play the piece, the notes each instrument is to play and when it is to play them, as well as a whole host of technical information such as the key signature, tempo, and loudness. Could this information be given in English, rather than a diagram? Probably, but it would be impossible to play music from such a description. For example, there is no way a pianist and a violinist could perform a piece described as follows: “The music is in march time, in the key of B minor. The fi rst bar begins with the A above middle C on the violin (a quarter note). While this note is being played, the pianist plays a chord consisting of seven notes. The right hand plays the following four notes: E sharp above middle C . . .” 

It is clear that, in some fi elds, a textual description simply cannot replace a diagram. Music is one such fi eld; software development is another. And for software development, the best modeling language available today is UML. 

Taking the software engineering world by storm with UML was not enough for the Three Amigos. Their next endeavor was to publish a complete software development methodology that unifi ed their three separate methodologies. This unifi ed methodology was fi rst called the Rational Unifi ed Process (RUP); Rational is in the name of the methodology not because the Three Amigos considered all other approaches to be irrational, but because at that time all three were senior managers at Rational, Inc. (Rational was bought by IBM in 2003). In their book on RUP [Jacobson, Booch, and Rumbaugh, 1999], the name Unifi ed Software Development Process (USDP) was used. The term Unifi ed Process is generally used today, for brevity. 

matter how outstanding they may be, almost never get the various work products right the fi rst time. How can this be? 

The nature of software products is such that virtually everything has to be developed iteratively and incrementally. After all, software engineers are human, and therefore subject to Miller’s Law (Section 2.5). That is, it is impossible to consider everything at the same time, so just seven or so chunks (units of information) are handled initially. Then, when the next set of chunks is considered, more knowledge about the target software product is gained, and the UML diagrams are modifi ed in the light of this additional information. The process continues in this way until eventually the software engineers are satisfi ed that all the models for a given workfl ow are correct. In other words, initially the best possible UML diagrams are drawn in the light of the knowledge available at the beginning of the workfl ow. Then, as more knowledge about the real-world system being modeled is gained, the diagrams are made more accurate (iteration) and extended (incrementation). Accordingly, no matter how experienced and skillful a software engineer may be, he or she repeatedly iterates and increments until satisfi ed that the UML diagrams are an accurate representation of the software product to be developed. 

Ideally, by the end of this book, the reader would have the software engineering skills necessary for constructing the large, complex software products for which the Unifi ed Process was developed. Unfortunately, there are three reasons why this is not feasible. 

1. Just as it is not possible to become an expert on calculus or a foreign language in one single course, gaining profi ciency in the Unifi ed Process requires extensive study and, more important, unending practice in object-oriented software engineering 

2. The Unifi ed Process was created primarily for use in developing large, complex software products. To be able to handle the many intricacies of such software products, the Unifi ed Process is itself large. It would be hard to cover every aspect of the Unifi ed Process in a textbook of this size. 

3. To teach the Unifi ed Process, it is necessary to present a case study that illustrates the features of the Unifi ed Process. To illustrate the features that apply to large software products, such a case study would have to be large. For example, just the specifi cations typically would take over 1000 pages. 

For these three reasons, this book presents most, but not all, of the Unifi ed Process. 

The fi ve core workfl ows of the Unifi ed Process (requirements workfl ow, analysis workfl ow, design workfl ow, implementation workfl ow, and test workfl ow) and their challenges are now discussed. 

## 3.3 The Requirements Workfl ow

Software development is expensive. The development process usually begins when the client approaches a development organization with regard to a software product that, in the opinion of the client, is either essential to the profi tability of his or her enterprise or somehow can be justifi ed economically. The aim of the requirements workfl ow is for the development organization to determine the client’s needs. The fi rst task of the development team is to acquire a basic understanding of the application domain ( domain for short), that is, the specifi c environment in which the target software product is to operate. The domain could be banking, automobile manufacturing, or nuclear physics. 

At any stage of the process, if the client stops believing that the software will be cost effective, development will terminate immediately. Throughout this chapter the assumption is made that the client feels that the cost is justifi ed. Therefore, a vital aspect of software development is the business case , a document that demonstrates the cost-effectiveness of the target product. (In fact, the “cost” is not always purely fi nancial. For example, military software often is built for strategic or tactical reasons. Here, the cost of the software is the potential damage that could be suffered in the absence of the weapon being developed.) 

At an initial meeting between client and developers, the client outlines the product as he or she conceptualizes it. From the viewpoint of the developers, the client’s description of the desired product may be vague, unreasonable, contradictory, or simply impossible to achieve. The task of the developers at this stage is to determine exactly what the client needs and to fi nd out from the client what constraints exist. 

• A major constraint is almost always the deadline . For example, the client may stipulate that the fi nished product must be completed within 14 months. In almost every application domain, it is now commonplace for a target software product to be mission critical. That is, the client needs the software product for core activities of his or her organization, and any delay in delivering the target product is detrimental to the organization. 

• A variety of other constraints often are present, such as reliability (for example, the product must be operational 99 percent of the time, or the mean time between failures must be at least 4 months). Another common constraint is the size of the executable load image (for example, it has to run on the client’s personal computer or on the hardware inside the satellite). 

• The cost is almost invariably an important constraint. However, the client rarely tells the developers how much money is available to build the product. Instead, a common practice is that, once the specifi cations have been fi nalized, the client asks the developers to name their price for completing the project. Clients follow this bidding procedure in the hope that the amount of the developers’ bid is lower than the amount the client has budgeted for the project. 

The preliminary investigation of the client’s needs sometimes is called concept exploration . In subsequent meetings between members of the development team and the client team, the functionality of the proposed product is successively refi ned and analyzed for technical feasibility and fi nancial justifi cation. 

Up to now, everything seems to be straightforward. Unfortunately, the requirements workfl ow often is performed inadequately. When the product fi nally is delivered to the user, perhaps a year or two after the specifi cations have been signed off on by the client, the client may say to the developers, “I know that this is what I asked for, but it isn’t really what I wanted.” What the client asked for and, therefore, what the developers thought the client wanted, was not what the client actually needed . There can be a number of reasons for this predicament. First, the client may not truly understand what is going on in his or her own organization. For example, it is no use asking the software developers for a faster operating system if the cause of the current slow turnaround is a badly designed database. Or, if the client operates an unprofi table chain of retail stores, the client may ask for a fi nancial management information system that refl ects such items as sales, salaries, accounts payable, and accounts receivable. Such a product will be of little use if the real reason for the losses is shrinkage (theft by employees and shoplifting). If that is the case, then a stock control system rather than a fi nancial management information system is required. 

But the major reason why the client frequently asks for the wrong product is that software is complex. If it is diffi cult for a software professional to visualize a piece of software and its functionality, the problem is far worse for a client who is barely computer literate. As will be shown in Chapter 11 , the Unifi ed Process can help in this regard; the many UML diagrams of the Unifi ed Process assist the client in gaining the necessary detailed understanding of what needs to be developed. 

## 3.4 The Analysis Workfl ow

The aim of the analysis workfl ow is to analyze and refi ne the requirements to achieve the detailed understanding of the requirements essential for developing a software product correctly and maintaining it easily. At fi rst sight, however, there is no need for an analysis workfl ow. Instead, an apparently simpler way to proceed would be to develop a software product by continuing with further iterations of the requirements workfl ow until the necessary understanding of the target software product has been obtained. 

The key point is that the output of the requirements workfl ow must be totally comprehended by the client. In other words, the artifacts of the requirements workfl ow must be expressed in the language of the client, that is, in a natural (human) language such as English, Armenian, or Zulu. But all natural languages, without exception, are somewhat imprecise and lend themselves to misunderstanding. For example, consider the following paragraph: 

A part record and a plant record are read from the database. If it contains the letter A directly followed by the letter Q, then calculate the cost of transporting that part to that plant. 

At fi rst sight, this requirement seems perfectly clear. But to what does it (the second word in the second sentence) refer: the part record, the plant record, or the database? 

Ambiguities of this kind cannot arise if the requirements are expressed (say) in a mathematical notation. However, if a mathematical notation is used for the requirements, then the client is unlikely to understand much of the requirements. As a result, there may well be miscommunication between client and developers regarding the requirements, and consequently, the software product developed to satisfy those requirements may not be what the client needs. 

The solution is to have two separate workfl ows. The requirements workfl ow is couched in the language of the client; the analysis workfl ow, in a more precise language that ensures that the design and implementation workfl ows are correctly carried out. In addition, more details are added during the analysis workfl ow, details not relevant to the client’s understanding of the target software product but essential for the software professionals who will develop the software product. For example, the initial state of a statechart (Section 13.6) would surely not concern the client in any way but has to be included in the specifi cations if the developers are to build the target product correctly. 

The specifi cations of the product constitute a contract. The software developers are deemed to have completed the contract when they deliver a product that satisfi es the acceptance criteria of the specifi cations. For this reason, the specifi cations should not include imprecise terms like suitable, convenient, ample , or enough , or similar terms that sound exact but in practice are equally imprecise, such as optimal or 98 percent complete . Whereas contract software development can lead to a lawsuit, there is no chance of the specifi cations forming the basis for legal action when the client and developers are from the same organization. Nevertheless, even in the case of internal software development, the specifi cations always should be written as if they will be used as evidence in a trial 

More important, the specifi cations are essential for both testing and maintenance. Unless the specifi cations are precise, there is no way to determine whether they are correct, let alone whether the implementation satisfi es the specifi cations. And it is hard to change the specifi cations unless some document states exactly what the specifi cations currently are. 

When the Unifi ed Process is used, there is no specifi cation document in the usual sense of the term. Instead, a set of UML artifacts are shown to the client, as described in Chapter 13 . These UML diagrams and their descriptions can obviate many (but by no means all) of the problems of the classical specifi cation document. 

One mistake that can be made by a classical analysis team is that the specifi cations are ambiguous; as previously explained, ambiguity is intrinsic to natural languages. Incompleteness is another problem in the specifi cations; that is, some relevant fact or requirement may be omitted. For instance, the specifi cation document may not state what actions are to be taken if the input data contain errors. Moreover, the specifi cation document may contain contradictions . For example, one place in the specifi cation document for a product that controls a fermentation process states that if the pressure exceeds 35 psi, then valve M17 immediately must be shut. However, another place states that, if the pressure exceeds 35 psi, then the operator immediately must be alerted; only if the operator takes no remedial action within 30 seconds should valve M17 be shut automatically. Software development cannot proceed until such problems in the specifi cations have been corrected. As pointed out in the previous paragraph, many of these problems can be reduced by using the Unifi ed Process. This is because UML diagrams together with descriptions of those diagrams are less likely to contain ambiguity, incompleteness, and contradictions. 

Once the client has approved the specifi cations, detailed planning and estimating commences. No client authorizes a software project without knowing in advance how long the project will take and how much it will cost. From the viewpoint of the developers, these two items are just as important. If the developers underestimate the cost of a project, then the client pays the agreed-upon fee, which may be signifi cantly less than the developers’ actual cost. Conversely, if the developers overestimate what the project costs, then the client may turn down the project or have the job done by other developers whose estimate is more reasonable. Similar issues arise with regard to duration estimates. If the developers underestimate how long completing a project will take, then the resulting late delivery of the product, at best, results in a loss of confi dence by the client. At worst, lateness penalty clauses in the contract are invoked, causing the developers to suffer fi nancially. Again, if the developers overestimate how long it will take for the product to be delivered, the client may well award the job to developers who promise faster delivery. 

For the developers, merely estimating the duration and total cost is not enough. The developers need to assign the appropriate personnel to the various workfl ows of the development process. For example, the implementation team cannot start until the relevant design artifacts have been approved by the software quality assurance (SQA) group, and the design team is not needed until the analysis team has completed its task. In other words, the developers have to plan ahead. A software project management plan (SPMP) must be drawn up that refl ects the separate workfl ows of the development process and shows which members of the development organization are involved in each task, as well as the deadlines for completing each task. 

The earliest that such a detailed plan can be drawn up is when the specifi cations have been fi nalized. Before that time, the project is too amorphous for complete planning. Some aspects of the project certainly must be planned right from the start, but until the developers know exactly what is to be built, they cannot specify all aspects of the plan for building it. 

Therefore, once the specifi cations have been approved by the client, preparation of the software project management plan commences. Major components of the plan are the deliverables (what the client is going to get), the milestones (when the client gets them), and the budget (how much it is going to cost). 

The plan describes the software process in fullest detail. It includes aspects such as the life-cycle model to be used, the organizational structure of the development organization, project responsibilities, managerial objectives and priorities, the techniques and CASE tools to be used, and detailed schedules, budgets, and resource allocations. Underlying the entire plan are the duration and cost estimates; techniques for obtaining such estimates are described in Section 9.2. 

The analysis workfl ow is described in Chapters 12 and 13 : classical analysis techniques are described in Chapter 12 , and object-oriented analysis is the subject of Chapter 13 . A major artifact of the analysis workfl ow is the software project management plan. An explanation of how to draw up the SPMP is given in Sections 9.3 though 9.5. 

Now the design workfl ow is examined. 

## 3.5 The Design Workfl ow

The specifi cations of a product spell out what the product is to do; the design shows how the product is to do it. More precisely, the aim of the design workfl ow is to refi ne the artifacts of the analysis workfl ow until the material is in a form that can be implemented by the programmers. 

As explained in Section 1.3, during the classical design phase, the design team determines the internal structure of the product. The designers decompose the product into modules , independent pieces of code with well-defi ned interfaces to the rest of the product. The interface of each module (that is, the arguments passed to the module and the arguments returned by the module) must be specifi ed in detail. For example, a module might measure the water level in a nuclear reactor and cause an alarm to sound if the level is too low. A module in an avionics product might take as input two or more sets of coordinates of an incoming enemy missile, compute its trajectory, and invoke another module to advise the pilot as to possible evasive action. Once the team has completed the decomposition into modules (the architectural design ), the detailed design is performed. For each module, algorithms are selected and data structures chosen. 

Turning now to the object-oriented paradigm, the basis of that paradigm is the class , a specific type of module. Classes are extracted during the analysis workfl ow and designed during the design workfl ow. Consequently, the object-oriented counterpart of architectural design is performed as a part of the object-oriented analysis workfl ow, and the objectoriented counterpart of detailed design is part of the object-oriented design workfl ow. 

The design team must keep a meticulous record of the design decisions that are made. This information is essential for two reasons. 

1. While the product is being designed, a dead end will be reached at times and the design team must backtrack and redesign certain pieces. Having a written record of why specifi c decisions were made assists the team when this occurs and helps it get back on track. 

2. Ideally, the design of the product should be open-ended, meaning future enhancements (postdelivery maintenance) can be done by adding new classes or replacing existing classes without affecting the design as a whole. Of course, in practice, this ideal is diffi cult to achieve. Deadline constraints in the real world are such that designers struggle against the clock to complete a design that satisfi es the original specifi cations, without worrying about any later enhancements. If future enhancements (to be added after the product is delivered to the client) are included in the specifi cations, then these must be allowed for in the design, but this situation is extremely rare. In general, the specifi cations, and hence the design, deal with only present requirements. In addition, while the product is still being designed, there is no way to determine all possible future enhancements. Finally, if the design has to take all future possibilities into account, at best it will be unwieldy; at worst, it will be so complicated that implementation is impossible. So the designers have to compromise, putting together a design that can be extended in many reasonable ways without the need for total redesign. But, in a product that undergoes major enhancement, the time will come when the design simply cannot handle further changes. When this stage is reached, the product must be redesigned as a whole. The task of the redesign team is considerably easier if the team members are provided a record of the reasons for all the original design decisions. 

## 3.6 The Implementation Workfl ow

The aim of the implementation workfl ow is to implement the target software product in the chosen implementation language(s). A small software product is sometimes implemented by the designer. In contrast, a large software product is partitioned into smaller subsystems, which are then implemented in parallel by coding teams. The subsystems, in turn, consist of components or code artifacts implemented by an individual programmer. 

Usually, the only documentation given a programmer is the relevant design artifact. For example, in the case of the classical paradigm, the programmer is given the detailed design of the module he or she is to implement. The detailed design usually provides enough information for the programmer to implement the code artifact without too much diffi culty. If there are any problems, they can quickly be cleared up by consulting the responsible designer. However, there is no way for the individual programmer to know if the architectural design is correct. Only when integration of individual code artifacts commences do the shortcomings of the design as a whole start coming to light. 

Suppose that a number of code artifacts have been implemented and integrated and the parts of the product integrated so far appear to be working correctly. Suppose further that a programmer has correctly implemented artifact a45, but when this artifact is integrated with the other existing artifacts, the product fails. The cause of the failure lies not in artifact a45 itself, but rather in the way that artifact a45 interacts with the rest of the product, as specifi ed in the architectural design. Nevertheless, in this type of situation the programmer who just coded artifact a45 tends to be blamed for the failure. This is unfortunate, because the programmer has simply followed the instructions provided by the designer and implemented the artifact exactly as described in the detailed design for that artifact. The members of the programming team are rarely shown the “big picture,” that is, the architectural design, let alone asked to comment on it. Although it is grossly unfair to expect an individual programmer to be aware of the implications of a specifi c artifact for the product as a whole, this unfortunately happens in practice all too often. This is yet another reason why it is so important for the design to be correct in every respect. 

The correctness of the design (as well as the other artifacts) is checked as part of the test workfl ow. 

## 3.7 The Test Workfl ow

As shown in Figure 2.4 , in the Unifi ed Process, testing is carried out in parallel with the other workfl ows, starting from the beginning. There are two major aspects to testing 

1. Every developer and maintainer is personally responsible for ensuring that his or her work is correct. Therefore, a software professional has to test and retest each artifact he or she develops or maintains. 

2. Once the software professional is convinced that an artifact is correct, it is handed over to the software quality assurance group for independent testing, as described in Chapter 6. 

The nature of the test workfl ow changes depending on the artifacts being tested. However, a feature important to all artifacts is traceability. 

## 3.7.1 Requirements Artifacts

If the requirements artifacts are to be testable over the life cycle of the software product, then one property they must have is traceability . For example, it must be possible to trace every item in the analysis artifacts back to a requirements artifact and similarly for the design artifacts and the implementation artifacts. If the requirements have been presented methodically, properly numbered, cross-referenced, and indexed, then the developers should have little diffi culty tracing through the subsequent artifacts and ensuring that they are indeed a true refl ection of the client’s requirements. When the work of the members of the requirements team is subsequently checked by the SQA group, traceability simplifi es their task, too. 

## 3.7.2 Analysis Artifacts

As pointed out in Chapter 1 , a major source of faults in delivered software is faults in the specifi cations that are not detected until the software has been installed on the client’s computer and used by the client’s organization for its intended purpose. Both the analysis team and the SQA group must therefore check the analysis artifacts assiduously. In addition, they must ensure that the specifi cations are feasible, for example, that a specifi c hardware component is fast enough or that the client’s current online disk storage capacity is adequate to handle the new product. An excellent way of checking the analysis artifacts is by means of a review. Representatives of the analysis team and of the client are present. 

The meeting usually is chaired by a member of the SQA group. The aim of the review is to determine whether the analysis artifacts are correct. The reviewers go through the analysis artifacts, checking to see if there are any faults. Walkthroughs and inspections are two types of reviews, and they are described in Section 6.2. 

We turn now to the checking of the detailed planning and estimating that takes place once the client has signed off on the specifi cations. Whereas it is essential that every aspect of the SPMP be meticulously checked by the development team and then by the SQA group, particular attention must be paid to the plan’s duration and cost estimates. One way to do this is for management to obtain two (or more) independent estimates of both duration and cost when detailed planning starts, and then reconcile any signifi cant differences. With regard to the SPMP document, an excellent way to check it is by a review similar to the review of the analysis artifacts. If the duration and cost estimates are satisfactory, the client will give permission for the project to proceed. 

## 3.7.3 Design Artifacts

As mentioned in Section 3.7.1, a critical aspect of testability is traceability. In the case of the design, this means that every part of the design can be linked to an analysis artifact. A suitably cross-referenced design gives the developers and the SQA group a powerful tool for checking whether the design agrees with the specifi cations and whether every part of the specifi cations is refl ected in some part of the design. 

Design reviews are similar to the reviews that the specifi cations undergo. However, in view of the technical nature of most designs, the client usually is not present. Members of the design team and the SQA group work through the design as a whole as well as through each separate design artifact, ensuring that the design is correct. The types of faults to look for include logic faults, interface faults, lack of exception handling (processing of error conditions), and most important, nonconformance to the specifi cations. In addition, the review team always should be aware of the possibility that some analysis faults were not detected during the previous workfl ow. A detailed description of the review process is given in Section 6.2. 

## 3.7.4 Implementation Artifacts

Each component should be tested while it is being implemented (desk checking); and after it has been implemented, it is run against test cases. This informal testing is done by the programmer. Thereafter, the quality assurance group tests the component methodically; this is termed unit testing . A variety of unit-testing techniques are described in Chapter 15. 

In addition to running test cases, a code review is a powerful, successful technique for detecting programming faults. Here, the programmer guides the members of the review team through the listing of the component. The review team must include an SQA representative. The procedure is similar to reviews of specifi cations and designs described previously. As in all the other workfl ows, a record of the activities of the SQA group are kept as part of the test workfl ow. 

Once a component has been coded, it must be combined with the other coded components so that the SQA group can determine whether the (partial) product as a whole functions correctly. The way in which the components are integrated (all at once or one at a time) and the specifi c order (from top to bottom or from bottom to top in the component interconnection diagram or class hierarchy) can have a critical infl uence on the quality of the resulting product. For example, suppose the product is integrated bottom up. A major design fault, if present, will show up late, necessitating an expensive reimplementation. Conversely, if the components are integrated top down, then the lower-level components usually do not receive as thorough a testing as would be the case if the product were integrated bottom up. These and other problems are discussed in detail in Chapter 15 . A detailed explanation is given there as to why coding and integration must be performed in parallel. 

The purpose of this integration testing is to check that the components combine correctly to achieve a product that satisfi es its specifi cations. During integration testing, particular care must be paid to testing the component interfaces. It is important that the number, order, and types of formal arguments match the number, order, and types of actual arguments. This strong type checking [van Wijngaarden et al., 1975] is best performed by the compiler and linker. However, many languages are not strongly typed. When such a language is used, members of the SQA group must check the interfaces. 

When the integration testing has been completed (that is, when all the components have been coded and integrated), the SQA group performs product testing . The functionality of the product as a whole is checked against the specifi cations. In particular, the constraints listed in the specifi cations must be tested. A typical example is whether the response time has been met. Because the aim of product testing is to determine whether the specifi cations have been correctly implemented, many of the test cases can be drawn up once the specifi - cations are complete. 

Not only must the correctness of the product be tested but its robustness must also be tested. That is, intentionally erroneous input data are submitted to determine whether the product will crash or whether its error-handling capabilities are adequate for dealing with bad data. If the product is to be run together with the client’s currently installed software, then tests also must be performed to check that the new product will have no adverse effect on the client’s existing computer operations. Finally, a check must be made as to whether the source code and all other types of documentation are complete and internally consistent. Product testing is discussed in Section 15.21. On the basis of the results of the product test, a senior manager in the development organization decides whether the product is ready to be released to the client. 

The fi nal step in testing the implementation artifacts is acceptance testing . The software is delivered to the client, who tests it on the actual hardware, using actual data as opposed to test data. No matter how methodical the development team or the SQA group might be, there is a signifi cant difference between test cases, which by their very nature are artifi cial, and actual data. A software product cannot be considered to satisfy its specifi cations until the product has passed its acceptance test. More details about acceptance testing are given in Section 15.22. 

In the case of COTS software (Section 1.11), as soon as product testing is complete, versions of the complete product are supplied to selected possible future clients for testing on site. The fi rst such version is termed the alpha release . The corrected alpha release is called the beta release ; in general, the beta release is intended to be close to the fi nal version. (The terms alpha release and beta release are generally applied to all types of software products, not just COTS.) 

Faults in COTS software usually result in poor sales of the product and huge losses for the development company. So that as many faults as possible come to light as early as possible, developers of COTS software frequently give alpha or beta releases to selected companies, in the expectation that on-site tests will uncover any latent faults. In return, the alpha and beta sites frequently are promised free copies of the delivered version of the software. Risks are involved for a company participating in alpha or beta testing. In particular, alpha releases can be fault laden, resulting in frustration, wasted time, and possible damage to databases. However, the company gets a head start in using the new COTS software, which can give it an advantage over its competitors. A problem occurs sometimes when software organizations use alpha testing by potential clients in place of thorough product testing by the SQA group. Although alpha testing at a number of different sites usually brings to light a large variety of faults, there is no substitute for the methodical testing that the SQA group can provide. 

## 3.8 Postdelivery Maintenance

Postdelivery maintenance is not an activity grudgingly carried out after the product has been delivered and installed on the client’s computer. On the contrary, it is an integral part of the software process that must be planned for from the beginning. As explained in Section 3.5, the design, as far as is feasible, should take future enhancements into account. Coding must be performed with future maintenance kept in mind. After all, as pointed out in Section 1.3, more money is spent on postdelivery maintenance than on all other software activities combined. It therefore is a vital aspect of software production. Postdelivery maintenance must never be treated as an afterthought. Instead, the entire software development effort must be carried out in such a way as to minimize the impact of the inevitable future postdelivery maintenance. 

A common problem with postdelivery maintenance is documentation or, rather, lack of it. In the course of developing software against a time deadline, the original analysis and design artifacts frequently are not updated and, consequently, are almost useless to the maintenance team. Other documentation such as the database manual or the operating manual may never be written, because management decided that delivering the product to the client on time was more important than developing the documentation in parallel with the software. In many instances, the source code is the only documentation available to the maintainer. The high rate of personnel turnover in the software industry exacerbates the maintenance situation, in that none of the original developers may be working for the organization at the time when maintenance is performed. Postdelivery maintenance frequently is the most challenging aspect of software production for these reasons and the additional reasons given in Chapter 16. 

Turning now to testing, there are two aspects to testing changes made to a product when postdelivery maintenance is performed. The fi rst is checking that the required changes have been implemented correctly. The second aspect is ensuring that, in the course of making the required changes to the product, no other inadvertent changes were made. Therefore, once the programmer has determined that the desired changes have been implemented, the product must be tested against previous test cases to make certain that the functionality of the rest of the product has not been compromised. This procedure is called regression testing . To assist in regression testing, it is necessary that all previous test cases be retained, together with the results of running those test cases. Testing during postdelivery maintenance is discussed in greater detail in Chapter 16. 

A major aspect of postdelivery maintenance is a record of all the changes made, together with the reason for each change. When software is changed, it has to be regression tested. Therefore, the regression test cases are a central form of documentation. 

## 3.9 Retirement

The fi nal stage in the software life cycle is retirement . After many years of service, a stage is reached when further postdelivery maintenance no longer is cost effective. 

• Sometimes the proposed changes are so drastic that the design as a whole would have to be changed. In such a case, it is less expensive to redesign and recode the entire product. 

• So many changes may have been made to the original design that interdependencies inadvertently have been built into the product, and even a small change to one minor component might have a drastic effect on the functionality of the product as a whole. 

• The documentation may not have been adequately maintained, thereby increasing the risk of a regression fault to the extent that it would be safer to recode than maintain 

• The hardware (and operating system) on which the product runs is to be replaced; it may be more economical to reimplement from scratch than to modify. 

In each of these instances the current version is replaced by a new version, and the software process continues. 

True retirement, on the other hand, is a somewhat rare event that occurs when a product has outgrown its usefulness. The client organization no longer requires the functionality provided by the product, and it fi nally is removed from the computer. 

## 3.10 The Phases of the Unifi ed Process

Figure 3.1 differs from Figure 2.4 in that the labels of the increments have been changed. Instead of Increment A, Increment B, and so on, the four increments are now labeled Inception phase, Elaboration phase, Construction phase, and Transition phase. In other words, the phases of the Unifi ed Process correspond to increments. 

FIGURE 3.1 The core workfl ows and the phases of the Unifi ed Process. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/14d7f3a1aea3f3f838b460d3cd122d6fcc7eb2f197581ed3ad4f7aa1c1254a2b.jpg)


Although in theory the development of a software product could be performed in any number of increments, development in practice often seems to consist of four increments. The increments or phases are described in Sections 3.10.1 through 3.10.4, together with the deliverables of each phase, that is, the artifacts that should be completed by the end of that phase. 

Every step performed in the Unifi ed Process falls into one of fi ve core workfl ows and also into one of four phases, the inception phase, elaboration phase, construction phase, and transition phase. The various steps of these four phases are already described in Sections 3.3 through 3.7. For example, building a business case is part of the requirements workfl ow (Section 3.3). It is also part of the inception phase. Nevertheless, each step has to be considered twice, as will be explained. 

Consider the requirements workfl ow. To determine the client’s needs, one of the steps is, as just stated, to build a business case. In other words, within the framework of the requirements workfl ow, building a business case is presented within a technical context. In Section 3.10.1, a description is presented of building a business case within the framework of the inception phase, the phase in which management decides whether or not to develop the proposed software product. That is, building a business case shortly is presented within an economic context (Section 1.2). 

At the same time, there is no point in presenting each step twice, both times at the same level of detail. Accordingly, the inception phase is described in depth to highlight the difference between the technical context of the workfl ows and the economic context of the phases, but the other three phases are simply outlined. 

## 3.10.1 The Inception Phase

The aim of the inception phase (first increment) is to determine whether it is worthwhile to develop the target software product. In other words, the primary aim of this phase is to determine whether the proposed software product is economically viable. 

Two steps of the requirements workfl ow are to understand the domain and build a business model. Clearly, there is no way the developers can give any kind of opinion regarding a possible future software product unless they fi rst understand the domain in which they are considering developing the target software product. It does not matter if the domain is a television network, a machine tool company, or a hospital specializing in liver disease—if the developers do not fully understand the domain, little reliance can be placed on what they subsequently build. Hence, the fi rst step is to obtain domain knowledge. Once the developers have a full comprehension of the domain, the second step is to build a business model, that is, a description of the client’s business processes. In other words, the fi rst need is to understand the domain itself, and the second need is to understand precisely how the client organization operates in that domain. 

Now the scope of the target project has to be delimited. For example, consider a proposed software product for a new highly secure ATM network for a nationwide chain of banks. The size of the business model of the banking chain as a whole is likely to be huge. To determine what the target software product should incorporate, the developers have to focus on only a subset of the business model, namely, the subset covered by the proposed software product. Therefore, delimiting the scope of the proposed project is the third step. 

Now the developers can begin to make the initial business case. The questions that need to be answered before proceeding with the project include [Jacobson, Booch, and Rumbaugh, 1999]: 

• Is the proposed software product cost effective? That is, will the benefits to be gained as a consequence of developing the software product outweigh the costs involved? How long will it take to obtain a return on the investment needed to develop the proposed software product? Alternatively, what will be the cost to the client if he or she decides not to develop the proposed software product? If the software product is to be sold in the marketplace, have the necessary marketing studies been performed? 

• Can the proposed software product be delivered in time? That is, if the software product is delivered late to the market, will the organization still make a profi t or will a competitive software product obtain the lion’s share of the market? Alternatively, if the software product is to be developed to support the client organization’s own activities (presumably including mission-critical activities), what is the impact if the proposed software product is delivered late? 

What risks are involved in developing the software product, and how can these risks be mitigated? Do the team members who will develop the proposed software product have the necessary experience? Is new hardware needed for this software product and, if so, is there a risk that it will not be delivered in time? If so, is there a way to mitigate that risk, perhaps by ordering backup hardware from another supplier? Are software tools ( Chapter 5 ) needed? Are they currently available? Do they have all the necessary functionality? Is it likely that a COTS package (Section 1.11) with all (or almost all) the functionality of the proposed custom software product will be put on the market while the project is under way, and how can this be determined? 

By the end of the inception phase the developers need answers to these questions so that the initial business case can be made. 

The next step is to identify the risks. There are three major risk categories: 

1. Technical risks . Examples of technical risks were just listed. 

2. Not getting the requirements right . This risk can be mitigated by performing the requirements workfl ow correctly. 

3. Not getting the architecture right . The architecture may not be suffi ciently robust. (Recall from Section 2.7 that the architecture of a software product consists of the various components and how they fi t together, and that the property of being able to handle extensions and changes without falling apart is its robustness.) In other words, while the software product is being developed, there is a risk that trying to add the next piece to what has been developed so far might require the entire architecture to be redesigned from scratch. An analogy would be to build a house of cards, only to fi nd the entire edifi ce tumbling down when an additional card is added. 

The risks need to be ranked so that the critical risks are mitigated fi rst. 

As shown in Figure 3.1 , a small amount of the analysis workfl ow is performed during the inception phase. All that is usually done is to extract the information needed for the design of the architecture. This design work is also refl ected in Figure 3.1. 

Turning now to the implementation workfl ow, during the inception phase frequently no coding is performed. However, on occasion, it is necessary to build a proof-of-concept prototype to test the feasibility of part of the proposed software product, as described in Section 2.9.7. 

The test workfl ow commences at the start of the inception phase. The major aim here is to ensure that the requirements are accurately determined. 

Planning is an essential part of every phase. In the case of the inception phase, the developers have insuffi cient information at the beginning of the phase to plan the entire development, so the only planning done at the start of the project is the planning for the inception phase itself. For the same reason, a lack of information, the only planning that can meaningfully be done at the end of the inception phase is to plan for just the next phase, the elaboration phase. 

Documentation, too, is an essential part of every phase. The deliverables of the inception phase include [Jacobson, Booch, and Rumbaugh, 1999] 

• The initial version of the domain model. 

• The initial version of the business model. 

• The initial version of the requirements artifacts. 

• A preliminary version of the analysis artifacts. 

• A preliminary version of the architecture. 

• The initial list of risks. 

• The initial use cases (see Chapter 11 ). 

• The plan for the elaboration phase. 

• The initial version of the business case. 

Obtaining the last item, the initial version of the business case, is the overall aim of the inception phase. This initial version incorporates a description of the scope of the software product as well as fi nancial details. If the proposed software product is to be marketed, the business case includes revenue projections, market estimates, and initial cost estimates. If the software product is to be used in-house, the business case includes the initial cost– benefi t analysis (Section 5.2). 

## 3.10.2 The Elaboration Phase

The aim of the elaboration phase (second increment) is to refi ne the initial requirements, refi ne the architecture, monitor the risks and refi ne their priorities, refi ne the business case, and produce the software project management plan. The reason for the name elaboration phase is clear; the major activities of this phase are refi nements or elaborations of the previous phase. 

Figure 3.1 shows that these tasks correspond to all but completing the requirements workfl ow ( Chapter 11 ), performing virtually the entire analysis workfl ow ( Chapter 13 ), and then starting the design of the architecture (Section 8.5.4). 

The deliverables of the elaboration phase include [Jacobson, Booch, and Rumbaugh, 1999] 

• The completed domain model. 

• The completed business model. 

• The completed requirements artifacts. 

• The completed analysis artifacts. 

• An updated version of the architecture. 

• An updated list of risks. 

• The software project management plan (for the remainder of the project). 

• The completed business case. 

## 3.10.3 The Construction Phase

The aim of the construction phase (third increment) is to produce the fi rst operationalquality version of the software product, the so-called beta release (Section 3.7.4). Consider Figure 3.1 again. Even though the fi gure is only a symbolic representation of the phases, it is clear that the emphasis in this phase is on implementation and testing the software product. That is, the various components are coded and unit tested. The code artifacts are then compiled and linked (integrated) to form subsystems, which are integration tested. Finally, the subsystems are combined into the overall system, which is product tested. This was described in Section 3.7.4. 

The deliverables of the construction phase include [Jacobson, Booch, and Rumbaugh, 1999] 

• The initial user manual and other manuals, as appropriate. 

• All the artifacts (beta release versions). 

• The completed architecture. 

• The updated risk list. 

• The software project management plan (for the remainder of the project). 

• If necessary, the updated business case. 

## 3.10.4 The Transition Phase

The aim of the transition phase (fourth increment) is to ensure that the client’s requirements have indeed been met. This phase is driven by feedback from the sites at which the beta version has been installed. (In the case of a custom software product developed for a specifi c client, there is just one such site.) Faults in the software product are corrected. Also, all the manuals are completed. During this phase, it is important to try to discover any previously unidentifi ed risks. (The importance of uncovering risks even during the transition phase is highlighted in Just in Case You Wanted to Know Box 3.3.) 

The deliverables of the transition phase include [Jacobson, Booch, and Rumbaugh, 1999] 

• All the artifacts (fi nal versions). 

• The completed manuals. 

## 3.11 One- versus Two-Dimensional Life-Cycle Models

A classical life-cycle model (like the waterfall model of Section 2.9.2) is a one-dimensional model, as represented by the single axis in Figure 3.2 (a). Underlying the Unifi ed Process is a two-dimensional life-cycle model, as represented by the two axes in Figure 3.2 (b). 

A real-time system frequently is more complex than most people, even its developers, realize. As a result, sometimes subtle interactions take place among components that even the most skilled testers usually would not detect. An apparently minor change therefore can have major consequences. 

A famous example of this is the fault that delayed the fi rst space shuttle orbital fl ight in April 1981 [Garman, 1981]. The space shuttle avionics are controlled by four identical synchronized computers. Also, an independent fi fth computer is ready for backup in case the set of four computers fails. Two years earlier, a change had been made to the module that performs initialization before the avionics computers are synchronized. An unfortunate side effect of this change was that a record containing a time just slightly later than the current time was erroneously sent to the data area used for synchronization of the avionics computers. The time sent was suffi ciently close to the actual time for this fault not to be detected. About 1 year later, the time difference was slightly increased, just enough to cause a 1 in 67 chance of a failure. Then, on the day of the fi rst space shuttle launch, with hundreds of millions of people watching on television all over the world, the synchronization failure occurred and three of the four identical avionics computers were synchronized one cycle late relative to the fi rst computer. 

A fail-safe device that prevents the independent fi fth computer from receiving information from the other four computers unless they are in agreement had the unanticipated consequence of preventing initialization of the fi fth computer, and the launch had to be postponed. An all too familiar aspect of this incident was that the fault was in the initialization module, a module that apparently had no connection whatsoever with the synchronization routines. 

Unfortunately, this was by no means the last real-time software fault affecting a space launch. For example, in April 1999, a Milstar military communications satellite was hurled into a uselessly low orbit at a cost of $1.2 billion; the cause was a software fault in the upper stage of the Titan 4 rocket [ Florida Today , 1999]. 

Not just space launches are affected by real-time faults but landings, too. In May 2003, a Soyuz TMA-1 spaceship launched from the international space station landed 300 miles off course in Kazakhstan after a ballistic descent. The cause of the landing problems was, yet again, a real-time software fault [CNN.com, 2003]. 

The one-dimensional nature of the waterfall model is clearly refl ected in Figure 2.3 . In contrast, Figure 2.2 shows the evolution-tree model of the Winburg mini case study. This model is two-dimensional and should therefore be compared to Figure 3.2 (b). 

Are the additional complications of a two-dimensional model necessary? The answer was given in Chapter 2 , but this is such an important issue that it is repeated here. During the development of a software product, in an ideal world, the requirements workfl ow would be completed before proceeding to the analysis workfl ow. Similarly, the analysis workfl ow would be completed before starting the design workfl ow, and so on. In reality, however, all but the most trivial software products are too large to handle as a single unit. Instead, the task has to be divided into increments (phases), and within each increment the developers have to iterate until they have completed the task under construction. As humans, we are limited by Miller’s Law [Miller, 1956], which states that we can actively process only seven concepts at a time. We therefore cannot deal with software products as a whole, but instead we have to break those systems into subsystems. Even subsystems can be too large at times—components may be all that we can handle until we have a fuller understanding of the software product as a whole. 


FIGURE 3.2 Comparison of (a) a classical one-dimensional life-cycle model and (b) the twodimensional Unifi ed Process life-cycle model.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/ba3a4c1ecf3bc7bc08941fb5b9d4b30e017ff23f9ba1b88d87670e2fa0243552.jpg)



(a)



(b)


The Unifi ed Process is the best solution to date for treating a large problem as a set of smaller, largely independent subproblems. It provides a framework for incrementation and iteration, the mechanism used to cope with the complexity of large software products. 

Another challenge that the Unifi ed Process handles well is the inevitable changes. One aspect of this challenge is changes in the client’s requirements while a software product is being developed, the so-called moving-target problem (Section 2.4). 

For all these reasons, the Unifi ed Process is currently the best methodology available. However, in the future, the Unifi ed Process will doubtless be superseded by some new methodology. Today’s software professionals are looking beyond the Unifi ed Process to the next major breakthrough. After all, in virtually every fi eld of human endeavor, the discoveries of today are often superior to anything that was put forward in the past. The Unifi ed Process is sure to be superseded, in turn, by the methodologies of the future. The important lesson is that, based on today’s knowledge, the Unifi ed Process appears to be better than the other alternatives currently available. 

The remainder of this chapter is devoted to national and international initiatives aimed at process improvement. 

## 3.12 Improving the Software Process

Our global economy depends critically on computers and hence on software. For this reason, the governments of many countries are concerned about the software process. For example, in 1987, a task force of the U.S. Department of Defense (DoD) reported, “After two decades of largely unfulfi lled promises about productivity and quality gains from applying new software methodologies and technologies, industry and government organizations are realizing that their fundamental problem is the inability to manage the software process” [Brooks et al., 1987]. 

In response to this and related concerns, the DoD founded the Software Engineering Institute (SEI) and set it up at Carnegie Mellon University in Pittsburgh on the basis of a competitive procurement process. A major success of the SEI has been the capability maturity model (CMM) initiative. Related software process improvement efforts include the ISO 9000-series standards of the International Organization for Standardization, and ISO/IEC 15504, an international software improvement initiative involving more than 40 countries. We begin by describing the CMM. 

## 3.13 Capability Maturity Models

The capability maturity models of the SEI are a related group of strategies for improving the software process, irrespective of the actual life-cycle model used. (The term maturity is a measure of the goodness of the process itself.) The SEI has developed CMMs for software (SW–CMM), for management of human resources (P–CMM; the P stands for “people”), for systems engineering (SE–CMM), for integrated product development (IPD–CMM), and for software acquisition (SA–CMM). There are some inconsistencies between the models and an inevitable level of redundancy. Accordingly, in 1997, it was decided to develop a single integrated framework for maturity models, capability maturity model integration (CMMI), which incorporates all fi ve existing capability maturity models. Additional disciplines may be added to CMMI in the future [SEI, 2002]. 

For reasons of space, only one capability maturity model, SW–CMM, is examined here, and an overview of the P–CMM is given in Section 4.8. The SW–CMM was fi rst put forward in 1986 by Watts Humphrey [Humphrey, 1989]. Recall that a software process encompasses the activities, techniques, and tools used to produce software. It therefore incorporates both technical and managerial aspects of software production. Underlying the SW–CMM is the belief that the use of new software techniques in itself will not result in increased productivity and profi tability, because our problems are caused by how we manage the software process. The strategy of the SW–CMM is to improve the management of the software process in the belief that improvements in technique are a natural consequence. The resulting improvement in the process as a whole should result in better-quality software and fewer software projects that suffer from time and cost overruns. 

Bearing in mind that improvements in the software process cannot occur overnight, the SW–CMM induces change incrementally. More specifi cally, fi ve levels of maturity are defi ned, and an organization advances slowly in a series of small evolutionary steps toward the higher levels of process maturity [Paulk, Weber, Curtis, and Chrissis, 1995]. To understand this approach, the fi ve levels now are described. 

## Maturity Level 1. Initial Level

At the initial level , the lowest level, essentially no sound software engineering management practices are in place in the organization. Instead, everything is done on an ad hoc basis. A specifi c project that happens to be staffed by a competent manager and a good software development team may be successful. However, the usual pattern is time and cost overruns caused by a lack of sound management in general and planning in particular. As a result, most activities are responses to crises rather than preplanned tasks. In level-1 organizations, the software process is unpredictable, because it depends totally on the current staff; as the staff changes, so does the process. As a consequence, it is impossible to predict with any accuracy such important items as the time it will take to develop a product or the cost of that product. 

It is unfortunate that the vast majority of software organizations all over the world are still level-1 organizations. 

## Maturity Level 2. Repeatable Level

At the repeatable level , basic software project management practices are in place. Planning and management techniques are based on experience with similar products; hence, the name repeatable . At level 2, measurements are taken, an essential fi rst step in achieving an adequate process. Typical measurements include the meticulous tracking of costs and schedules. Instead of functioning in a crisis mode, as in level 1, managers identify problems as they arise and take immediate corrective action to prevent them from becoming crises. The key point is that, without measurements, it is impossible to detect problems before they get out of hand. Also, measurements taken during one project can be used to draw up realistic duration and cost schedules for future projects. 

## Maturity Level 3. Defi ned Level

At the defi ned level , the process for software production is fully documented. Both the managerial and technical aspects of the process are clearly defi ned, and continual efforts are made to improve the process wherever possible. Reviews (Section 6.2) are used to achieve software quality goals. At this level, it makes sense to introduce new technology, such as CASE environments (Section 5.8), to increase quality and productivity further. In contrast, “high tech” only makes the crisis-driven level-1 process even more chaotic. 

Although a number of organizations have attained maturity levels 2 and 3, few have reached levels 4 or 5. The two highest levels therefore are targets for the future. 

## Maturity Level 4. Managed Level

A managed-level organization sets quality and productivity goals for each project. These two quantities are measured continually and corrective action is taken when there are unacceptable deviations from the goal. Statistical quality controls ([Deming, 1986], [Juran, 1988]) are in place to enable management to distinguish a random deviation from a meaningful violation of quality or productivity standards. (A simple example of a statistical quality control measure is the number of faults detected per 1000 lines of code. A corresponding objective is to reduce this quantity over time.) 

## Maturity Level 5. Optimizing Level

The goal of an optimizing-level organization is continuous process improvement. Statistical quality and process control techniques are used to guide the organization. The knowledge gained from each project is utilized in future projects. The process therefore incorporates a positive feedback loop, resulting in a steady improvement in productivity and quality. 


FIGURE 3.3 The fi ve levels of the software capability maturity model and their key process areas (KPAs).


<table><tr><td colspan="2">5. Optimizing level:Process control</td><td colspan="2">Defect preventionTechnology change managementProcess change management</td></tr><tr><td colspan="2">4. Managed level:Process measurement</td><td colspan="2">Quantitative process managementSoftware quality management</td></tr><tr><td colspan="2">3. Defined level:Process definition</td><td colspan="2">Organization process focusOrganization process definitionTraining programIntegrated software managementSoftware project engineeringIntergroup coordinationPeer reviews</td></tr><tr><td colspan="2">2. Repeatable level:Basic project management</td><td colspan="2">Requirements managementSoftware project planningSoftware project tracking and oversightSoftware subcontract managementSoftware quality assuranceSoftware configuration management</td></tr><tr><td>1. Initial level:Ad hoc process</td><td colspan="3">Not applicable</td></tr></table>

These fi ve maturity levels are summarized in Figure 3.3 , which also shows the key process areas (KPAs) associated with each maturity level. To improve its software process, an organization fi rst attempts to gain an understanding of its current process and then formulates the intended process. Next, actions to achieve this process improvement are determined and ranked in priority. Finally, a plan to accomplish this improvement is drawn up and executed. This series of steps is repeated, with the organization successively improving its software process; this progression from level to level is refl ected in Figure 3.3 . Experience with the capability maturity model has shown that advancing a complete maturity level usually takes from 18 months to 3 years, but moving from level 1 to level 2 can sometimes take 3 or even 5 years. This is a refl ection of how diffi cult it is to instill a methodical approach in an organization that up to now has functioned on a purely ad hoc and reactive basis. 

For each maturity level, the SEI has highlighted a series of key process areas (KPAs) that an organization should target in its endeavor to reach the next maturity level. For example, as shown in Figure 3.3 , the KPAs for level 2 (repeatable level) include confi guration management (Section 5.10), software quality assurance (Section 6.1.1), project planning ( Chapter 9 ), project tracking (Section 9.2.5), and requirements management ( Chapter 11 ). These areas cover the basic elements of software management: Determine the client’s needs (requirements management), draw up a plan (project planning), monitor deviations from that plan (project tracking), control the various pieces that make up the software product key process area (confi guration management), and ensure that the product is fault free (quality assurance). Within each KPA is a group of between two and four related goals that, if achieved, result in that maturity level being attained. For example, one project planning goal is the development of a plan that appropriately and realistically covers the activities of software development. 

At the highest level, maturity level 5, the KPAs include fault prevention, technology change management, and process change management. Comparing the KPAs of the two levels, it is clear that a level-5 organization is far in advance of one at level 2. For example, a level-2 organization is concerned with software quality assurance, that is, with detecting and correcting faults (software quality is discussed in more detail in Chapter 6 ). In contrast, the process of a level-5 organization incorporates fault prevention, that is, trying to ensure that no faults are in the software in the fi rst place. To help an organization to reach the higher maturity levels, the SEI has developed a series of questionnaires that form the basis for an assessment by an SEI team. The purpose of the assessment is to highlight current shortcomings in the organization’s software process and to indicate ways in which the organization can improve its process. 

The CMM program of the Software Engineering Institute was sponsored by the U.S. Department of Defense. One of the original goals of the CMM program was to raise the quality of defense software by evaluating the processes of contractors who produce software for the DoD and awarding contracts to those contractors who demonstrate a mature process. The U.S. Air Force stipulated that any software development organization that wished to be an Air Force contractor had to conform to SW–CMM level 3 by 1998, and the DoD as a whole subsequently issued a similar directive. Consequently, pressure is put on organizations to improve the maturity of their software processes. However, the SW–CMM program has moved far beyond the limited goal of improving DoD software and is being implemented by a wide variety of software organizations that wish to improve software quality and productivity 

## 3.14 Other Software Process Improvement Initiatives

A different attempt to improve software quality is based on the International Organization for Standardization (ISO) 9000-series standards, a series of fi ve related standards applicable to a wide variety of industrial activities, including design, development, production, installation, and servicing; ISO 9000 certainly is not just a software standard. Within the ISO 9000 series, standard ISO 9001 [1987] for quality systems is the standard most applicable to software development. Because of the broadness of ISO 9001, ISO has published specifi c guidelines to assist in applying ISO 9001 to software: ISO 9000-3 [1991]. (For more information on ISO, see Just in Case You Wanted to Know Box 1.4.) 

ISO 9000 has a number of features that distinguish it from the CMM [Dawood, 1994]. ISO 9000 stresses documenting the process in both words and pictures to ensure consistency and comprehensibility. Also, the ISO 9000 philosophy is that adherence to the standard does not guarantee a high-quality product but rather reduces the risk of a poor-quality product. ISO 9000 is only part of a quality system. Also required are management commitment to quality, intensive training of workers, and setting and achieving goals for continual quality improvement. ISO 9000-series standards have been adopted by over 60 countries, including the United States, Japan, Canada, and the countries of the European Union (EU). This means, for example, that if a U.S. software organization wishes to do business with a European client, the U.S. organization must fi rst be certifi ed as ISO 9000 compliant. A certifi ed registrar (auditor) has to examine the company’s process and certify that it complies with the ISO standard. 

Following their European counterparts, more and more U.S. organizations are requiring ISO 9000 certifi cation. For example, General Electric Plastic Division insisted that 340 vendors achieve the standard by June 1993 [Dawood, 1994]. It is unlikely that the U.S. government will follow the EU lead and require ISO 9000 compliance for non-U.S. companies that wish to do business with organizations in the United States. Nevertheless, pressures both within the United States and from its major trading partners ultimately may result in signifi cant worldwide ISO 9000 compliance. 

ISO/IEC 15504 is an international process improvement initiative, like ISO 9000. The initiative was formerly known as SPICE , an acronym formed from Software Process Improvement Capability dEtermination. Over 40 countries actively contributed to the SPICE endeavor. SPICE was initiated by the British Ministry of Defence (MOD) with the long-term aim of establishing SPICE as an international standard (MOD is the UK counterpart of the U.S. DoD, which initiated the CMM). The fi rst version of SPICE was completed in 1995. In July 1997, the SPICE initiative was taken over by a joint committee of the International Organization for Standardization and the International Electrotechnical Commission. For this reason, the name of the initiative was changed from SPICE to ISO/IEC 15504, or 15504 for short. 

## 3.15 Costs and Benefi ts of Software Process Improvement

Does implementing software process improvement lead to increased profi tability? Results indicate that this indeed is the case. For example, the Software Engineering Division of Hughes Aircraft in Fullerton, California, spent nearly $500,000 between 1987 and 1990 for assessments and improvement programs [Humphrey, Snider, and Willis, 1991]. During this 3-year period, Hughes Aircraft moved up from maturity level 2 to level 3, with every expectation of future improvement to level 4 and even level 5. As a consequence of improving its process, Hughes Aircraft estimated its annual savings to be on the order of $2 million. These savings accrued in a number of ways, including decreased overtime hours, fewer crises, improved employee morale, and lower turnover of software professionals. 

Comparable results have been reported at other organizations. For example, the Equipment Division at Raytheon moved from level 1 in 1988 to level 3 in 1993. A twofold increase in productivity resulted, as well as a return of $7.70 for every dollar invested in the process improvement effort [Dion, 1993]. As a consequence of results like these, the capability maturity models are being applied rather widely within the U.S. software industry and abroad. 


FIGURE 3.4 Results of 34 Motorola GED projects (MEASL stands for “million equivalent assembler source lines”) [Diaz and Sligo, 1997]. (© 1997, IEEE.)


<table><tr><td>CMM Level</td><td>Number of Projects</td><td>Relative Decrease in Duration</td><td>Faults per MEASL Detected during Development</td><td>Relative Productivity</td></tr><tr><td>Level 1</td><td>3</td><td>1.0</td><td>—</td><td>—</td></tr><tr><td>Level 2</td><td>9</td><td>3.2</td><td>890</td><td>1.0</td></tr><tr><td>Level 3</td><td>5</td><td>2.7</td><td>411</td><td>0.8</td></tr><tr><td>Level 4</td><td>8</td><td>5.0</td><td>205</td><td>2.3</td></tr><tr><td>Level 5</td><td>9</td><td>7.8</td><td>126</td><td>2.8</td></tr></table>

For example, Tata Consultancy Services in India used both the ISO 9000 framework and CMM to improve its process [Keeni, 2000]. Between 1996 and 2000, the errors in effort estimation decreased from about 50 percent to only 15 percent. The effectiveness of reviews (that is, the percentage of faults found during reviews) increased from 40 to 80 percent. The percentage of effort devoted to reworking projects dropped from nearly 12 percent to less than 6 percent. 

Motorola Government Electronics Division (GED) has been actively involved in SEI’s software process improvement program since 1992 [Diaz and Sligo, 1997]. Figure 3.4 depicts 34 GED projects, categorized according to the maturity level of the group that developed each project. As can be seen from the fi gure, the relative duration (that is, the duration of a project relative to a baseline project completed before 1992) decreased with increasing maturity level. Quality was measured in terms of faults per million equivalent assembler source lines (MEASL); to be able to compare projects implemented in different languages, the number of lines of source code was converted into the number of equivalent lines of assembler code [Jones, 1996]. As shown in Figure 3.4 , quality increased with increasing maturity level. Finally, productivity was measured as MEASL per person-hour. For reasons of confi dentiality, Motorola does not publish actual productivity fi gures, so Figure 3.4 refl ects productivity relative to the productivity of a level-2 project. (No quality or productivity fi gures are available for the level-1 projects because these quantities cannot be measured when the team is at level 1.) 

Galin and Avrahami [2006] analyzed 85 projects that had previously been reported in the literature as having advanced by one level as a consequence of implementing CMM. These projects were divided into four groups (CMM level 1 to level 2, CMM level 2 to level 3, and so on). For the four groups, the median fault density (number of faults per KLOC) decreased by between 26 and 63 percent. The median productivity (KLOC per person month) increased by between 26 and 187 percent. Median rework decreased by between 34 and 40 percent. The median project duration decreased by between 28 and 53 percent. Fault detection effectiveness (percentage of faults detected during development of the total detected project faults) increased as follows: For the three lowest groups, the median increased by between 70 and 74 percent, and 13 percent for the highest group (CMM level 4 to level 5). The return on investment varied between 120 and 650 percent, with a median value of 360 percent. 

# Just in Case You Wanted to Know

There are constraints on the speed of hardware because electrons cannot travel faster than the speed of light. In a famous article entitled “No Silver Bullet,” Brooks [1986] suggested that inherent problems exist in software production, and that these problems can never be solved because of analogous constraints on software. Brooks argued that intrinsic properties of software, such as its complexity, the fact that software is invisible and unvisualizable, and the numerous changes to which software is typically subjected over its lifetime, make it unlikely that there will ever be an order-of-magnitude increment (or “silver bullet”) in software process improvement. 

As a consequence of published studies such as those described in this section and those listed in the For Further Reading section of this chapter, more and more organizations worldwide are realizing that process improvement is cost effective. 

An interesting side effect of the process improvement movement has been the interaction between software process improvement initiatives and software engineering standards. For example, in 1995 the International Organization for Standardization published ISO/IEC 12207, a full life-cycle software standard [ISO/IEC 12207, 1995]. Three years later, a U.S. version of the standard [IEEE/EIA 12207.0-1996, 1998] was published by the Institute of Electrical and Electronic Engineers (IEEE) and the Electronic Industries Alliance (EIA). This version incorporates U.S. software “best practices,” many of which can be traced back to CMM. To achieve compliance with IEEE/EIA 12207, an organization must be at or near CMM capability level 3 [Ferguson and Sheard, 1998]. Also, ISO 9000-3 now incorporates parts of ISO/IEC 12207. This interplay between software engineering standards organizations and software process improvement initiatives surely will lead to even better software processes. 

Another dimension of software process improvement appears in Just in Case You Wanted to Know Box 3.4. 

## Chapter Review

After some preliminary defi nitions, the Unifi ed Process is introduced in Section 3.1. The importance of iteration and incrementation within the object-oriented paradigm is described in Section 3.2. Now the core workfl ows of the Unifi ed Process are explained in detail; the requirements workfl ow (Section 3.3), analysis workfl ow (Section 3.4), design workfl ow (Section 3.5), implementation workfl ow (Section 3.6), and test workfl ow (Section 3.7). The various artifacts tested during the test workfl ow are described in Sections 3.7.1 through 3.7.4. Postdelivery maintenance is discussed in Section 3.8, and retirement in Section 3.9. The relationship between the work fl ows and the phases of the Unifi ed Process is analyzed in Section 3.10, and a detailed description is given of the four phases of the Unifi ed Process: the inception phase (Section 3.10.1), the elaboration phase (Section 3.10.2), the construction phase (Section 3.10.3), and the transition phase (Section 3.10.4). The importance of two-dimensional life-cycle models is discussed in Section 3.11. 

The last part of the chapter is devoted to software process improvement (Section 3.12). Details are given of various national and international software improvement initiatives, including the capa bility maturity models (Section 3.13), and ISO 9000 and ISO/IEC 15504 (Section 3.14). The costeffectiveness of software process improvement is discussed in Section 3.15. 

The March–April 2003 issue of IEEE Software contains a number of articles on the software process, including [Eickelmann and Anant, 2003], a discussion of statistical process control. Practical applications of statistical process control are described in [Weller, 2000] and [Florac, Carleton, and Barnard, 2000]. 

With regard to testing during each workfl ow, an excellent source is [Ammann and Offutt, 2008]. More specifi c references are given in Chapter 6 of this book and in the For Further Reading section at the end of that chapter. 

A detailed description of the original SEI capability maturity model is given in [Humphrey, 1989]. Capability maturity model integration is described in [SEI, 2002]. Humphrey [1996] describes a personal software process (PSP); results of applying the PSP appear in [Ferguson et al., 1997]. The results of an experiment to measure the effectiveness of PSP training are presented in [Prechelt and Unger, 2000]. Extensions needed to the Unifi ed Process for it to comply with CMM levels 2 and 3 are presented in [Manzoni and Price, 2003]. Implementing SW–CMM in small organizations is described in [Guerrero and Eterovic, 2004] and [Dangle, Larsen, Shaw, and Zelkowitz, 2005]. The July–August 2000 issue of IEEE Software has three papers on software process maturity, and there are four papers on the PSP in the November–December 2000 issue of IEEE Software . 

A compendium of the results of many studies of process improvement appears in [Galin and Avrahami, 2006]. 

Pitterman [2000] describes how a group at Telecordia Technologies reached level 5; a study of how a Computer Sciences Corporation group attained level 5 appears in [McGarry and Decker, 2002]. Insights into the nature of level-5 organizations appear in [Eickelmann, 2003] and [Agrawal and Chari, 2007]. Cost–benefi t analysis of software process improvement is described in [van Solingen, 2004]. An empirical investigation of the key factors for success in software process improvement is presented in [Dybå, 2005]. 

Problems of software product improvement appear in [Conradi and Fuggetta, 2002]. The results of 18 different software process improvement initiatives conducted at Ericsson are described in [Borjesson and Mathiassen, 2004]. A wealth of information on the CMM is available at the SEI CMM website www.sei.cmu.edu . An assessment of the success of the SPICE project can be found in [Rout et al., 2007]. The ISO/IEC 15504 (SPICE) home page is at www.sei.cmu.edu/technology/ process/spice/ . 

A comparison between CMM and IEEE/EIA 12207 is given in [Ferguson and Sheard, 1998], and a comparison between CMM and Six Sigma (another approach to process improvement) appears in [Murugappan and Keeni, 2003]. An approach to implementing both ISO 9001 and CMMI appears in [Yoo et al., 2006]. A repository containing the results of some 400 software improvement experiments is described in [Blanco, Gutiérrez, and Satriani, 2001]. 

## Key Terms

acceptance testing 86 alpha release 86 ambiguity 81 analysis workfl ow 80 application domain 78 architectural design 82 beta release 86 budget 82 business case 79 

business model 89 capability maturity model (CMM) 95 class 82 code artifact 83 component 83 concept exploration 79 construction phase 92 contradiction 81 

core workfl ow 78 cost 79 deadline 79 defi ned level 96 deliverable 82 design workfl ow 82 detailed design 82 domain 78 elaboration phase 91 

implementation workfl ow 83 managed level 96 retirement 88 inception phase 89 maturity 95 SPICE 99 incompleteness 81 milestone 82 test workfl ow 84 initial level 95 model 76 traceability 84 integration testing 86 module 82 transition phase 92 International Organization for optimizing level 96 Unifi ed Modeling Language Standardization (ISO) 98 product testing 86 (UML) 76 ISO 9000-3 98 regression testing 87 Unifi ed Process 76 ISO 9001 98 reliability 79 unit testing 85 ISO/IEC 15504 99 repeatable level 96 key process area (KPA) 98 requirements workfl ow 78 

## Problems

3.1 Defi ne the terms software process and Unifi ed Process . 

3.2 In the software engineering context, what is meant by the term model ? 

3.3 What is meant by a phase of the Unifi ed Process? 

3.4 Distinguish clearly between an ambiguity, a contradiction, and incompleteness. 

3.5 Consider the requirements workfl ow and the analysis workfl ow. Would it make more sense to combine these two activities into one workfl ow than to treat them separately? 

3.6 More testing is performed during the implementation workfl ow than in any other workfl ow. Would it be better to divide this workfl ow into two separate workfl ows, one incorporating the nontesting aspects, the other all the testing? 

3.7 “Correctness is the responsibility of the SQA group.” Discuss this statement. 

3.8 Maintenance is the most important activity of software production and the most diffi cult to perform. Nevertheless, it is looked down on by many software professionals, and maintenance programmers often are paid less than developers. Do you think that this is reasonable? If not, how would you try to change it? 

3.9 Why do you think that, as stated in Section 3.9, true retirement is a rare event? 

3.10 Because of a fi re at Elmer’s Software, all documentation for a product is destroyed just before it is delivered. What is the impact of the resulting lack of documentation? 

3.11 You have just purchased Antedeluvian Software Developers, an organization on the verge of bankruptcy because the company is at maturity level 1. What is the fi rst step you will take to restore the organization to profi tability? 

3.12 Section 3.13 states that it makes little sense to introduce CASE environments within organizations at maturity level 1 or 2. Explain why this is so. 

3.13 What is the effect of introducing CASE tools (as opposed to environments) within organizations with a low maturity level? 

3.14 Maturity level 1, the initial level, refers to an absence of good software engineering management practices. Would it not have been better for the SEI to have labeled the initial level as maturity level 0? 

3.15 (Term Project) What differences would you expect to fi nd if the Chocoholics Anonymous product of Appendix A were developed by an organization at CMM level 1, as opposed to an organization at level 5? 

3.16 (Readings in Software Engineering) Your instructor will distribute copies of [Agrawal and Chari, 2007]. Would you like to work in a level-5 organization? Explain your answer. 

References 



[Agrawal and Chari, 2007] M. AGRAWAL AND K. CHARI, “Software Effort, Quality, and Cycle Time: A Study of CMM Level 5 Projects,” IEEE Transactions on Software Engineering 32 (March 2007), pp. 145–56. 





[Ammann and Offutt, 2008] P. AMMANN AND J. OFFUTT, Introduction to Software Testing, Cambridge University Press, Cambridge, UK, 2008. 





[Blanco, Gutiérrez, and Satriani, 2001] M. BLANCO, P. GUTIÉRREZ, AND G. SATRIANI, “SPI Patterns: Learning from Experience,” IEEE Software 18 (May–June 2001), pp. 28–35. 





[Booch, 1994] G. BOOCH, Object-Oriented Analysis and Design with Applications, 2nd ed., Benjamin/ Cummings, Redwood City, CA, 1994. 





[Booch, Rumbaugh, and Jacobson, 1999] G. BOOCH, J. RUMBAUGH, AND I. JACOBSON, The UML Users Guide , Addison-Wesley, Reading, MA, 1999. 





[Borjesson and Mathiassen, 2004] A. BORJESSON AND L. MATHIASSEN, “Successful Process Implementation,” IEEE Software 21 (July–August 2004), pp. 36–44. 





[Brooks, 1986] F. P. BROOKS, JR., “No Silver Bullet,” in: Information Processing ’86 , H.-J. Kugler (Editor), Elsevier North-Holland, New York, 1986; reprinted in IEEE Computer 20 (April 1987), pp. 10–19. 





[Brooks et al., 1987] F. P. BROOKS, V. BASILI, B. BOEHM, E. BOND, N. EASTMAN, D. L. EVANS, A. K. JONES, M. SHAW, AND C. A. ZRAKET, “Report of the Defense Science Board Task Force on Military Software,” Department of Defense, Offi ce of the Under Secretary of Defense for Acquisition, Washington, DC, September 1987. 





[CNN.com, 2003] “Russia: Software Bug Made Soyuz Stray,” edition.cnn.com/2003/TECH/ space/05/06/soyuz.landing.ap/, May 6, 2003. 





[Conradi and Fuggetta, 2002] R. CONRADI AND A. FUGGETTA, “Improving Software Process Improvement,” IEEE Software 19 (July–August 2002), pp. 92–99. 





[Dangle, Larsen, Shaw, and Zelkowitz, 2005] K. C. DANGLE, P. LARSEN, M. SHAW, AND M. V. ZEL-KOWITZ, “Software Process Improvement in Small Organizations: A Case Study,” IEEE Software 22 (September–October 2005), pp. 68–75. 





[Dawood, 1994] M. DAWOOD, “It’s Time for ISO 9000,” CrossTalk (March 1994), pp. 26–28. 





[Deming, 1986] W. E. DEMING, Out of the Crisis , MIT Center for Advanced Engineering Study, Cambridge, MA, 1986. 





[Diaz and Sligo, 1997] M. DIAZ AND J. SLIGO, “How Software Process Improvement Helped Motorola,” IEEE Software 14 (September–October 1997), pp. 75–81. 





[Dion, 1993] R. DION, “Process Improvement and the Corporate Balance Sheet,” IEEE Software 10 (July 1993), pp. 28–35. 





[Dybå, 2005] T. DYBÅ, “An Empirical Investigation of the Key Factors for Success in Software Process Improvement,” IEEE Transactions in Software Engineering 31 (May 2005), pp. 410–24. 





[Eickelmann, 2003] N. EICKELMANN, “An Insider’s View of CMM Level 5,” IEEE Software 20 (July– August 2003), pp. 79–81. 





[Eickelmann and Anant, 2003] N. EICKELMANN AND A. ANANT, “Statistical Process Control: What You Don’t Know Can Hurt You!” IEEE Software 20 (March–April 2003), pp. 49–51. 





[Ferguson and Sheard, 1998] J. FERGUSON AND S. SHEARD, “Leveraging Your CMM Efforts for IEEE/ EIA 12207,” IEEE Software 15 (September–October 1998), pp. 23–28. 





[Ferguson et al., 1997] P. FERGUSON, W. S. HUMPHREY, S. KHAJENOORI, S. MACKE, AND A. MAT-VYA, “Results of Applying the Personal Software Process,” IEEE Computer 30 (May 1997), pp. 24–31. 





[Florac, Carleton, and Barnard, 2000] W. A. FLORAC, A. D. CARLETON, AND J. BARNARD, “Statistical Process Control: Analyzing a Space Shuttle Onboard Software Process,” IEEE Software 17 (July–August 2000), pp. 97–106. 





[ Florida Today , 1999] “Milstar Satellite Lost during Air Force Titan 4b Launch from Cape,” Florida Today , www.fl oridatoday.com/space/explore/uselv/titan/b32/ , June 5, 1999. 





[Galin and Avrahami, 2006] D. GALIN AND M. AVRAHAMI, “Are CMM Program Investments Benefi - cial? Analyzing Past Studies,” IEEE Software 23 (November–December 2006), pp. 81–87. 





[Garman, 1981] J. R. GARMAN, “The ‘Bug’ Heard ’Round the World,” ACM SIGSOFT Software Engineering Notes 6 (October 1981), pp. 3–10. 





[Guerrero and Eterovic, 2004] F. GUERRERO AND Y. ETEROVIC, “Adopting the SW-CMM in a Small IT Organization,” IEEE Software 21 (July–August 2004), pp. 29–35. 





[Humphrey, 1989] W. S. HUMPHREY, Managing the Software Process , Addison-Wesley, Reading, MA, 1989. 





[Humphrey, 1996] W. S. HUMPHREY, “Using a Defi ned and Measured Personal Software Process,” IEEE Software 13 (May 1996), pp. 77–88. 





[Humphrey, Snider, and Willis, 1991] W. S. HUMPHREY, T. R. SNIDER, AND R. R. WILLIS, “Software Process Improvement at Hughes Aircraft,” IEEE Software 8 (July 1991), pp. 11–23. 





[IEEE/EIA 12207.0-1996, 1998] “IEEE/EIA 12207.0-1996 Industry Implementation of International Standard ISO/IEC 12207:1995,” Institute of Electrical and Electronic Engineers, Electronic Industries Alliance, New York, 1998. 





[ISO 9000-3, 1991] “ISO 9000-3, Guidelines for the Application of ISO 9001 to the Development, Supply, and Maintenance of Software,” International Organization for Standardization, Geneva, 1991. 





[ISO 9001, 1987] “ISO 9001, Quality Systems—Model for Quality Assurance in Design/Development, Production, Installation, and Servicing,” International Organization for Standardization, Geneva, 1987. 





[ISO/IEC 12207, 1995] “ISO/IEC 12207:1995, Information Technology—Software Life-Cycle Processes,” International Organization for Standardization, International Electrotechnical Commission, Geneva, 1995. 





[Jacobson, Booch, and Rumbaugh, 1999] I. JACOBSON, G. BOOCH, and J. RUMBAUGH, The Unifi ed Software Development Process, Addison-Wesley, Reading, MA, 1999. 





[Jones, 1996] C. JONES, Applied Software Measurement, McGraw-Hill, New York, 1996. 





[Juran, 1988] J. M. JURAN, Juran on Planning for Quality , Macmillan, New York, 1988. 





[Keeni, 2000] G. KEENI, “The Evolution of Quality Processes at Tata Consultancy Services,” IEEE Software 17 (July–August 2000), pp. 79–88. 





[Manzoni and Price, 2003] L. V. MANZONI AND R. T. PRICE, “Identifying Extensions Required by RUP (Rational Unifi ed Process) to Comply with CMM (Capability Maturity Model) Levels 2 and 3,” IEEE Transactions on Software Engineering 29 (February 2003), pp. 181–92. 





[McGarry and Decker, 2002] F. MCGARRY AND B. DECKER, “Attaining Level 5 in CMM Process Maturity,” IEEE Software 19 (2002), pp. 87–96. 





[Miller, 1956] G. A. MILLER, “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,” The Psychological Review 63 (March 1956), pp. 81–97. Reprinted in: www.well.com/user/smalin/miller.html. 





[Murugappan and Keeni, 2003] M. MURUGAPPAN AND G. KEENI, “Blending CMM and Six Sigma to Meet Business Goals,” IEEE Software 20 (March–April 2003), pp. 42–48. 





[Paulk, Weber, Curtis, and Chrissis, 1995] M. C. PAULK, C. V. WEBER, B. CURTIS, AND M. B. CHRISSIS, The Capability Maturity Model: Guidelines for Improving the Software Process , Addison-Wesley, Reading, MA, 1995. 





[Pitterman, 2000] B. PITTERMAN, “Telecordia Technologies: The Journey to High Maturity,” IEEE Software 17 (July–August 2000), pp. 89–96. 





[Prechelt and Unger, 2000] L. PRECHELT AND B. UNGER, “An Experiment Measuring the Effects of Personal Software Process (PSP) Training,” IEEE Transactions on Software Engineering 27 (May 2000), pp. 465–72. 





[Rout et al., 2007] T. P. ROUT, K. EL EMAM, M. FUSANI, D. GOLDENSON, AND H.-W. JUNG, “SPICE in Retrospect: Developing a Standard for Process Assessment,” Journal of Systems and Software 80 (September 2007), pp. 1483–93. 





[Rumbaugh et al., 1991] J. RUMBAUGH, M. BLAHA, W. PREMERLANI, F. EDDY, AND W. LORENSEN, Object-Oriented Modeling and Design , Prentice Hall, Englewood Cliffs, NJ, 1991. 





[SEI, 2002] “CMMI Frequently Asked Questions (FAQ),” Software Engineering Institute, Carnegie Mellon University, Pittsburgh, June 2002. 





[van Solingen, 2004] R. VAN SOLINGEN, “Measuring the ROI of Software Process Improvement,” IEEE Software 21 (May–June 2004), pp. 32–38. 





[van Wijngaarden et al., 1975] A. VAN WIJNGAARDEN, B. J. MAILLOUX, J. E. L. PECK, C. H. A. KOSTER, M. SINTZOFF, C. H. LINDSEY, L. G. L. T. MEERTENS, AND R. G. FISKER, “Revised Report on the Algorithmic Language ALGOL 68,” Acta Informatica 5 (1975), pp. 1–236. 





[Weller, 2000] E. F. WELLER, “Practical Applications of Statistical Process Control,” IEEE Software 18 (May–June 2000), pp. 48–55. 





[Yoo et al., 2006] C. YOO, J. YOON, B. LEE, C. LEE, J. LEE, S. HYUN, AND C.WU, “A Unifi ed Model for the Implementation of Both ISO 9001:2000 and CMMI by ISO-Certifi ed Organizations,” Journal of Systems and Software 79 (July 2006), pp. 954–61. 



## Teams

Learning Objectives 

After studying this chapter, you should be able to 

• Explain the importance of a well-organized team. 

• Describe how modern hierarchical teams are organized. 

• Analyze the strengths and weaknesses of a variety of different team organizations. 

• Appreciate the issues that arise when choosing an appropriate team organization. 

Without competent, well-trained software engineers, a software project is doomed to fail ure. However, having the right people is not enough; teams must be organized in such a way that the team members can work productively in cooperation with one another. Team organization is the subject of this chapter. 

## 4.1 Team Organization

Most products are too large to be completed by a single software professional within the given time constraints. As a result, the product must be assigned to a group of professionals organized as a team . For example, consider the analysis workfl ow. To specify the target product within 2 months, it may be necessary to assign the task to three analysis specialists organized as a team under the direction of the analysis manager. Similarly, the design task may be shared between members of the design team. 

Suppose now that a product has to be coded within 3 months, even though 1 person-year of coding is involved (a person-year is the amount of work that can be done by one person in 1 year). The solution is apparently simple: If one programmer can code the product in 1 year, four programmers can do it in 3 months. 

This, of course, does not work. In practice, the four programmers may take nearly a year, and the quality of the resulting product may well be lower than if one programmer had coded the entire product. The reason is that some tasks can be shared, but others must be done individually. For instance, if one farmhand can pick a strawberry fi eld in 10 days, the same strawberry fi eld can be picked by 10 farmhands in 1 day. On the other hand, one elephant can produce a calf in 22 months, but this feat cannot possibly be accomplished in 1 month by 22 elephants. 

In other words, tasks like strawberry picking can be fully shared; others, like elephant production, cannot be shared at all. Unlike elephant production, it is possible to share implementation tasks between members of a team by distributing the coding among the team members. However, team programming also is unlike strawberry picking in that team members have to interact with one another in a meaningful and effective way. For example, suppose Sheila and Harry have to code two modules, m1 and m2. A number of things can go wrong. For instance, both Sheila and Harry may code m1 and ignore m2. Or Sheila may code m1, and Harry may code m2. But when m1 calls m2 it passes four arguments; Harry has coded m2 in such a way that it requires fi ve arguments. Or the order of the arguments in m1 and m2 may be different. Or the order may be the same, but the data types may be slightly different. Such problems usually are caused by a decision made while the design workfl ow is performed that is not propagated throughout the development organization. The issue has nothing whatsoever to do with the technical competency of the programmers. Team organization is a managerial issue; management must organize the programming teams so that each team is highly productive. 

A different type of diffi culty that arises from team development of software is shown in Figure 4.1 . Three channels of communication exist between the three software professionals working on the project. Now, suppose that the work is slipping, a deadline is rapidly approaching, and the task is not nearly complete. The obvious thing to do is to add a fourth professional to the team. But the fi rst thing that must happen when the fourth professional joins the team is for the other three to explain in detail what has been accomplished to date and what is still incomplete. In other words, adding personnel to a late software project makes it even later. This principle is known as Brooks’s Law after Fred Brooks who observed it while managing the development of OS/360 [Brooks, 1975], an operating system for IBM 360 mainframe computers. 

In a large organization, teams are used in every workfl ow of software production, but especially when the implementation workfl ow is performed; during that workfl ow, programmers work independently on separate code artifacts. Accordingly, the implementation workfl ow is 


FIGURE 4.1 Communication paths between three software professionals (solid lines) and when a fourth professional joins them (dashed lines).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/354326b345299c6d6f1b43f6f6b8c54ead9d9dbf82cd770ca47dd713def53193.jpg)


# Just in Case You Wanted to Know

Some 40 years ago, when software was still input on punched cards, all too many programmers regarded “bugs” in software in the same light as insects that would invade their card deck unless prevented from doing so. This attitude was amusingly lampooned by the marketing of an aerosol spray named Shoo-Bug. The instructions on the label solemnly explained that spraying one’s card deck with Shoo-Bug would ensure that no bugs could possibly infest the code. Of course, the spray can contained nothing but air. 

a prime candidate for sharing the task among several software professionals. In some smaller organizations, one individual may be responsible for the requirements, analysis, and design, after which the implementation is done by a team of two or three programmers. Because teams are used most heavily when performing the implementation workfl ow, the problems of team organization are felt most acutely during implementation. In the remainder of this chapter, team organization therefore is presented within the context of implementation, even though the problems and their solutions are equally applicable to all the other workfl ows. 

There are two extreme approaches to programming-team organization, democratic teams and chief programmer teams. The approach taken here is to describe each of the two approaches, highlight its strengths and weaknesses, and then suggest other ways of organiz ing a programming team that incorporate the best features of the two extremes. 

## 4.2 Democratic Team Approach

The democratic team organization was fi rst described by Weinberg in 1971 [Weinberg, 1971]. The basic concept underlying the democratic team is egoless programming. Weinberg points out that programmers can be highly attached to their code. Sometimes, they even name their modules after themselves: They therefore see their modules as an extension of themselves. The diffi culty with this is that a programmer who sees a module as an extension of his or her ego is certainly not going to try to fi nd all the faults in “his” code or “her” code. And, if there is a fault, it is termed a bug , like some insect that crept unasked into the code and could have been prevented if only the code had been guarded more zealously against invasion (see Just in Case You Wanted to Know Box 4.1). 

Weinberg’s solution to the problem of programmers being too closely attached to their own code is egoless programming. The social environment must be restructured and so must programmer values. Every programmer must encourage the other members of the team to fi nd faults in his or her code. The presence of a fault must not be considered something bad but a normal and accepted event; the attitude of the reviewer should be appreciation at being asked for advice, rather than ridicule of the programmer for making coding mistakes. The team as a whole thereby develops an ethos, a group identity; and modules belong to the team as a whole rather than to any one individual. 

A group of up to 10 egoless programmers constitutes a democratic team. Weinberg warns that management may have diffi culty working with such a team. After all, consider the managerial career path. When a programmer is promoted to a management position, his or her fellow programmers are not promoted and must strive to attain the higher level at the next round of promotions. In contrast, a democratic team is a group working for a common cause with no single leader, with no programmers trying to get promoted to the next level. What is important is team identity and mutual respect. 

Weinberg tells of a democratic team that developed an outstanding product. Management decided to give a cash award to the team’s nominal manager (by defi nition, a democratic team has no leader). He refused to accept it personally, saying that it had to be shared equally among all members of the team. Management thought that he was angling for more money and that the team (and especially its nominal manager) had some rather unorthodox ideas. Management forced the nominal manager to accept the money, which he then divided equally among the team. Next, the entire team resigned and joined another company as a team. 

The strengths and weaknesses of democratic teams are now presented. 

## 4.2.1 Analysis of the Democratic Team Approach

A major strength of the democratic team approach is the positive attitude toward the fi nding of faults. The more found, the happier are the members of a democratic team. This positive attitude leads to more rapid detection of faults and hence to high-quality code. But there are some major problems. As pointed out previously, managers may have diffi culty accepting egoless programming. In addition, a programmer with, say, 15 years of experience is likely to resent having his or her code appraised by fellow programmers, especially beginners. 

Weinberg feels that egoless teams spring up spontaneously and cannot be imposed from outside. Little experimental research has been done on democratic programming teams, but the experience of Weinberg is that democratic teams are enormously productive. Mantei [1981] has analyzed the democratic team organization using arguments based on theories of and experiments on group organization in general rather than specifi cally on programming teams. She points out that decentralized groups work best when the problem is diffi cult and suggests that democratic teams should function well in a research environment. It has been my experience that a democratic team also works well in an industrial setting when a hard problem must be solved. On a number of occasions I have been a member of democratic teams that have sprung up spontaneously among software professionals with research experience. But, once the task has been reduced to the implementation of a hardwon solution, the team must then be reorganized in a more hierarchical fashion, such as the chief programmer team approach described in Section 4.3. 

## 4.3 Classical Chief Programmer Team Approach

Consider the six-person team shown in Figure 4.2 , with 15 two-person communication channels. In fact, the total number of two-, three-, four-, fi ve-, and six-person groups is 57. This multiplicity of communication channels is the major reason why a six-person team structured as in Figure 4.2 is unlikely to be able to perform 36 person-months of work in 6 months; many hours are wasted in meetings involving two or more team members at a time. 

Now consider the six-person team shown in Figure 4.3 . Again, there are six programmers, but now only fi ve lines of communication. This is the basic concept behind what now is termed the chief programmer team . A related idea was put forward by Brooks [1975], who drew the analogy of a chief surgeon directing an operation. The surgeon is assisted by other surgeons, the anesthesiologist, and a variety of nurses. In addition, when necessary, the team uses experts in other areas, such as cardiologists or nephrologists. This analogy highlights two key aspects of a chief programmer team. The fi rst is specialization : Each member of the team carries out only those tasks for which he or she has been trained. The second aspect is hierarchy : The chief surgeon directs the actions of all the other members of the team and is responsible for every aspect of the operation. 


FIGURE 4.2 Communication paths between six software professionals.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/594f69368275393ff9c39029426800cbfbe4a0e3d7dfd7587ec853a50d4187e1.jpg)



FIGURE 4.3 The structure of a classical chief programmer team.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/3328a508006f9ced1b77f6248792fa7af0b5d9bebdbc90078dfd41c58285c710.jpg)


The chief programmer team concept was formalized by Mills [Baker, 1972]. A classical chief programmer team, as described by Baker some 40 years ago, is shown in Figure 4.3 . It consisted of the chief programmer, who was assisted by the backup programmer, the programming secretary, and from one to three programmers. When necessary, the team was assisted by specialists in other areas, such as legal or fi nancial matters, or the job control language (JCL) statements used to give operating system commands to the mainframe computers of that era. The chief programmer was both a successful manager and a highly skilled programmer who did the architectural design and any critical or complex sections of the code. The other team members worked on the detailed design and the coding, under the direction of the chief programmer. As shown in Figure 4.3 , no lines of communication existed between the programmers; all interfacing issues were handled by the chief programmer. Finally, the chief programmer reviewed the work of the other team members, because the chief programmer was personally responsible for every line of code. 

The position of backup programmer was necessary only because the chief programmer was human and could therefore become ill, fall under a bus, or change jobs. Therefore, the backup programmer had to be as competent as the chief programmer in every respect and had to know as much about the project as the chief programmer. In addition, to free the chief programmer to concentrate on the architectural design, the backup programmer did black-box test case planning (Section 15.11) and other tasks independent of the design process. 

The word secretary has a number of meanings. A secretary can be a person who assists a busy executive by answering the telephone, typing correspondence, and so on. But when we talk about the American Secretary of State or the British Foreign Secretary, we refer to one of the most senior members of the Cabinet. The programming secretary was not a part-time clerical assistant but a highly skilled, well-paid, central member of a chief programmer team. The programming secretary was responsible for maintaining the project production library, the documentation of the project. This included source code listings, JCL, and test data. The programmers handed their source code to the secretary, who was responsible for its conversion to machine-readable form, compilation, linking, loading, execution, and running test cases. Programmers therefore did nothing but program. All other aspects of their work were handled by the programming secretary. (Because the programming secretary maintained the project production library, some organizations used the title librarian .) 

Recall that what is described here are Mills’s and Baker’s original ideas, dating back to 1971, when keypunches still were widely used. Coding no longer is done that way. Programmers now have their own terminals or workstations in which they enter their code, edit it, test it, and so on. A modern version of the classical chief programmer team is described in Section 4.4. 

## 4.3.1 The New York Times Project

The chief programmer team concept was fi rst used in 1971 by IBM to automate the clipping fi le (“morgue”) of The New York Times. The clipping fi le contains abstracts and full articles from The New York Times and other publications. Reporters and other members of the editorial staff use this information bank as a reference source. 

The facts of the project are astounding. For example, 83,000 lines of code (LOC) were implemented in 22 calendar months, an effort of 11 person-years. After the fi rst year, only the fi le maintenance system consisting of 12,000 LOC had been implemented. Most of the code was implemented in the last 6 months. Only 21 faults were detected in the fi rst 5 weeks of acceptance testing; only 25 further faults were detected in the fi rst year of operation. Principal programmers averaged one detected fault and 10,000 LOC per person-year. The fi le maintenance system, delivered 1 week after coding was completed, operated 20 months before a single fault was detected. Almost half the subprograms, usually 200 to 400 lines of PL/I, a language developed by IBM, were correct on the fi rst compilation [Baker, 1972]. 

Nevertheless, after this fantastic success, no comparable claims for the chief programmer team concept have been made. Yes, many successful projects have been carried out using chief programmer teams, but the fi gures reported, although satisfactory, are not as impressive as those obtained for The New York Times project. Why was The New York Times project such a success, and why have similar results not been obtained on other projects? 

One possible explanation is that this was a prestige project for IBM. It was the fi rst real trial for PL/I. An organization known for its superb software experts, IBM set up a team comprising what can only be described as its crème de la crème from one division. Second, technical backup was extremely strong. PL/I compiler writers were on hand to assist the programmers in every way they could, and JCL experts assisted with the job control language. A third possible explanation was the expertise of the chief programmer, F. Terry Baker. He is what is now called a superprogrammer , a programmer whose output is four or fi ve times that of an average good programmer. In addition, Baker is a superb manager and leader, and his skills, enthusiasm, and personality could be the reasons underlying the success of the project. 

If the chief programmer is competent, then the chief programmer team organization works well. Although the remarkable success of The New York Times project has not been repeated, many successful projects have employed variants of the chief programmer approach. The reason for the phrase variants of the approach is that the classical chief programmer team as described in [Baker, 1972] is impractical in many ways. 

## 4.3.2 Impracticality of the Classical Chief Programmer Team Approach

Consider the chief programmer, a combination of a highly skilled programmer and successful manager. Such individuals are diffi cult to fi nd due to a shortage of highly skilled programmers as well as a shortage of successful managers; and the job description of a chief programmer requires both abilities. Also, the qualities needed to be a highly skilled programmer appear to be different from those needed to be a successful manager; therefore, the chances of fi nding a chief programmer are small. 

If chief programmers are hard to fi nd, backup programmers are as rare as hen’s teeth. After all, the backup programmer is expected to be as good as the chief programmer but has to take a backseat and a lower salary while waiting for something to happen to the chief programmer. Few top programmers or top managers would accept such a role. 

A programming secretary also is diffi cult to fi nd. Software professionals are notorious for their aversion to paperwork, and the programming secretary is expected to do nothing but paperwork all day. 

Therefore, chief programmer teams, at least as proposed by Baker, are impractical to implement. Democratic teams also were shown to be impractical but for different reasons. Furthermore, neither technique seems to be able to handle products that require 20, let alone 120, programmers for the implementation workfl ow. What is needed is a way of organizing programming teams that uses the strengths of democratic teams and chief programmer teams and can be extended to the implementation of larger products. 

## 4.4 Beyond Chief Programmer and Democratic Teams

Democratic teams have a major strength: a positive attitude toward fi nding faults. A number of organizations use chief programmer teams in conjunction with code reviews (Section 6.2), creating a potential pitfall. The chief programmer is personally responsible for every line of code and, therefore, must be present during all code reviews. However, a chief programmer also is a manager and, as explained in Chapter 6 , reviews should not be used for any sort of performance appraisal. So, because the chief programmer is also the manager responsible for the primary evaluation of the team members, it is strongly inadvisable for that individual to be present at a code review. 

FIGURE 4.4 The structure of a modern programming team. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/71302274a313f2157cf7ead19c0dbacc32b281884db76c6227bd6eab5725b771.jpg)


The way out of this contradiction is to remove much of the managerial role from the chief programmer. After all, the diffi culty of fi nding one individual who is both a highly skilled programmer and successful manager has been pointed out. Instead, the chief programmer should be replaced by two individuals: a team leader in charge of the technical aspects of the team’s activities and a team manager responsible for all nontechnical managerial decisions. The structure of the resulting team is shown in Figure 4.4 . It is important to realize that this organizational structure does not violate the fundamental managerial principle that no employee should report to more than one manager. The areas of responsibility are clearly delineated. The team leader is responsible for only technical management. Consequently, budgetary and legal issues are not handled by the team leader nor are performance appraisals. On the other hand, the team leader has sole responsibility on technical issues. The team manager therefore has no right to promise, say, that the product will be delivered within 4 weeks; promises of that sort have to be made by the team leader. The team leader naturally participates in all code reviews; after all, he or she is personally responsible for every aspect of the code. At the same time, the team manager is not permitted at a review, because programmer performance appraisal is a function of the team manager. Instead, the team manager acquires knowledge of the technical skills of each programmer in the team during regularly scheduled team meetings. 

Before implementation begins, it is important to demarcate clearly those areas that appear to be the responsibility of both the team manager and the team leader. For example, consider the issue of annual leave. The situation can arise that the team manager approves a leave application because leave is a nontechnical issue, only to fi nd the application vetoed by the team leader because a deadline is approaching. The solution to this and related issues is for higher management to draw up a policy regarding areas that both the team manager and the team leader consider to be their responsibility. 

What about larger projects? This approach can be scaled up as shown in Figure 4.5 , which shows the technical managerial organizational structure; the nontechnical side is similarly organized. Implementation of the product as a whole is under the direction of the project leader. The programmers report to their team leaders, and the team leaders report to the project leader. For even larger products, additional levels can be added to the hierarchy. 

Another way of drawing on the best features of both democratic and chief programmer teams is to decentralize the decision-making process where appropriate. The resulting channels of communication are shown in Figure 4.6 . This scheme is useful for the sorts of problems for which the democratic approach is good, that is, in a research environment or whenever a hard problem requires the synergistic effect of group interaction for its solution. Notwithstanding the decentralization, the arrows from level to level still point downward; allowing programmers to dictate to the project leader can lead only to chaos. 


F I G U R E 4<sub>.</sub> 5 The technical managerial organizational structure for larger proj ects .


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/146398a67a6a5247f5032aca87f9761ca7e6eb3a34ec4a10dc41b281b416b3e3.jpg)



F I G U RE 4 6 Th<sub>e</sub> d<sub>ecen</sub>t<sub>ra</sub>li<sub>ze</sub>d d<sub>ec</sub>i<sub>s</sub>i<sub>on</sub>-<sub>ma</sub>ki<sub>ng vers</sub>i<sub>on o</sub>f th<sub>e</sub> t<sub>eam organ</sub>i<sub>za</sub>ti<sub>on o</sub>f Fi<sub>gure</sub> 4 5 <sub>s</sub>h<sub>ow</sub>i<sub>ng</sub> th<sub>e commun</sub>i<sub>ca</sub>ti<sub>on c</sub>h<sub>anne</sub>l<sub>s</sub> f<sub>or</sub> t<sub>ec</sub>h<sub>n</sub>i<sub>ca</sub>l <sup>m</sup>a<sup>n</sup>age<sup>m</sup>e<sup>nt</sup>


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/b4e98fcc92205e2ce965f5045fc7254e78dfd026b4e1964e37a6f38f5ea7014c.jpg)


## 4.5 Synchronize-and-Stabilize Teams

An alternative approach to team organization is the synchronize-and-stabilize team utilized by Microsoft [Cusumano and Selby, 1997]. Microsoft builds large products; for example, Windows 2000 consists of more than 30 million lines of code, built by over 3000 programmers and testers, reusing much of Windows NT 4.0 [Business Week Online, 1999]. Team organization is a vital aspect of the successful construction of a product of this size. 

The synchronize-and-stabilize life-cycle model was described in Section 2.9.6. The success of this model is largely a consequence of the way the teams are organized. Each of the three or four sequential builds of the synchronize-and-stabilize model is constructed by a number of small parallel teams led by a manager and consisting of between three and eight developers together with three to eight testers who work one-to-one with the developers. The team is provided the specifi cations of its overall task; individual team members then are given the freedom to design and implement their portions of that task as they wish. The reason that this does not rapidly devolve into hacker-induced chaos is the synchronization step performed each day: The partially completed components are tested and debugged on a daily basis. Accordingly, even though individual creativity and autonomy are nurtured, the individual components always work together. 

The strength of this approach is that, on the one hand, individual programmers are encouraged to be creative and innovative, a characteristic of a democratic team. On the other hand, the daily synchronization step ensures that the hundreds of developers work together toward a common goal without requiring the communication and coordination characteristic of a chief programmer team ( Figure 4.3 ). 

Microsoft developers must follow very few rules, but one of them is that they must adhere strictly to the time laid down to enter their code into the product database for that day’s synchronization. Cusumano and Selby [1997] liken this to telling children that they can do what they like all day but have to be in bed by 9 P.M. Another rule is that, if a developer’s code prevents the product from being compiled for that day’s synchronization, the problem must be fi xed immediately so that the rest of the team can test and debug that day’s work. 

Will use of the synchronize-and-stabilize model and associated team organization guarantee that every other software organization will be as successful as Microsoft? This is extremely unlikely. Microsoft, Inc., is more than just the synchronize-and-stabilize model. It is an organization consisting of a highly talented set of managers and software developers with an evolved group ethos. Merely using the synchronize-and-stabilize model does not magically turn an organization into another Microsoft. At the same time, the use of many of the features of the model in other organizations could lead to process improvement. On the other hand, it has been suggested that the synchronize-and-stabilize model is simply a way of allowing a group of hackers to develop large products and that Microsoft’s success is due to superb marketing, rather than quality software. 

## 4.6 Teams for Agile Processes

Section 2.9.5 gives an overview of agile processes [Beck et al., 2001]. In this section, we describe how teams are organized when agile processes are used. 

A somewhat unusual feature of agile processes is that all code is implemented by a team of two programmers sharing a single computer; this is referred to as pair programming [Williams, Kessler, Cunningham, and Jeffries, 2000]. The reasons for this approach include: 

• As explained in Section 2.9.5, pair programmers fi rst draw up test cases and then implement that piece of code ( task ). As explained in Section 6.6, it is highly inadvisable for a programmer to test his or her own code. Agile processes get around this problem by having one pair programmer in a team draw up the test cases for a task and the other pair programmer jointly implement the code using those test cases. 

• In a more conventional life-cycle model, when a developer leaves a project, all the knowledge accumulated by that developer leaves as well. In particular, the software on which that developer was working may not yet have been documented and may have to be redeveloped from scratch. In contrast, if one member of a pair programming team leaves, the other is suffi ciently knowledgeable to continue working on the same part of the software with a new pair programmer. Furthermore, the presence of the test cases assists in highlighting a fault, should the new team accidentally damage the software by making an ill-advised modifi cation. 

• Working closely in pairs enables a less experienced software professional to acquire the skills of the more experienced team member. 

• As mentioned in Section 2.9.5, all the computers used by the various pair teams are placed together in the middle of a large room. This promotes group ownership of code, a positive feature of egoless teams (Section 4.2). 

So, even though the idea of two programmers working together on the same computer may seem somewhat unusual, the practice can have distinct advantages. 

An interesting experiment on pair programming is described in [Arisholm, Gallis, Dybå, and Sjøberg, 2007]. A total of 295 professional programmers (99 individuals and 98 pairs) were hired to take part in a carefully conducted one-day experiment on pair programming. The subjects were required to perform several maintenance tasks on two Java software products, one simple and one complex. The pair programmers required 84 percent more effort to perform the tasks correctly. In light of this result, some software engineers may reconsider using pair programming, and, hence, agile processes. 

Furthermore, as stated in Section 2.9.5, an analysis of 15 published studies compared the effectiveness of individual and pair programming [Dybå et al., 2007] and came to the conclusion that it depends on both the programmer’s expertise and the complexity of the system and the specifi c tasks to be solved. Clearly, more research, preferably performed on large samples of professional programmers, needs to be conducted in this area. 

## 4.7 Open-Source Programming Teams

It is surprising that any open-source projects have succeeded, let alone that some of the most successful software products ever developed used the open-source life-cycle model. After all, open-source projects are generally staffed by teams of unpaid volunteers. They communicate asynchronously (i.e., via e-mail), with no team meetings and no managers— informality reigns in every respect. Furthermore, no specifi cations or designs exist; in fact, documentation of any kind is extremely rare, even in mature projects. But despite these virtually insurmountable obstacles, a small number of open-source projects such as Linux and Apache have attained the highest levels of success. 

Individuals volunteer to take part in an open-source project for two main reasons: for the sheer enjoyment of accomplishing a worthwhile task, or for the learning experience. 

• To attract volunteers to an open-source project and keep them interested, it is essential that at all times they view the project as “worthwhile.” Individuals are unlikely to devote a considerable portion of their spare time to a project unless they truly believe that the project will succeed and that the product will be widely utilized. Participants will start to drift away if they start viewing the project as futile. 

With regard to the second reason, many software professionals join an open-source project to gain skills in a technology that is new to them, such as a modern programming language or an operating system with which they are unfamiliar. They can then leverage the knowledge they gain to obtain a promotion within their own organization or acquire a better position in another organization. After all, employers frequently view experience gained working on a large, successful open-source project as more desirable than acquiring additional academic qualifi cations. Conversely, there is no point in devoting months of hard work to a project that ultimately fails. 

In other words, unless a project is viewed at all times as a winner, it will not attract and retain volunteers to work on that project. Furthermore, the members of the open-source team must at all times feel that they are making a contribution. For all these reasons, it is essential that the key individual behind an open-source project be a superb motivator. Unless this is the case, the project is doomed to inevitable failure. 

Another prerequisite for successful open-source development is the skills of the team members. As explained in detail in Section 9.2, large differences in skill levels have been observed between programmers. Bearing in mind the obstacles to successful open-source software production listed in the fi rst paragraph of this section, there is virtually no way that an open-source project can succeed unless the members of the core group (Section 2.9.4) are top-caliber individuals with fi nely honed skills of the highest order. Such top-class individuals will thrive in almost any environment, including one as unstructured as an open-source team 

In other words, an open-source project succeeds because of the nature of the target prod uct, the personality of the instigator, and the talents of the members of the core group. The way that a successful open-source team is organized is essentially irrelevant. 

## 4.8 People Capability Maturity Model

The people capability maturity model (P–CMM) describes best practices for managing and developing the workforce of an organization [Curtis, Hefl ey, and Miller, 2002]. As with the software capability maturity model, SW–CMM (Section 3.13), an organization progresses through fi ve maturity levels with the aim of continuously improving individual skills and engendering effective teams. 

Every maturity level has its own key process areas (KPAs), each of which needs to be addressed satisfactorily before an organization can be deemed to have attained that maturity level. For example, for level 2, the managed level, the KPAs are staffi ng, communication and coordination, work environment, performance management, training and development, and compensation. In contrast, the KPAs for level 5, the optimizing level, are continuous capability improvement, organizational performance alignment, and continuous workforce innovation. 

The SW–CMM is a framework for improving an organization’s software process—no specifi c process or methodology is recommended. In the same way, the P–CMM is a framework for improving an organization’s processes for managing and developing its workforce, and no specifi c approach to team organization is put forward. 

## 4.9 Choosing an Appropriate Team Organization

A comparison of the various types of team organization appears in Figure 4.7 , which also shows the section in which each team organization is described. Unfortunately, no one solution solves the problem of programming team organization or, by extension, the 

FIGURE 4.7 Comparison of approaches to team organization and the section in this chapter in which each is described. 

<table><tr><td>Team Organization</td><td>Strengths</td><td>Weaknesses</td></tr><tr><td>Democratic teams (Section 4.2)</td><td>High-quality code as consequence of positive attitude to finding faultsParticularly good with hard problems</td><td>Experienced staff resent their code being appraised by beginnersCannot be externally imposed</td></tr><tr><td>Classical chief programmer teams (Section 4.3)</td><td>Major success of The New York Times project</td><td>Impractical</td></tr><tr><td>Modified chief programmer teams (Section 4.3.1)</td><td>Many successes</td><td>No successes comparable to The New York Times project</td></tr><tr><td>Modern hierarchical programming teams (Section 4.4)</td><td>Team manager/team leader structure obviates need for chief programmerScales upSupports decentralization when needed</td><td>Problems can arise unless areas of responsibility of the team manager and the team leader are clearly delineated</td></tr><tr><td>Synchronize-and-stabilize teams (Section 4.5)</td><td>Encourages creativityEnsures that a huge number of developers can work toward a common goal</td><td>No evidence so far that this method can be utilized outside Microsoft</td></tr><tr><td>Agile process teams (Section 4.6)</td><td>Programmers do not test their own codeKnowledge is not lost if one programmer leavesLess-experienced programmers can learn from othersGroup ownership of code</td><td>Still too little evidence regarding efficacy</td></tr><tr><td>Open-source teams (Section 4.7)</td><td>A few projects are extremely successful</td><td>Narrowly applicableMust be led by a superb motivatorRequires top-caliber participants</td></tr></table>

problem of organizing teams for all the other workfl ows. The optimal way of organizing a team depends on the product to be built, previous experience with various team structures, and most important, the culture of the organization. For example, if senior management is uncomfortable with decentralized decision making, then it will not be implemented. 

In practice, most teams are currently organized as described in Section 4.4. That is, some variant of the chief programmer team is the usual practice. 

Not much research has been done on software development team organization, and many of the generally accepted principles are based on research on group dynamics in general and not on software development teams. Even when studies on software teams have been conducted, the sample sizes have generally been small, so the results have not been convincing. 

Until experimental results on team organization have been obtained within the software industry, it will not be easy to determine the optimal team organization for a specifi c product. 

<table><tr><td>Chapter Review</td><td>The issue of team organization (Section 4.1) is approached by first considering democratic teams (Section 4.2) and chief programmer teams (Section 4.3). The success of The New York Times project (Section 4.3.1) is contrasted with the impracticality of classic chief programmer teams (Section 4.3.2). A team organization that uses the strengths of both approaches is suggested in Section 4.4. Synchronize-and-stabilize teams (used by Microsoft) are described in Section 4.5. Teams for agile processes are discussed in Section 4.6 and for open-source software in Section 4.7. The people capability maturity model (P-CMM) is described in Section 4.8. Finally, Section 4.9 describes the factors involved in choosing the optimal team organization for a given project.</td></tr><tr><td>For Further Reading</td><td>The classic works on team organization are [Weinberg, 1971], [Baker, 1972], and [Brooks, 1975]. Newer books on the subject include [DeMarco and Lister, 1987] and [Cusumano and Selby, 1995]. An interesting description of how team interactions evolve is found in [Mackey, 1999]. Chapter 11 of [Royce, 1998] contains useful information on the roles played by team members. A promising approach is the use of personality type analysis in selecting team members; see, for example, [Gorla and Lam, 2004].Synchronize-and-stabilize teams are outlined in [Cusumano and Selby, 1997] and described in detail in [Cusumano and Selby, 1995]. Extreme programming teams are described in [Beck, 2000]. The May-June 2003 issue of IEEE Software includes a number of papers on extreme programming, especially [Reifer, 2003] and [Murru, Deias, and Mugheddue, 2003].Views on agile processes are expressed in [Boehm, 2002] and [DeMarco and Boehm, 2002], and in the May-June 2005 issue of IEEE Software. Williams, Kessler, Cunningham, and Jeffries [2000] describes an experiment on pair programming, one component of extreme programming. Pair programming is evaluated in [Drobka, Noftz, and Raghu, 2004], [Flor, 2006], and [Lui, Chan, and Nosek, 2008]. The results of [Arisholm, Gallis, Dybå, and Sjøberg, 2007] regarding the possible benefits of pair programming should be studied in detail.P-CMM is described in [Curtis, Hefley, and Miller, 2002]. Globally distributed (remote) pair programming is put forward in [Flor, 2006].</td></tr></table>

## Key Terms

<table><tr><td>backup programmer 111</td><td>hierarchy 111</td><td>specialization 111</td></tr><tr><td>Brooks&#x27;s Law 108</td><td>key process area (KPA) 119</td><td>superprogrammer 113</td></tr><tr><td>chief programmer 111</td><td>librarian 112</td><td>task 118</td></tr><tr><td>chief programmer team 110</td><td>pair programming 118</td><td>team 107</td></tr><tr><td>democratic team 109</td><td>programmer 112</td><td>team leader 114</td></tr><tr><td>egoless programming 109</td><td>programming secretary 112</td><td>team manager 114</td></tr></table>

## Problems

4.1 How would you organize a team to develop a payroll project? Explain your answer. 

4.2 How would you organize a team for developing state-of-the-art military communications software? Explain your answer. 

4.3 State Brooks’s Law. Explain why it holds. 

4.4 You have just started a new software company. All your employees are recent college graduates; this is their fi rst programming job. Is it possible to implement democratic teams in your organization, and if so, how? 

4.5 A student programming team is organized as a democratic team. What can be deduced about the students in the team? 

4.6 A student programming team is organized as a chief programming team. What can be deduced about the students in the team? 

4.7 To compare two different team organizations, $\mathrm { T O } _ { 1 }$ and $\mathrm { T O } _ { 2 } ,$ within a large software company, the following experiment is proposed. The same software product will be built by two different teams, one organized according to $\mathrm { T O } _ { 1 }$ and the other according to $\mathrm { T O } _ { 2 } .$ . The company estimates that each team will take about 18 months to build the product. Give three reasons why this experiment is impractical and unlikely to yield meaningful results. 

4.8 The company you own has just taken over a smaller competitor, and you discover that one of their programmers is a superprogrammer. How do you ensure that she does not leave and take a job in another company? 

4.9 Why do teams for agile processes have to share a computer? 

4.10 What are the differences between a democratic team and an open-source team? 

4.11 How would you organize an open-source team? 

4.12 Would you like to work in an organization that uses synchronize-and-stabilize teams? Explain your answer. 

4.13 Which team organizations conform to P–CMM? 

4.14 You are the vice president for software development in a large company. How would you implement P–CMM in your company? 

4.15 (Term Project) What type of team organization would be appropriate for developing the Chocoholics Anonymous product described in Appendix A? 

4.16 (Readings in Software Engineering) Your instructor will distribute copies of [Arisholm, Gallis, Dybå, and Sjøberg, 2007]. What are the implications of this paper for agile processes? 

## References



[Arisholm, Gallis, Dybå, and Sjøberg, 2007] E. ARISHOLM, H. GALLIS, T. DYBÅ, AND D. I. K. SJØBERG, “Evaluating Pair Programming with Respect to System Complexity and Programmer Expertise,” IEEE Transactions on Software Engineering 33 (February 2007), pp. 65–86. 





[Baker, 1972] F. T. BAKER, “Chief Programmer Team Management of Production Programming,” IBM Systems Journal 11 (No. 1, 1972), pp. 56–73. 





[Beck, 2000] K. BECK, Extreme Programming Explained: Embrace Change, Addison-Wesley Longman, Reading, MA, 2000. 





[Beck et al., 2001] K. BECK, M. BEEDLE, A. COCKBURN, W. CUNNINGHAM, M. FOWLER, J. GRENNING, J. HIGHSMITH, A. HUNT, R. JEFFRIES, J. KERN, B. MARICK, R. C. MARTIN, S. MELLOR, K. SCHWABER, J. SUTHERLAND, D. THOMAS, AND A. VAN BENNEKUM, “Manifesto for Agile Software Development,” agilemanifesto.org, 2001. 





[Boehm, 2002] B. W. BOEHM, “Get Ready for Agile Methods, with Care,” IEEE Computer 35 (January 2002), pp. 64–69. 





[Brooks, 1975] F. P. BROOKS, JR., The Mythical Man-Month: Essays in Software Engineering, Addison-Wesley, Reading, MA, 1975; Twentieth Anniversary Edition, Addison-Wesley, Reading, MA, 1995. 





[Business Week Online, 1999] Business Week Online , www.businessweek.com/1999/99_08/ b3617025.htm , February 2, 1999. 





[Curtis, Hefl ey, and Miller, 2002] B. CURTIS, W. E. HEFLEY, AND S. A. MILLER, The People Capability Maturity Model: Guidelines for Improving the Workforce , Addison-Wesley, Reading, MA, 2002. 





[Cusumano and Selby, 1995] M. A. CUSUMANO AND R. W. SELBY, Microsoft Secrets: How the World’s Most Powerful Software Company Creates Technology, Shapes Markets, and Manages People , The Free Press/Simon and Schuster, New York, 1995. 





[Cusumano and Selby, 1997] M. A. CUSUMANO AND R. W. SELBY, “How Microsoft Builds Software,” Communications of the ACM 40 (June 1997), pp. 53–61. 





[DeMarco and Boehm, 2002] T. DEMARCO AND B. BOEHM, “The Agile Methods Fray,” IEEE Computer 35 (June 2002), pp. 90–92. 





[DeMarco and Lister, 1987] T. DEMARCO AND T. LISTER, Peopleware: Productive Projects and Teams, Dorset House, New York, 1987. 





[Drobka, Noftz, and Raghu, 2004] J. DROBKA, D. NOFTZ, AND R. RAGHU, “Piloting XP on Four Mission-Critical Projects,” IEEE Software 21 (November–December 2004), pp. 70–75. 





[Dybå et al., 2007] T. DYBÅ, E. ARISHOLM, D. I. K. SJØBERG, J. E. HANNAY, AND F. SHULL, “Are Two Heads Better than One? On the Effectiveness of Pair Programming,” IEEE Software 24 (November– December 2007), pp. 12–15. 





[Flor, 2006] N. V. FLOR. “Globally Distributed Software Development and Pair Programming,” Communications of the ACM 49 (October 2006), pp. 57–58. 





[Gorla and Lam, 2004] N. GORLA AND Y. W. LAM, “Who Should Work with Whom?” Communications of the ACM 47 (June 2004), pp. 79–82. 





[Lui, Chan, and Nosek, 2008] K. M. LUI, K. C. C. CHAN, AND J. T. NOSEK, “The Effect of Pairs in Program Design Tasks,” IEEE Transactions on Software Engineering 34 (March–April 2008), pp. 197–211. 





[Mackey, 1999] K. MACKEY, “Stages of Team Development,” IEEE Software 16 (July–August 1999), pp. 90–91. 





[Mantei, 1981] M. M , “The Effect of Programming Team Structures on Programming Tasks,” Communications of the ACM 24 (March 1981), pp. 106–13. 





[Murru, Deias, and Mugheddue, 2003] O. MURRU, R. DEIAS, AND G. MUGHEDDUE, “Assessing XP at a European Internet Company,” IEEE Software 20 (May–June 2003), pp. 37–43. 





[Reifer, 2003] D. REIFER, “XP and the CMM,” IEEE Software 20 (May–June 2003), pp. 14–15. 





[Royce, 1998] W. ROYCE, Software Project Management: A Unifi ed Framework , Addison-Wesley, Reading, MA, 1998. 





[Weinberg, 1971] G. M. WEINBERG, The Psychology of Computer Programming , Van Nostrand Reinhold, New York, 1971. 





[Williams, Kessler, Cunningham, and Jeffries, 2000] L. WILLIAMS, R. R. KESSLER, W. CUNNINGHAM, AND R. JEFFRIES, “Strengthening the Case for Pair Programming,” IEEE Software 17 (July–August 2000), pp. 19–25. 



# The Tools of the Trade

Learning Objectives 

After studying this chapter, you should be able to 

• Appreciate the importance of stepwise refi nement and utilize it in practice. 

• Understand divide-and-conquer. 

• Appreciate the importance of separation of concerns. 

• Apply cost–benefi t analysis. 

• Select appropriate software metrics. 

• Discuss the scope and taxonomy of CASE. 

• Describe version-control tools, confi guration-control tools, and build tools. 

• Understand the importance of CASE. 

Software engineers need two types of tools. First are the analytical tools used in software development, such as stepwise refi nement and cost–benefi t analysis. Then come the software tools, that is, products that assist the teams of software engineers in developing and maintaining software. These usually are termed CASE tools (CASE is an acronym for Computer-Aided Software Engineering). This chapter is devoted to these two types of tools of the trade, fi rst theoretical (analytical) tools and then software (CASE) tools. We begin with stepwise refi nement. 

## 5.1 Stepwise Refi nement

Stepwise refi nement, introduced in Section 2.5, is a problem-solving technique that underlies many software engineering techniques. Stepwise refi nement can be defi ned as a means to postpone decisions on details until as late as possible to concentrate on the important issues. As a consequence of Miller’s Law (Section 2.5), we can concentrate on only approximately seven chunks (units of information) at a time. Accordingly, we use stepwise refi nement to defer nonessential decisions until later while focusing on the key issues. 

As will be seen during the course of this book, stepwise refi nement underlies many analysis techniques, design and implementation techniques, and even testing and integration techniques. Stepwise refi nement is of critical importance within the context of the objectoriented paradigm, because the underlying life-cycle model is iterative and incremental. 

The following mini case study illustrates how stepwise refi nement can be used in the design of a product. 

Mini ase Study C 

5.1.1 

## Stepwise Refi nement Mini Case Study

The mini case study presented in this section may seem almost trivial in that it involves updating a sequential master fi le, a common operation in many application areas. This choice of a simple, familiar problem is to enable you to concentrate on stepwise refi nement rather than on the application domain. 

Design a product to update the sequential master fi le containing name and address data for the monthly magazine True Life Software Disasters . There are three types of transactions: insertions, modifi cations, and deletions, with transaction codes 1, 2, and 3, respectively. The transaction types are 

Type 1: INSERT (a new subscriber into the master fi le) 

Type 2: MODIFY (an existing subscriber record) 

Type 3: DELETE (an existing subscriber record) 

Transactions are sorted into alphabetical order by name of subscriber. If more than one transaction is performed for a given subscriber, the transactions for that subscriber are sorted so that insertions occur before modifi cations and modifi cations before deletions. 

The fi rst step in designing a solution is to set up a typical fi le of input transactions, such as that shown in Figure 5.1 . The fi le contains fi ve records: DELETE Brown, INSERT Harris, Jones, Jones, and Smith. (It is not unusual to perform both a modifi cation and a deletion of the same subscriber in one run.) 


FIGURE 5.1 Input transaction records for the sequential master fi le update.


<table><tr><td>Transaction Type</td><td>Name</td><td>Address</td></tr><tr><td>3</td><td>Brown</td><td></td></tr><tr><td>1</td><td>Harris</td><td>2 Oak Lane, Townsville</td></tr><tr><td>2</td><td>Jones</td><td>Box 345, Tarrytown</td></tr><tr><td>3</td><td>Jones</td><td></td></tr><tr><td>1</td><td>Smith</td><td>1304 Elm Avenue, Oak City</td></tr></table>

FIGURE 5.2 

A representation of the sequential master fi le update. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/c7cef757d862d35f2a3d2d9bc1f118cea20dcb4ecccbbab2ddb10a14521117b8.jpg)



FIGURE 5.3 First refi nement of the design.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/183dd3b9781e16bdfece2f52141d2fe389a842d193093866a543e4befb130fdc.jpg)


The problem may be represented as shown in Figure 5.2 . There are two input fi les: 

1. Old master fi le name and address record 

2. Transaction fi le and three output fi les: 

3. New master fi le name and address records 

4. Exception report 

5. Summary and end-of-job message 

To begin the design process, the starting point is the single box update master fi le shown in Figure 5.3 . This box can be decomposed into three boxes, input, process, and output. The assumption is that, when process requires a record, our level of competence is such that the correct record can be produced at the right time. Similarly, we are capable of writing the correct record to the correct fi le at the right time. Therefore, the technique is to separate out the input and output aspects and concentrate on the process. What is this process? To determine what it does, consider the example shown in Figure 5.4 . The key of the fi rst transaction record (Brown) is compared with the key of the fi rst old master fi le record (Abel). Because Brown comes after Abel, the Abel record is written to the new master fi le, and the next old master fi le record (Brown) is read. In this case, the key of the transaction record matches the key of the old master fi le record, and because the transaction type is 3 (DELETE), the Brown record must be deleted. This is implemented by not copying the Brown record onto the new master fi le. The next transaction record (Harris) and old master fi le record (James) are read, overwriting the Brown records in their respective buffers. Harris comes before James and, therefore, is inserted into the new master fi le; the next transaction record (Jones) is read. Because Jones comes after James, the James record is written to the new master fi le, and the next old master fi le record is read; this is Jones. As can be seen from the transaction fi le, the Jones record is to be modifi ed and then deleted, so the next transaction record (Smith) and the next old master fi le record (also Smith) are read. Unfortunately, the transaction type is 1 (INSERT), but Smith already is in the master fi le. So there is an error of some sort in the data, and the Smith record is written to the exception report. To be more precise, the Smith transaction record is written to the exception report, and the Smith old master fi le record is written to the new master fi le. 

<table><tr><td>Transaction file</td></tr><tr><td>3 Brown</td></tr><tr><td>1 Harris</td></tr><tr><td>2 Jones</td></tr><tr><td>3 Jones</td></tr><tr><td>1 Smith</td></tr></table>


FIGURE 5.4 The transaction fi le, old master fi le, new master fi le, and exception report.



FIGURE 5.5 A diagrammatic representation of the process.


<table><tr><td>Transaction record key= old master file record key</td><td>1. INSERT: Print error message2. MODIFY: Change master file record3. DELETE: *Delete master file record</td></tr><tr><td>Transaction record key&gt; old master file record key</td><td>Copy old master file record to new master file</td></tr><tr><td>Transaction record key&lt; old master file record key</td><td>1. INSERT: Write transaction record to new master file2. MODIFY: Print error message3. DELETE: Print error message</td></tr></table>


* Deletion of a master fi le record is implemented by not copying the record onto the new master fi le.


Now that the process is understood, it may be represented as in Figure 5.5 . Next, the process box of Figure 5.3 may be refi ned, resulting in the second refi nement shown in Figure 5.6 . The dashed lines to the input and output boxes denote that decisions as to how to handle input and output have been deferred until a later refi nement. The remainder of the fi gure is the fl owchart of the process, or rather, an early refi nement of the fl owchart. As already pointed out, input and output have been deferred. Also, there is no provision for an end-of-fi le condition, nor has it yet been specifi ed what to do when an error condition is encountered. The strength of stepwise refi nement is that these and similar problems can be solved in later refi nements. 


FIGURE 5.6 The second refi nement of the design.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/38388e99d7015e40c7bc0289e26ad73ab2ce036a7d573e8ada8d670743580b27.jpg)


The next step is to refi ne the input and output boxes of Figure 5.6 , resulting in Figure 5.7 . End-of-fi le conditions still have not been handled nor has the writing of the end-of-job message. Again, these can be done at a later iteration. What is critical, however, is that the design of Figure 5.7 has a major fault. To see this, consider the situation with regard to the data of Figure 5.4 when the current transaction is 2 Jones, that is, modify Jones, and the current old master fi le record is Jones. In the design of Figure 5.7 , because the key of the transaction record is the same as the key of the old master fi le record, the leftmost path is followed to the test transaction type decision box. Because the current transaction type is MODIFY, the old master fi le record is modifi ed and written to the new master fi le, and the next transaction record is read. This record is 3 Jones, that is, delete Jones. But the modifi ed Jones record has already been written to the new master fi le. 

The reader may wonder why an incorrect refi nement is deliberately presented. The point is that, when using stepwise refi nement, it is necessary to check each successive refi nement before proceeding to the next. If a particular refi nement turns out to be faulty, it is not necessary to restart the process from the beginning but merely to go back to the previous refi nement and proceed from there. In this instance, the second refi nement ( Figure 5.6 ) is correct, so it may be used as the basis for another attempt at a third refi nement. This time, the design uses level-1 lookahead ; that is, a transaction record is processed only after the next transaction record has been analyzed. The details are left as an exercise; see Problem 5.1. 


FIGURE 5.7 The third refi nement of the design (the design has a major fault).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/677b85729ad141dc678c101d8762703c5decedccb129590c42fd560f963acc91.jpg)


In the fourth refi nement, details that have been ignored up to now, such as opening and closing fi les, have to be introduced. With stepwise refi nement, such details are handled last, after the logic of the design has been fully developed. Obviously, it is impossible to execute the product without opening and closing fi les. However, what is important here is the stage in the design process at which such details as fi le openings and closings are handled. While the design is being developed, the seven or so chunks on which the designer can concentrate at once should not include details like open ing and closing fi les. File openings and closings have nothing to do with the design itself; they are merely implementation details that are part of any design. However, in later refi nements, opening and closing fi les becomes vital. In other words, stepwise refi nement can be considered a technique for setting the priorities of the various problems that have to be solved within a workfl ow. Stepwise refi nement ensures that every problem is solved and each is solved at the appropriate time, without having to handle more than 7 ± 2 chunks at any one time. 

The term stepwise refi nement was fi rst introduced by Wirth [1971]. In the preceding mini case study, stepwise refi nement was applied to a fl owchart, whereas Wirth applied the technique to pseudocode. The specifi c representation to which stepwise refi nement is applied is not important; stepwise refi nement is a general technique that can be used for every workfl ow and with almost every representation. 

Miller’s Law is a fundamental restriction on the mental powers of humans. Because we cannot fi ght our nature, we must live with it, accepting our limitations and doing the best we can under the circumstances. 

The power of stepwise refi nement is that it helps the software engineer to concentrate on the relevant aspects of the current development task and ignore details that, although essential in the overall scheme, need not be considered, and in fact should be ignored, until later. Unlike divide-and-conquer (Section 5.3), in which the problem as a whole is decomposed into subproblems of essentially equal importance, in stepwise refi nement, the importance of a particular aspect of the problem changes from refi nement to refi nement. Initially, a particular issue may be irrelevant, but later that same issue is of critical importance. The challenge with stepwise refi nement is deciding which issues must be handled in the current refi nement and which can be postponed until a later refi nement. 

Like stepwise refi nement, cost–benefi t analysis is a fundamental theoretical software engineering technique used throughout the software life cycle. This technique is described in Section 5.2. 

## 5.2 Cost–Benefi t Analysis

One way of determining whether a possible course of action would be profi table is to compare estimated future benefi ts against projected future costs. This is termed cost–benefi t analysis . As an example of cost–benefi t analysis within the computer context, consider how Krag Central Electric Company (KCEC) decided in 1965 whether or not to computerize its billing system. Billing was being done manually by 80 clerks who mailed bills every 2 months to KCEC customers. Computerization would require KCEC to buy or lease the necessary software and hardware, including data-capture equipment for recording the input data on punch cards or magnetic tape. 

One advantage of computerization would be that bills could be mailed monthly instead of every 2 months, improving the company’s cash fl ow considerably. Furthermore, 

FIGURE 5.8 Cost–benefi t analysis data for KCEC. 

<table><tr><td colspan="2">Benefits</td><td colspan="2">Costs</td></tr><tr><td>Salary savings (7 years)</td><td>1,575,000</td><td>Hardware and software (7 years)</td><td>1,250,000</td></tr><tr><td>Improved cash flow (7 years)</td><td>875,000</td><td>Conversion cost (first year only)</td><td>350,000</td></tr><tr><td></td><td></td><td>Explanations to customers (first year only)</td><td>125,000</td></tr><tr><td>Total benefits</td><td>$2,450,000</td><td>Total costs</td><td>$1,725,000</td></tr></table>

the 80 billing clerks would be replaced by 11 data-capture clerks. As shown in Figure 5.8 , salary savings over the next 7 years were estimated to be $1.575 million, and improved cash fl ow was projected to be worth $875,000. The total benefi ts therefore were estimated at $2.45 million. On the other hand, a complete data processing department would have to be set up, staffed by well-paid computer professionals. Over a 7-year period, costs were estimated as follows: The cost of hardware and software, including postdelivery maintenance, was estimated to be $1.25 million. In the fi rst year, there would be a conversion cost of $350,000, and the cost of explaining the new system to customers was estimated at an additional $125,000. Total costs were estimated at $1.725 million, about $750,000 less than the estimated benefi ts for that 7-year period. KCEC immediately decided to computerize. 

Cost–benefi t analysis is not always straightforward. On the one hand, a management consultant can estimate salary savings, an accountant can project cash fl ow improvements, net present value (NPV) can be used to handle the change in the cost of money, and a software engineering consultant can estimate the costs of hardware, software, and conversion. But how are we to determine the cost of dealing with customers trying to adjust to computerization? How can we measure the benefi ts of inoculating an entire population against measles? And how can we make estimates regarding a market window, that is, the benefi t of being fi rst on the market with a new product or the cost of not being the fi rst (and hence losing customers)? 

The point is that tangible benefi ts are easy to measure, but intangible benefi ts can be hard to quantify directly. A practical way of assigning a dollar value to intangible benefi ts is to make assumptions . These assumptions always must be stated in conjunction with the resulting estimates of the benefi ts. After all, managers have to make decisions. If no data are available, then making assumptions from which such data can be determined usually is the best that can be done under the circumstances. This approach has the further advantage that, if someone else reviewing the data and the underlying assumptions can come up with better assumptions, then better data can be produced and the associated intangible benefi ts can be computed more accurately. The same technique can be used for intangible costs. 

Cost–benefi t analysis is a fundamental technique in deciding whether a client should computerize his or her business, and if so, in what way. The costs and benefi ts of various alternative strategies are compared. For example, a product for storing the results of drug trials can be implemented in a number of different ways, including fl at fi les and various database management systems. For each possible strategy, the costs and benefi ts are computed, and the one for which the difference between benefi ts and costs is the largest is selected as the optimal strategy. 

# Just in Case You Wanted to Know

The phrase divide and conquer has been widely attributed to Phillip II of Macedon (382–336 . . ). Unfortunately, there is no evidence that he said it. Then, despite the vigorous claims on the Internet, the phrase divide et impera (“divide and rule”) does not appear in Book VII of Caesar’s Commentarii de Bello Gallico (“Commentaries on the Gallic War”), nor, for that matter, anywhere else in the works of Julius Caesar (100–44 B.C.E.). Also, notwithstanding equally strong assertions, it also does not appear in the works of Vegetius (Publius Flavius Vegetius Renatus, who lived in the fourth century C.E.). The phrase has been widely attributed to the diplomat and political philosopher Niccolò Machiavelli (1469–1527), but it does not appear anywhere in his writings, either. 

In fact, the phrase probably fi rst appeared only about 330 years ago, in a collection of commentaries on Tacitus [Publius (or Gaius) Cornelius Tacitus, the Roman historian, ca. 56–ca. 117 C.E.] by Traiano Boccalini, an Italian satirist who lived from 1556–1613. The book was published posthumously in 1677. It was entitled Comentarii di Traiano Boccalini Romano sopra Cornelio Tacito, Come Sono Stati Lasciati dall’ Autore. Opera Non Ancora Stampata & Grandemente Desiderata da Tutti li Virtuosi (“Commentaries by Traiano Boccalini, of Rome, on Cornelius Tacitus, as left by the author. The work has not previously been printed and is greatly desired by all virtuous men”). 

## 5.3 Divide-and-Conquer

Divide-and-conquer is probably the oldest analytical tool in this book (see Just in Case You Wanted to Know Box 5.1). The idea is to break up a large problem that is hard to solve into smaller subproblems that hopefully will be easier to solve. 

This approach is used in the Unifi ed Process to handle a large, complex system. As explained in Section 14.9, during the analysis workfl ow we partition the software product into analysis packages. Each package consists of a set of related classes that can be implemented as a single unit. 

The technique of divide-and-conquer is carried forward to the design workfl ow. Here, the objective is to break up the upcoming implementation workfl ow into manageable pieces, termed subsystems. The subsystems are then implemented in the chosen programming language(s). 

A problem with divide-and-conquer is that the approach does not tell us how to break up a software product into appropriate smaller components 

The next theoretical tool is separation of concerns. 

## 5.4 Separation of Concerns

Separation of concerns was first put forward by Dijkstra in a 1974 paper, which was republished in [Dijkstra, 1982]. It is the process of breaking a software product into components that overlap as little as possible with regard to functionality. When separation of concerns is achieved, regression faults are minimized; if functionality is localized to a single component, changing that functionality cannot affect any other component. 

Also, when concerns are adequately separated, components can be reused in future products. Conversely, suppose that object A contains an invocation of a method of object B. In this situation, object A cannot be reused without reusing object B as well. To maximize reuse, it is important to minimize interactions between components. 

In Chapter 7 , we discuss composite/structured design [Stevens, Myers, and Constantine, 1974], a technique for achieving modularization of a software product with maximum interaction within each module (“high cohesion”) and minimum interaction between modules (“low coupling”). Both high cohesion and low coupling are instances of separation of concerns. 

In Section 1.9, information hiding (or physical independence) was discussed. This, too, is an instance of separation of concerns; isolating implementation details within a component minimizes the interaction between that component and the rest of the software product. Information hiding is described in greater detail in Section 7.6. 

Encapsulation or conceptual independence was also discussed in Section 1.9. Encapsulation is yet another instance of separation of concerns. Data encapsulation is discussed in Section 7.4. 

The three-tier architecture of Section 8.5.4 is yet another instance of separation of concerns. So is the model-view-controller (MVC) architecture pattern, also in that section. 

It is clear that separation of concerns underlies much of software engineering. Sometimes, however, it is not possible to separate concerns adequately. One way of dealing with this situation is to use aspect-oriented programming, described in Section 18.1. 

The fi nal theoretical tool described in this chapter is software metrics. 

## 5.5 Software Metrics

As explained in Section 3.13, without measurements (or metrics ) it is impossible to detect problems early in the software process, before they get out of hand. Metrics therefore can serve as an early warning system for potential problems. A wide variety of metrics can be used. For example, lines of code (LOC) is one way of measuring the size of a product (see Section 9.2.1). If LOC measurements are taken at regular intervals, they provide a measure of how fast the project is progressing. In addition, the number of faults per 1000 lines of code is a measure of software quality. After all, it is of little use if a programmer consistently turns out 2000 lines of code a month but half of them have to be thrown away because they are unacceptable. Accordingly, LOC in isolation is not a meaningful metric. 

Once the product has been installed on the client’s computer, a metric such as mean time between failures provides management an indication of its reliability. If a certain product fails every other day, its quality is clearly lower than that of a similar product that on average runs for 9 months without a failure. 

Certain metrics can be applied throughout the software process. For example, for each workfl ow, we can measure the effort in person-months (1 person-month is the amount of work done by one person in 1 month). Staff turnover is another important metric. High turnover adversely affects current projects because it takes time for a new employee to learn the relevant facts about the project (see Section 4.1). In addition, new employees may have to be trained in aspects of the software process; if new employees are less educated in software engineering than the individuals they replace, then the process as a whole may suffer. Of course, cost is an essential metric that must also be monitored continually throughout the entire process. 

A number of different metrics are described in this book. Some are product metrics ; they measure some aspect of the product itself, such as its size or its reliability. Others are process metrics used by the developers to deduce information about the software process. A typical metric of this kind is the effi ciency of fault detection during development, that is, the ratio of the number of faults detected during development to the total number of faults detected in the product over its lifetime. 

Many metrics are specifi c to a given workfl ow. For example, lines of code cannot be used before the implementation workfl ow, and the number of faults detected per hour in reviewing specifi cations is relevant to only the analysis workfl ow. In subsequent chapters describing each of the various workfl ows of the software process, the metrics relevant to that workfl ow are discussed. 

A cost is involved in gathering the data needed to compute the values of metrics. Even if the data gathering is fully automated, the CASE tool (Section 5.6) that accumulates the required information is not free, and interpreting the output from the tool consumes human resources. Bearing in mind that hundreds (if not thousands) of metrics have been put forward, an obvious question is, What should a software organization measure? There are fi ve essential, fundamental metrics: 

1. Size (in lines of code or, better, in a more meaningful metric, such as those of Section 9.2.1). 

2. Cost (in dollars). 

3. Duration (in months). 

4. Effort (in person-months). 

5. Quality (number of faults detected). 

Each of these metrics must be measured by workfl ow (metrics for the specifi cation, analysis, design, and implementation workfl ows are described in Sections 11.17, 13.21, 14.15, and 15.26, respectively). On the basis of the data from these fundamental metrics, management can identify problems within the software organization, such as high fault rates during the design workfl ow or code output that is well below the industry average. Once problem areas have been highlighted, a strategy to correct these problems can be considered. To monitor the success of this strategy, more-detailed metrics can be introduced. For example, it may be deemed appropriate to collect data on the fault rates of each programmer or to conduct a survey of user satisfaction. Consequently, in addition to the fi ve fundamental metrics, more-detailed data gathering and analysis should be performed only toward a specifi c objective. 

Finally, one aspect of metrics is still fairly controversial. Questions have been raised as to the validity of some popular metrics; these issues are discussed in Section 15.13.2. Although it is agreed that we cannot control the software process unless we can measure it, there is still some disagreement as to precisely what should be measured. 

We now turn from theoretical tools to software (CASE) tools. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/4a3d63e5fa6b502027f768f321de3859f4218ed832b8d65b25e8cfdbc413ae3d.jpg)


## C ase Study

## 5.6

## CASE

During the development of a software product, a number of very different operation have to be carried out. Typical activities include estimating resource requirements, drawing up the specifi cation document, performing integration testing, and writing 

# Just in Case You Wanted to Know

As explained in Section 1.11, for software engineers the term system is frequently used to mean a software–hardware combination. The fi eld of systems engineering spans a wide range of activities, starting with defi ning the client’s needs and requirements until they have been fully implemented in the constructed system. Subsequently, after the system has been delivered to the client, following successful acceptance tests, it undergoes extensive modifi cations throughout its entire life cycle, to remove defects or add needed improvements or adaptations [Tomer and Schach, 2002]. 

Accordingly, there are strong similarities between systems engineering and software engineering. It is therefore not surprising that, for systems engineers, the acronym CASE stands for “computer-aided systems engineering.” Because of the major role often played by software in systems engineering, within the context of systems engineering it is sometimes hard to determine which version of the CASE acronym is meant. 

the user manual. Unfortunately, none of these activities, nor the others in the soft ware process, can be fully automated and performed by a computer without human intervention. 

However, computers can assist every step of the way. The title of this section, “CASE,” stands for computer-aided (or computer-assisted) software engineering (but see Just in Case You Wanted to Know Box 5.2). Computers can help by carrying out much of the drudge work associated with software development, including the creation and organization of artifacts of all kinds, such as plans, contracts, speci fi cations, designs, source code, and management information. Documentation is essential for software development and maintenance, but the majority of individuals involved in software development are not fond of creating or updating documentation. Maintaining diagrams on the computer is especially useful as it allows change to be made with ease. 

But CASE is not restricted to assisting with documentation. In particular, computers can help software engineers to cope with the complexity of software development, especially in managing all the details. CASE involves all aspects of computer support for software engineering. At the same time, it is important to remember that CASE stands for computer- aided software engineering, and not computer- automated software engineering—no computer can yet replace a human with respect to development or maintenance of software. For the foreseeable future at least, the computer must remain a tool of the software professional. 

## 5.7 Taxonomy of CASE

The simplest form of CASE is the software tool , a product that assists in just one aspect of the production of software. CASE tools currently are being used with every workfl ow of the life cycle. For example, a variety of tools are on the market, many of them for use with personal computers, that assist in the construction of graphical representations of software products, such as fl owcharts and UML diagrams. CASE tools that help the developer during the earlier workfl ows of the process (the requirements, analysis, and design workfl ows) sometimes are termed upperCASE or front-end tools, whereas those that assist with the 

When typesetting was done by hand, each character was cast in relief on a piece of metal called a sort. The sorts were combined to make words, then sentences, paragraphs, and so on. All the A’s were stored in one box, all the B’s in another, and so on. The capital letters or majuscules were kept in upper boxes of a desk or in the upper case, whereas the more frequently used minuscule letters were closer at hand in the lower case. That is why capital letters are referred to as uppercase letters, and similarly for lowercase letters. The terms upperCASE tool and lowerCASE tool are therefore puns. 


FIGURE 5.9 A representation of (a) a tool, (b) a workbench, and (c) an environment.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/07a2eabea36cbd2f48819930a8af71d8956ca3e63d57392874b86978c029d3e7.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/7067c24cd28e8e8d45ec06ee83c1e6d8b717b80748dde2d3080cf0eac806e831.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/c6d5433599fe66a0d6db287de49db5ea2c82e59f00855aceb0e3ee7c78ad64bb.jpg)



(c)


implementation workfl ow and postdelivery maintenance are termed lowerCASE or backend tools (see Just in Case you Wanted to Know Box 5.3). For example, Figure 5.9 (a) represents a CASE tool that assists with part of the requirements workfl ow. 

An important class of CASE tools is the data dictionary , a computerized list of all data defi ned within the product. A large product contains tens (if not hundreds) of thousands of data items, and the computer is ideal for storing information such as variable names and types, and the location where each is defi ned, as well as procedure names and parameters and their types. An important part of every data dictionary entry is a description of the item; for example, This procedure takes as input the body weight of the newborn infant and computes the appropriate dosage of the drug or List of aircraft arrival times sorted with earliest times fi rst. 

The power of a data dictionary can be enhanced by combining it with a consistency checker , a tool to check that every data item in the specifi cation document is refl ected in the design and, conversely, every item in the design has been defi ned in the specifi cation document. 

Another use of a data dictionary is to provide the data for report generators and screen generators. A report generator is used to generate the code needed for producing a report. A screen generator is used to assist the software developer in producing the code for a data capture screen. Suppose that a screen is being designed to enter the weekly sales at each branch of a chain of bookstores. The branch number is a four-digit integer in the range 1000–4500 or 8000–8999, entered on the screen three lines from the top. This information is given to the screen generator. The screen generator then automatically generates code to display the string BRANCH NUMBER _ _ _ _ three lines from the top and position the cursor at the fi rst underline character. As the user enters each digit, it is displayed; and the cursor moves on to the next underline. The screen generator also generates code for checking that the user enters only digits and that the resulting four-digit integer is in the specifi ed range. If the data entered are invalid or the user presses the ? key, help information is displayed. 

Use of such generators can result in the implementation being quickly constructed. Furthermore, a graphical representation tool combined with a data dictionary, consistency checker, report generator, and screen generator constitute a requirements, analysis, and design workbench that supports the fi rst three core workfl ows. An example of a commercial workbench that incorporates all these features is Software through Pictures. 

Another class of workbench is a requirements management workbench. Such a workbench allows systems analysts to organize and track the requirements of a software development project. RequisitePro is a commercial example of such a workbench. 

A CASE workbench therefore is a collection of tools that together support one or two activities, whereas an activity is a related collection of tasks. For example, the coding activity includes editing, compiling, linking, testing, and debugging. An activity is not the same as a workfl ow of a life-cycle model. In fact, the tasks of an activity can even cross workfl ow boundaries. For example, a project management workbench is used for every workfl ow of the project, and a coding workbench can be used for building a proof-ofconcept prototype, as well as for the implementation workfl ow and postdelivery maintenance. Figure 5.9 (b) represents a workbench of upperCASE tools. The workbench includes the requirements workfl ow tool of Figure 5.9 (a), as well as tools for parts of the analysis and design workfl ows. 

Continuing the progression of CASE technology from tools to workbenches, the next item is the CASE environment. Unlike the workbench, which supports one or two activities, an environment supports the complete software process or, at the very least, a large portion of the software process [Fuggetta, 1993]. Figure 5.9 (c) depicts an environment that supports all aspects of all workfl ows of the life cycle. Environments are discussed in greater detail in Chapter 15 . 

Having set up a CASE taxonomy (tools, workbenches, and environments), we now consider the scope of CASE. 

## 5.8 Scope of CASE

As mentioned previously, the need to have accurate and up-to-date documentation available at all times is a primary reason for implementing CASE technology. For example, suppose that specifi cations are produced manually. A member of the development team has no way of telling whether a particular specifi cation document is the current version or an older version. There is no way of knowing if the handwritten changes on that document are part of the current specifi cation or merely a suggestion later rejected. On the other hand, if the specifi cations of the product are produced using a CASE tool, then at any time there is only one copy of the specifi cations, the online version accessed via the CASE tool. Then, if the specifi cations are changed, members of the development team can easily access the document and be sure that they are seeing the current version. In addition, the consistency checker will fl ag any design changes without corresponding changes to the specifi cation document. 

Programmers also need online documentation . For example, online help information must be provided for the operating system, editor, programming language, and so on. In addition, programmers have to consult manuals of many kinds, such as editor manuals and programming manuals. It is highly desirable that, wherever possible, these manuals be available online. Apart from the convenience of having everything at one’s fi ngertips, it is generally quicker to query by computer than to try to fi nd the appropriate manual and plow through it to fi nd the needed item. In addition, it usually is much easier to update an online manual than to try to fi nd all hard-copy versions of a manual within an organization and make the necessary page changes. As a result, online documentation is likely to be more accurate than hard-copy versions of the same material—another reason for providing online documentation to programmers. An example of such online documentation is the UNIX manual pages [Sobell, 1995]. CASE also can assist with communication among team members. E-mail is as much a part of an office today as a computer or a fax machine. There are many advantages to e-mail. From the viewpoint of software production, storing copies of all e-mail relevant to a specifi c project in a particular mailbox provides a written record of the decisions made during the project. This can be used to resolve confl icts that may arise later. Many CASE environments and some CASE workbenches now incorporate e-mail systems. In other organizations, the e-mail system is implemented via a World Wide Web browser such as Chrome or Firefox. Other tools that are equally essential are spreadsheets and word processors. 

The term coding tools refers to CASE tools such as text editors, debuggers, and pretty printers designed to simplify the programmer’s task, reduce the frustration many programmers experience in their work, and increase programmer productivity. Before discussing such tools, three defi nitions are required. Programming-in-the-small refers to software development at the level of the code of a single module, whereas programming-in-thelarge is software development at the module level [DeRemer and Kron, 1976]. The latter includes aspects such as architectural design and integration. Programming-in-themany refers to software production by a team. At times, the team works at the module level; at times, at the code level. Accordingly, programming-in-the-many incorporates aspects of both programming-in-the-large and programming-in-the-small. 

A structure editor is a text editor that “understands” the implementation language. That is, a structure editor can detect a syntax fault as soon as it has been keyed in by the programmer, speeding the implementation because time is not wasted on futile compilations. Structure editors exist for a wide variety of languages, operating systems, and hardware. Because a structure editor has knowledge of the programming language, it is easy to incorporate a pretty printer (or formatter ) into the editor to ensure that the code always has a good visual appearance. For example, a pretty printer for C++ ensures that each } is indented the same amount as its corresponding {. Reserved words are automatically put in boldface so that they stand out, and indentation has been designed to aid readability. Nowadays, structure editors of this kind form part of numerous programming workbenches, such as Visual C++ and JBuilder. 

Now consider the problem of invoking a method within the code, only to discover at linkage time that either the method does not exist or it has been wrongly specifi ed in some way. What is needed is for the structure editor to support online interface checking. That is, just as the structure editor has information regarding the name of every variable declared by the programmer, so it must also know the name of every method defi ned within the product. For example, if the programmer enters a call such as 

average = dataArray.computeAverage (numberOfValues); 

but method computeAverage has not yet been defi ned, then the editor immediately responds with a message such as 

## Method computeAverage not known

At this point, the programmer is given two choices, either to correct the name of the method or to declare a new method named computeAverage. If the second option is chosen, the programmer also must specify the arguments of the new method. Argument types must be supplied when declaring a new method because the major reason for having online interface checking is precisely to be able to check full interface information, not just the names of methods. A common fault is for method p to call method q passing, say, four arguments, whereas method q has been specifi ed with fi ve arguments. It is more diffi cult to detect the fault when the call correctly uses four arguments, but two of the arguments are transposed. For example, the declaration of method q might be 

void q ( fl oat fl oatVar, int intVar, string s1, string s2) 

whereas the call is 

## q (intVar, fl oatVar, s1, s2);

The fi rst two arguments have been transposed in the call statement. Java compilers and linkers detect this fault but only when they are invoked later. In contrast, an online interface checker immediately detects this and similar faults. In addition, if the editor has a help facility, the programmer can request online information as to the precise arguments of method q before attempting to code the call to q. Better yet, the editor should generate a template for the call, showing the type of each argument. The programmer merely has to replace each formal argument with an actual argument of the correct type. 

A major advantage of online interface checking is that hard-to-detect faults caused by calling methods with the wrong number of arguments or arguments of the wrong type are immediately fl agged. Online interface information is important for the effi cient production of high-quality software, particularly when the software is produced by a team (programming-in-the-many). It is essential that online interface information regarding all code artifacts be available to all programming team members at all times. Furthermore, if one programmer changes the interface of method vaporCheck, perhaps by changing the type of one argument from int to fl oat or by adding an additional argument, then every component that calls vaporCheck must automatically be disabled until the relevant call statements have been altered to refl ect the new state of affairs. 

Even with a syntax-directed editor incorporating an online interface checker, the programmer still has to exit from the editor and invoke the compiler and linker. Clearly, there can be no compilation faults, but the compiler still has to be invoked to perform code generation. Then the linker has to be called. Again, the programmer can be sure that all external references will be satisfi ed as a consequence of the presence of the online interface checker, but the linker is still needed to link the product. The solution to this is to incorporate an operating system front end within the editor. That is, a programmer should be able to give operating system commands from within the editor. To cause the editor to invoke the compiler, linker, loader, and any other system software needed to cause the code artifact to be executed, the programmer should be able to type a single command, named go or run, or use the mouse to choose the appropriate icon or menu selection. In UNIX, this can be achieved by using the make command (Section 5.11) or by invoking a shell script [Sobell, 1995]. Such front ends can be implemented in other operating systems, as well. 

One of the most frustrating computing experiences is for a product to execute for a sec ond or so, and then terminate abruptly, printing a message such as 

## Overfl ow at 506

The programmer is working in a high-level language such as Java or C++, not a lowlevel language like assembler or machine code. But when debugging support is of the Overfl ow at 506 variety, the programmer is forced to examine machine code core dumps, assembler listings, linker listings, and a variety of similar low-level documentation, thereby destroying the whole advantage of programming in a high-level language. A similar situation arises when the only information provided is the infamous UNIX message 

## Core dumped

or the equally uninformative 

## Segmentation fault

Here again, the user is forced to examine low-level information 

In the event of a failure, the message shown in Figure 5.10 is a great improvement over the earlier terse error messages. The programmer immediately can see that the method failed because of an attempt to divide by 0. Even more useful is for the operating system to enter edit mode and automatically display the line at which the failure was detected, line 6, together with the preceding and following four or fi ve lines. The programmer probably can then see what caused the failure and make the necessary changes. 

Another type of source-level debugging is tracing. Before the advent of CASE tools, programmers had to insert appropriate print statements into their code by hand that, at execution time, would indicate the line number and the values of relevant variables. This now can be done by giving commands to a source-level debugger that automatically causes trace output to be produced. Even better is an interactive source-level debugger . 

```txt
OVERFLOW ERROR
Class: cyclotronEnergy
Method: performComputation
Line 6: newValue = (oldValue + tempValue) / tempValue;
    oldValue = 3.9583    tempValue = 0.0000 
```

Suppose that the value of variable escapeVelocity seems to be incorrect and that method computeTrajectory seems to be faulty. Using the interactive source-level debugger, the programmer can set breakpoints in the code. When a breakpoint is reached, execution stops and debugging mode is entered. The programmer now asks the debugger to trace the variable escapeVelocity and the method computeTrajectory. That is, every time the value of escapeVelocity subsequently is either used or changed, execution again halts. The programmer then has the option of entering further debugging commands, for example, to request that the value of a specifi c variable be displayed. Alternatively, the programmer may choose to continue execution in debugging mode or return to normal execution mode. The programmer similarly can interact with the debugger whenever the method computeTrajectory is entered or exited. Such an interactive source-level debugger offers almost every conceivable type of assistance to the programmer when a product fails. The UNIX debugger dbx is an example of such a CASE tool. 

As has been pointed out many times, it is essential that documentation of all kinds be available online. In the case of programmers, all documentation they might need should be accessible from within the editor. 

What has now been described—a structure editor with online interface checking capabilities, operating system front end, source-level debugger, and online documentation— constitutes an adequate and effective programming workbench. 

This sort of workbench is by no means new. All these features were supported by the FLOW software development workbench as far back as 1980 [Dooley and Schach, 1985]. Therefore, what has been put forward as a minimal but essential programming workbench does not require many years of research before a prototype can be tentatively produced. Quite the contrary, the necessary technology has been in place for over 30 years, and it is somewhat surprising that there are programmers who still implement code the “old-fashioned way,” instead of using a workbench like Sun ONE Studio. 

An essential tool, especially when software is developed by a team, is a version-control tool 

## 5.9 Software Versions

Whenever a product is maintained, there will be at least two versions of the product: the old version and the new version. Because a product is composed of code artifacts, there will also be two or more versions of each of the component artifacts that have been changed. 

Version control is described fi rst within the context of postdelivery maintenance, and then broadened to include earlier parts of the process. 

## 5.9.1 Revisions

Suppose a product has been installed at a number of different sites. If a fault is found in an artifact, then that artifact has to be fi xed. After appropriate changes have been made, there will be two versions of the artifact, the old version and the new version intended to replace it. The new version is termed a revision . The presence of multiple versions apparently is easy to solve—any old versions should be thrown away, leaving just the correct one. But that would be most unwise. Suppose that the previous version of the artifact was revision n, and that the new version is revision n + 1. First, there is no guarantee that revision n + 1 is any more correct than revision n. Even though revision n + 1 may have been thoroughly tested by the software quality assurance group, both in isolation and linked to the rest of the product, there may be disastrous consequences when the new version of the product is run by the user on actual data. Revision n must be kept for a second reason. The product may have been distributed to a variety of sites, and not all of them may have installed revision n + 1. If a fault report is received from a site still using revision n, then to analyze this new fault, it is necessary to confi gure the product in exactly the same way it is confi gured at the user’s site, that is, incorporating revision n of the artifact. It therefore is necessary to retain a copy of every revision of each artifact. 

As described in Section 1.3, perfective maintenance is performed to extend the functionality of a product. In some instances, new artifacts are implemented; in other cases, existing artifacts are changed to incorporate this additional functionality. These new versions also are revisions of existing artifacts. So are artifacts that are changed when performing adaptive maintenance—that is, when changes are made to the product in response to changes in the environment in which the product operates. As with corrective maintenance, all previous versions must be retained because issues arise not just during postdelivery maintenance but from implementation onward. After all, once an artifact has been coded, it continually undergoes changes as a consequence of faults being detected and corrected. As a result, there are numerous versions of every artifact, and it is vital to have some sort of control to ensure that every member of the development team knows which is the current version of a given artifact. Before we can present a solution to this problem, a further complication must be taken into account. 

## 5.9.2 Variations

Consider the following example. Most computers support more than one type of printer. For example, a personal computer may support an ink-jet printer and a laser printer. The operating system therefore must contain two variations of the printer driver, one for each type of printer. Unlike revisions, each of which is implemented specifi cally to replace its predecessor, variations are designed to coexist. Another situation where variations are needed is when a product is to be ported to a variety of different operating systems and hardware. A different variation of many of the artifacts may have to be produced for each operating system–hardware combination. 

Versions are schematically depicted in Figure 5.11 , which shows both revisions and variations. To complicate matters further, in general, there are multiple revisions of each 

FIGURE 5.11 A schematic representation of multiple versions of artifacts, showing (a) revisions and (b) variations. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/68def65e16398b89784da00f8185254a733a087ee6d5babe4b91757344bcf426.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/b5366b8c795f9f24f982766e1c14e27a0af68488801a845667762cd657baf518.jpg)



(b)


variation. For a software organization to avoid drowning in a morass of multiple versions, a CASE tool is needed. 

## 5.10 Confi guration Control

The code for every artifact exists in three forms. First is the source code, nowadays generally implemented in a high-level language like C++ or Java. Next comes the object code, produced by compiling the source code. In this book, because of possible confusion of the word object , we refer to object code as compiled code . Finally, the compiled code for each artifact is combined with run-time routines to produce an executable load image. This is shown in Figure 5.12 . The programmer can use various different versions of each artifact. The specifi c version of each artifact from which a given version of the complete product is built is called the confi guration of that version of the product. 

Suppose that a programmer is given a test report from the SQA group stating that an artifact failed on a specifi c set of test data. One of the fi rst things to do is attempt to re-create the failure. But how can the programmer determine which revisions of which variations went into the version of the product that crashed? Unless a confi guration-control tool (described in the following discussion) is used, the only way to pinpoint the cause of the failure is to look at the executable load image, in octal or hexadecimal format, and compare it to the compiled code, also in octal or hexadecimal. Specifi cally, the various versions of the source code have to be compiled and compared to the compiled code that went into the executable load image. Although this can be done, it can take a long time, particularly if the product has dozens (if not hundreds) of code artifacts, each with multiple versions. Therefore, two problems must be solved when dealing with multiple versions. First, we must distinguish between versions so that the correct version of each code artifact is compiled and linked to the product. Second, there is the inverse problem: Given an executable load image, determine which version of each of its components went into it. 

The fi rst item needed to solve this problem is a version-control tool. Many operating systems, particularly for mainframe computers, support version control. But many do not, in 

FIGURE 5.12 Components of an executable load image. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/1a9b17a17051a36f41f0aeec1cdb87b54264becac888927053664a47eb1379e8.jpg)


FIGURE 5.13 Multiple revisions and variations. (a) Four revisions of artifact acknowledgeMessage. (b) Two variations of artifact printerDriver, with three revisions of variation printerDriver (laser) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/0fa985ee201b4a6d1891fded8a42c4dce6d11eb0862193626e0a93bc3303a3d1.jpg)


which case a separate version-control tool is needed. A common technique used in version control is for the name of each fi le to consist of two pieces, the fi le name itself and the revision number. For example, an artifact that acknowledges receipt of a message has revisions acknowledgeMessage/1, acknowledgeMessage/2, and so on, as depicted in Figure 5.13 (a). A programmer then can specify exactly which revision is needed for a given task. 

With regard to multiple variations (slightly changed versions that fulfi ll the same role in different situations), one useful notation is to have a basic fi le name, followed by a variation name in parentheses [Babich, 1986]. Accordingly, two printer drivers are given the names printerDriver (inkJet) and printerDriver (laser). 

Of course, there will be multiple revisions of each variation, such as printerDriver (laser)/12, printerDriver (laser)/13, and printerDriver (laser)/14. This is depicted in Figure 5.13 (b). 

A version-control tool is the fi rst step toward being able to manage multiple versions. Once it is in place, a detailed record (or derivation ) of every version of the product must be kept. The derivation contains the name of each source code element, including the variation and revision, the versions of the various compilers and linkers used, the name of the person who constructed the product, and of course, the date and the time at which it was constructed. 

Version control is a great help in managing multiple versions of artifacts and the product as a whole. But more than just version control is needed, because of additional problems associated with maintaining multiple variations. 

Consider the two variations printerDriver (inkJet) and printerDriver (laser). Suppose that a fault is found in printerDriver (inkJet) and suppose that the fault occurs in a part of the artifact common to both variations. Then it is necessary to fi x not only printerDriver (inkJet) but also printerDriver (laser). In general, if there are v variations of an artifact, all v of them have to be fi xed. Not only that, they have to be fi xed in exactly the same way. 

One solution to this problem is to store just one variation, say, printerDriver (inkJet). Then any other variation is stored in terms of the list of changes that have to be made to go from the original to that variation. The list of differences is termed a delta. What is stored is one variation and v – 1 deltas. Variation printerDriver (laser) is retrieved by accessing printerDriver (inkJet) and applying the delta. A change made just to printerDriver (laser) is implemented by changing the appropriate delta. However, any change made to printer-Driver (inkJet), the original variation, automatically applies to all the other variations. 

A confi guration-control tool can automatically manage multiple variations. But confi guration control goes beyond multiple variations. A confi guration-control tool can also handle problems caused by development and maintenance by teams, as described in Section 5.10.1. 

## 5.10.1 Confi guration Control during Postdelivery Maintenance

All sorts of diffi culties can arise when more than one programmer simultaneously maintains a product. For example, suppose each of two programmers is assigned a different fault report on a Monday morning. By coincidence, both localize the fault they are to fi x to different parts of the same artifact mDual. Each programmer makes a copy of the current version of the artifact, mDual/16, and they start to work on the faults. The fi rst programmer fi xes the fi rst fault, has the changes approved, and replaces the artifact, now called mDual/17. A day later the second programmer fi xes the second fault, has the changes approved, and installs artifact mDual/18. Unfortunately, revision 17 contains the changes of only the fi rst programmer, whereas revision 18 contains those of only the second programmer. None of the changes of the fi rst programmer are in mDual/18, because the second programmer made changes to mDual/16, instead of to mDual/17. 

Although the idea of each programmer making individual copies of an artifact is far better than both working together on the same piece of software, clearly it is inadequate for maintenance by a team. What is needed is some mechanism that allows only one user at a time to change an artifact. 

## 5.10.2 Baselines

The maintenance manager must set up a baseline , a confi guration (set of versions) of all the artifacts in the product. When trying to fi nd a fault, a maintenance programmer puts copies of any needed artifacts into his or her private workspace . In this private workspace, the programmer can change anything at all without having an impact on any other programmer in any way, because all changes are made to the programmer’s private copy; the baseline version is left untouched. 

Once it has been decided which artifact has to be changed to fi x the fault, the programmer freezes the current version of the artifact he or she is going to alter. No other programmer may make changes to any frozen version. After the maintenance programmer has made changes and they have been tested, the new version of the artifact is installed, thereby modifying the baseline. The previous version, now frozen, is retained because it may be needed in the future, as explained previously, but it cannot be altered. Once a new version has been installed, any other maintenance programmer can freeze the new version and make changes to it. The resulting artifact, in turn, becomes the next baseline version. A similar procedure is followed if two or more artifacts have to be changed simultaneously. 

This scheme solves the problem with artifact mDual. Both programmers make private copies of mDual/16 and use those copies to analyze the respective faults that they have been assigned to fi x. The fi rst programmer decides what changes to make, freezes mDual/16 and makes those changes to repair the fi rst fault. After the changes have been tested, the resulting revision, mDual/17, becomes the baseline version. In the meantime, the second programmer has found the second fault by experimenting with a private copy of mDual/16. However, changes cannot now be made to mDual/16 because it was frozen by the fi rst programmer. Once mDual/17 becomes the baseline, it is frozen by the second programmer whose changes are made to mDual/17. The resulting artifact now is installed as mDual/18, a version that incorporates the changes of both programmers. Revisions mDual/16 and mDual/17 are retained for possible future reference, but they can never be altered. 

## 5.10.3 Confi guration Control during Development

While an artifact is in the process of being coded, versions are changing too rapidly for confi guration control to be helpful. Once coding of the artifact has been completed, it should immediately be tested informally by its programmer, as described in Section 6.6. During this informal testing, the artifact again passes through numerous versions. When the programmer is satisfi ed, the artifact is handed over to the SQA group for methodical testing. As soon as the artifact has been passed by the SQA group, it is ready to be integrated into the product. From then on, it should be subject to the same confi guration-control procedures as those of postdelivery maintenance. Any change to an integrated artifact can have an impact on the product as a whole in the same way as a change made during postdelivery maintenance. Therefore, confi guration control is needed not only during postdelivery maintenance but also during implementation. Furthermore, management cannot monitor the development process adequately unless every artifact is subject to confi guration control as soon as is reasonable, that is, after it has been passed by the SQA group. When confi guration control is properly applied, management is aware of the status of every artifact and can take early corrective action if project deadlines seem to be slipping. 

Two major UNIX version-control tools are sccs (source code control system) [Rochkind, 1975] and rcs (revision control system) [Tichy, 1985]. PVCS is a popular, commercially available confi guration-control tool. Microsoft SourceSafe is a confi guration-control tool for personal computers. CVS (concurrent versions system) [Loukides and Oram, 1997] and Subversion are open-source confi guration management tools (open-source software is described in Section 1.11). 

## 5.11 Build Tools

If a software organization does not wish to purchase a complete confi guration-control tool, then at the very least, a version-control tool must be used in conjunction with a build tool , that is, a tool that assists in selecting the correct version of each compiled-code artifact to be linked to form a specifi c version of the product. At any time, multiple variations and revisions of each artifact are in the product library. All version-control tools assist users in distinguishing among different versions of artifacts of source code. But keeping track of compiled code is more diffi cult, because some version-control tools do not attach revision numbers to compiled versions. 

To cope with this, some organizations automatically compile the latest version of each artifact every night, thereby ensuring that all the compiled code is up to date. Although this technique works, it can be extremely wasteful of computer time because frequently a large number of unnecessary compilations are performed. The UNIX tool make can solve this problem [Feldman, 1979]. For each executable load image, the programmer sets up a Makefi le specifying the hierarchy of source and compiled fi les that go into that particular confi guration; such a hierarchy is shown in Figure 5.12 . More complex dependencies, such as included fi les in C or C++, also can be handled by make . When invoked by a programmer, the tool works as follows: UNIX, like virtually every other operating system, attaches a date and time stamp to each fi le. Suppose that the stamp on a source fi le is Friday, June 6, at 11:24 A.M., whereas the stamp on the corresponding compiled fi le is Friday, June 6, at 11:40 A.M. Then it is clear that the source fi le has not been changed since the compiled fi le was created by the compiler. On the other hand, if the date and time stamp on the source fi le is later than that on the compiled fi le, then make calls the appropriate compiler or assembler to create a version of the compiled fi le that corresponds to the current version of the source fi le. 

Next, the date and time stamp on the executable load image is compared to those on every compiled fi le in that confi guration. If the executable load image was created later than all the compiled fi les, then there is no need to relink. But if a compiled fi le has a later stamp than that of the load image, then the load image does not incorporate the latest version of that compiled fi le. In this case, make calls the linker and constructs an updated load image. 

In other words, make checks whether the load image incorporates the current version of every artifact. If so, then nothing further is done and no CPU time is wasted on needless compilations and linkage. If not, then make calls the relevant system software to create an up-to-date version of the product. 

In addition, make simplifi es the task of building a compiled fi le. The user need not specify each time what artifacts are to be used and how they are to be connected, because this information already is in the Makefi le. Therefore, a single make command is all that is needed to build a product with hundreds of artifacts and ensure that the complete product is put together correctly. 

Tools like make have been incorporated into an endless variety of programming environments, including Visual Java and Visual C++. An open-source version of make is Ant (a product of the Apache project). 

## 5.12 Productivity Gains with CASE Technology

Reifer (as reported in [Myers, 1992]) conducted an investigation into productivity gains as a consequence of introducing CASE technology. He collected data from 45 companies in 10 industries. Half the companies were in the fi eld of information systems, 25 percent in scientifi c areas, and 25 percent in real-time aerospace. Average annual productivity gains varied from 9 percent (real-time aerospace) to 12 percent (information systems). If only productivity gains are considered, then these fi gures do not justify the cost of $125,000 per user of introducing CASE technology. However, the companies surveyed felt that the justifi cation for CASE was not merely increased productivity but also shorter development time 

FIGURE 5.14 Summary of the theoretical (analytical) tools and software (CASE) tools presented in this chapter and the sections in which each is described. 

<table><tr><td>Analytical Tools</td></tr><tr><td>Cost-benefit analysis (Section 5.2)</td></tr><tr><td>Divide-and-conquer (Section 5.3)</td></tr><tr><td>Metrics (Section 5.5)</td></tr><tr><td>Separation of concerns (Section 5.4)</td></tr><tr><td>Stepwise refinement (Section 5.1)</td></tr><tr><td>CASE Taxonomy</td></tr><tr><td>Environment (Section 5.7)</td></tr><tr><td>LowerCASE tool (Section 5.7)</td></tr><tr><td>UpperCASE tool (Section 5.7)</td></tr><tr><td>Workbench (Section 5.7)</td></tr><tr><td>CASE Tools</td></tr><tr><td>Build tool (Section 5.11)</td></tr><tr><td>Coding tool (Section 5.8)</td></tr><tr><td>Configuration-control tool (Section 5.10)</td></tr><tr><td>Consistency checker (Section 5.7)</td></tr><tr><td>Data dictionary (Section 5.7)</td></tr><tr><td>E-mail (Section 5.8)</td></tr><tr><td>Interface checker (Section 5.8)</td></tr><tr><td>Online documentation (Section 5.8)</td></tr><tr><td>Operating system front end (Section 5.8)</td></tr><tr><td>Pretty printer (Section 5.8)</td></tr><tr><td>Report generator (Section 5.7)</td></tr><tr><td>Screen generator (Section 5.7)</td></tr><tr><td>Source-level debugger (Section 5.8)</td></tr><tr><td>Spreadsheet (Section 5.8)</td></tr><tr><td>Structure editor (Section 5.8)</td></tr><tr><td>Version-control tool (Section 5.9)</td></tr><tr><td>Word processor (Section 5.8)</td></tr><tr><td>World Wide Web browser (Section 5.8)</td></tr></table>

and improvement in software quality. In other words, the introduction of CASE environments boosted productivity, although less than some proponents of CASE technology have claimed. Nevertheless, other, equally important reasons were given for introducing CASE technology into a software organization, such as faster development, fewer faults, better usability, easier maintenance, and improved morale. 

Newer results on the effectiveness of CASE technology from over 100 development projects at 15 Fortune 500 companies refl ect the importance of training and the software process [Guinan, Cooprider, and Sawyer, 1997]. When teams using CASE were given training in application development in general as well as tool-specifi c training, user satisfaction increased and development schedules were met. However, when training was not provided, software was delivered late and users were less satisfi ed. Also, performance increased by 50 percent when teams used CASE tools in conjunction with a structured methodology. These results support the assertion in Section 3.13 that CASE environments should not be used by groups at maturity levels 1 or 2. To put it bluntly, a fool with a tool is still a fool [Guinan, Cooprider, and Sawyer, 1997]. The fi nal fi gure in this chapter, Figure 5.14 , is an alphabetical list of the theoretical tools and CASE tools described in this chapter, together with the section in which each is described. 

## Chapter Review

First, a number of analytical tools are presented. Stepwise refinement, based on Miller’s Law, is described in Section 5.1 and illustrated by means of an example in Section 5.1.1. Another analytical tool, cost–benefit analysis, is presented in Section 5.2. Separation of concerns is described in Section 5.3, and divide-and-conquer in Section 5.4. Software metrics are introduced in Section 5.5. 

Computer-aided software engineering (CASE) is defined in Section 5.6, and the taxonomy and scope of CASE are described in Sections 5.7 and 5.8, respectively. A variety of CASE tools are next described. When large products are constructed, version-control tools, configuration-control tools, and build tools are essential; these are presented in Sections 5.9 through 5.11. Productivity gains, as a consequence of the use of CASE technology, are described in Section 5.12. 

## For Further Reading

For further information regarding Miller’s Law and his theory of how the brain operates on chunks, consult [Tracz, 1979] as well as Miller’s original paper [Miller, 1956] 

Wirth’s [1971] paper on stepwise refi nement is a classic of its kind and deserves detailed study. Equally signifi cant from the viewpoint of stepwise refi nement are the books by Dijkstra [1976] and Wirth [1975]. 

The extent to which CASE is used in the software industry is described in [Sharma and Rai, 2000]. A tool that supports incremental software development while ensuring consistency between the artifacts is described in [Reiss, 2006]. Experiences with open-source software engineering tools are described in [Toth, 2006]. 

In this book, CASE tools for the separate workfl ows of the software process are described in the chapters on each workfl ow. For information on workbenches or CASE environments, consult the For Further Reading section of Chapter 15. 

An introduction to version control in general and CVS in particular is given in [Louridas, 2006]. Articles on confi guration management include [van der Hoek, Carzaniga, Heimbigner, and Wolf, 2002], [Mens, 2002], and [Walrad and Strom, 2002]. The interaction between confi guration management and traceability is discussed in [Mohan, Xu, and Ramesh, 2008]. Refactoring poses problems for software confi guration management tools; a solution is put forward in [Dig, Manzoor, Johnson, and Nguyen, 2008]. The proceedings of the International Workshops on Software Confi guration Manage ment are a useful source of information 

CASE tools for refactoring are presented in [Black and Murphy-Hill, 2008]. 

There are many excellent books on cost–benefi t analysis, including [Gramlich, 1997]. Cost– benefi t analysis of software product lines (Section 8.5.4) is discussed in [Bockle et al., 2004]. Van Solingen [2004] presents a cost–benefi t analysis of software process improvement. 

Jones [1994] highlights unworkable and invalid metrics that nevertheless continue to be mentioned in the literature. The validity of object-oriented metrics is discussed in [El Emam, Benlarbi, Goel, and Rai, 2001] and [Alshayeb and Li, 2003]. Kilpi [2001] describes how a metrics program was implemented at Nokia. Metrics for COTS-based systems are presented in [Sedigh-Ali and Paul, 2001]. Metrics for measuring the success of a website are put forward in [Belanger et al., 2006]. The May 2008 issue of the Journal of Systems and Software contains a number of articles on process and product metrics. 

A number of articles from the Seventh International Software Metrics Symposium appear in the November 2001 issue of IEEE Transactions on Software Engineering; of particular interest is [Briand and Wüst, 2001]. 

## Key Terms

activity 137 formatter 138 report generator 136 assumptions 131 freeze 145 revision 141 back-end tool 136 front-end tool 135 screen generator 136 baseline 145 interactive source-level separation of concerns 132 browser 138 debugger 140 source-level debugger 140 build tool 146 lookahead 129 spreadsheet 138 CASE 124 lowerCASE tool 136 stepwise refi nement 124 coding tool 138 metrics 133 structure editor 138 confi guration 143 online documentation 138 syntax-directed editor 139 confi guration control 145 online interface checker 139 systems engineering 135 confi guration-control tool 145 operating system front end 140 tool 135 consistency checker 136 pretty printer 138 upperCASE tool 135 cost–benefi t analysis 130 private workspace 145 variation 142 data dictionary 136 process metric 133 version 141 derivation 144 product metric 133 word processor 138 divide-and-conquer 132 programming-in-the-large 138 workbench 137 e-mail 138 programming-in-the-many 138 environment 137 programming-in-the-small 138 

## Problems

5.1 Consider the effect of introducing lookahead to the design of the corrected third refi nement of the sequential master fi le update problem. That is, before processing a transaction the next transaction must be read. If both transactions apply to the same master fi le record, then the decision regarding the processing of the current transaction depends on the type of the next transaction. Draw up a 3 × 3 table with the rows labeled by the type of the current transaction and the columns labeled by the type of the next transaction and fi ll in the action to be taken in each instance. For example, two successive insertions of the same record clearly are an error. But two modifi cations may be perfectly valid; for example, a subscriber can change address more than once in a given month. Now develop a fl owchart for the third refi nement that incorporates lookahead. 

5.2 Check whether your answer to Problem 5.1 can correctly handle a modifi cation transaction followed by a deletion transaction, both transactions being applied to the same master fi le record. If not, modify your answer. 

5.3 Check whether your answer to Problem 5.1 also can correctly handle an insertion followed by a modifi cation followed by a deletion, all applied to the same master fi le record. If not, modify your answer. 

5.4 Check whether your answer to Problem 5.1 can also handle correctly n insertions, modifications, or deletions, n > 2, all applied to the same master f ile record. If not, modify your answer. 

5.5 The last transaction record has no successor. Check whether your fl owchart for Problem 5.1 takes this into account and processes the last transaction record correctly. If not, modify your answer. 

5.6 In some applications, an alternative to lookahead can be achieved by cleverly ordering the transactions. For example, the original problem caused by a modifi cation followed by a deletion of the same master fi le record could have been solved by processing a deletion before a modifi cation. This would have resulted in the master fi le being written correctly and an error message appearing in the exception report. Investigate whether there is an ordering of the transactions that can solve all the diffi culties listed in Problems 5.2 through 5.4. 

5.7 Is separation of concerns a special case of divide-and-conquer? 

5.8 Carefully distinguish between duration and effort . 

5.9 What can you deduce if the rate of fault detection during design inspections doubles? 

5.10 Why are the fi ve fundamental metrics measured for each workfl ow, and not for the product as a whole? 

5.11 A new form of gastrointestinal disease is sweeping the country of Concordia. Like histoplasmosis, it is transmitted as an airborne fungus. Although the disease is almost never fatal, an attack is extremely painful and the sufferer is unable to work for about 2 weeks. The government of Concordia wishes to determine how much money, if any, to spend on attempting to eradicate the disease. The committee charged with advising the Department of Public Health is considering four aspects of the problem: health care costs (Concordia provides free health care to all its citizens), loss of earnings (and hence loss of taxes), pain and discomfort, and gratitude toward the government. Explain how cost–benefi t analysis can assist the committee. For each benefi t or cost, suggest how a dollar estimate for that benefi t or cost could be obtained. 

5.12 Does a one-person software production organization need a version-control tool, and if so, why? 

5.13 Does a one-person software production organization need a confi guration-control tool, and if so, why? 

5.14 You are the manager in charge of the software that controls the navigation system for a midget submarine. Three different user-reported faults have to be fi xed, and you assign one each to Paul, Quentin, and Rachel. A day later you learn that, to implement each of the three fi xes, the same four artifacts must be changed. However, your confi guration-control tool is inoperative, so you will have to manage the changes yourself. How will you do it? 

5.15 Which of the case tools listed in Figure 5.14 promote stepwise refi nement during software development? Justify your answer. 

5.16 Is it possible to interface an upperCASE workbench to a lowerCASE workbench to create a CASE environment? 

5.17 (Term Project) What types of CASE tools would be appropriate for developing the Chocoholics Anonymous product described in Appendix A? 

5.18 (Readings in Software Engineering) Your instructor will distribute copies of [Mohan, Xu, and Ramesh, 2008]. What is your view regarding the interplay of confi guration management and traceability? 

## References



[Alshayeb and Li, 2003] M. ALSHAYEB, AND W. LI, “An Empirical Validation of Object-Oriented Metrics in Two Different Iterative Software Processes,” IEEE Transactions on Software Engineering 29 (November 2003), pp. 1043–49. 





[Babich, 1986] W. A. BABICH, Software Confi guration Management: Coordination for Team Productivity , Addison-Wesley, Reading, MA, 1986. 





[Belanger et al., 2006] F. BELANGER, W. FAN, L. C. SCHAUPP, A. KRISHEN, J. EVERHART, D. POTEET, AND K. NAKAMOTO, “Web Site Success Metrics: Addressing the Duality of Goals,” Communications of the ACM 49 (December 2006), pp. 114–16. 





[Black and Murphy-Hill, 2008] E. BLACK AND A. P. MURPHY-HILL, “Refactoring Tools: Fitness for Purpose,” IEEE Software 25 (September–October 2008), pp. 38–44. 





[Bockle et al., 2004] G. BOCKLE, P. CLEMENTS, J. D. MCGREGOR, D. MUTHIG, AND K. SCHMID, “Calculating ROI for Software Product Lines,” IEEE Software 21 (May–June 2004), pp. 23–31. 





[Briand and Wüst, 2001] L. C. BRIAND AND J. WÜST, “Modeling Development Effort in Object-Oriented Systems Using Design Properties,” IEEE Transactions on Software Engineering 27 (November 2001), pp. 963–86. 





[DeRemer and Kron, 1976] F. DEREMER AND H. H. KRON, “Programming-in-the-Large versus Programming-in-the-Small,” IEEE Transactions on Software Engineering SE-2 (June 1976), pp. 80–86. 





[Dig, Manzoor, Johnson, and Nguyen, 2008] D. DIG, K. MANZOOR, R. E. JOHNSON, AND T. N. NGUYEN, “Effective Software Merging in the Presence of Object-Oriented Refactorings,” IEEE Transactions on Software Engineering 34 (May–June 2008), pp. 321–35. 





[Dijkstra, 1976] E. W. DIJKSTRA, A Discipline of Programming, Prentice Hall, Englewood Cliffs, NJ, 1976. 





[Dijkstra, 1982] E. W. DIJKSTRA, “On the Role of Scientifi c Thought,” in: Dijkstra, Edsger W., Selected Writings on Computing: A Personal Perspective, Springer-Verlag, New York, pp. 60–66. 





[Dooley and Schach, 1985] J. W. M. DOOLEY AND S. R. SCHACH, “FLOW: A Software Development Environment Using Diagrams,” Journal of Systems and Software 5 (August 1985), pp. 203–19. 





[El Emam, Benlarbi, Goel, and Rai, 2001] K. EL EMAM, S. BENLARBI, N. GOEL, AND S. N. RAI, “The Confounding Effect of Class Size on the Validity of Object-Oriented Metrics,” IEEE Transactions on Software Engineering 27 (July 2001), pp. 630–50. 





[Feldman, 1979] S. I. FELDMAN, “Make—A Program for Maintaining Computer Programs,” Software—Practice and Experience 9 (April 1979), pp. 225–65. 





[Fuggetta, 1993] A. FUGGETTA, “A Classifi cation of CASE Technology,” IEEE Computer 26 (December 1993), pp. 25–38. 





[Gramlich, 1997] E. M. GRAMLICH, A Guide to Benefi t–Cost Analysis , 2nd ed., Waveland Books, Prospect Heights, IL, 1997. 





[Guinan, Cooprider, and Sawyer, 1997] P. J. GUINAN, J. G. COOPRIDER, AND S. SAWYER, “The Effective Use of Automated Application Development Tools,” IBM Systems Journal 36 (No. 1, 1997), pp. 124–39. 





[Jones, 1994] C. JONES, “Software Metrics: Good, Bad, and Missing,” IEEE Computer 27 (September 1994), pp. 98–100. 





[Kilpi, 2001] T. KILPI, “Implementing a Software Metrics Program at Nokia,” IEEE Software 18 (November–December 2001), pp. 72–76. 





[Loukides and Oram, 1997] M. K. LOUKIDES AND A. ORAM, Programming with GNU Software , O’Reilly and Associates, Sebastopol, CA, 1997. 





[Louridas, 2006] P. LOURIDAS, “Version Control,” IEEE Software 23 (January–February 2006), pp. 104–107. 





[Mens, 2002] T. MENS, “A State-of-the-Art Survey on Software Merging,” IEEE Transactions on Software Engineering 28 (May 2002), pp. 449–62. 





[Miller, 1956] G. A. MILLER, “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,” The Psychological Review 63 (March 1956), pp. 81–97. Reprinted in: www.well.com/user/smalin/miller.html. 





[Mohan, Xu, and Ramesh, 2008] K. MOHAN, P. XU, AND B. RAMESH, “Improving the Change-Management Process,” Communications of the ACM 51 (May 2008), pp. 59–64. 





[Myers, 1992] W. MYERS, “Good Software Practices Pay off—or Do They?” IEEE Software 9 (March 1992), pp. 96–97. 





[Reiss, 2006] S. P. REISS, “Incremental Maintenance of Software Artifacts,” IEEE Transactions on Software Engineering 32 (September 2006), pp. 682–97. 





[Rochkind, 1975] M. J. ROCHKIND, “The Source Code Control System,” IEEE Transactions on Software Engineering SE-1 (October 1975), pp. 255–65. 





[Sedigh-Ali and Paul, 2001] S. SEDIGH-ALI AND R. A. PAUL, “Software Engineering Metrics for COTS-Based Systems,” IEEE Computer 34 (May 2001), pp. 44–50. 





[Sharma and Rai, 2000] S. SHARMA AND A. RAI, “CASE Deployment in IS Organizations,” Communications of the ACM 43 (January 2000), pp. 80–88. 





[Sobell, 1995] M. G. SOBELL, A Practical Guide to the UNIX System , 3rd ed., Benjamin/Cummings, Menlo Park, CA, 1995. 





[Stevens, Myers, and Constantine, 1974] W. P. STEVENS, G. J. MYERS, AND L. L. CONSTANTINE, “Struc tured Design,” IBM Systems Journal 13 (No. 2, 1974), pp. 115–39. 





[Tichy, 1985] W. F. TICHY, “RCS—A System for Version Control,” Software—Practice and Experience 15 (July 1985), pp. 637–54. 





[Tomer and Schach, 2002] A. TOMER AND S. R. SCHACH, “A Three-Dimensional Model for System Design Evolution,” Systems Engineering 5 (No. 4, 2002), pp. 264–73. 





[Toth, 2006] K. TOTH, “Experiences with Open Source Software Engineering Tools,” IEEE Software 23 (November–December 2006), pp. 44–52. 





[Tracz, 1979] W. J. TRACZ, “Computer Programming and the Human Thought Process,” Software— Practice and Experience 9 (February 1979), pp. 127–37. 





[van der Hoek, Carzaniga, Heimbigner, and Wolf, 2002] A. VAN DER HOEK, A. CARZANIGA, D. HEIM-BIGNER, AND A. L. WOLF, “A Testbed for Confi guration Management Policy Programming,” IEEE Transactions on Software Engineering 28 (January 2002), pp. 79–99. 





[van Solingen, 2004] R. VAN SOLINGEN, “Measuring the ROI of Software Process Improvement,” IEEE Software 21 (May–June 2004), pp. 32–38. 





[Walrad and Strom, 2002] C. WALRAD AND D. STROM, “The Importance of Branching Models in SCM,” IEEE Computer 35 (September 2002), pp. 31–38. 





[Wirth, 1971] N. WIRTH, “Program Development by Stepwise Refi nement,” Communications of the ACM 14 (April 1971), pp. 221–27. 





[Wirth, 1975] N. WIRTH, Algorithms + Data Structures = Programs, Prentice Hall, Englewood Cliffs, NJ, 1975. 



## Testing

Learning Objectives 

After studying this chapter, you should be able to 

• Describe quality assurance issues. 

• Describe how to perform non-execution-based testing (inspections) of artifacts. 

• Describe the principles of execution-based testing. 

• Explain what needs to be tested. 

Classical software life-cycle models all too frequently include a separate testing phase, after integration and before postdelivery maintenance. Nothing could be more dangerous from the viewpoint of trying to achieve high-quality software. Testing is an integral component of the software process and an activity that must be carried out throughout the life cycle: During the requirements workfl ow, the requirements must be checked; during the analysis workfl ow, the specifi cations must be checked; and the software production management plan must undergo similar scrutiny. The design workfl ow requires meticulous checking at every stage. During the implementation workfl ow, each code artifact certainly must be tested; and the product as a whole needs testing when it has been fully integrated. After passing the acceptance test, the product is installed and postdelivery maintenance begins. And hand in hand with maintenance goes repeated checking of modifi ed versions of the product. 

In other words, it is not suffi cient to test the product of a workfl ow merely at the end of that workfl ow. For example, consider the design workfl ow. The members of the design team must consciously and conscientiously check the design while they develop it. It is not much use for the team to develop the complete design artifacts only to fi nd, weeks or months later, that a mistake made early in the process necessitates redesigning almost the entire product. Therefore, continual testing must be carried out by the development team while it performs each workfl ow, in addition to more methodical testing at the end of each workfl ow. 

The terms verifi cation and validation were introduced in Section 1.7. Verifi cation refers to the process of determining whether a workfl ow has been correctly carried out; this takes place at the end of each workfl ow. On the other hand, validation is the intensive evaluation process that takes place just before the product is delivered to the client. Its purpose is to determine whether the product as a whole satisfi es its specifi cations. Even though both terms are defi ned in the IEEE software engineering glossary [IEEE 610.12, 1990] in this way, and notwithstanding the common usage of the term V & V to denote testing, the words verifi cation and validation are used as little as possible in this book. One reason is that, as explained in Section 6.5, the word verifi cation has another meaning within the context of testing. A second reason is that the phrase verifi cation and validation (or V & V) implies that the process of checking a workfl ow can wait until the end of that workfl ow. On the contrary, it is essential that this checking be carried out in parallel with all software development and maintenance activities. Therefore, to avoid the undesirable implications of the phrase V & V , the term testing is used. A second reason why we use the word testing is that this is the terminology of the Unifi ed Process. For example, the fi fth core workfl ow is the test workfl ow. 

Essentially there are two types of testing: execution-based testing and non-executionbased testing. For example, it is impossible to execute a written specifi cation document; the only alternatives are to review it as carefully as possible or subject it to some form of analysis. However, once there is executable code, it becomes possible to run test cases, that is, to perform execution-based testing. Nevertheless, the existence of code does not preclude non-execution-based testing, because as will be explained, methodically reviewing code can uncover as many faults as running test cases. In this chapter, the principles of both execution-based and non-execution-based testing are described. These principles are applied in Chapters 11 through 16, where a description is given of each workfl ow of the process model and the specifi c testing practices applicable to it. The fi rst two faults described in Just in Case You Wanted to Know Box 1.1 led to fatal consequences. Fortunately, in most cases, the result of delivering software with residual faults is considerably less catastrophic. Nevertheless, the importance of testing cannot be stressed too strongly. 

## 6.1 Quality Issues

We begin this section by expanding on the defi nitions of Section 1.11 that relate to testing. A fault is injected into the software when a human makes a mistake [IEEE 610.12, 1990]. One mistake on the part of a software professional may cause several faults; conversely, various mistakes may cause the identical fault. A failure is the observed incorrect behavior of the software product as a consequence of a fault, and the error is the amount by which a result is incorrect [IEEE 610.12, 1990]. A specifi c failure may be caused by several faults, and some faults may never cause a failure. The word defect is a generic term for a fault, failure, or error. 

Now we turn to quality issues. The term quality frequently is misunderstood when used within the software context. After all, quality implies excellence of some sort, but this unfortunately is seldom the meaning intended by software engineers. To put it bluntly, al that many software development organizations can achieve is merely to get the software 

The use of the term quality to denote “adheres to specifi cations” (as opposed to “excellent” or “luxurious”) is the practice in fi elds such as engineering and manufacturing. Consider, for example, the quality control manager at a Coca-Cola bottling plant. The job of that quality control manager is to ensure that every bottle or can that leaves the production line satisfi es the specifi cations for Coca-Cola in every way. There is no attempt to produce “excellent” Coca-Cola or “luxurious” Coca-Cola; the sole aim is to be certain that each bottle or can of Coca-Cola stringently adheres to the company’s formula (specifi cations) for that carbonated beverage. 

The word quality is used identically in the automobile industry. Quality Is Job One is a former slogan of the Ford Motor Company. In other words, the aim of Ford is to ensure that every car that comes off a Ford production line adheres rigorously to the specifi cations for that car; in common software engineering parlance, the car must be “bug free” in every way. 

to function correctly—excellence is an order of magnitude more than what is generally possible for organizations at CMM level 1 (Section 3.13). 

The quality of software is the extent to which the product satisfi es its specifi cations (see Just in Case You Wanted to Know Box 6.1). However, this is not enough. For example, to ensure that a product can be easily maintained, the product must be well designed and meticulously coded. Therefore, it is necessary that software have high quality, but this is by no means suffi cient. 

The task of every software professional is to ensure high-quality software at all times. That is, each developer and maintainer is personally responsible for checking that his or her work is correct. Quality is not something added afterward by the software quality assurance (SQA) group but rather must be built in by the developers from the very beginning. One role of the SQA group is to ensure that the developers are indeed doing high-quality work. The SQA group has additional responsibilities, too, as described in Section 6.1.1. 

## 6.1.1 Software Quality Assurance

As previously stated, one aspect of the role of the SQA group is to test that the developers product is correct. More precisely, once the developers have completed a workfl ow and carefully checked their work, members of the SQA group have to ensure that the workfl ow has indeed been carried out correctly. Also, when the product is complete and the developers are confi dent that the product as a whole is correct, the SQA group has to make sure that this is so. However, software quality assurance goes further than just testing at the end of a workfl ow or the end of the development process. SQA applies to the software process itself. For example, the responsibilities of the SQA group include the development of the various standards to which the software must conform as well as the establishment of the monitoring procedures for ensuring compliance with those standards. In brief, the role of the SQA group is to ensure the quality of the software process and thereby ensure the quality of the product. 

## 6.1.2 Managerial Independence

It is important to have managerial independence between the development team and the SQA group. That is, development should be under one manager, SQA under a different manager, and neither manager should be able to overrule the other. The reason is that, all too frequently, serious defects are found in a product as the delivery deadline approaches. The software organization must now choose between two unsatisfactory options. Either the product can be released on time but full of faults, leaving the client to struggle with faulty software, or the developers can fi x the software but deliver it late. No matter what, the client probably will lose confi dence in the software organization. The decision to deliver faulty software on time should not be made by the manager responsible for development, nor should the SQA manager be able to make the decision to perform further testing and deliver the product late. Instead, both managers should report to a more senior manager who can decide which choice would be in the best interests of both the software develop ment organization and the client. 

At fi rst sight, having a separate SQA group would appear to add considerably to the cost of software development, but this is not so. The additional cost is relatively small compared to the resulting benefi t—higher-quality software. Without an SQA group, every member of the software development organization would have to be involved to some extent with quality assurance activities. Suppose an organization has 100 software professionals and each devotes about 30 percent of his or her time to quality assurance activities. Instead, the 100 individuals should be divided into two groups, with 70 individuals performing software development and the other 30 people responsible for SQA. The same amount of time is devoted to SQA, the only additional expense being a manager to lead the SQA group. Quality assurance now can be performed by an independent group of specialists, leading to products of higher quality than when SQA activities are performed throughout the organization. 

In the case of a very small software company (four employees or fewer), it may simply not be economically viable to have a separate SQA group. The best that can be done under such circumstances is to ensure that the analysis artifacts are checked by someone other than the person responsible for producing those artifacts and similarly for the design arti facts, code artifacts, and so on. The reason for this is explained in Section 6.2 

## 6.2 Non-Execution-Based Testing

Testing software without running test cases is termed non-execution-based testing. Examples of non-execution-based testing methods include reviewing software (carefully reading through it) and analyzing software mathematically (Section 6.5). 

It is not a good idea for the person responsible for drawing up a document to be the only one responsible for reviewing it. Almost everyone has blind spots that allow faults to creep into the document, and those same blind spots prevent the faults from being detected on review. Therefore, the review task must be assigned to someone other than the original author of the document. In addition, having only one reviewer may not be adequate; we all have had the experience of reading through a document many times while failing to detect a blatant spelling mistake that a second reader picks up almost immediately. This is one principle underlying review techniques like walkthroughs or inspections. In both types of review, a document (such as a specifi cation document or design document) is painstakingly checked by a team of software professionals with a broad range of skills. The strength of a review by a team of experts is that the different skills of the participants increase the chances of fi nding a fault. In addition, a team of skilled individuals working together often generates a synergistic effect. 

Walkthroughs and inspections are two types of reviews. The fundamental difference between them is that walkthroughs have fewer steps and are less formal than inspections. 

## 6.2.1 Walkthroughs

A walkthrough team should consist of four to six individuals. An analysis walkthrough team should include at least one representative from the team responsible for drawing up the specifi cations, the manager responsible for the analysis workfl ow, a client representative, a representative of the team that will perform the next workfl ow of the development (in this instance the design team), and a representative of the software quality assurance group. For reasons that will be explained in Section 6.2.2, the SQA group member should chair the walkthrough. 

The members of the walkthrough team should, as far as possible, be experienced senior technical staff members because they tend to fi nd the important faults. That is, they detect the faults that would have a major negative impact on the project [R. New, personal communication, 1992]. 

The material for the walkthrough must be distributed to the participants well in advance to allow for thorough preparation. Each reviewer should study the material and develop two lists: a list of items the reviewer does not understand and a list of items the reviewer believes are incorrect. 

## 6.2.2 Managing Walkthroughs

The walkthrough should be chaired by the SQA representative because the SQA representative has the most to lose if the walkthrough is performed poorly and faults slip through. In contrast, the representative responsible for the analysis workfl ow may be eager to have the specifi cation document approved as quickly as possible to start some other task. The client representative may decide that any faults not detected at the review probably will show up during acceptance testing and be fi xed at that time at no cost to the client organization. But the SQA representative has the most at stake: The quality of the product is a direct refl ection of the professional competence of the SQA group. 

The person leading the walkthrough guides the other members of the walkthrough team through the document to uncover any faults. It is not the task of the team to correct faults, but merely to record them for later correction. There are four reasons for this: 

1. A correction produced by a committee (that is, the walkthrough team) within the time constraints of the walkthrough is likely to be lower in quality than a correction produced by an individual trained in the necessary techniques. 

2. A correction produced by a walkthrough team of fi ve individuals takes at least as much time as a correction produced by one person and, therefore, costs fi ve times as much when the salaries of the fi ve participants are considered. 

3. Not all items fl agged as faults actually are incorrect. In accordance with the dictum, “If it ain’t broke, don’t fi x it,” it is better for faults to be analyzed methodically and corrected only if there really is a problem, rather than have a team attempt to “fi x” something that is completely correct. 

4. There simply is not enough time in a walkthrough to both detect and correct faults. No walkthrough should last longer than 2 hours. The time should be spent detecting and recording faults, not correcting them. 

There are two ways of conducting a walkthrough. The fi rst is participant driven. Participants present their lists of unclear items and items they think are incorrect. The representative of the analysis team must respond to each query, clarifying what is unclear to the reviewer and either agreeing that indeed there is a fault or explaining why the reviewer is mistaken. 

The second way of conducting a review is document driven. A person responsible for the document, either individually or as part of a team, walks the participants through that document, with the reviewers interrupting either with their prepared comments or comments triggered by the presentation. This second approach is likely to be more thorough. In addition, it generally leads to the detection of more faults because the majority of faults at a document-driven walkthrough are spontaneously detected by the presenter. Time after time, the presenter will pause in the middle of a sentence, his or her face will light up, and a fault, one that has lain dormant through many readings of the document, suddenly becomes obvious. A fruitful fi eld for research by a psychologist would be to determine why verbalization so often leads to fault detection during walkthroughs of all kinds, including requirements walkthroughs, analysis walkthroughs, design walkthroughs, plan walkthroughs, and code walkthroughs. Not surprisingly, the more thorough documentdriven review is the technique prescribed in the IEEE Standard for Software Reviews [IEEE 1028, 1997]. 

The primary role of the walkthrough leader is to elicit questions and facilitate discussion. A walkthrough is an interactive process; it is not supposed to be one-sided instruction by the presenter. It also is essential that the walkthrough not be used as a means of evaluating the participants. If that happens, the walkthrough degenerates into a point-scoring session and does not detect faults, no matter how well the session leader tries to run it. It has been suggested that the manager who is responsible for the document being reviewed should be a member of the walkthrough team. If this manager also is responsible for the annual evalu ations of the members of the walkthrough team (and particularly of the presenter), the fault detection capabilities of the team will be compromised, because the primary motive of the presenter will be to minimize the number of faults that show up. To prevent this confl ict of interests, the person responsible for a given workfl ow should not also be directly responsible for evaluating any member of the walkthrough team for that workfl ow. 

## 6.2.3 Inspections

Inspections were fi rst proposed by Fagan [1976] for testing designs and code. An inspection goes far beyond a walkthrough and has fi ve formal steps. 

1. An overview of the document to be inspected (requirements, specifi cation, design, code, or plan) is given by one of the individuals responsible for producing that document. At the end of the overview session, the document is distributed to the participants. 

2. In the preparation , the participants try to understand the document in detail. Lists of fault types found in recent inspections, with the fault types ranked by frequency, are excellent aids. These lists help team members concentrate on the areas where the most faults have occurred. 

3. To begin the inspection, one participant walks through the document with the inspection team, ensuring that every item is covered and that every branch is taken at least once. Then fault fi nding commences. As with walkthroughs, the purpose is to fi nd and document the faults, not to correct them. Within one day the leader of the inspection team (the moderator ) must produce a written report of the inspection to ensure meticulous follow-through. 

4. In the rework , the individual responsible for the document resolves all faults and problems noted in the written report. 

5. In the follow-up , the moderator must ensure that every issue raised has been resolved satisfactorily, by either fi xing the document or clarifying items incorrectly fl agged as faults. All fi xes must be checked to ensure that no new faults have been introduced [Fagan, 1986]. If more than 5 percent of the material inspected has been reworked, then the team must reconvene for a 100 percent reinspection. 

The inspection should be conducted by a team of four. For example, in the case of a design inspection, the team consists of a moderator, designer, implementer, and tester. The moderator is both manager and leader of the inspection team. There must be a representative of the team responsible for the current workfl ow as well as a representative of the team responsible for the next workfl ow. The designer is a member of the team that produced the design, whereas the implementer is responsible, either individually or as part of a team, for translating the design into code. Fagan suggests that the tester be any programmer responsible for setting up test cases; it is, of course, preferable that the tester be a member of the SQA group. The IEEE standard recommends a team of between three and six participants [IEEE 1028, 1997]. Special roles are played by the moderator, the reader who leads the team through the design, and the recorder responsible for producing a written report of the detected faults. 

An essential component of an inspection is the checklist of potential faults. For example, the checklist for a design inspection should include items such as these: Is each item of the specifi cation document adequately and correctly addressed? For each interface, do the actual and formal arguments correspond? Have error-handling mechanisms been adequately identifi ed? Is the design compatible with the hardware resources or does it require more hardware than actually is available? Is the design compatible with the software resources; for example, does the operating system stipulated in the analysis artifacts have the functionality required by the design? 

An important component of the inspection procedure is the record of fault statistics. Faults must be recorded by severity (major or minor; an example of a major fault is one that causes premature termination or damages a database) and fault type. In the case of a design inspection, typical fault types include interface faults and logic faults. This information can be used in a number of useful ways: 

• The number of faults in a given product can be compared with averages of faults detected at the same stage of development in comparable products, giving management an early warning that something is amiss and allowing timely corrective action to be taken. 

• If inspecting two or three code artifacts results in the discovery of a disproportionate number of faults of a particular type, management can begin checking other code artifacts for faults of that type, and take corrective action if necessary. 

• If the inspection of a particular code artifact reveals far more faults than were found in any other code artifact in the product, there is usually a strong case for redesigning that artifact from scratch and implementing the new design. 

• Information regarding the number and types of faults detected at an inspection of a design artifact aids the team performing the code inspection of the implementation of that artifact at a later stage. 

The fi rst experiment of Fagan [1976] was performed on a systems product. One hundred person-hours were devoted to inspections, at a rate of two 2-hour inspections per day by a four-person team. Of all the faults found during the development of the product, 67 percent were located by inspections before unit testing was started. Furthermore, during the fi rst 7 months after the product was installed, 38 percent fewer faults were detected in the inspected product than in a comparable product reviewed using informal walkthroughs 

Fagan [1976] conducted another experiment on an application product and found that 82 percent of all detected faults were discovered during design and code inspections. A useful side effect of the inspections was that programmer productivity rose because less time had to be spent on unit testing. Using an automated estimating model, Fagan determined that, as a result of the inspection process, the savings on programmer resources were 25 percent despite the time that had to be devoted to the inspections. In a different experiment Jones [1978] found that over 70 percent of detected faults could be detected by conducting design and code inspections. 

Subsequent studies have produced equally impressive results. In a 6000-line business data-processing application, 93 percent of all detected faults were found during inspections [Fagan, 1986]. As reported in [Ackerman, Buchwald, and Lewski, 1989], the use of inspections rather than testing during the development of an operating system decreased the cost of detecting a fault by 85 percent; in a switching system product, the decrease was 90 percent [Fowler, 1986]. At the Jet Propulsion Laboratory (JPL), on average, each 2-hour inspection exposed 4 major faults and 14 minor faults [Bush, 1990]. Translated into dollar terms, this meant a saving of approximately $25,000 per inspection . Another JPL study [Kelly, Sherif, and Hops, 1992] showed that the number of faults detected decreased exponentially by classical phase. In other words, with the aid of inspections, faults can be detected early in the software process. The importance of this early detection is refl ected in Figure 1.6 . 

One advantage that code inspections have over running test cases (execution-based test ing) is that the testers need not deal with failures. It frequently happens that, when a product under test is executed, it fails. The fault that caused the failure must now be located and fi xed before execution-based testing can continue. In contrast, a fault found in the code during non-execution-based testing is logged and the review continues. 

A risk of the inspection process is that, like the walkthrough, it might be used for performance appraisal. The danger is particularly acute in the case of inspections because of the detailed fault information available. Fagan dismisses this fear by stating that, over a period of 3 years, he knew of no IBM manager who used such information against a programmer, or as he put it, no manager tried to “kill the goose that lays the golden eggs” [Fagan, 1976]. However, if inspections are not conducted properly, they may not be as wildly successful as they have been at IBM. Unless top management is aware of the potential problem, misuse of inspection information is a distinct possibility. 

## 6.2.4 Comparison of Inspections and Walkthroughs

Superfi cially, the difference between an inspection and a walkthrough is that the inspection team uses a checklist of queries to aid it in fi nding the faults. But the difference goes deeper than that. A walkthrough is a two-step process: preparation followed by team analysis of the document. 

An inspection is a fi ve-step process: overview, preparation, inspection, rework, and follow-up; and the procedure to be followed in each step is formalized. Examples of such formalization are the methodical categorization of faults and the use of that information in the inspection of the documents of the succeeding workfl ows as well as in inspections of future products. 

The inspection process takes much longer than a walkthrough. Is inspection worth the additional time and effort? The data of Section 6.2.3 clearly indicate that inspections are a powerful, cost-effective tool to detect faults. 

## 6.2.5 Strengths and Weaknesses of Reviews

There are two major strengths of a review (walkthrough or inspection). First, a review is an effective way to detect a fault; second, faults are detected early in the software process, that is, before they become expensive to fi x. For example, design faults are detected before implementation commences, and coding faults are found before the artifact is integrated into the product. 

However, the effectiveness of a review can be reduced if the software process is inadequate. 

• First, large-scale software is extremely hard to review unless it consists of smaller, largely independent components. A strength of the object-oriented paradigm is that, if correctly carried out, the resulting product consists of largely independent pieces. 

• Second, a design review team sometimes has to refer to the analysis artifacts; a code review team often needs access to the design documents. Unless the documentation of the previous workfl ows is complete, updated to refl ect the current version of the project, and available online, the effectiveness of review teams is severely hampered. 

## 6.2.6 Metrics for Inspections

To determine the effectiveness of inspections, a number of different metrics can be used. The fi rst is the inspection rate . When specifications and designs are inspected, the number of pages inspected per hour can be measured; for code inspections, an appropriate metric is lines of code inspected per hour. A second metric is the fault density , measured in faults per page inspected or faults per 1000 lines of code (KLOC) inspected. This metric can be subdivided into major faults per unit of material and minor faults per unit of material. Another useful metric is the fault detection rate , that is, the number of major and minor faults detected per hour. A fourth metric is the fault detection effi ciency , that is, the number of major and minor faults detected per person-hour. 

Although the purpose of these metrics is to measure the effectiveness of the inspection process, the results instead may refl ect defi ciencies of the development team. For example, if the fault detection rate suddenly rises from 20 faults per thousand lines of code to 30, this does not necessarily mean that the inspection team has suddenly become 50 percent more effi cient. Another explanation could be that the quality of code has decreased and there simply are more faults to be detected. 

Having discussed non-execution-based testing, we now move on to execution-based testing 

## 6.3 Execution-Based Testing

It has been claimed that testing is a demonstration that faults (“bugs”) are not present. Even though some organizations spend up to 50 percent of their software budget on testing, delivered “tested” software is notoriously unreliable. 

The reason for this contradiction is simple. As Dijkstra put it, “Program testing can be a very effective way to show the presence of bugs, but it is hopelessly inadequate for showing their absence” [Dijkstra, 1972]. What Dijkstra is saying is that, if a product is executed with test data and the output is wrong, then the product defi nitely contains a fault. But, if the output is correct, then there still may be a fault in the product; the only information that can be deduced from that particular test is that the product runs correctly on that particular set of test data. 

## 6.4 What Should Be Tested?

To be able to describe what properties should be tested, it is fi rst necessary to give a precise description of execution-based testing. According to Goodenough [1979], executionbased testing is a process of inferring certain behavioral properties of a product based, in part, on the results of executing the product in a known environment with selected inputs. This defi nition has three troubling implications. 

1. First, the defi nition states that testing is an inferential process. The tester takes the product, runs it with known input data, and examines the output. The tester has to infer what, if anything, is wrong with the product. From this viewpoint, testing is comparable to trying to fi nd the proverbial black cat in a dark room, but without knowing whether or not a cat is in the room in the fi rst place. The tester has few clues to help fi nd any faults: perhaps 10 or 20 sets of inputs and corresponding outputs, possibly a user fault report, and thousands of lines of code. From this, the tester has to deduce if there is a fault and, if so, what it is. 

2. A problem with the defi nition arises from the phrase in a known environment . We never really can know our environment, either the hardware or the software. We never can be certain that the operating system is functioning correctly or that the run-time routines are correct. An intermittent hardware fault may lie in the main memory of the computer. So what is observed as the behavior of the product in fact may be a correct product interacting with a faulty compiler or faulty hardware or some other faulty component of the environment. 

3. Another worrisome part of the defi nition of execution-based testing is the phrase with selected inputs . In the case of a real-time system, frequently no control is possible over the inputs to the system. Consider avionics software. The fl ight control system has two types of inputs. The fi rst type of input is what the pilot wants the aircraft to do. If the pilot pulls back on the joystick to climb or opens the throttle to increase the speed of the aircraft, these mechanical motions are transformed into digital signals sent to the fl ight control computer. The second type of input is the current physical state of the aircraft, such as its altitude, speed, and the elevation of the wing fl aps. The fl ight control software uses the values of such quantities to compute what signals should be sent to the components of the aircraft, such as the wing fl aps and the engines, to implement the pilot’s directives. Whereas the pilot’s inputs can easily be set to any desired values simply by setting the aircraft’s controls appropriately, the inputs corresponding to the current physical state of the aircraft cannot be manipulated so easily. In fact, there is no way one can force the aircraft to provide “selected inputs.” 

How then can such a real-time system be tested? The answer is to use a simulator. A simulator is a working model of the environment in which the product, in this case the fl ight control software, executes. The fl ight control software can be tested by causing the simulator to send selected inputs to the fl ight control software. The simulator has controls that allow the operator to set an input variable to any selected value. If the purpose of the test is to determine how the fl ight control software performs if one engine catches fi re, then the controls of the simulator are set so that the inputs sent to the fl ight control software are indistinguishable from the inputs that would be sent if an engine of the actual aircraft were on fi re. The output is analyzed by examining the output signals sent from the fl ight control software to the simulator. But, at best, a simulator can be a good approximation of a faithful model of some aspect of the system; it never can be the system itself. Using a simulator means that, whereas there indeed is a “known environment,” there is little likelihood that this known environment is in every way identical to the actual environment in which the product will be installed. 

The preceding defi nition of testing speaks of “behavioral properties.” What behavioral properties must be tested? An obvious answer is, Test whether the product functions correctly. But, as will be shown, correctness is neither necessary nor suffi cient. Before discussing correctness, four other behavioral properties are considered: utility, reliability, robustness, and performance [Goodenough, 1979]. 

## 6.4.1 Utility

Utility is the extent to which a user’s needs are met when a correct product is used under conditions permitted by its specifi cations. In other words, a product that is functioning correctly is now subjected to inputs that are valid in terms of the specifi cations. The user may test, for example, how easy the product is to use, whether the product performs useful functions, and whether the product is cost effective compared to competing products. Irrespective of whether the product is correct or not, these vital issues have to be tested. If the product is not cost effective, then there is no point in buying it. And unless the product is easy to use, it will not be used at all or it will be used incorrectly. Therefore, when considering buying an existing product (including shrink-wrapped software), the utility of the product should be tested fi rst, and if the product fails on that score, testing should stop. 

## 6.4.2 Reliability

Another aspect of a product that must be tested is its reliability. Reliability is a measure of the frequency and criticality of product failure; recall that a failure is an unacceptable effect or behavior, under permissible operating conditions, that occurs as a consequence of a fault. In other words, it is necessary to know how often the product fails ( mean time between failures ) and how bad the effects of that failure can be. When a product fails, an important issue is how long it takes, on average, to repair it ( mean time to repair ). But, often more important is how long it takes to repair the results of the failure. This last point frequently is overlooked. Suppose that the software running on a communications front end fails, on average, only once every 6 months; but when it fails, it completely wipes out a database. At best, the database can be reinitialized to its status when the last checkpoint dump was taken, and the audit trail can then be used to put the database into a state that is virtually up to date. But, if this recovery process takes the better part of 2 days, during which time the database and communications front end are inoperative, then the reliability of the product is low, notwithstanding that the mean time between failures is 6 months. 

An embedded computer is an integral part of a larger system whose primary purpose is not computation. The function of embedded software is to control the device in which the computer is embedded. Military examples include a network of avionics computers on board a warplane or a computer built into an intercontinental ballistic missile. The embedded computer in the nose cone of a missile controls only that missile; it cannot be used, say, for printing the payroll checks for the soldiers on the missile base. 

More familiar examples are the computer chip in a digital watch or a washing machine. Again, the chip in a washing machine is used exclusively to control the washing machine. There is no way that the owner of that washing machine could use the chip to balance a checkbook. 

## 6.4.3 Robustness

Another aspect of every product that requires testing is its robustness. Although it is diffi cult to come up with a precise defi nition, robustness essentially is a function of a number of factors, such as the range of operating conditions, the possibility of unacceptable results with valid input, and the acceptability of effects when the product is given invalid input. A product with a wide range of permissible operating conditions is more robust than a more-restrictive product. A robust product should not yield unacceptable results when the input satisfi es its specifi cations; for example, giving a valid command should not have disastrous consequences. A robust product should not crash when the product is not used under permissible operating conditions. To test for this aspect of robustness, test data that do not satisfy the input specifi cations are deliberately entered, and the tester determines how badly the product reacts. For example, when the product solicits a name, the tester may reply with a stream of unacceptable characters, such as control-A escape-% ?$#@. If the computer responds with a message such as Incorrect data—Try again or, better, informs the user as to why the data do not conform to what was expected, it is more robust than a product that crashes whenever the data deviate even slightly from what is required. 

## 6.4.4 Performance

Performance is another aspect of the product that must be tested. For example, it is essential to know the extent to which the product meets its constraints with regard to response time or space requirements. For an embedded computer system such as an onboard computer in a handheld antiaircraft missile, the space constraints of the system may be such that only 128 megabytes (MB) of main memory are available for the software. No matter how excellent the software may be, if it needs 256 MB of main memory, then it cannot be used at all. (For more information on embedded software, see Just in Case You Wanted to Know Box 6.2.) 

Real-time software is characterized by hard time constraints, that is, time constraints of such a nature that, if a constraint is not met, information is lost. For example, a nuclear reactor control system may have to sample the temperature of the core and process the data every 10th of a second. If the system is not fast enough to handle interrupts from the temperature sensor every 10th of a second, then data are lost, and there is no way of ever recovering the data; the next time the system receives temperature data, it will be the current temperature, not the reading that was missed. If the reactor is on the point of a meltdown, then it is critical that all relevant information be both received and processed as laid down in the specifi cations. With all real-time systems, the performance must meet every time constraint listed in the specifi cations. 

## 6.4.5 Correctness

Finally, a defi nition of correctness can be given. A product is correct if it satisfi es its output specifi cations, independent of its use of computing resources, when operated under permitted conditions [Goodenough, 1979]. In other words, if input that satisfi es the input specifi cations is provided and the product is given all the resources it needs, then the product is correct if the output satisfi es the output specifi cations. 

This defi nition of correctness , like the defi nition of testing itself, has worrisome implications. Suppose a product has been tested successfully against a broad variety of test data. Does this mean that the product is acceptable? Unfortunately, it does not. If a product is correct, all that means is that it satisfi es its specifi cations. But what if the specifi cations themselves are incorrect? To illustrate this diffi culty, consider the specifi cation shown in Figure 6.1 . The specifi cations state that the input to the sort is an array p of n integers, whereas the output is another array q sorted in nondecreasing order. Superfi cially, the specifi cations seem perfectly correct. But consider method trickSort shown in Figure 6.2 . In that method, all n elements of array q are set to 0. The method satisfi es the specifi cations of Figure 6.1 and is therefore correct. 

What happened? Unfortunately, the specifi cations of Figure 6.1 are wrong. What has been omitted is a statement that the elements of q, the output array, are a permutation (rearrangement) of the elements of the input array p. An intrinsic aspect of sorting is that it is a rearrangement process. And the method of Figure 6.2 capitalizes on this specifi cation fault. In other words, the method trickSort is correct, but the specifi cations of Figure 6.1 are wrong. Corrected specifi cations appear in Figure 6.3 . From this example, it is clear that the consequences of specifi cation faults are nontrivial. After all, the correctness of a product is meaningless if its specifi cations are incorrect. 

The fact that a product is correct is not suffi cient , because the specifi cations in terms of which it was shown to be correct may be wrong. But is it necessary ? Consider the following example. A software organization has acquired a superb new C++ compiler. The new 

FIGURE 6.1 Incorrect specifi cations for a sort. 

<table><tr><td>Input specification:</td><td>p : array of n integers, n &gt; 0.</td></tr><tr><td>Output specification:</td><td>q : array of n integers such that q[0] ≤ q[1] ≤ ⋯ ≤ q[n - 1]</td></tr></table>

```txt
FIGURE 6.2 void trickSort (int p[ ], int q[ ])
Method {
    int i;
    for (i = 0; i < n; i++)
    q[i] = 0;
}
specifications of
Figure 6.1. 
```

<table><tr><td>Input specification:</td><td>p : array of n integers, n &gt; 0.</td></tr><tr><td>Output specification:</td><td>q : array of n integers such that<eq>q[0] \leq q[1] \leq \cdots \leq q[n - 1]</eq>The elements of array q are a permutation of the elements of array p, which are unchanged.</td></tr></table>

compiler can translate twice as many lines of source code per second as the old compiler, the object code runs nearly 45 percent faster, and the size of the object code is about 20 percent smaller. In addition, the error messages are much clearer and the cost of postdelivery maintenance and updates is less than half of that of the old compiler. There is one problem, however; the fi rst time that a for statement appears in any class, the compiler prints a spurious error message. The compiler therefore is not correct, because the specifi cations for a compiler implicitly or explicitly require that error messages be printed if, and only if, there is a fault in the source code. It is certainly possible to use the compiler—in fact, in every way but one the compiler is absolutely ideal. Furthermore, it is reasonable to expect that this minor fault will be corrected in the next release. In the meantime, the programmers learn to ignore the spurious error message. Not only can the organization live with the incorrect compiler, but if anyone were to suggest replacing it with the old correct compiler, there would be an outcry. Therefore, the correctness of a product is neither necessary nor suffi cient. 

Both preceding examples admittedly are somewhat artifi cial. But they do make the point that correctness simply means that the product is a correct implementation of its specifi cations. In other words, there is more to testing than just showing that the product is correct. 

With all the diffi culties associated with execution-based testing, computer scientists have tried to come up with other ways of ensuring that a product does what it is supposed to do. One such non-execution-based alternative that has received considerable attention for more than 50 years is correctness proving. 

## 6.5 Testing versus Correctness Proofs

A correctness proof is a mathematical technique for showing that a product is correct, in other words, that it satisfi es its specifi cations. The technique is sometimes termed verifi - cation . However, as previously pointed out, the term has another meaning within the testing context. In addition, verifi cation is also often used to denote all non-execution-based techniques, not only correctness proving. For clarity, this mathematical procedure will be termed correctness proving , to remind the reader that it is a mathematical proof process 

## 6.5.1 Example of a Correctness Proof

To see how correctness is proven, consider the code fragment shown in Figure 6.4 . The fl owchart equivalent to the code is given in Figure 6.5 . We now show that the code fragment is correct—after the code has been executed, the variable s will contain the sum of the n elements of the array y. In Figure 6.6 , an assertion is placed before and after each statement, at the places labeled with the letters A through H ; that is, a claim has been made at each place that a certain mathematical property holds there. The correctness of each assertion is now proven. 

```txt
int k, s;
int y[n];
k = 0;
s = 0;
while (k < n)
{
    s = s + y[k];
    k = k + 1;
} 
```

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/534379268b316245a3279c54be31c106f5ad407be5239eb555dca036b27cae1d.jpg)


The input specifi cation, the condition that holds at A before the code is executed, is that the variable n is a positive integer; that is, 

$$
A: \quad n \in \{1, 2, 3, \dots \}\tag{6.1}
$$

An obvious output specifi cation is that, if control reaches point H , the value of s contains the sum of the n values stored in array y, that is, 

$$
H: \quad s = y [ 0 ] + y [ 1 ] + \dots + y [ n - 1 ]\tag{6.2}
$$

In fact, the code fragment can be proven correct with respect to a stronger output specifi cation: 

$$
H: \quad k = n \text { and } s = y [ 0 ] + y [ 1 ] + \dots + y [ n - 1 ]\tag{6.3}
$$


FIGURE 6.6 Figure 6.5 with input specifi cation, output specifi cation, loop invariant, and assertions added.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1ce9ee98-da07-4d0b-847b-a174047bcb19/d04832dc2819a3a38b76af2ad7971709eb6d7095ba20c36c94e4f8bb0235e04d.jpg)


A natural reaction to the last sentence is to ask, From where did output specifi cation (6.3) come? By the end of the proof, we hope you have the answer to that question. 

In addition to the input and output specifi cations, a third aspect of the proof process is to provide an invariant for the loop. That is, a mathematical expression must be provided that holds at point D irrespective of whether the loop has been executed 0, 1, or many times. The loop invariant that will be proven to hold is 

$$
D: \quad k \leq n \text {   and   } s = y [ 0 ] + y [ 1 ] + \dots + y [ k - 1 ]\tag{6.4}
$$

Now it will be shown that if input specifi cation (6.1) holds at point A , then output specifi cation (6.3) will hold at point $H ;$ that is, the code fragment will be proven to be correct. 

First, the assignment statement ${ \sf k }  0$ is executed. Control now is at point $B ,$ where the following assertion holds: 

$$
B: \quad k = 0\tag{6.5}
$$

To be more precise, at point B , the assertion should read ${ \sf k } = 0$ and $\mathsf { n } \in \{ 1 , 2 , 3 , \ldots \}$ However, the input specifi cation (6.1) holds at all points in the fl owchart. For brevity, the and $\mathsf { n } \in \{ 1 , 2 , 3 , \ldots \}$ therefore is omitted from now on. 

At point C , as a consequence of the second assignment statement, $s \gets 0$ , the following assertion is true: 

$$
C: \quad k = 0 \text {   and   } s = 0\tag{6.6}
$$

Now the loop is entered. It will be proven by induction that the loop invariant (6.4) indeed is correct. Just before the loop is executed for the fi rst time, assertion (6.6) holds; that is, ${ \sf k } = 0 $ , and $s = 0$ . Now consider loop invariant (6.4). Because ${ \sf k } = 0$ by assertion (6.6) and ${ \mathsf n } \geq 1$ from input specifi cation (6.1), it follows that ${ \sf k } \le { \sf n }$ as required. Furthermore, because ${ \sf k } = 0$ , it follows that $\ v { k } - \ v { I } _ { 1 } = - \ v { I }$ , so the sum in (6.4) is empty and $s = 0$ as required. Loop invariant (6.4) therefore is true just before the fi rst time the loop is entered. 

Next, the inductive hypothesis step is performed. Assume that, at some stage during the execution of the code fragment, the loop invariant holds. That is, for k equal to some value $\mathsf { k } _ { 0 } , 0 \leq \mathsf { k } _ { 0 } \leq \mathsf { n }$ , execution is at point D , and the assertion that holds is 

$$
D: \quad k _ {0} \leq n \text {   and   } s = y [ 0 ] + y [ 1 ] + \dots + y [ k _ {0} - 1 ]\tag{6.7}
$$

Control now passes to the test box. If $\mathsf { k } _ { 0 } \geq \mathsf { n }$ , then because $\mathsf { k } _ { 0 } \le \mathsf { n }$ by hypothesis, it follows that $\mathsf { k } _ { 0 } = \mathsf { n }$ . By inductive hypothesis (6.7), this implies that 

$$
H: \quad k _ {0} = n \text {   and   } s = y [ 0 ] + y [ 1 ] + \dots + y [ n - 1 ]\tag{6.8}
$$

which is precisely the output specifi cation (6.3). 

On the other hand, if the test is ${ \sf k } _ { 0 } \geq { \sf n } ?$ fails, then control passes from point D to point E . Because $\mathsf { k } _ { 0 }$ is not greater than or equal to $\mathsf { n } , \mathsf { k } _ { 0 } < \mathsf { n }$ and (6.7) becomes 

$$
E: \quad k _ {0} <   n \text {   and   } s = y [ 0 ] + y [ 1 ] + \dots + y [ k _ {0} - 1 ]\tag{6.9}
$$

The statement $\mathsf { s } \gets \mathsf { s } + \mathsf { y } [ \mathsf { k } _ { 0 } ]$ now is executed, so from assertion (6.9), at point $F ,$ the following assertion must hold: 

$$
\begin{array}{r l} F \colon & k _ {0} <   n \text { and } s = y [ 0 ] + y [ 1 ] + \dots + y [ k _ {0} - 1 ] + y [ k _ {0} ] \\ & = y [ 0 ] + y [ 1 ] + \dots + y [ k _ {0} ] \end{array}\tag{6.10}
$$

The next statement to be executed is $\mathsf { k } _ { 0 } \gets \mathsf { k } _ { 0 } + 1$ . To see the effect of this statement, suppose that the value of $\mathsf { k } _ { 0 }$ before executing this statement is 17. Then the last term in the sum in (6.10) is y[17]. Now the value of $\mathbf { \dot { k } } _ { 0 }$ is increased by 1 to 18. The sum s is unchanged, so the last term in the sum still is y[17], which is now $\mathsf { y } [ \mathsf { k } _ { 0 } - 1 ]$ . Also, at point $\boldsymbol { F } , \mathsf { k } _ { 0 } < \mathsf { n }$ Increasing the value of $\mathbf { \dot { k } } _ { 0 }$ by 1 means that if the inequality is to hold at point $G ,$ , then $\mathsf { k } _ { 0 } \leq \mathsf { n }$ Therefore, the effect of increasing $\mathsf { k } _ { 0 }$ by 1 is that the following assertion holds at point G : 

$$
G: \quad k _ {0} \leq n \text {   and   } s = y [ 0 ] + y [ 1 ] + \dots + y [ k _ {0} - 1 ]\tag{6.11}
$$

Assertion (6.11) that holds at point G is identical to assertion (6.7) that, by assumption, holds at point D. But point D is topologically identical to point G. In other words, if (6.7) holds at D for $\mathbf { k } = \mathbf { k } _ { 0 } ,$ , then it again will hold at D with $\mathsf { k } = \mathsf { k } _ { 0 } + 1$ . It has been shown that the loop invariant holds for ${ \sf k } = 0$ . By induction, it follows that loop invariant (6.4) holds for all values of k, $0 \leq \boldsymbol { \mathsf { k } } \leq \boldsymbol { \mathsf { n } }$ 

All that remains is to prove that the loop terminates. Initially, by assertion (6.6), the value of k is equal to 0. Each iteration of the loop increases the value of k by 1 when the statement $\mathsf { k } \gets \mathsf { k } + \mathsf { 1 }$ is executed. Eventually, k must reach the value n, at which time the loop is exited and the value of s is given by assertion (6.8), thereby satisfying output specifi cation (6.3). 

To review, given the input specifi cation (6.1), it was proven that loop invariant (6.4) holds whether the loop has been executed 0, 1, or more times. Furthermore, it was proven that after n iterations the loop terminates; and when it does, the values of k and s satisfy the output specifi cation (6.3). In other words, the code fragment of Figure 6.4 has been mathematically proven to be correct. 

## Correctness Proof Mini Case Study

An important aspect of correctness proofs is that they should be done in conjunction with design and coding. As Dijkstra put it, “The programmer should let the program proof and program grow hand in hand” [Dijkstra, 1972]. For example, when a loop is incorporated into the design, a loop invariant is put forward; and as the design is refi ned stepwise, so is the invariant. Developing a product in this way gives the programmer confi dence that the product is correct and tends to reduce the number of faults. Quoting Dijkstra again, “The only effective way to raise the confi dence level of a program signifi cantly is to give a convincing proof of its correctness” [Dijkstra, 1972]. But even if a product is proven to be correct, it must be thoroughly tested as well. To illustrate the necessity for testing in conjunction with correctness proving, consider the following. 

In 1969, Naur reported on a technique for constructing and proving a product correct [Naur, 1969]. The technique was illustrated by what Naur termed a line-editing problem; today this would be considered a text-processing problem. It may be stated as follows: 

Given a text consisting of words separated by blank characters or by newline (new line) characters, convert it to line-by-line form in accordance with the following rules: 

1. Line breaks must be made only where the given text contains a blank or newline; 

2. Each line is fi lled as far as possible, as long as 

3. No line will contain more than maxpos characters. 

Naur constructed a procedure using his technique and informally proved its correctness. The procedure consisted of approximately 25 lines of code. The paper then was reviewed by Leavenworth in Computing Reviews [Leavenworth, 1970]. The reviewer pointed out that, in the output of Naur’s procedure, the fi rst word of the fi rst line is preceded by a blank unless the fi rst word is exactly maxpos characters long. Although this may seem a trivial fault, it is a fault that surely would have been detected had the procedure been tested, that is, executed with test data rather than only proven correct. But worse was to come. London [1971] detected three additional faults in Naur’s procedure. One is that the procedure does not terminate unless a word longer than maxpos characters is encountered. Again, this fault is likely to have been detected if the procedure had been tested. London then presented a corrected version of the procedure and proved formally that the resulting procedure was correct; recal that Naur had used only informal proof techniques. 

The next episode in this saga is that Goodenough and Gerhart [1975] found three faults that London had not detected, despite his formal “proof.” These included the fact that the last word is not output unless it is followed by a blank or newline. Yet again, a reasonable choice of test data would have detected this fault without much diffi culty. In fact, of the total of seven faults collectively detected by Leavenworth, London, and Goodenough and Gerhart, four could have been detected simply by running the procedure on test data, such as the illustrations given in Naur’s original paper. The lesson from this saga is clear. Even if a product has been proven correct, it still must be tested thoroughly. 

The example in Section 6.5.1 showed that proving the correctness of even a small code fragment can be a lengthy process. Furthermore, the mini case study of this section showed that it is a diffi cult, error-prone process, even for a 25-line procedure. The following issue therefore must be put forward: Is correctness proving just an interesting research idea or is it a powerful software engineering technique whose time has come? This is answered in Section 6.5.3. 

## 6.5.3 Correctness Proofs and Software Engineering

A number of software engineering practitioners have put forward reasons why correctness proving should not be viewed as a standard software engineering technique. First, it is claimed that software engineers lack adequate mathematical training. Second, it is suggested that proving is too expensive to be practical; and third, proving is too hard. Each of these reasons will be shown to be an oversimplifi cation: 

1. Although the proof given in Section 6.5.1 can be understood with hardly more than high school algebra, nontrivial proofs require that input specifi cations, output specifi cations, and loop invariants be expressed in fi rst- or second-order predicate calculus or its equivalent. Not only does this make the proof process simpler for a mathematician, it allows correctness proving to be done by a computer. To complicate matters further, predicate calculus now is somewhat outdated. To prove the correctness of concurrent products, techniques using temporal or other modal logics are required [Manna and Pnueli, 1992]. There is no doubt that correctness proving requires training in mathematical logic. Fortunately, most computer science majors today either take courses in the requisite material or have the background to learn correctness-proving techniques on the job. Therefore, colleges now are turning out computer science graduates with suffi cient mathematical skills for correctness proving. The claim that practicing software engineers lack the necessary mathematical training may have been true in the past, but it no longer applies in the light of the thousands of computer science majors joining the industry each year. 

2. The claim that proving is too expensive for use in software development also is false. On the contrary, the economic viability of correctness proving can be determined on a project-by-project basis using cost–benefi t analysis (Section 5.2). For example, consider the software for the international space station. Human lives are at stake, and if something goes wrong, a space shuttle rescue mission may not arrive in time. The cost of proving life-critical space station software correct is large. But the potential cost of a software fault that might be overlooked if correctness proving is not performed is even larger. 

3. Despite the claim that correctness proving is too hard, many nontrivial products have successfully been proven correct, including operating system kernels, compilers, and communications systems [Landwehr, 1983], [Berry and Wing, 1985]. Furthermore, many tools such as theorem provers assist in correctness proving. A theorem prover takes as input a product, its input and output specifi cations, and loop invariants. The theorem prover then attempts to prove mathematically that the product, when given input data satisfying the input specifi cations, produces output data satisfying the output specifi cations. 

At the same time, there are some diffi culties with correctness proving: 

• For example, how can we be sure that a theorem prover is correct? If the theorem prover prints out This product is correct, can we believe it? To take an extreme case, consider the so-called theorem prover shown in Figure 6.7 . No matter what code is submitted to this theorem prover, it will print out This product is correct. In other words, what reliability can be placed on the output of a theorem prover? One suggestion is to submit a theorem prover to itself and see whether it is correct. Apart from the philosophical implications, a simple way of seeing that this will not work is to consider what would happen if the theorem prover of Figure 6.7 were submitted to itself for proving. As always, it would print out This product is correct, thereby “proving” its own correctness. 

• A further diffi culty is fi nding the input and output specifi cations, and especially the loop invariants or their equivalents in other logics such as modal logic. Suppose a product is correct. Unless a suitable invariant for each loop can be found, there is no way of proving the product correct. Yes, tools do exist to assist in this task. But even with state-ofthe-art tools, a software engineer simply may not be able to come up with a correctness proof. One solution to this problem is to develop the product and proof in parallel, as advocated in Section 6.5.2. When a loop is designed, an invariant for that loop is specifi ed at the same time. With this approach, it is somewhat easier to prove that a code artifact is correct. 

• Worse than not being able to fi nd loop invariants, what if the specifi cations themselves are incorrect? An example of this is method trickSort ( Figure 6.2 ). A good theorem prover, when given the incorrect specifi cations of Figure 6.1 , undoubtedly will declare that the method shown in Figure 6.2 is correct. 

Manna and Waldinger [1978] stated that, “We can never be sure that the specifi cations are correct” and “We can never be certain that a verifi cation system is correct.” These statements from two leading experts in the fi eld encapsulate the various points made previously. 

Does all this mean that there is no place for correctness proofs in software engineering? Quite the contrary. Proving products correct is an important, and sometimes vital, software engineering tool. Proofs are appropriate where human lives are at stake or where otherwise indicated by cost–benefi t analysis. If the cost of proving software correct is less than the probable cost if the product fails, then the product should be proven. However, as the text-processing mini case study shows, proving alone is not enough. Instead, correctness proving should be viewed as an important component of the set of techniques that must be utilized together to check that a product is correct. Because the aim of software engineering is the production of quality software, correctness proving is indeed an important software engineering technique. 

Even when a full formal proof is not justifi ed, the quality of software can be markedly improved through the use of informal proofs. For example, a proof similar to that 

One feature of languages such as Java (but not C or C++) is bounds checking. An example of bounds checking is examining every array index during execution to ensure that it is within its declared range. 

Hoare suggested that using bounds checking while developing a product but turning it off once the product is working correctly can be likened to learning to sail on dry land wearing a life jacket and then taking the life jacket off when actually at sea. In his Turing Award lecture, Hoare [1981] described a compiler he developed in 1961. When users later were offered the opportunity to turn off bounds checking after the fi nal version of the compiler had been installed, they unanimously refused, because they had experienced so many incidents of values out of range during test runs of earlier versions of the compiler. 

Bounds checking can be viewed as a special case of a more general concept, assertion checking. Hoare’s life jacket analogy is equally applicable to turning off assertion checking once the fi nal version has been installed. 

Hoare’s remarks were sadly prophetic. Today, a major technique used by hackers to penetrate computers is to send a long stream of data to an operating system to deliberately cause a buffer to overfl ow and overwrite a portion of the operating system with malicious executable code. This technique can work only if the programmers neglected to include bounds checking in the code for reading data into the buffer of an operating system implemented in C or C++, or turned off bounds checking. 

of Section 6.5.1 assists in checking that a loop is executed the correct number of times. A second way of improving software quality is to insert assertions such as those of Figure 6.6 into the code. Then, if at execution time an assertion does not hold, the product is halted and the software team can investigate whether the assertion that terminated execution is incorrect or whether indeed a fault in the code was detected by triggering the assertion. Languages such as Java (from version 1.4 onward) support assertions directly by means of an assert statement. Suppose that an informal proof requires that the value of variable xxx be positive at a particular point in the code. Even though the members of the design team may be convinced that there is no way for xxx to be negative, for additional reliability they may specify that the statement 

$$
\text { assert } (x x x > 0)
$$

must appear at that point in the code. If xxx is less than or equal to 0, execution terminates, and the situation can be investigated by the software team. Unfortunately, Assert in C++ is a debugging statement, similar to assert in C; it is not part of the language itself. 

Once the users are confi dent that the product works correctly, they have the option of switching off assertion checking. This speeds up execution, but any fault that would have been detected by an assertion may not be found if assertion checking is switched off. Therefore, there is a trade-off between run-time effi ciency and continuing assertion checking even after the product has been installed on the client’s computer. (Just in Case You Wanted to Know Box 6.3 gives an interesting insight on this issue.) 

Model checking is a new technology that may eventually take the place of correctness proving of software. Model checking is outlined in Section 18.11. 

A fundamental issue in execution-based testing is which members of the software development team should be responsible for carrying it out. This is discussed in Section 6.6. 

## 6.6 Who Should Perform Execution-Based Testing?

Suppose a programmer is asked to test a code artifact he or she has implemented. Testing has been described by Myers [1979] as the process of executing a product with the intention of fi nding faults. Testing therefore is a destructive process. On the other hand, the programmer doing the testing ordinarily does not wish to destroy his or her work. If the fundamental attitude of the programmer toward the code is the usual protective one, then the chances of that programmer using test data that will highlight faults is considerably lower than if the major motivation were truly destructive. A successful test fi nds faults. This, too, poses a diffi culty. It means that, if the code artifact passes the test, then the test has failed. Conversely, if the code artifact does not perform according to specifi cations, then the test succeeds. A programmer who is asked to test a code artifact he or she has implemented is being asked to execute the code artifact in such a way that a failure (incorrect behavior) ensues. This goes against the creative instincts of programmers. 

An inescapable conclusion is that programmers should not test their own code artifacts. After a programmer has been con structive and built a code artifact, testing that code artifact requires the creator to perform a de structive act and attempt to destroy that creation. A second reason why execution-based testing should be done by someone else is that the programmer may have misunderstood some aspect of the design or specifi cations. If testing is done by someone else, such faults may be discovered. Nevertheless, debugging (fi nding the cause of the failure and correcting the fault) is best done by the original programmer, the person most familiar with the code. 

The statement that a programmer should not test his or her own code must not be taken too far. Consider the programming process. The programmer begins by reading the detailed design of the code artifact; this may be in the form of a fl owchart or, more likely, pseudocode. But, whatever technique is used, the programmer must certainly desk check the code artifact before entering it into the computer. That is, the programmer must try out the fl owchart or pseudocode with various test cases, tracing through the detailed design to check that each test case is executed correctly. Only when the programmer is satisfi ed that the detailed design is correct should the text editor be invoked to code the artifact. 

Once the code artifact is in machine-readable form, it undergoes a series of tests. Test data are used to determine that the code artifact works successfully, probably the same test data used to desk check the detailed design. Next, if the code artifact executes correctly when correct test data are used, then the programmer tries out incorrect data to test the robustness of the code artifact. When the programmer is satisfi ed that the code artifact operates correctly, systematic testing commences. This systematic testing should not be performed by the programmer. 

If the programmer is not to perform this systematic testing, who is to do it? As stated in Section 6.1.2, independent testing must be performed by the SQA group. The key word here is independent . Only if the SQA group truly is independent of the development team can its members fulfi ll their mission of ensuring that the product indeed satisfi es its specifi - cations, without software development managers applying pressures such as product deadlines that might hamper their work. SQA personnel must report to their own manager and thereby protect their independence. 

How is systematic testing performed? An essential part of a test case is a statement of the expected output before the test is executed. It is a complete waste of time for the tester to sit at a terminal, execute the code artifact, enter haphazard test data, and then peer at the screen and say, “I guess that looks right.” Equally futile is for the tester to plan test cases with great care and execute each test case in turn, look at the output, and say, “Yes, that certainly looks right.” It is far too easy to be fooled by plausible results. If programmers are allowed to test their own code, then there is always the danger that the programmer will see what he or she wants to see. The same danger can occur even when the testing is done by someone else. The solution is for management to insist that, before a test is performed, both the test data and the expected results of that test be recorded. After the test has been performed, the actual results should be recorded and compared with the expected results. 

Even in small organizations and with small products, it is important that this recording be done in machine-readable form, because test cases should never be thrown away. The reason for this is postdelivery maintenance. While the product is being maintained, regression testing must be performed. Stored test cases that the product has previously executed correctly must be rerun to ensure that the modifi cations made to add new functionality to the product have not destroyed the product’s existing functionality. This is dis cussed further in Chapter 16 . 

## 6.7 When Testing Stops

After a product has been successfully maintained for many years, it eventually may lose its usefulness and be superseded by a totally different product, in much the same way that electronic valves were replaced by transistors. Alternatively, a product still may be useful, but the cost of porting it to new hardware or running it under a new operating system may be more than the cost of constructing a new product, using the old one as a prototype. So, fi nally, the software product is decommissioned and removed from service. Only at that point, when the software has been irrevocably discarded, is it time to stop testing. 

Now that all the necessary background material has been covered, objects can be examined in greater detail. This is the subject of Chapter 7. 

Chapter A key theme of this chapter is that testing must be carried out in parallel with all activities of the Review software process. The chapter begins with a description of quality issues (Section 6.1). Next, nonexecution-based testing is described (Section 6.2), with a careful discussion of walkthroughs and inspections. This is followed by a defi nition of execution-based testing (Sections 6.3 and 6.4) and a discussion of behavioral properties of a product that must be tested, including utility, reliability, robustness, performance, and correctness (Sections 6.4.1 through 6.4.5). In Section 6.5, correctness proving is introduced and an example of such a proof is given in Section 6.5.1. The role of correctness proofs in software engineering then is analyzed (Sections 6.5.2 and 6.5.3). Another important issue is that systematic execution-based testing must be performed by the independent SQA group and not by the programmer (Section 6.6). Finally, the issue of when testing can fi nally stop is discussed in Section 6.7. 

## For Further Reading

The attitude of software producers to the testing process has changed over the years, from viewing testing as a means of showing that a product runs correctly to the modern attitude that testing should be used to prevent requirements, analysis, design, and implementation faults. This progression is described in [Gelperin and Hetzel, 1988]. The nature of software testing and the reasons why it is so hard are discussed in [Whittaker, 2000]. The pervasiveness of faults is described in [Lieberman and Fry, 2001]. Ways to reduce the number of faults appear in [Boehm and Basili, 2001] 

Whittaker and Voas [2000] present an interesting theory of reliability. Having an effective requirements workfl ow can have a positive impact on software quality; this is shown in [Damian and Chisan, 2006]. The quality of open-source software is reviewed in [Aberdour, 2007]. 

A standard technique of correctness proving uses the so-called Hoare logic, as described in [Hoare, 1969]. An alternative approach to ensuring that products satisfy their specifi cations is to construct the product stepwise, checking that each step preserves correctness. This is described in [Dijkstra, 1968] and [Wirth, 1971]. An important article regarding acceptance of correctness proofs by the software engineering community is [DeMillo, Lipton, and Perlis, 1979]. Interesting views on correctness proving are given in [Hinchey et al., 2008]. 

The IEEE Standard for Software Reviews [IEEE 1028, 1997] is an excellent source of information on non-execution-based testing. Experiments evaluating inspections of a large-scale software product are described in [Perry et al., 2002]. Vitharana and Ramamurthy [2003] suggest that inspections should be anonymous and computer mediated. The impact of group process support on inspections is presented in [Tyran and George, 2002]. The selection of inspection team members is discussed in [Miller and Yin, 2004]. A review of inspections is given in [Parnas and Lawford, 2003], and the state of the practice is described in [Ciolkowski, Laitenberger, and Biffl , 2003]. Object-oriented code inspections are discussed in [Dunsmore, Roper, and Wood, 2003]. The cost-effectiveness of inspections is presented in [Freimut, Briand, and Vollei, 2005]. Tailoring inspections to an organization’s needs is described in [Denger and Shull, 2007]. Design and code reviews conducted over the Internet are presented in [Meyer, 2008]. An experiment to test the value of the checklists is described in [Hatton, 2008]. 

The classic work on execution-based testing is [Myers, 1979], a work that has had a signifi cant impact on the fi eld of testing. [DeMillo, Lipton, and Sayward, 1978] remains an excellent source of information on selection of test data. [Beizer, 1990] is a compendium on testing, a true handbook on the subject. [Ammann and Offutt, 2008] is strongly recommended as an introduction to testing. 

Turning specifi cally to the object-oriented paradigm, [Kung, Hsia, and Gao, 1998] is a book on object-oriented testing, and so is [Sykes and McGregor, 2000]. 

The proceedings of the IEEE International Symposium on Software Testing and Analysis cover a similar broad spectrum of testing issues. The April 2005 of IEEE Transactions on Software Engineering contains a variety of papers from the 2004 Symposium. Two articles of particular interest are [Ostrand, Weyuker, and Bell, 2005], which describes a method for predicting the location and number of faults in large software products, and [Fu, Milanova, Ryder, Wonnacott, 2005] on the robustness testing of Java server applications. The July–August 2006 issue of IEEE Software contains a wide variety of papers on testing. 

## Key Terms

correctness 166 correctness proof 167 defect 155 desk check 175 error 155 execution-based testing 163 failure 155 fault 155 fault density 162 fault detection effi ciency 162 fault detection rate 162 follow-up 160 

inspection 159 inspection rate 162 loop invariant 169 managerial independence 156 mean time between failures 164 

```txt
mean time to repair 164 quality 156 software quality assurance mistake 155 reader 160 (SQA) 156 model checking 174 recorder 160 systematic testing 175 moderator 160 regression testing 176 test workflow 155 non-execution-based testing 157 reliability 164 testing 155 rework 160 utility 164 overview 159 robustness 165 V & V 155 performance 165 simulator 164 validation 155 preparation 159 verification 155 
```

## Problems

6.1 How are the terms correctness proving, verifi cation, and validation used in this book? 

6.2 A software development organization currently employs 91 software professionals, including 18 managers, all of whom develop as well as test software. The latest fi gures show that 26 percent of their time is spent on testing activities. The average annual cost to the company of a manager is $162,000, whereas nonmanagerial professionals cost $121,000 a year on average; both fi gures include overhead. Use cost–benefi t analysis to determine whether a separate SQA group should be set up within the organization. 

6.3 Repeat the cost–benefi t analysis of Problem 6.2 for a fi rm with only eight software professionals, including three managers. Assume that the other fi gures remain unchanged. 

6.4 You have been testing a code artifact for 11 days and found two faults. What does this tell you about the existence of other faults? 

6.5 What are the similarities between a walkthrough and an inspection? What are the differences? 

6.6 You are a member of the SQA group at Ye Olde Fashioned Software. You suggest to your manager that inspections be introduced. He responds that he sees no reason why four people should waste their time looking for faults when one person can run test cases on the same piece of code. How do you respond? 

6.7 You are the SQA manager at Farm and Field, a national chain of 1539 farm supply stores. Your organization is considering buying a stock-control package for use throughout the organization. Before authorizing the purchase of the package, you decide to test it thoroughly. What properties of the package do you investigate? 

6.8 All 1539 stores in the Farm and Field organization are now to be connected by a communications network. A sales representative is offering you a 6-week free trial to experiment with the communications package he is trying to sell you. What sort of software tests would you perform and why? 

6.9 You are a rear admiral in the Valerian Navy in charge of developing the software for controlling the ship-to-ship missile of Problem 1.4. The software has been delivered to you for acceptance testing. What properties of the software do you test? 

6.10 Consider the following code fragment: 

$$
\begin{array}{l} \text {k = 0;} \\ \text {g = 1;} \\ \text {while (k <   n)} \\ \{\quad \quad \quad \quad \quad \quad \text {k = k + 1;} \\ \quad \quad \quad \quad \quad \text {g = g*k;} \\ \} \end{array}
$$

Prove that this code fragment correctly computes g = n! if n is a positive integer. 6.11 Consider the following code fragment: 

$$
\begin{array}{l} \text {m = 1;} \\ \text {q = 2;} \\ \text {while (m <   n)} \\ \{\quad \quad \quad \quad \quad \text {m = m + 1;} \\ \quad \quad \quad \quad \quad \text {q = q*2;} \\ \} \end{array}
$$

Prove that this code fragment correctly computes ${ \mathsf { q } } = 2 ^ { \mathsf { n } } { \mathrm { ~ i f ~ } } { \mathsf { n } } \in \{ 1 , 2 , 3 , \ldots \}$ 

6.12 Can correctness proving solve the problem that the product as delivered to the client may not be what the client really needs? Give reasons for your answer. 

6.13 How should Dijkstra’s statement (Section 6.3) be changed to apply to correctness proofs rather than testing? Bear in mind the mini case study of Section 6.5.2. 

6.14 Design and implement a solution to the Naur text-processing problem (Section 6.5.2) using the language specifi ed by your instructor. Execute it against test data and record the number of faults you fi nd and the cause of each fault (e.g., logic fault, loop counter fault). Do not correct any of the faults you detect. Now exchange products with a fellow student and see how many faults each of you fi nds in the other’s product and whether or not they are new faults. Again record the cause of each fault and compare the fault types found by each of you. Tabulate the results for the class as a whole. 

6.15 Why is there a need to distinguish between a fault, a failure, and an error? Surely the use of the umbrella term defect simplifi es matters? 

6.16 Give an example of a software product that has been successfully maintained for many years, but has lost its usefulness and has been superseded by a totally different product. 

6.17 (Term Project) Explain how you would test the utility, reliability, robustness, performance, and correctness of the Chocoholics Anonymous product in Appendix A. 

6.18 (Readings in Software Engineering) Your instructor will distribute copies of [Ostrand, Weyuker, and Bell, 2005]. What is your view on using regression models to predict fault numbers and locations? Justify your answer. 

## References



[Aberdour, 2007] M. ABERDOUR, “Achieving Quality in Open-Source Software,” IEEE Software 24 (January–February 2007), pp. 58–64. 





[Ackerman, Buchwald, and Lewski, 1989] A. F. ACKERMAN, L. S. BUCHWALD, AND F. H. LEWSKI, “Software Inspections: An Effective Verifi cation Process,” IEEE Software 6 (May 1989), pp. 31–36. 





[Ammann and Offutt, 2008] P. AMMANN AND J. OFFUTT, Introduction to Software Testing, Cambridge University Press, Cambridge, UK, 2008. 





[Beizer, 1990] B. BEIZER, Software Testing Techniques, 2nd ed., Van Nostrand Reinhold, New York, 1990. 





[Berry and Wing, 1985] D. M. BERRY AND J. M. WING, “Specifying and Prototyping: Some Thoughts on Why They Are Successful,” in: Formal Methods and Software Development, Proceedings of the International Joint Conference on Theory and Practice of Software Development , Vol. 2, Springer-Verlag, Berlin, 1985, pp. 117–28. 

