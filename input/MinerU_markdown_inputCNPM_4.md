object is active from message 5: Determine price of order until message 6: Return price , and similarly for the other objects. 

2. The : Order Class object is created only when the : Assemble Order Control Class sends message 3: Create order to the : Order Class object. This is denoted by the lifeline starting at only the point of dynamic creation. 

3. Figure 17.14 also shows the destruction of the : Order Class object after the : Order Class object receives the message 9: [price too high] Destroy order . The destruction is denoted by the heavy X. 

4. This destruction takes place after a return has taken place, denoted by the dashed horizontal line below event 9, terminated by an open arrow. In the rest of the sequence diagram, each message is eventually followed by a message sent back to the object that sent the original message. In fact, this reciprocity is optional; it is perfectly valid to send a message without eventually receiving any sort of reply. Even if there is a reply, it is not necessary that a specifi c new message be sent back. Instead, a dashed line ending in an open arrow is drawn (a return ) to indicate a return from the original message, as opposed to a new message. 

5. There is a guard on message 9: [price too high] Destroy order . That is, message 9 is sent only if the buyer decides not to purchase the item because the price is too high. A guard (condition) is something that is true or false; only if it is true is the message sent. In Section 17.7, guards are described within the context of statecharts, but here they are used in a sequence diagram. 

(In Figure 17.14 , the message 9: [price too high] Destroy order should be sent from the Buyer to the : User Interface Class object, and the latter should then send a message to the : Assemble Order Control Class object. Next, the : Assemble Order Control Class object should send a message to the : Order Class object, instructing it to destroy the order. To highlight dynamic destruction of an object, these details have been suppressed in Figure 17.14 .) 

Many other options are supported by UML interaction diagrams. For example, suppose we model an elevator going up. We do not know in advance which elevator button will be pressed, so we have no idea how many fl oors up the elevator will go. We model this iteration by labeling the relevant message *move up one fl oor, as shown in Figure 17.15 . The asterisk is, once again, the Kleene star (see Just in Case You Wanted to Know Box 17.1). So this message means, “move up zero or more fl oors.” 

An object can send a message to itself. This is termed a self-call . For example, suppose that the elevator has arrived at a fl oor. The elevator controller sends a message to the elevator doors to open. Once the return has been received, the elevator controller sends a message to itself to start its timer; this self-call is also shown in Figure 17.15 . At the end of the time period, the elevator controller sends a message to the doors to close. When the second return has been received (that is, when the doors have been safely closed), the elevator is instructed to move again. 

Turning now to communication diagrams ( collaboration diagrams in earlier versions of UML), it was stated in Section 13.15.1 that communication diagrams are equivalent to sequence diagrams. So, all the features of sequence diagrams presented in this section are equally applicable to communication diagrams, such as Figure 13.36 

FIGURE 17.15 A sequence diagram showing iteration and self-call. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/e7d77d0e48270b9455977d22af3133bea9687b2bde2f43b3e1470d7d97ddac92.jpg)


## 17.7 Statecharts

Consider the statechart of Figure 17.16 . This is similar to the statechart of Figure 13.25, but modeled using guards instead of events. It shows the start state (the solid circle) with an unlabeled transition leading to state MSG Foundation Event Loop. Five transitions lead from that state, each with a guard, that is, a condition that is true or false. When one of the guards becomes true, the corresponding transition takes place. 

An event also causes transitions between states. A common event is the receipt of a message. Consider Figure 17.17 , which depicts a part of a statechart for an elevator. The elevator is in state Elevator Moving . It stays in motion, performing operation Move up one fl oor , while guard [no message received yet] remains true, until it receives the message Elevator has arrived at fl oor. The receipt of this message (event) causes the guard to be false and also enables a transition to state Stopped At Floor . In this state, the activity Open the elevator doors is performed. 

So far, transition labels have been in the form of [guard] or event . In fact, the most general form of a transition label is 

$$
\text { event   [guard]   /   action }
$$

That is, if event has taken place and [guard] is true, then the transition occurs and, while it is occurring, action is performed. An example of such a transition label is shown in Figure 17.18 , which is equivalent to Figure 17.17 . The transition label is Elevator has arrived at fl oor [a message has been received] / Open the elevator doors . The guard [a message has been received] is true when the event Elevator has arrived at fl oor has occurred and a message to this effect has been sent. The action to be taken, indicated by the instruction following the slash / , is Open the elevator doors. 


FIGURE 17.16 A statechart for the MSG Foundation case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/fb8c3cb480c6c75a9517a5ac3ae2856f8cd05e986547e948d1fc296713399dec.jpg)


Comparing Figures 17.17 and 17.18 , we see that there are two places where an action can be performed in a statechart. First, as refl ected in state Stopped At Floor in Figure 17.17 , an action can be performed when a state is entered. Such an action is called an activity in UML. Second, as shown in Figure 17.18 , an action can take place as part of a transition. (Technically, there is a slight difference between an activity and an action. 


FIGURE 17.18 A statechart equivalent to Figure 17.17 .


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/924db9a3f12aed7cc46308e0605d8c0a590800d192715029b56607d625cc144b.jpg)



FIGURE 17.19 Statechart (a) without and (b) with superstate.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/a45f07503864a8356274e49dfa3a43b674272df86fed1ea8612caf2efca71ad2.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/f38b1349d14c7af7ff8bc1922f5fea19041f87acd5e68a775477485126f5d4b4.jpg)



(b)


An action is assumed to take place essentially instantaneously, but an activity may take place less quickly, perhaps over several seconds.) 

UML supports a wide variety of different types of actions and events in statecharts. For instance, an event can be specifi ed in terms of words like when or after . Therefore, an event might stipulate when (cost > 1000) or after (2.5 seconds). 

A statechart with a large number of states tends to have a large number of transitions. The many arrows representing these transitions soon make the statechart look like a large bowl of spaghetti. One technique for dealing with this is to use a superstate . Consider the statechart of Figure 17.19(a) . The four states A, B, C , and D all have transitions to Next State . Figure 17.19(b) shows how these four states can be combined into one superstate, ABCD Combined , which needs only one transition, as opposed to the four in Figure 17.19(a) . This reduces the number of arrows from four to only one. At the same time, states A, B, C , and D still exist in their own right, so any existing actions associated with those states are not affected nor are any existing transitions into those states. Another example of a superstate is shown in Figure 17.20 , where the four lower states of Figure 17.16 are unifi ed into one superstate, MSG Foundation Combined , leading to a cleaner and clearer diagram. 

## 17.8 Activity Diagrams

Activity diagrams show how various events are coordinated. They are therefore used when activities are carried out in parallel. 

Suppose a couple seated at a restaurant orders their meal. One orders a chicken dish; the other orders fi sh. The waiter writes down their order and hands the order to the chef so that she knows what dishes to prepare. It does not matter which dish is completed fi rst because the meal is served only when both dishes have been prepared. This is shown in 


FIGURE 17.20 Figure 17.16 with four states combined into a superstate, MSG Foundation Combined


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/e23febee094b074531e9ff2291afaf3538e7fad52b2fe6191ad67b412b368672.jpg)



An activity diagram for a restaurant order for two diners.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/5ef8b1af872f7e7f4fef1a450c5d18d917bc9c486787420f1bf319f6e09ce11c.jpg)



Figure 17.21 . The upper heavy horizontal line is called $\mathrm { ~ a ~ } f o r k ,$ and the lower one is called a join . In general, a fork has one incoming transition and many outgoing transitions, each of which starts an activity to be executed in parallel with the other activities. Conversely, a join has many incoming transitions, each of which lead from an activity executed in parallel with the other activities, and one outgoing transition that is started when all the parallel activities have been completed.


FIGURE 17.22 An activity diagram for a computer assembly company. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/424e90ec4a4ae35dcf3a60d0ab5b065d177a839058b8f3dc5e9007de48dcae0c.jpg)


Activity diagrams are useful for modeling businesses where a number of activities are carried out in parallel. For example, consider a company that assembles computers as specifi ed by the customer. As shown in the activity diagram of Figure 17.22 , when an order is received, it is passed on to the Assembly Department . It is also passed to the Accounts Receivable Department . The order is complete when the computer has been assembled and delivered, and the customer’s payment has been processed. Each of the three departments involved, the Assembly Department , the Order Department , and the Accounts Receivable Department , is in its own swimlane . In general, the combination of forks, joins, and swimlanes shows clearly which branches of an organization are involved in each specifi c activity, which tasks are carried on in parallel, and which tasks have to be completed in parallel before the next task can be started. 

## 17.9 Packages

As explained in Section 14.9, the way to handle a large software product is to decompose it into relatively independent packages . The UML notation for a package is a rectangle with a name tag, as shown in Figure 17.23 . This fi gure shows that My Package is a package, but the rectangle is empty. This is a valid UML diagram—the diagram simply models the fact that My Package is a package. Figure 17.24 is more interesting—it shows the contents of My Package , including a class, an entity class, and another package. We can continue to supply more details until the package is at the appropriate level of detail for the current iteration and incrementation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/41972e6d462f594fbb7ef62e435d8d75ea89f471be1ef5a4592d04910b02b0bc.jpg)



FIGURE 17.25 Component diagram.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/005331da5b62066519c12042972b4d112e6f4a98df6d320e141922ff4af0956d.jpg)


## 17.10 Component Diagrams

A component diagram shows dependencies among software components, including source code, compiled code, and executable load images. For example, the component diagram of Figure 17.25 shows source code (represented by a note) and the executable load image created from the source code. 

## 17.11 Deployment Diagrams

A deployment diagram shows on which hardware component each software component is installed (or deployed). It also shows the communication links among the hardware components. A simple deployment diagram is shown in Figure 17.26. 


FIGURE 17.26 A deployment diagram.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/5c66564c7b39333c1d6991bd303d1957296c0ad0787ef79828f0abd3599ef449.jpg)



Laptop computer


## 17.12 Review of UML Diagrams

A wide variety of different UML diagrams have been presented in this chapter. In the inter ests of clarity, here is a list of some of the diagram types that might be confused: 

• A use case models the interaction between actors (external users of a software product) and the software product itself. 

• A use-case diagram is a single diagram that incorporates a number of use cases. 

• A class diagram is a model of the classes showing the static relationships among them, including association and generalization. 

• A statechart shows states (specifi c values of attributes of objects), events that cause transitions between states (subject to guards), and actions and activities performed by objects. A statechart is therefore a dynamic model—it refl ects the behavior of objects, that is, the way they react to specifi c events. 

• An interaction diagram ( sequence diagram or communication diagram ) shows the way that objects interact with one another as messages are passed between them. This is another dynamic model; that is, it also shows how objects behave. 

• An activity diagram shows how events that occur at the same time are coordinated. This is yet another dynamic model. 

## 17.13 UML and Iteration

Consider a statechart. The transitions can be labeled with a guard, an event, an action, or all three. Now consider a sequence diagram. The lifelines may or may not include activation boxes, there may or may not be returns, and there may or may not be guards on the messages. 

A wide range of options are available for every UML diagram. That is, a valid UML diagram consists of a small required part plus any number of options. UML diagrams have so many options for two reasons. First, not every feature of UML is applicable to every software product, so there has to be freedom with regard to choice of options. Second, we cannot perform the iteration and incrementation of the Unifi ed Process unless we are permitted to add features stepwise to diagrams, rather than create the complete fi nal diagram at the beginning. That is, UML allows us to start with a basic diagram. We can then add optional features as we wish, bearing in mind that, at all times, the resulting UML diagram is still valid. This is one of the many reasons why UML is so well suited to the Unifi ed Process. 

## Chapter Review

It is explained in Section 17.1 that UML is a language, not a methodology. Class diagrams are described in Section 17.2. Specifi c aspects of class diagrams are discussed, including aggregation (Section 17.2.1), multiplicity (Section 17.2.2), composition (Section 17.2.3), generalization (Section 17.2.4), and association (Section 17.2.5). Next, a variety of UML diagrams are presented, including notes (Section 17.3), use-case diagrams (Section 17.4), stereotypes (Section 17.5), interaction diagrams (both sequence diagrams and communication diagrams; Section 17.6), statecharts (Section 17.7), activity diagrams (Section 17.8), packages (Section 17.9), component diagrams (Section 17.10), and deployment diagrams (Section 17.11). The chapter concludes with a review of UML diagrams (Section 17.12) and a discussion of why UML is so suitable for the Unifi ed Process (Section 17.13). 

## For Further Reading

There is no substitute for reading the current version of the UML manual, to be found at the OMG website, www.omg.org . Two good introductory texts on UML are [Fowler and Scott, 2000] and [Stevens and Pooley, 2000]. 

<table><tr><td rowspan="13">Key Terms</td><td>action 582</td><td>deployment diagram 586</td><td>package 585</td></tr><tr><td>activation box 579</td><td>discriminator 576</td><td>part-whole relationship 573</td></tr><tr><td>activity 582</td><td>event 581</td><td>return 580</td></tr><tr><td>activity diagram 583</td><td>extend relationship 578</td><td>self-call 580</td></tr><tr><td>actor 577</td><td>fork 584</td><td>sequence diagram 579</td></tr><tr><td>aggregation 573</td><td>generalization 576</td><td>statechart 581</td></tr><tr><td>association 576</td><td>guard 580</td><td>stereotype 578</td></tr><tr><td>association class 577</td><td>guillemets 578</td><td>superstate 583</td></tr><tr><td>class diagram 572</td><td>include relationship 578</td><td>swimlane 585</td></tr><tr><td>collaboration diagram 580</td><td>interaction diagram 579</td><td>transition 581</td></tr><tr><td>communication diagram 580</td><td>join 584</td><td>use case 577</td></tr><tr><td>component diagram 586</td><td>multiplicity 574</td><td>use-case diagram 577</td></tr><tr><td>composition 575</td><td>note 577</td><td></td></tr></table>

## Problems

17.1 Is UML a methodology? Carefully explain your answer. 

17.2 Use UML to model airports. (Hint: Do not show any more details than are strictly needed to answer the question.) 

17.3 Use UML to model chocolate cakes. A chocolate cake is made with eggs, fl our, sugar, baking powder, milk, and cocoa. A chocolate cake is mixed, baked, frosted, and then eaten. To prevent unauthorized individuals from baking a chocolate cake, the ingredients are private, as are all but the last operation. 

17.4 Add a note to your diagram of Problem 17.3 pointing out that the cake you modeled is a chocolate cake. 

17.5 Use UML to model the following: Turn on the oven. Mix the ingredients for a chocolate cake. Mix the ingredients for an apple pie. Place the (raw) cake and pie in the oven. Remove the chocolate cake when it is done. Remove the apple pie when it is done. Turn off the oven. 

17.6 How does your UML model of Problem 17.5 cope with the fact that we do not know, from the information given, which of the two items is removed from the oven fi rst? 

17.7 Modify your model of Problem 17.6 to refl ect that the chocolate cake is prepared by the chocolate cake baker, the apple pie by the apple pie baker, and that the oven is switched on and off by the chief baker. 

17.8 Model chocolate cakes and apple pies using one package. 

17.9 Use UML to model dining rooms. Every dining room has to have a table, four or more chairs, and a sideboard. Optionally, it may also have a fi replace. 

17.10 Model the dining rooms of Problem 17.9 using a combination of aggregation and composition. 

17.11 Modify your UML model of Problem 17.9 to refl ect that a dining room is a specifi c type of 

17.12 Use UML to model John Cage’s somewhat controversial 1952 piano composition entitled $4 ^ { \prime } 3 3 ^ { \prime \prime }$ . The piece consists of three silent movements, of length 30 seconds, 2 minutes 23 seconds, and 1 minute 40 seconds, respectively. (The title of the piece comes from its total length.) The pianist walks onto the stage holding a stopwatch and the score (in conventional music notation but with blank measures). The pianist sits down on the piano stool, puts the score and the stopwatch on the piano, opens the score, starts the stopwatch, and then signals the start of the fi rst movement by lowering the lid of the piano. At the end of the fi rst movement (that is, after 30 seconds of silence during which the pianist carefully follows the blank score, turning the page when necessary), the lid of the piano is raised to signal the end of the fi rst movement. These actions are repeated for the second movement (2 minutes 23 seconds) and the third movement (1 minute 40 seconds). The pianist then closes the score, picks up the score and the stopwatch, gets up, and leaves the stage. 

## References



[Booch, Rumbaugh, and Jacobson, 1999] G. BOOCH, J. RUMBAUGH, AND I. JACOBSON, The UML Users Guide , Addison-Wesley, Reading, MA, 1999. 





[Fowler and Scott, 2000] M. FOWLER WITH K. SCOTT, UML Distilled, 2nd ed., Addison-Wesley, Upper Saddle River, NJ, 2000. 





[Stevens and Pooley, 2000] P. STEVENS WITH R. POOLEY, Using UML: Software Engineering with Objects and Components , updated edition, Addison-Wesley, Upper Saddle River, NJ, 2000. 





[Wikipedia, 2010] WIKIPEDIA, “Guillemets,” en.wikipedia.org/wiki/Guillements, February 13, 2010. 



# Emerging Technologies

## Learning Objectives

After studying this chapter, you should appreciate the importance of a variety of emerging technologies, including 

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

In what direction is software engineering moving? What are the technologies of the future? How will we develop and maintain software in the year 2020? Or the year 2050? 

As explained in Just in Case You Wanted to Know Box 18.1, predicting the future is no easy task. In this chapter, we give an overview of a number of promising emerging technologies that may (or may not) be harbingers of the future direction of software engineering. The aim of this chapter is to give the fl avor of 10 emerging technologies, with the technical details suppressed. 

The topics in this chapter are generally taught in graduate-level courses in software engineering. They are included in this textbook for the fi rst course in software engineering because it is important to have a basic understanding of these emerging technologies. 

Lawrence Peter “Yogi” Berra (born in 1925) achieved fame not only as a top baseball player and manager, but also for his witty comments, known as Yogiisms. A characteristic of a Yogiism is that, on fi rst hearing, it appears to be meaningless, but after some thought, it makes perfect sense. For example, his home in New Jersey was equally accessible via two different roads that branched off at a fork. So, when giving directions to his home, he would say: “When you come to a fork in the road, take it.” 

Regarding the subject of this chapter, Berra declared: “It’s tough making predictions, especially about the future.” 

Throughout this book we have carefully analyzed the strengths and weaknesses of the techniques we have presented. However, it is too soon to determine the strengths and weaknesses of the technologies presented in this chapter. 

## 18.1 Aspect-Oriented Technology

A concern of a software product is a specifi c set of behaviors of that product. For example, in a banking product, one concern is the set of interest computations: Banks pay interest to depositors and charge interest to borrowers. A second concern is the writing of information to the audit trail. A core concern of a software product is a primary set of behaviors of that product. In the banking example, interest computation is clearly primary, whereas writing to the audit trail, though absolutely essential from the viewpoints of auditing and security, is not a core banking concern. 

As described in Section 5.4, separation of concerns [Dijkstra, 1982] is a principle underlying a technique for achieving modularization by designing software with each concern isolated in its own module or group of modules, thereby maximizing cohesion and minimizing coupling ( Chapter 7 ). However, it is sometimes impossible to achieve such a separation of concerns. In the banking example, interest computations can probably be isolated to one or more modules, but virtually every operation of the banking product has to write information to the audit trail. Cross-cutting concerns are concerns that cut across module boundaries, such as the audit trail concern in the banking product. Cross-cutting can have a deleterious effect on maintenance, because the presence of cross-cutting can lead to regression faults; if a concern has to be implemented in a variety of otherwise unrelated modules, a change to that concern has to be made consistently to all instances of the concern in all relevant modules. 

When a part of a software product cross-cuts its core concerns, the principle of separation of concerns is violated. In the banking example, the code for writing to the audit trail will cross-cut many modules. This is illustrated in Figure 18.1(a) , which shows three modules, each with one or more pieces of cross-cutting code for writing to the audit trail. A change to the audit trail mechanism requires all six pieces of audit trail code to be consistently changed. 

The aim of aspect-oriented programming (AOP) is to isolate such cross-cutting aspects by letting the developer sequester cross-cutting concerns in special modules called aspects . Aspects contain advice , code that is to be linked to specifi c places in the software. An example of advice is an audit trail routine in the bank software. A pointcut is a place in the code where the cross-cutting concern is to be applied, that is, where the advice is to be executed. An aspect therefore consists of two pieces: the advice and its associated set of pointcuts. 

FIGURE 18.1 Banking product with cross-cutting concern. (a) Conventional design (b) Aspect-oriented design. 

Audit trail code 

Audit trail code 

Audit trail code 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/a7cae0e5dd797d94dae25f1520c70334145f7609a9cb66fb431132d7d82d4a84.jpg)


Audit trail code 

Audit trail code 

Audit trail code 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/7ce2ac08cf155a29d4e6c47c5bb71dc775cc89f290928bcccc380af752476228.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/a4d66936e09dc22e027e78ada0fb08731bf06404a936151c07793f52070b9e03.jpg)


Pointcut 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/f71affe9e3e4201afabdb656b49e845076b8cc713c58e81a3aa535150273e495.jpg)


Advice 


(b)


Separation of concerns can now be achieved by placing each cross-cutting concern into its own aspect, thereby isolating the relevant code (the advice) and reducing the risk of a regression fault. The pointcuts inserted into the product merely show where the specifi c advice is to be executed. Figure 18.1(b) shows how the six pieces of audit trail code of Figure 18.1(a) are replaced by an aspect (containing advice), and six pointcuts. Now, a change to the audit trail mechanism is localized to the aspect. 

To employ aspect-oriented programming, an aspect-oriented programming language is needed. A compiler for an aspect-oriented programming language is called a weaver . A major task of a weaver is to insert the relevant advice at each pointcut before compiling the code; this operation is termed composition . That is, development and maintenance are performed on the uncompiled source code, including its aspects and pointcuts; separation of concerns is thereby achieved. Before the code can be compiled and executed, the weaver composes the code by inserting the cross-cutting code into the correct places. Returning to Figure 18.1 , once composition has been applied to Figure 18.1(b) , it becomes Figure 18.1(a) . However, the composed code is rarely, if ever, inspected by the programmer. That is, programmers work on software that resembles Figure 18.1(b) , not Figure 18.1(a) . 

The most popular aspect-oriented programming language is AspectJ, an aspect-oriented extension for Java [Kiczales et al., 2001; Laddad, 2003]. Aspect-oriented implementations have been developed for a wide variety of programming languages, including C++ and C#, and even for COBOL [Cobble, 2004]. 

Aspect-oriented programming is one part of aspect-oriented software development (AOSD ), also called early aspects . A primary aim of AOSD is the early identifi cation of both functional and nonfunctional cross-cutting concerns such as writing to audit trails, security, error checking, and real-time constraints. Once the cross-cutting concerns have been identifi ed, they are specifi ed (aspect-oriented analysis), modularized (aspectoriented design), and coded (aspect-oriented implementation) 

Aspect-oriented programming has been used in a number of commercial applications, including IBM Websphere (Section 8.5.2), and in open-source software such as JBoss, a Java application server. 

## 18.2 Model-Driven Technology

In Section 8.6.5, the problem of porting a widget generator from one architecture to another was solved by using the abstract factory design pattern. That is, the widget generator was designed as an abstract class, and then implemented in terms of concrete classes, one for each target architecture. This solution is at the design level. 

The model-driven architecture (MDA) [MDA, 2008] solves the problem of moving a software product to a new platform at the analysis level rather than at the design level. 

1. As shown in Figure 18.2 , the functionality of the desired software product is specifi ed by means of a platform-independent model (PIM). This is done using UML, or an appropriate domain-specifi c language, that is, a special-purpose language for the specifi c problem domain. 

2. A platform-specifi c model (PSM) is chosen, for example, CORBA, .NET, or J2EE, and the PIM is mapped into the selected PSM. The PSM is expressed in UML. 

3. The PSM is translated into code, using an automatic code generator, and run on a computer. 

4. If multiple platforms are required, steps 2 and 3 are repeated for each PSM 

In other words, as can be seen in Figure 18.2 , MDA totally decouples the functionality of a software product from the implementation of that software product, and thereby provides a powerful mechanism for achieving portability (Section 8.13). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/56dd2b9d02bdd2db40886c43a976281015f1a1242e13928072ca435c3a8e5f21.jpg)


Patterns play an important role in MDA-based software products. The PIM has to incorporate suffi cient detail to enable the mapping into the PSM to take place. This detail could be supplied manually each time, but it is clearly preferable to supply these details via patterns (“archetype patterns” [Arlow and Neustadt, 2004]). Furthermore, as explained in Section 8.8, once a design pattern has been implemented, that implementation can be reused when the pattern is reused. Similarly, in the case of MDA-based software, the mapping of an archetype pattern within the PIM into the PSM may already have been done. 

The key to MDA is that this approach raises the level of abstraction from the platformdependent code level to the platform-independent model level. A current research topic in MDA is how to construct the necessary CASE tools to automate the approach. If the CASE tools can indeed be built, then this will allow software engineers to develop software at the model level. The modeling language of the PIM (a domain-specifi c language or UML) will then be the lowest level of abstraction for software development and maintenance. The PSM and the code will be automatically generated, and will be as “invisible” to the software engineer of the future as machine code usually is today. 

## 18.3 Component-Based Technology

The goal of component-based technology is to construct a standard collection of reusable components. Then, instead of reinventing the wheel each time, in the future all software will be constructed by choosing a standard architecture and standard reusable frameworks and inserting standard reusable code artifacts into the hot spots of the frameworks (see Chapter 8 ). That is, software products will be built by composing reusable components. This will be done using an automated tool. That is, production automation is a key aspect of component-based software engineering. 

For this technology to work, the components have to be independent, that is, fully encapsulated (Section 7.4). In fact, the components have to be at a higher level of abstraction than objects, because they cannot share state. Like objects, however, they communicate by exchanging messages. 

In Chapter 8 , the many advantages that accrue through the reuse of code artifacts, design patterns, and software architectures are described. Hence, achieving component-based software engineering would lead to order-of-magnitude increases in software productivity and quality, and decreases in time to market and maintenance effort. 

Unfortunately, the state of the art with regard to reuse is currently far from this ambitious target. In addition, component-based software construction has many challenges, including the defi nition, standardization, and retrieval of components. However, researchers in many centers are actively engaged in trying to achieve the goal of component-based software engineering. 

## 18.4 Service-Oriented Technology

One way to create a document on a computer is for the user to install a copy of Microsoft Word on the user’s computer, and then use Microsoft Word to create the document on that computer. Another alternative is for the user to open a Web browser (Section 5.8) and create the document using Google Docs. In this case, the word-processing software stays on the Google computer. (The document also resides on the Google computer, but a copy can be downloaded to the user’s computer, for additional security.) 

Docs is a service provided by Google for the user. The American Heritage Dictionary defi nes a service as “An act or a variety of work done for others . . .” [Service, 2000]. In other words, with service-oriented technology, capabilities are provided by service providers over a network (frequently the Internet) to meet specifi c needs of service consumers . 

## 18.5 Comparison of Service-Oriented and Component-Based Technology

Service-oriented technology has many features in common with component-based technology: 

• First, both are instances of distributed computing; services and components are both distributed over a network. 

• Second, both are primarily reuse technologies. In the case of service-oriented technology, the service consumers reuse the services of the service providers. And the basis for component-based technology is the standard collection of reusable components, together with standard architectures and standard reusable frameworks. 

• Third, encapsulation is essential for both technologies, to ensure that the components and the services are indeed independent (and hence reusable). 

• Fourth, both components and services are accessed through their interfaces; careful adherence to interface specifi cations is of major importance. 

• Fifth, both components and services must have the highest possible cohesion and the lowest possible coupling, to ensure reusability via separation of concerns. 

• Sixth, both technologies have low entry costs. With service-oriented technology, service consumers pay for the use of services, on a pay-per-use basis or monthly subscription; they do not need to purchase the service itself. (Some services, such as Google Docs, are free.) With component-based technology, users compose their own software from standard components; they do not have to pay to have custom software built. 

• Seventh, there is no need to install software, confi gure it, and then continually update it with each new release. Instead, the latest version of software is automatically downloaded each time. These ideas are extended in Just in Case You Wanted to Know Box 18.2. 

• Eighth, both technologies are generally geographic location independent. Components and services are usually accessible over the Web and can be accessed ubiquitously using any appropriate device. 

A major difference between the two technologies is granularity. Component-based technology constructs a software product by combining components into an executable program, whereas service-oriented technology utilizes existing executable programs. In other words, the basic building blocks of component-based technology are components, whereas the basic building blocks of service-oriented technology are complete executable programs. 

In 1999, Salesforce.com, Inc., was the fi rst company to provide major business applications as a service. The company’s slogan is “No software!” This catchphrase implies that serviceoriented computing obviates the problems that organizations face when they install their own software. 

A second difference is that, although both component-based technology and serviceoriented technology are emerging technologies, early versions of service-oriented technology are already being used today by a wide variety of service consumers, whereas component-based technology still requires breakthrough research before it can be used in practice. 

## 18.6 Social Computing

The term social computing is used in two different contexts. First, it is used in the context of the ways in which computers support social behavior. This includes chat rooms, instant messaging, e-mail, blogs, and shared work spaces like wikis. Popular sites that allow users to interact and share data include personal profi le sites like MySpace and Facebook, networking sites like LinkedIn, media sites like Flickr (for sharing photographs) and YouTube (for sharing videos), and many others. In this usage, the term social computing does not refer to the underlying technologies as such, but rather to the social interactions and structure brought about and supported by those technologies. 

In other words, this usage of the term focuses on the “social” rather than the “computing.” For example, consider Wikipedia from this perspective. The underlying wiki technology itself is not of interest. Instead, social computing here focuses on the community that has grown around the online encyclopedia and the interactions between the members of that community. Disputes between contributors, fraudulent user credentials, deliberate misstatements of facts in postings are all relevant here, as is the overall high standard of the articles. 

Second, the term social computing is used in the context of group computations. Examples include online auctions, multiplayer online games, and collaborative fi ltering (analysis of large data sets to extract information like “Individuals who bought Book A also bought Book B,” to make purchase suggestions to online shoppers). Here the emphasis is on the “computing” rather than the “social.” This usage, unlike the fi rst, therefore relates to an emerging technology. 

## 18.7 Web Engineering

As stated at the beginning of Chapter 1 , software engineering is a discipline whose aim is the production of fault-free software delivered on time, within budget, and satisfying the user’s needs. Analogously, Web engineering is a discipline whose aim is the production of fault-free Web software delivered on time, within budget, and satisfying the user’s needs. 

Web software is a subset of software in general. Accordingly, Web engineering is technically a subset of software engineering. However, proponents of Web engineering point out that Web software has characteristics of its own, and the Web engineering should therefore be considered a separate discipline. Characteristics of Web software include: 

• Unstable requirements. The moving target problem (Section 2.4) tends to be more acute in the case of Web software, because there are three moving targets: the members of the community of users, the experience level of the users, and Web technology. Accordingly, the requirements of Web software tend to change rapidly. 

• Wide range of user skills. The skill set of a Web user can range from total beginner to expert. This can have major implications for the design of the human–computer interface. 

• No opportunity to train users. When a new software product is installed in an organization, management can require every employee who is to use the product to undergo appropriate training. This is not possible with Web applications. At best, a help menu can be provided. 

• Varied content. The website of an online retailer can contain text, graphics, audio, and video. Furthermore, these elements may be integrated with the all-important sales functionality of the website. This can drastically affect response times. 

• Exceedingly short maintenance turnaround times. The time between releases of new versions of commercial software is typically six months or a year. In contrast, Web software can be updated as often as daily. Furthermore, updating can often be performed in the background, that is, seamlessly to the user. 

• The human–user interface is of prime importance. As pointed out in Section 11.14, a poorly designed human–computer interface for a software product can lead to increased learning times and higher error rates. In the case of Web software, a poorly designed human–computer interface can lead to the site in question being ignored by users, with severe fi nancial consequences for the owner of the website. 

• Diverse run-time environments. It should be possible to successfully access a given Web page using any of the many popular Web browsers. These browsers run on different hardware (including the PC and the Macintosh) under different operating systems (Linux, Mac OS X, Windows, and so on). Web software must be compatible with all these combinations of browsers, hardware, and operating systems. 

• Privacy and security requirements are usually stringent. When a hacker breaks into an online database containing unencrypted credit card data, millions of credit card holders can be exposed to identity theft. 

• Accessibility through multiple devices. The Web can be accessed via computer, cell phone, PDA, and so on. Web software must take this multiplicity of devices into account. 

In fact, some researchers feel that Web technology is so different from computer technology that they have put forward a new discipline, Web science, analogous to computer science [Berners-Lee et al., 2006a; Berners-Lee et al., 2006b]. 

## 18.8 Cloud Technology

The Internet is sometimes referred to as The Cloud . The term comes from extending the term iCloud (information cloud) [Heinemann, Kangasharju, Lyardet, and Mühlhäuser, 2003], the communication range of a mobile device, to the Internet [Vander Wal, 2004]. 

Cloud technology is a synonym for Internet-based technology. Specifi c to cloud computing is the idea that the users are not expected to have any knowledge of the underlying infrastructure; the metaphor is that users are operating “in a cloud.” 

## 18.9 Web 3.0

The World Wide Web (or Web for short) is a collection of hypertext documents. In contrast, Web 2.0 is a term that refers to the technology that individuals now use when they make use of the Web. Accordingly, it would be incorrect to describe Web 2.0 as “emerging technology,” the subject of this chapter. 

On the other hand, Web 3.0 (or the Semantic Web) is indeed an emerging technology. The term refers to ways that the Web will be used in the future. Many excellent suggestions have been put forward. Following the advice in Just in Case You Wanted to Know Box 18.1, we will just have to wait and see which of those suggestions, if any, will in fact eventuate. 

## 18.10 Computer Security

Computer security is a fi eld in its own right; it is not a branch of software engineering. Nevertheless, there are aspects of computer security that are also of concern to software engineers. In fact, all the new technologies in this chapter have security aspects. 

One important area of overlap between software engineering and computer security is human factors (Section 11.14), because users are generally more interested in the features of a software product than in security issues. As a result of the statement made by McGraw and Felten [1999], “Given a choice between dancing pigs and security, users will pick dancing pigs every time,” the lack of attention to security issues among all-too-many users has become known as the dancing pigs problem. 

Ironically, a scientifi c study of phishing (a criminal attempt to obtain confi dential information by falsely pretending to be a legitimate website) found that people really do prefer dancing animals to security [Dhamija, Tygar, and Hearst, 2006]. Participants were shown a fraudulent Web page for Bank of the West, whose logo is a bear. At the top of the page there was a video of a bear swimming. The researchers found that the “cute” design was one of the factors that convinced them that the page was real. In fact, the animated bear video was so appealing that many participants reloaded the fraudulent page just to see the animation again 

The design of human interfaces has to take into account that many users simply do not care about security. Accordingly, security has to be built into a software product, rather than offered as an option. This is a hard problem. After all, at the time of writing there are no comprehensive solutions to the problems of spam e-mail or phishing. Nevertheless, it is essential that, in the near future, software engineers and security specialists undertake joint research to tackle the many serious problems common to both fi elds. 

## 18.11 Model Checking

The 2007 ACM Turing Award (sometimes called the “Nobel Prize for Computer Science”) was awarded to Edmund M. Clarke, E. Allen Emerson, and Joseph Sifakis for developing model checking. Model checking is a testing technology for hardware that is starting to be applied to software. 

As discussed in Section 6.5.3, correctness proving is still somewhat problematic. What is needed is an alternative to a human having to construct a proof. Certain software products, such as operating systems, are designed to run forever. Temporal logic (Section 6.5.3) is a good way to model these software products. So, we specify a software product using temporal logic, and then realize that software product as a fi nite state machine (Section 12.7). As discussed in Section 12.7, the properties of a fi nite state machine can be determined. Accordingly, the idea behind model checking is fi rst to check whether a given fi nite state machine is a model of a temporal logic specifi cation, and then to determine the properties of that fi nite state machine. In this way, we can mathematically show that a software product is correct without explicitly constructing a proof of correctness. 

## 18.12 Present and Future

<table><tr><td></td><td colspan="3">This chapter contains an outline of 10 emerging technologies. At the time of writing, all are promising, all have the potential to become mainstream technologies. But, as Yogi Berra has stated (in Just in Case You Wanted to Know Box 18.1), “It’s tough making predictions, especially about the future.” So, only in the future will we know what the future will bring.</td></tr><tr><td>Chapter Review</td><td colspan="3">An outline is given of aspect-oriented technology, model-driven technology, component-based technology, and service-oriented technology in Sections 18.1 through 18.4, respectively. In Section 18.5, a comparison is made between service-oriented and component-based technology. Social computing is described in Section 18.6, and Web engineering in Section 18.7. The subject of Section 18.8 is cloud technology. Web 3.0 is described in Section 18.9. Computer security is outlined in Section 18.10, and model checking in Section 18.11. The future of these technologies is discussed in Section 18.12.</td></tr><tr><td>For Further Reading</td><td colspan="3">The material in this chapter is changing at an ever-increasing rate. Any references cited here will be out of date by the time this book has appeared in print. Wikipedia, on the other hand, is constantly being updated, and should be utilized as a pointer to current articles on the topics of this chapter.</td></tr><tr><td>Key Terms</td><td>advice 591aspect 591aspect-oriented programming (AOP) 591aspect-oriented programming language 592aspect-oriented software development (AOSD) 593</td><td>component-based technology 594composing 594composition 592concern 591core concern 591cross-cutting concern 591dancing pigs problem 598early aspects 593</td><td>model-driven architecture (MDA) 593pointcut 591separation of concerns 591service 595service consumers 595service providers 595social computing 596weaver 592</td></tr></table>

## References



[Arlow and Neustadt, 2004] J. ARLOW AND I. NEUSTADT, Enterprise Patterns and MDA: Building Better Software with Archetype Patterns and UML , Addison-Wesley Professional, Reading, MA, 2004. 





[Berners-Lee et al., 2006a] T. BERNERS-LEE, W. HALL, J. HENDLER, N. SHADBOLT, AND D. WEITZNER, “Creating a Science of the Web,” Science 313 (August 2006), pp. 769–71. 





[Berners-Lee et al., 2006b] T. BERNERS-LEE, W. HALL, J. HENDLER, K. O’HARA, N. SHADBOLT, AND D. WEITZNER, “A Framework for Web Science,” Foundations and Trends in Web Science 1 (2006), pp. 1–130. 





[Cobble, 2004] “Cobble,” users.ugent.be/~kdschutt/cobble, 2004. 





[Dhamija, Tygar, and Hearst, 2006] R. DHAMIJA, J. D. TYGAR, AND M. HEARST, “Why Phishing Works,” Proceedings of the SIGCHI Conference on Human Factors , Montréal, Québec, Canada, April 2006, ACM, pp. 581–90. 





[Dijkstra, 1982] E. W. DIJKSTRA, “On the Role of Scientifi c Thought,” in: Dijkstra, Edsger W., Selected Writings on Computing: A Personal Perspective, Springer-Verlag, New York, 1982, pp. 60–66. 





[Heinemann, Kangasharju, Lyardet, and Mühlhäuser, 2003] A. HEINEMANN, J. KANGASHARJU, F. LYARDET, AND M. MÜHLHÄUSER, “iClouds—Peer-to-Peer Information Sharing in Mobile Environments,” Proceedings of the International Conference on Parallel and Distributed Computing (Euro-Par 2003) , IEEE, Klagenfurt, Austria, August 2003. 





[Kiczales et al., 2001] G. KICZALES, E. HILSDALE, J. HUGUNIN, M. KERSTEN, J. PALM, AND W. G. GRISWOLD, “An Overview of AspectJ.” In: J. L. Knudsen (Ed.), European Conference on Objectoriented Programming , Vol. 2072 of Lecture Notes in Computer Science , Springer-Verlag, New York, 2001, pp. 327–53. 





[Laddad, 2003] R. LADDAD, AspectJ in Action , Manning Publications, Greenwich, CT, 2003. 





[McGraw and Felten, 1999] G. MCGRAW AND E. FELTEN, Securing Java , John Wiley and Sons, New York, 1999. 





[MDA, 2008] “MDA,” www.omg.org/mda , 2008. 





[Service, 2000] “Service. The American Heritage Dictionary of the English Language: Fourth Edition. 2000,” www.bartleby.com/61/68/S0286800.html , 2000. 





[Vander Wal, 2004] T. VANDER WAL, “Understanding the Personal Info Cloud: Using the Model of Attraction,” Presentation, University of Maryland, Baltimore, MD, June 2004. 



## Bibliography

The chapter number in parentheses denotes the chapter in which the item has been referenced. 



[Aberdour, 2007] M. ABERDOUR, “Achieving Quality in Open-Source Software,” IEEE Software 24 (January– February 2007), pp. 58–64. (Chapter 6) 





[Abrial, 1980] J.-R. ABRIAL, “The Specifi cation Language Z: Syntax and Semantics,” Oxford University Computing Laboratory, Programming Research Group, Ox ford, UK, April 1980. (Chapter 12) 





[Ackerman, Buchwald, and Lewski, 1989] A. F. ACKER-MAN, L. S. BUCHWALD, AND F. H. LEWSKI, “Software Inspections: An Effective Verifi cation Process,” IEEE Software 6 (May 1989), pp. 31–36. (Chapter 6) 





[Agrawal and Chari, 2007] M. AGRAWAL AND K. CHARI “Software Effort, Quality, and Cycle Time: A Study of CMM Level 5 Projects,” IEEE Transactions on Software Engineering 32 (March 2007), pp. 145–56. (Chapter 3) 





[Albrecht, 1979] A. J. ALBRECHT, “Measuring Application Development Productivity,” Proceedings of the IBM SHARE/GUIDE Applications Development Symposium , Monterey, CA, IEEE, October 1979, pp. 83–92. (Chapter 9) 





[Alexander, 1999] C. ALEXANDER, “The Origins of Pat tern Theory,” IEEE Software 16 (September–October 1999), pp. 71–82. (Chapter 8) 





[Alexander et al., 1977] C. ALEXANDER, S. ISHIKAWA, M. SILVERSTEIN, M. JACOBSON, I. FIKSDAHL-KING, AND S. ANGEL, A Pattern Language , Oxford University Press, New York, 1977. (Chapter 8) 





[I. Alexander, 2003] I. ALEXANDER, “Misuse Cases: Use Cases with Hostile Intent,” IEEE Software 20 (January–February 2003), pp. 58–66. (Chapter 11) 





[R. Alexander, 2003] R. ALEXANDER, “The Real Costs of Aspect-Oriented Programming,” IEEE Software 20 (November–December 2003), pp. 92–93. (Chapter 7) 





[Alford, 1985] M. ALFORD, “SREM at the Age of Eight; The Distributed Computing Design System,” IEEE Computer 18 (April 1985), pp. 36–46. (Chapter 12) 





[Alshayeb and Li, 2003] M. ALSHAYEB, AND W. LI “An Empirical Validation of Object-Oriented Metrics in Two Different Iterative Software Processes,” IEEE Transactions on Software Engineering 29 (Novembe 2003), pp. 1043–49. (Chapters 5 and 15) 





[Ammann and Offutt, 2008] P. AMMANN AND J. OFFUTT, Introduction to Software Testing, Cambridge University Press, Cambridge, UK, 2008. (Chapters 3 and 6) 





[Andersson and Runeson, 2007] C. ANDERSSON AND P. RUNESON, “A Replicated Quantitative Analysis of Fault Distributions in Complex Software Systems,” IEEE Transactions on Software Engineering 33 (May 2007), pp. 273–86. (Chapter 15) 





[ANSI X3.159, 1989] The Programming Language C, ANSI X3.159-1989, American National Standards Institute, New York, 1989. (Chapter 8) 





[ANSI/IEEE 754, 1985] Standard for Binary Floating Point Arithmetic , ANSI/IEEE 754, American National Standards Institute, Institute of Electrical and Elec tronic Engineers, New York, 1985. (Chapter 8) 





[ANSI/IEEE 829, 1991] Software Test Documentation, ANSI/IEEE 829-1991, American National Standards Institute, Institute of Electrical and Electronic Engi neers, New York, 1991. (Chapter 9) 





[ANSI/MIL-STD-1815A, 1983] Reference Manual for the Ada Programming Language , ANSI/MIL-STD-1815A, American National Standards Institute, United States Department of Defense, Washington, DC, 1983. (Chapter 8) 





[Antoniol, Cimitile, Di Lucca, and Di Penta, 2004] G. ANTONIOL, A. CIMITILE, G. A. DI LUCCA, AND M. DI PENTA, “Assessing Staffi ng Needs for a Software Maintenance Project through Queuing Simulation,” IEEE Transactions on Software Engineering 30 (January 2004), pp. 43–58. (Chapter 16) 





[Arisholm, Briand, Hove, and Labiche, 2006] E. ARIS-HOLM, L. C. BRIAND, S. E. HOVE, AND Y. LABICHE, “The Impact of UML Documentation on Software Maintenance: An Experimental Evaluation,” IEEE Transactions on Software Engineering 32 (June 2006), pp. 365–81. (Chapter 16) 





[Arisholm, Gallis, Dybå, and Sjøberg, 2007] E. ARIS-HOLM, H. GALLIS, T. DYBÅ, AND D. I. K. SJØBERG, “Evaluating Pair Programming with Respect to System Complexity and Programmer Expertise,” IEEE Transactions on Software Engineering 33 (February 2007), pp. 65–86. (Chapters 2, 4, and 9) 





[Arlow and Neustadt, 2004] J. ARLOW AND I. NEUSTADT, Enterprise Patterns and MDA: Building Better Software with Archetype Patterns and UML , Addison-Wesley Professional, Reading, MA, 2004. (Chapter 18) 





[Awad, Kuusela, and Ziegler, 1996] M. AWAD, J. KUU-SELA, AND J. ZIEGLER, Object-Oriented Technology for Real-Time Systems: A Practical Approach Using OMT and Fusion, Prentice Hall, Upper Saddle River, NJ, 1996. (Chapter 13) 





[Babich, 1986] W. A. BABICH, Software Confi guration Management: Coordination for Team Productivity, Addison-Wesley, Reading, MA, 1986. (Chapter 5) 





[Baker, 1972] F. T. BAKER, “Chief Programmer Team Management of Production Programming,” IBM Systems Journal 11 (No. 1, 1972), pp. 56–73. (Chapter 4) 





[Balzer, 1985] R. BALZER, “A 15 Year Perspective on Automatic Programming,” IEEE Transactions on Software Engineering SE-11 (November 1985), pp. 1257–68. (Chapter 12) 





[Bandi, Vaishnavi, and Turk, 2003] R. K. BANDI, V. K. VAISHNAVI, AND D. E. TURK, “Predicting Maintenance Performance Using Object-Oriented Design Complexity Metrics,” IEEE Transactions on Software Engineering 29 (January 2003), pp. 77–87. (Chapter 16) 





[Banks, Carson, Nelson, and Nichol, 2001] J. BANKS, J. S. CARSON, B. L. NELSON, AND D. M. NICHOL, Discrete-Event System Simulation, 3rd ed., Prentice Hall, Upper Saddle River, NJ, 1995. (Chapter 12) 





[Bannerman, 2008] P. L. BANNERMAN, “Risk and Risk Management in Software Projects: A Reassessment,” Journal of Systems and Software 81 (December 2008), pp. 2118–33. (Chapter 1) 





[Bansiya and Davis, 2002] J. BANSIYA AND C. G. DAVIS, “A Hierarchical Model for Object-Oriented Design Quality Assessment,” IEEE Transactions on Software Engineering 28 (January 2002), pp. 4–17. (Chapter 14) 





[Basili and Hutchens, 1983] V. R. BASILI AND D. H. HUTCHENS, “An Empirical Study of a Syntactic Complexity Family,” IEEE Transactions on Software Engineering SE-9 (November 1983), pp. 664–72. (Chapter 15) 





[Basili and Selby, 1987] V. R. BASILI AND R. W. SELBY, “Comparing the Effectiveness of Software Testing 





Strategies,” IEEE Transactions on Software Engineering SE-13 (December 1987), pp. 1278–96. (Chapter 15) 





[Basili and Weiss, 1984] V. R. BASILI AND D. M. WEISS, “A Methodology for Collecting Valid Software Engineering Data,” IEEE Transactions on Software Engineering SE-10 (November 1984), pp. 728–38. (Chapter 15) 





[Bass, Clements, and Kazman, 2003] L. BASS, P. CLE-MENTS, AND R. KAZMAN, Software Architecture in Practice, 2nd ed., Addison-Wesley, Reading, MA, 2003. (Chapter 8) 





[Bass et al., 2008] L. BASS, R. NORD, W. WOOD, D. ZU BROW, AND I. OZKAYA, “Architectural Knowledge Discovery with Latent Semantic Analysis: Constructing a Reading Guide for Software Product Audits,” Journal of Systems and Software 81 (September 2008), pp 1443–55. (Chapter 8) 





[Baster, Konana, and Scott, 2001] G. BASTER, P. KONANA, AND J. E. SCOTT, “Business Components: A Case Study of Bankers Trust Australia Limited,” Com munications of the ACM 44 (May 2001), pp. 92–98 (Chapter 8) 





[Beck, 2000] K. BECK, Extreme Programming Explained: Embrace Change, Addison-Wesley Longman, Reading, MA, 2000. (Chapters 2 and 4) 





[Beck and Cunningham, 1989] K. BECK AND W. CUN-NINGHAM, “A Laboratory for Teaching Object-Oriented Thinking,” Proceedings of OOPSLA ’89, ACM SIG-PLAN Notices 24 (October 1989), pp. 1–6. (Chapter 13) 





[Beck et al., 2001] K. BECK, M. BEEDLE, A. COCKBURN, W. CUNNINGHAM, M. FOWLER, J. GRENNING, J. HIGH SMITH, A. HUNT, R. JEFFRIES, J. KERN, B. MARICK, R. C. M , S. M , K. S , J. S LAND, D. THOMAS, AND A. VAN BENNEKUM, Manifesto for Agile Software Development , agilemanifesto.org, 2001. (Chapters 2 and 4) 





[Beizer, 1990] B. BEIZER, Software Testing Techniques 2nd ed., Van Nostrand Reinhold, New York, 1990. (Chapters 6, 14, 15) 





[Beizer, 1995] B. BEIZER, Black-Box Testing: Technique for Functional Testing of Software and Systems, John Wiley and Sons, New York, 1995. (Chapter 15) 





[Beizer, 1997] B. BEIZER, “Cleanroom Process Model: A Critical Examination,” IEEE Software 14 (March– April 1997), pp. 14–16. (Chapter 15) 





[Belanger et al., 2006] F. BELANGER, W. FAN, L. C. SCHAUPP, A. KRISHEN, J. EVERHART, D. POTEET, AND 





K. NAKAMOTO, “Web Site Success Metrics: Addressing the Duality of Goals,” Communications of the ACM 49 (December 2006), pp. 114–16. (Chapter 5) 





[Bellinzona, Fugini, and Pernici, 1995] R. BELLINZONA, M. G. FUGINI, AND B. PERNICI, “Reusing Specifi cations in OO Applications,” IEEE Software 12 (March 1995), pp. 656–75. (Chapter 13) 





[Bennatan, 2000] E. M. BENNATAN, On Time within Budget: Software Project Management Practices and Techniques , 3rd ed., John Wiley and Sons, New York, 2000. (Chapter 9) 





[Berners-Lee et al., 2006a] T. BERNERS-LEE, W. HALL, J. HENDLER, N. SHADBOLT, AND D. WEITZNER, “Creating a Science of the Web,” Science 313 (August 2006), pp. 769–71. (Chapter 18) 





[Berners-Lee et al., 2006b] T. BERNERS-LEE, W. HALL, J. HENDLER, K. O’HARA, N. SHADBOLT, AND D. WEITZNER, “A Framework for Web Science,” Foundations and Trends in Web Science 1 (2006), pp. 1–130. (Chapter 18) 





[Berry, 2004] D. M. BERRY, “The Inevitable Pain of Software Development: Why There Is No Silver Bullet,” in: Radical Innovations of Software and Systems Engineering in the Future , Lecture Notes in Computer Science, Vol. 2941, Springer-Verlag, Berlin, 2004, pp. 50–74. (Chapter 11) 





[Berry and Wing, 1985] D. M. BERRY AND J. M. WING, “Specifying and Prototyping: Some Thoughts on Why They Are Successful,” in: Formal Methods and Software Development, Proceedings of the International Joint Conference on Theory and Practice of Software Development , Vol. 2, Springer-Verlag, Berlin, 1985, pp. 117–28. (Chapter 6) 





[Bianchi, Caivano, Marengo, and Visaggio, 2003] A. BIANCHI, D. CAIVANO, V. MARENGO, AND G. VISAGGIO, “Iterative Reengineering of Legacy Systems,” IEEE Transactions on Software Engineering 29 (March 2003), pp. 225–41. (Chapter 2) 





[Binkley and Schach, 1996] A. B. BINKLEY AND S. R. SCHACH, “A Comparison of Sixteen Quality Metrics for Object-Oriented Design,” Information Processing Letters 57 (No. 6, June 1996), pp. 271–75. (Chapters 14 and 15) 





[Binkley and Schach, 1997] A. B. BINKLEY AND S. R. SCHACH, “Toward a Unifi ed Approach to Object-Oriented Coupling,” Proceedings of the 35th Annual ACM Southeast Conference , Murfreesboro, TN, ACM, April 2–4, 1997, pp. 91–97. (Chapters 7, 14, and 15) 





[Binkley and Schach, 1998] A. B. BINKLEY AND S. R. SCHACH, “Validation of the Coupling Dependency Metric as a Predictor of Run-Time Failures and Maintenance Measures,” Proceedings of the 20th International Conference on Software Engineering , Kyoto, Japan, IEEE, April 1988, pp. 542–55. (Chapter 14) 





[Birk et al. 2003] A. BIRK, G. HELLER, I. JOHN, K. SCHMID T. VON DER MASSEN, AND K. MULLER, “Product Line Engineering, the State of the Practice,” IEEE Software 20 (November–December 2003), pp. 52–60. (Chapter 8) 





[Black and Murphy-Hill, 2008] E. BLACK AND A. P. MURPHY-HILL, “Refactoring Tools: Fitness for Purpose,” IEEE Software 25 (September–October 2008), pp. 38–44. (Chapter 5) 





[Blaha, Premerlani, and Rumbaugh, 1988] M. R. BLAHA, W. J. PREMERLANI, AND J. E. RUMBAUGH, “Relational Database Design Using an Object-Oriented Methodology,” Communications of the ACM 31 (April 1988), pp. 414–27. (Chapter 7) 





[Blaine and Cleland-Huang, 2008] J. D. BLAINE AND J. CLELAND-HUANG, “Software Quality Requirements: How to Balance Competing Priorities,” IEEE Software 25 (March–April 2008), pp. 22–24. (Chapter 11) 





[Blanco, Gutiérrez, and Satriani, 2001] M. BLANCO, P. GUTIÉRREZ, AND G. SATRIANI, “SPI Patterns: Learn ing from Experience,” IEEE Software 18 (May–June 2001), pp. 28–35. (Chapter 3) 





[Bockle et al., 2004] G. BOCKLE, P. CLEMENTS, J. D. MCGREGOR, D. MUTHIG, AND K. SCHMID, “Calculating ROI for Software Product Lines,” IEEE Software 21 (May–June 2004), pp. 23–31. (Chapters 5 and 8) 





[Boehm, 1976] B. W. BOEHM, “Software Engineering,” IEEE Transactions on Computers C-25 (December 1976), pp. 1226–41. (Chapter 1) 





[Boehm, 1979] B. W. BOEHM, “Software Engineering, R & D Trends and Defense Needs,” in: Research Directions in Software Technology , P. Wegner (Editor), The MIT Press, Cambridge, MA, 1979. (Chapter 1) 





[Boehm, 1980] B. W. BOEHM, “Developing Small-Scale Application Software Products: Some Experimental Results,” Proceedings of the Eighth IFIP World Computer Congress, IFIP, October 1980, pp. 321–26. (Chapter 1) 





[Boehm, 1981] B. W. BOEHM, Software Engineering Economics, Prentice Hall, Englewood Cliffs, NJ, 1981. (Chapters 1 and 9) 





[Boehm, 1984] B. W. BOEHM, “Software Engineering Economics,” IEEE Transactions on Software Engi neering SE-10 (January 1984), pp. 4–21. (Chapter 9) 





[Boehm, 1988] B. W. BOEHM, “A Spiral Model of Software Development and Enhancement,” IEEE Com puter 21 (May 1988), pp. 61–72. (Chapter 2) 





[Boehm, 2002] B. W. BOEHM, “Get Ready for Agile Methods, with Care,” IEEE Computer 35 (January 2002), pp. 64–69. (Chapters 2 and 4) 





[Boehm and Basili, 2001] B. BOEHM AND V. R. BASILI, “Software Defect Reduction Top Ten List,” IEEE Computer 34 (January 2001), pp. 135–37. (Chapter 6) 





[Boehm and Huang, 2003] B. BOEHM AND L. G. HUANG, “Value-Based Software Engineering: A Case Study,” IEEE Computer 36 (March 2003), pp. 33–41. (Chapter 1) 





[Boehm and Turner, 2003] B. BOEHM AND R. TURNER, Balancing Agility and Discipline: A Guide for the Perplexed , Addison-Wesley Professional, Boston, MA 2003. (Chapter 2) 





[Boehm and Turner, 2005] B. BOEHM AND R. TURNER, “Management Challenges to Implementing Agile Processes in Traditional Development Organizations,” IEEE Software 22 (September–October 2005), pp. 30–39. (Chapter 2) 





[Boehm et al., 1984] B. W. BOEHM, M. H. PENEDO, E. D. STUCKLE, R. D. WILLIAMS, AND A. B. PYSTER, “A Soft ware Development Environment for Improving Pro ductivity,” IEEE Computer 17 (June 1984), pp. 30–44. (Chapters 2 and 9) 





[Boehm et al., 2000] B. W. BOEHM, C. ABTS, A. W. BROWN, S. CHULANI, B. K. CLARK, E. HOROWITZ, R. MADACHY, D. REIFER, AND B. STEECE, Software Cost Estimation with COCOMO II , Prentice Hall, Upper Saddle River, NJ, 2000. (Chapter 9) 





[Booch, 1994] G. BOOCH, Object-Oriented Analysis and Design with Applications, 2nd ed., Benjamin/ Cummings, Redwood City, CA, 1994. (Chapter 3) 





[Booch, 2000] G. BOOCH, “The Future of Software Engineering,” keynote address, International Conference on Software Engineering, Limerick, Ireland, May 2000. (Chapter 2) 





[Booch, Rumbaugh, and Jacobson, 1999] G. BOOCH, J. RUM-BAUGH, AND I. JACOBSON, The UML Users Guide , Addison-Wesley, Reading, MA, 1999. (Chapters 3, 13, 17) 





[Borjesson and Mathiassen, 2004] A. BORJESSON AND L. MATHIASSEN, “Successful Process Implementation,” IEEE Software 21 (July–August 2004), pp. 36–44. (Chapter 3) 





[Borland, 2002] BORLAND, “Press Release: Borland Unveils C++ Application Development Strategy for 





2002,” www.borland.com/news/press_releases 2002/01_28_02_cpp.strategy.html, January 28, 2002. (Chapter 15) 





[Bosch, 2000] J. BOSCH, Design and Use of Software Architectures, Addison-Wesley, Reading, MA, 2000. (Chapter 8) 





[Bowen and Hinchey, 1995a] J. P. BOWEN AND M. G. HINCHEY, “Ten Commandments of Formal Methods,” IEEE Computer 28 (April 1995), pp. 56–63. (Chapter 12) 





[Bowen and Hinchey, 1995b] J. P. BOWEN AND M. G. HINCHEY, “Seven More Myths of Formal Methods,” IEEE Software 12 (July 1995), pp. 34–41. (Chapter 12) 





[Brady, 1977] J. M. BRADY, The Theory of Computer Sci ence , Chapman and Hall, London, 1977. (Chapter 12) 





[Brereton and Budgen, 2000] P. BRERETON AND D. BUD GEN, “Component-Based Systems: A Classifi cation of Issues,” IEEE Computer 33 (November 2000), pp. 54–62. (Chapter 8) 





[Briand and Wüst, 2001] L. C. BRIAND AND J. WÜST, “Modeling Development Effort in Object-Oriented Systems Using Design Properties,” IEEE Transactions on Software Engineering 27 (November 2001), pp. 963–86. (Chapters 5 and 9) 





[Briand, Bunse, and Daly, 2001] L. C. BRIAND, C. BUNSE, AND J. W. DALY, “A Controlled Experiment for Evalu ating Quality Guidelines on the Maintainability of Object-Oriented Designs,” IEEE Transactions on Software Engineering 27 (June 2001), pp. 513–30. (Chapters 14 and 16) 





[Briand, Daly, Porter, and Wüst, 1998] L. C. BRIAND, J. DALY, V. PORTER, AND J. WÜST, “A Comprehensive Empirical Validation of Design Measures for Object Oriented Systems,” Proceedings of the Fifth Inter national Metrics Symposium, Bethesda, MD, IEEE November 1998, pp. 246–257. (Chapter 7) 





[Briand, Labiche, and Leduc, 2006] L. C. BRIAND, Y. LABICHE, AND J. LEDUC, “Toward the Reverse Engineer ing of UML Sequence Diagrams for Distributed Java Software,” IEEE Transactions on Software Engineer ing 32 (September 2006), pp. 642–63. (Chapter 16) 





[Brooks, 1975] F. P. BROOKS, JR., The Mythical Man Month: Essays on Software Engineering, Addison Wesley, Reading, MA, 1975; Twentieth Anniversary Edition, Addison-Wesley, Reading, MA, 1995. (Chapters 1, 4, and 11) 





[Brooks, 1986] F. P. BROOKS, JR., “No Silver Bullet,” in: Information Processing ’86 , H.-J. Kugler (Editor), 





Elsevier North-Holland, New York, 1986; reprinted in IEEE Computer 20 (April 1987), pp. 10–19. (Chapters 3 and 14) 





[Brooks et al., 1987] F. P. BROOKS, V. BASILI, B. BOEHM, E. BOND, N. EASTMAN, D. L. EVANS, A. K. JONES, M. SHAW, AND C. A. ZRAKET, “Report of the Defense Science Board Task Force on Military Software,” Department of Defense, Offi ce of the Under Secretary of Defense for Acquisition, Washington, DC, September 1987. (Chapter 3) 





[Brown et al., 1998] W. J. BROWN, R. C. MALVEAU, W. H. BROWN, H. W. MCCORMICK III, AND T. J. MOWBRAY, AntiPatterns: Refactoring Software, Architectures, and Projects in Crisis, John Wiley and Sons, New York, 1998. (Chapter 8) 





[Brownsword, Oberndorf, and Sledge, 2000] L. BROWN SWORD, T. OBERNDORF, AND C. A. SLEDGE, “Develop ing New Process for COTS-Based Systems,” IEEE Software 17 (July–August 2000), pp. 40–47. (Chapter 1) 





[Bruegge, Blythe, Jackson, and Shufelt, 1992] B. BRUEGGE, J. BLYTHE, J. JACKSON, AND J. SHUFELT, “Object-Oriented Modeling with OMT,” Proceedings of the Con ference on Object-Oriented Programming, Languages, and Systems, OOPSLA ’92, ACM SIGPLAN Notices 27 (October 1992), pp. 359–76. (Chapter 7) 





[Bruno and Marchetto, 1986] G. BRUNO AND G. MAR-CHETTO, “Process-Translatable Petri Nets for the Rapid Prototyping of Process Control Systems,” IEEE Transactions on Software Engineering SE-12 (February 1986), pp. 346–57. (Chapter 12) 





[Budd, 2002] T. A. BUDD, An Introduction to Object-Oriented Programming , 3rd ed., Addison-Wesley, Reading, MA, 2002. (Chapter 1) 





[Bush, 1990] M. BUSH, “Improving Software Quality: The Use of Formal Inspections at the Jet Propulsion Laboratory,” Proceedings of the 12th International Conference on Software Engineering , Nice, France, IEEE, March 1990, pp. 196–99. (Chapter 6) 





[Business Week Online, 1999] Business Week Online, www.businessweek.com/1999/99_08/b3617025. htm, February 2, 1999. (Chapter 4) 





[Cao and Ramesh, 2008] L. CAO AND B. RAMESH, “Agile Requirements Engineering Practices: An Empirical Study,” IEEE Software 25 (January–February 2008), pp. 60–67. (Chapter 11) 





[Capper, Colgate, Hunter, and James, 1994] N. P. CAPPER, R. J. COLGATE, J. C. HUNTER, AND M. F. JAMES, “The 





Impact of Object-Oriented Technology on Software Quality: Three Case Histories,” IBM Systems Journa 33 (No. 1, 1994), pp. 131–57. (Chapters 1 and 7) 





[Cartwright and Shepperd, 2000] M. CARTWRIGHT AND M. SHEPPERD, “An Empirical Investigation of an Object-Oriented Software System,” IEEE Transactions on Software Engineering 26 (August 2000), pp. 786–95. (Chapters 7 and 9) 





[Ceschi, Sillitti, Succi, and De Panfi lis, 2005] M. CESCHI, A. SILLITTI, G. SUCCI, AND S. DE PANFILIS, “Projec Management in Plan-Based and Agile Companies,” IEEE Software 22 (May–June 2005), pp. 21–27. (Chapter 2) 





[Chen, 1976] P. CHEN, “The Entity-Relationship Model— Towards a Unifi ed View of Data,” ACM Transactions on Database Systems 1 (March 1976), pp. 9–36. (Chapter 12) 





[Chidamber and Kemerer, 1994] S. R. CHIDAMBER AND C. F. KEMERER, “A Metrics Suite for Object Oriented Design,” IEEE Transactions on Software Engineering 20 (June 1994), pp. 476–93. (Chapters 14 and 15) 





[Chow and Cao, 2008] T. CHOW AND D.-B. CAO, “A Sur vey Study of Critical Success Factors in Agile Soft ware Projects,” Journal of Systems and Software 81 (June 2008), pp. 961–71. (Chapter 2) 





[Ciolkowski, Laitenberger, and Biffl , 2003] M. CI-OLKOWSKI, O. LAITENBERGER, AND S. BIFFL, “Software Reviews, the State of the Practice,” IEEE Software 20 (November–December 2003), pp. 46–51. (Chapter 6) 





[Clements and Northrop, 2002] P. CLEMENTS AND L. NORTHROP, Software Product Lines: Practices and Patterns , Addison-Wesley, Reading, MA, 2002. (Chapter 8) 





[Clements, Jones, Northrop, and McGregor, 2005] P. C. CLEMENTS, L. G. JONES, L. M. NORTHROP, AND J. D. MCGREGOR, “Project Management in a Software Prod uct Line Organization,” IEEE Software 22 (September– October 2005), pp. 54–62. (Chapter 8) 





[CNN.com, 2003] “Russia: Software Bug Made Soyuz Stray,” edition.cnn.com/2003/TECH/space/05/06/ soyuz.landing.ap/, May 6, 2003. (Chapter 3) 





[Cobble, 2004] “Cobble,” users.ugent.be/~kdschutt cobble, 2004. (Chapter 18) 





[Cockburn, 2001] A. COCKBURN, Agile Software Development , Addison-Wesley Professional, Reading, MA, 2001. (Chapter 2) 





[Coleman et al., 1994] D. COLEMAN, P. ARNOLD, S. BODOFF, C. DOLLIN, H. GILCHRIST, F. HAYES, AND 





P. JEREMAES, Object-Oriented Development: The Fu sion Method , Prentice Hall, Englewood Cliffs, NJ, 1994. (Chapter 13) 





[Conradi and Fuggetta, 2002] R. CONRADI AND A. FUG-GETTA, “Improving Software Process Improvement,” IEEE Software 19 (July–August 2002), pp. 92–99. (Chapter 3) 





[Coolahan and Roussopoulos, 1983] J. E. COOLAHAN, JR., AND N. ROUSSOPOULOS, “Timing Requirements for Time-Driven Systems Using Augmented Petri Nets,” IEEE Transactions on Software Engineering SE-9 (September 1983), pp. 603–16. (Chapter 12) 





[Costagliola, Ferrucci, Tortora, and Vitiello, 2005] G. COSTAGLIOLA, F. FERRUCCI, G. TORTORA, AND G. VITI-ELLO, “Class Point: An Approach for the Size Estimation of Object-Oriented Systems,” IEEE Transactions on Software Engineering 31 (January 2005), pp. 52–74 (Chapter 9) 





[Crossman, 1982] T. D. CROSSMAN, “Inspection Teams, Are They Worth It?” Proceedings of the Second National Symposium on EDP Quality Assurance , Chicago, IEEE, November 1982. (Chapter 15) 





[Curtis, Hefl ey, and Miller, 2002] B. CURTIS, W. E. HEF-LEY, AND S. A. MILLER, The People Capability Matu rity Model: Guidelines for Improving the Workforce , Addison-Wesley, Reading, MA, 2002. (Chapter 4) 





[Cusumano and Selby, 1995] M. A. CUSUMANO AND R. W. SELBY, Microsoft Secrets: How the World’s Most Powerful Software Company Creates Technology, Shapes Markets, and Manages People , The Free Press/Simon and Schuster, New York, 1995. (Chapters 2 and 4) 





[Cusumano and Selby, 1997] M. A. CUSUMANO AND R. W. SELBY, “How Microsoft Builds Software,” Communications of the ACM 40 (June 1997), pp. 53–61. (Chapters 2 and 4) 





[Cutter Consortium, 2002] Cutter Consortium, “78% of IT Organizations Have Litigated,” The Cutter Edge, www.cutter.com/research/2002/edge020409. html, April 09, 2002. (Chapter 1) 





[Cysneiros and do Prado Leite, 2004] L. M. CYSNEIROS AND J. C. S. DO PRADO LEITE, “Nonfunctional Requirements: From Elicitation to Conceptual Models,” IEEE Transactions on Software Engineering 30 (May 2004), pp. 328–50. (Chapter 11) 





[D’Souza and Wills, 1999] D. D’SOUZA AND H. WILLS, Objects, Components, and Frameworks with UML: The Catalysis Approach , Addison-Wesley, Reading, MA, 1999. (Chapter 13) 





[Dahl and Nygaard, 1966] O.-J. DAHL AND K. NYGAARD, “SIMULA—An ALGOL-Based Simulation Lan guage,” Communications of the ACM 9 (Septembe 1966), pp. 671–78. (Chapter 7) 





[Daly, 1977] E. B. DALY, “Management of Software Development,” IEEE Transactions on Software Engineer ing SE-3 (May 1977), pp. 229–42. (Chapter 1) 





[Damian and Chisan, 2006] D. DAMIAN AND J. CHISAN, “An Empirical Study of the Complex Relationships between Requirements Engineering Processes and Other Processes That Lead to Payoffs in Productivity, Quality, and Risk Management,” IEEE Transactions on Software Engineering 32 (July 2006), pp. 433–53. (Chapters 6, 9, and 11) 





[Dangle, Larsen, Shaw, and Zelkowitz, 2005] K. C. DANGLE, P. LARSEN, M. SHAW, AND M. V. ZELKOWITZ “Software Process Improvement in Small Organizations: A Case Study,” IEEE Software 22 (September– October 2005), pp. 68–75. (Chapter 3) 





[Dart, Ellison, Feiler, and Habermann, 1987] S. A. DART R. J. ELLISON, P. H. FEILER, AND A. N. HABERMANN, “Software Development Environments,” IEEE Com puter 20 (November 1987), pp. 18–28. (Chapter 12) 





[Date, 2003] C. J. DATE, An Introduction to Database Systems, 8th ed., Addison-Wesley, Reading, MA, 2003. (Chapter 15) 





[Dawood, 1994] M. DAWOOD, “It’s Time for ISO 9000,” CrossTalk (March 1994), pp. 26–28. (Chapter 3) 





[de Champeaux and Faure, 1992] D. DE CHAMPEAUX AND P. FAURE, “A Comparative Study of Object Oriented Analysis Methods,” Journal of Object-Oriented Programming 5 (March–April 1992), pp. 21–33. (Chapter 13) 





[Delisle and Garlan, 1990] N. DELISLE AND D. GARLAN, “A Formal Description of an Oscilloscope,” IEEE Software 7 (September 1990), pp. 29–36. (Chapter 12) 





[Delisle and Schwartz, 1987] N. DELISLE AND M. SCHWARTZ, “A Programming Environment for CSP,” Proceedings of the Second ACM SIGSOFT/SIGPLAN Software Engineering Symposium on Practical Soft ware Development Environments, ACM SIGPLAN Notices 22 (January 1987), pp. 34–41. (Chapter 12) 





[DeMarco, 1978] T. DEMARCO, Structured Analysis and System Specifi cation , Yourdon Press, New York, 1978. (Chapter 12) 





[DeMarco and Boehm, 2002] T. DEMARCO AND B. BOEHM, “The Agile Methods Fray,” IEEE Computer 35 (June 2002), pp. 90–92. (Chapters 2 and 4) 





[DeMarco and Lister, 1987] T. DEMARCO AND T. LISTER, Peopleware: Productive Projects and Teams, Dorset House, New York, 1987. (Chapter 4) 





[DeMillo, Lipton, and Perlis, 1979] R. A. DEMILLO, R. J. LIPTON, AND A. J. PERLIS, “Social Processes and Proofs of Theorems and Programs,” Communications of the ACM 22 (May 1979), pp. 271–80. (Chapter 6) 





[DeMillo, Lipton, and Sayward, 1978] R. A. DEMILLO, R. J. LIPTON, AND F. G. SAYWARD, “Hints on Test Data Selection: Help for the Practicing Programmer,” IEEE Computer 11 (April 1978), pp. 34–43. (Chapter 6) 





[Deming, 1986] W. E. DEMING, Out of the Crisis , MIT Center for Advanced Engineering Study, Cambridge, MA, 1986. (Chapter 3) 





[Denger and Shull, 2007] C. DENGER AND F. SHULL, “A Practical Approach for Quality-Driven Inspections,” IEEE Software 24 (March–April 2007), pp. 79–86. (Chapter 6) 





[DeRemer and Kron, 1976] F. DEREMER AND H. H. KRON, “Programming-in-the-Large versus Programming-inthe-Small,” IEEE Transactions on Software Engineering SE-2 (June 1976), pp. 80–86. (Chapter 5) 





[Devenny, 1976] T. DEVENNY, “An Exploratory Study of Software Cost Estimating at the Electronic Systems Division,” Thesis No. GSM/SM/765–4, Ai Force Institute of Technology, Dayton, OH, 1976. (Chapter 9) 





[Devlin, 2001] K. DEVLIN, “The Real Reason Why Software Engineers Need Math,” Communications of the ACM 44 (October 2001), pp. 21–22. (Chapter 1) 





[Dhamija, Tygar, and Hearst, 2006] R. DHAMIJA, J. D. TYGAR, AND M. HEARST, “Why Phishing Works,” Proceedings of the SIGCHI Conference on Human Factors , Montréal, Québec, Canada, ACM, April 2006, pp. 581–90. (Chapter 18) 





[Diaz and Sligo, 1997] M. DIAZ AND J. SLIGO, “How Software Process Improvement Helped Motorola,” IEEE Software 14 (September–October 1997), pp. 75–81. (Chapter 3) 





[Dig, Manzoor, Johnson, and Nguyen, 2008] D. DIG, K. MANZOOR, R. E. JOHNSON, AND T. N. NGUYEN, “Effective Software Merging in the Presence of Object-Oriented Refactorings,” IEEE Transactions on Soft ware Engineering 34 (May–June 2008), pp. 321–35. (Chapters 2 and 5) 





[Dijkstra, 1968] E. W. DIJKSTRA, “A Constructive Approach to the Problem of Program Correctness,” BIT 8 (No. 3, 1968), pp. 174–86. (Chapter 6) 





[Dijkstra, 1972] E. W. DIJKSTRA, “The Humble Programmer,” Communications of the ACM 15 (October 1972), pp. 859–66. (Chapter 6) 





[Dijkstra, 1976] E. W. DIJKSTRA, A Discipline of Pro gramming, Prentice Hall, Englewood Cliffs, NJ, 1976. (Chapter 5) 





[Dijkstra, 1982] E. W. DIJKSTRA, “On the Role of Scientifi c Thought,” in: Dijkstra, Edsger W., Selected Writ ings on Computing: A Personal Perspective, Springer-Verlag, New York, 1982, pp. 60–66. (Chapters 5 and 18) 





[Diller, 1994] A. DILLER, Z: An Introduction to Formal Methods , 2nd ed., John Wiley and Sons, Chichester, UK, 1994. (Chapter 12) 





[Dion, 1993] R. DION, “Process Improvement and the Corporate Balance Sheet,” IEEE Software 10 (July 1993), pp. 28–35. (Chapter 3) 





[Donzelli et al., 2005] P. DONZELLI, M. ZELKOWITZ, V. BASILI, D. ALLARD, AND K. N. MEYER, “Evaluat ing COTS Component Dependability in Context,” IEEE Software 22 (July–August 2005), pp. 46–53. (Chapter 1) 





[Doolan, 1992] E. P. DOOLAN, “Experience with Fagan’s Inspection Method,” Software—Practice and Experi ence 22 (February 1992), pp. 173–82. (Chapter 12) 





[Dooley and Schach, 1985] J. W. M. DOOLEY AND S. R. SCHACH, “FLOW: A Software Development Environ ment Using Diagrams,” Journal of Systems and Soft ware 5 (August 1985), pp. 203–19. (Chapter 5) 





[Drobka, Noftz, and Raghu, 2004] J. DROBKA, D. NOFTZ, AND R. RAGHU, “Piloting XP on Four Mission-Critica Projects,” IEEE Software 21 (November–Decembe 2004), pp. 70–75. (Chapters 2 and 4) 





[Dunn, 1984] R. H. DUNN, Software Defect Removal, McGraw-Hill, New York, 1984. (Chapter 15) 





[Dunsmore, Roper, and Wood, 2003] A. DUNSMORE, M. ROPER, AND M. WOOD, “The Development and Evalu ation of Three Diverse Techniques for Object-Oriented Code Inspection,” IEEE Transactions on Software Engineering 29 (August 2003), pp. 677–86. (Chapter 6) 





[Dybå, 2005] T. DYBÅ, “An Empirical Investigation of the Key Factors for Success in Software Process Improvement,” IEEE Transactions in Software Engineering 31 (May 2005), pp. 410–24. (Chapter 3) 





[Dybå et al., 2007] T. DYBÅ, E. ARISHOLM, D. I. K. SJØ- BERG, J. E. HANNAY, AND F. SHULL, “Are Two Heads Better than One? On the Effectiveness of Pair Pro gramming,” IEEE Software 24 (November–December 2007), pp. 12–15. (Chapters 2 and 4) 





[Dzidek, Arisholm, and Briand, 2008] W. J. DZIDEK, E. ARISHOLM, AND L. C. BRIAND, “A Realistic Empiri cal Evaluation of the Costs and Benefi ts of UML in Software Maintenance,” IEEE Transactions on Software Engineering 34 (May–June 2008), pp. 407–32. (Chapter 16) 





[Ebert, 2006] C. EBERT, “Understanding the Product Life Cycle: Four Key Requirements Engineering Techniques,” IEEE Software 23 (May–June 2006), pp. 19–25. (Chapter 11) 





[Ebner and Kaindl, 2002] G. EBNER AND H. KAINDL, “Tracing All Around in Reengineering,” IEEE Software 19 (May–June 2002), pp. 70–77. (Chapter 16) 





[Eickelmann, 2003] N. EICKELMANN, “An Insider’s View of CMM Level 5,” IEEE Software 20 (July–August 2003), pp. 79–81. (Chapter 3) 





[Eickelmann and Anant, 2003] N. EICKELMANN AND A. ANANT, “Statistical Process Control: What You Don’t Know Can Hurt You!” IEEE Software 20 (March– April 2003), pp. 49–51. (Chapter 3) 





[Elbaum, Malishevsky, and Rothermel, 2002] S. ELBAUM, A. G. MALISHEVSKY, AND G. ROTHERMEL, “Test Case Prioritization: A Family of Empirical Studies,” IEEE Transactions on Software Engineering 28 (February 2002), pp. 159–82. (Chapter 15) 





[El Emam, Benlarbi, Goel, and Rai, 2001] K. EL EMAM, S. BENLARBI, N. GOEL, AND S. N. RAI, “The Confounding Effect of Class Size on the Validity of Object Oriented Metrics,” IEEE Transactions on Software Engineering 27 (July 2001), pp. 630–50. (Chapter 5) 





[Elrad et al., 2001] T. ELRAD, M. AKSIT, G. KICZALES, K. LIEBERHERR, AND H. OSSHER, “Discussing Aspects of AOP,” Communications of the ACM 44 (October 2001), pp. 33–38. (Chapter 7) 





[Elshoff, 1976] J. L. ELSHOFF, “An Analysis of Some Commercial PL/I Programs,” IEEE Transactions on Software Engineering SE-2 (June 1976), pp. 113–20. (Chapter 1) 





[Embley, Jackson, and Woodfi eld, 1995] D. W. EMBLEY, R. B. JACKSON, AND S. N. WOODFIELD, “OO Systems Analysis: Is It or Isn’t It?” IEEE Software 12 (July 1995), pp. 18–33. (Chapter 13) 





[Endres, 1975] A. ENDRES, “An Analysis of Errors and Their Causes in System Programs,” IEEE Transactions on Software Engineering SE-1 (June 1975), pp. 140–49. (Chapter 15) 





[Erdogmus, Morisio, and Torchiano, 2005] H. ERDOGMUS, M. MORISIO, AND M. TORCHIANO, “On the Effectiveness 





of the Test-First Approach to Programming,” IEEE Transactions on Software Engineering 31 (March 2005), pp. 226–37. (Chapter 2) 





[Fach, 2001] P. W. FACH, “Design Reuse through Frame works and Patterns,” IEEE Software 18 (September– October 2001), pp. 71–76. (Chapter 8) 





[Fagan, 1974] M. E. FAGAN, “Design and Code Inspec tions and Process Control in the Development of Pro grams,” Technical Report IBM-SSD TR 21.572, IBM Corporation, December 1974. (Chapter 1) 





[Fagan, 1976] M. E. FAGAN, “Design and Code Inspections to Reduce Errors in Program Development,” IBM Systems Journal 15 (No. 3, 1976), pp. 182–211 (Chapters 6, 12, and 14) 





[Fagan, 1986] M. E. FAGAN, “Advances in Software Inspections,” IEEE Transactions on Software Engi neering SE-12 (July 1986), pp. 744–51. (Chapters 6 and 14) 





[Feather et al., 2008] M. S. FEATHER, S. L. CORNFORD, K. A. HICKS, J. D. KIPER, AND T. MENZIES, “A Broad, Quantitative Model for Making Early Requirements Decisions,” IEEE Software 25 (March–April 2008), pp. 49–56. (Chapter 11) 





[Feldman, 1979] S. I. FELDMAN, “Make—A Program for Maintaining Computer Programs,” Software—Prac tice and Experience 9 (April 1979), pp. 225–65. (Chapter 5) 





[Ferguson and Sheard, 1998] J. FERGUSON AND S. SHEARD, “Leveraging Your CMM Efforts for IEEE/EIA 12207,” IEEE Software 15 (September–October 1998), pp. 23–28. (Chapter 3) 





[Ferguson et al., 1997] P. FERGUSON, W. S. HUMPHREY, S. KHAJENOORI, S. MACKE, AND A. MATVYA, “Result of Applying the Personal Software Process,” IEEE Computer 30 (May 1997), pp. 24–31. (Chapter 3) 





[Ferrari and Madhavji, 2008] R. FERRARI AND N. H. MAD-HAVJI, “Software Architecting without Requirements Knowledge and Experience: What Are the Repercussions?” Journal of Systems and Software 81 (Septem ber 2008), pp. 1470–90. (Chapter 8) 





[Fichman and Kemerer, 1992] R. G. FICHMAN AND C. F. KEMERER, “Object-Oriented and Conventional Analy sis and Design Methodologies: Comparison and Critique,” IEEE Computer 25 (October 1992), pp. 22–39. (Chapters 13 and 14) 





[Fingar, 2000] P. FINGAR, “Component-Based Frameworks for e-Commerce,” Communications of the ACM 43 (October 2000), pp. 61–66. (Chapter 8) 





[Finkelstein, 2000] A. FINKELSTEIN (Editor), The Future of Software Engineering , IEEE Computer Society Press, Los Alamitos, CA, 2000. (Chapter 1) 





[Finney, 1996] K. FINNEY, “Mathematical Notation in Formal Specifi cation: Too Diffi cult for the Masses?” IEEE Transactions on Software Engineering 22 (1996), pp. 158–59. (Chapter 12) 





[Fioravanti and Nesi, 2001] F. FIORAVANTI AND P. NESI, “Estimation and Prediction Metrics for Adaptive Maintenance Effort of Object-Oriented Systems,” IEEE Transactions on Software Engineering 27 (December 2001), pp. 1062–84. (Chapter 16) 





[Flanagan, 2005] D. FLANAGAN, Java in a Nutshell: A Desktop Quick Reference , 5th ed., O’Reilly and Associates, Sebastopol, CA, 2005. (Chapters 7, 8, and 14) 





[Flor, 2006] N. V. FLOR. “Globally Distributed Software Development and Pair Programming,” Communications of the ACM 49 (October 2006), pp. 57–58. (Chapter 4) 





[Florac, Carleton, and Barnard, 2000] W. A. FLORAC, A. D. CARLETON, AND J. BARNARD, “Statistical Process Control: Analyzing a Space Shuttle Onboard Software Process,” IEEE Software 17 (July–August 2000), pp. 97–106. (Chapter 3) 





[ Florida Today , 1999] “Milstar Satellite Lost during Air Force Titan 4b Launch from Cape,” Florida Today, www.fl oridatoday.com/space/explore/uselv/titan/ b32/, June 5, 1999. (Chapter 3) 





[Fowler, 1986] P. J. FOWLER, “In-Process Inspections of Work Products at AT&T,” AT&T Technical Journal 65 (March–April 1986), pp. 102–12. (Chapter 6) 





[Fowler, 1997] M. FOWLER, Analysis Patterns: Reusable Object Models , Addison-Wesley, Reading, MA, 1997. (Chapter 8) 





[Fowler and Scott, 2000] M. FOWLER WITH K. SCOTT, UML Distilled, 2nd ed., Addison-Wesley, Upper Sad dle River, NJ, 2000. (Chapter 17) 





[Fowler et al., 1999] M. FOWLER WITH K. BECK, J. BRANT, W. OPDYKE, AND D. ROBERTS, Refactoring: Improving the Design of Existing Code , Addison-Wesley, Reading, MA, 1999. (Chapter 2) 





[Frakes and Kang, 2005] W. B. FRAKES AND K. KANG, “Software Reuse Research: Status and Future,” IEEE Transactions on Software Engineering 31 (July 2005), pp. 529–36. (Chapter 8) 





[Främling, Ala-Risku, Kärkkäinen, and Holmström, 2007] K. FRÄMLING, T. ALA-RISKU, M. KÄRKKÄINEN, AND J. HOLMSTRÖM, “Design Patterns for Managing Product 





Life Cycle Information,” Communications of the ACM 50 (June 2007), pp. 75–79. (Chapter 8) 





[Freeman and Schach, 2005] G. L. FREEMAN, JR. AND S. R. SCHACH, “The Task-Dependent Nature of the Maintenance of Object-Oriented Programs,” Journa of Systems and Software 76 (May 2005), pp. 195–206. (Chapter 16) 





[Freimut, Briand, and Vollei, 2005] B. FREIMUT, L. C. BRIAND, AND F. VOLLEI, “Determining Inspection Cost-Effectiveness by Combining Project Data and Exper Opinion,” IEEE Transactions on Software Engineering 31 (December 2005), pp. 1074–92. (Chapter 6) 





[Fu, Milanova, Ryder, and Wonnacott, 2005] C. FU, A. MILANOVA, B. G. RYDER, AND D. G. WONNACOTT, “Robustness Testing of Java Server Applications,” IEEE Transactions on Software Engineering 31 (Apri 2005), pp. 292–311. (Chapter 6) 





[Fuggetta, 1993] A. FUGGETTA, “A Classifi cation of CASE Technology,” IEEE Computer 26 (December 1993), pp. 25–38. (Chapter 5) 





[Furey and Kitchenham, 1997] S. FUREY AND B. KITCH ENHAM, “Function Points,” IEEE Software 14 (March– April 1997), pp. 28–32. (Chapter 9) 





[Galin and Avrahami, 2006] D. GALIN AND M. AVRAHAMI, “Are CMM Program Investments Benefi cial? Analyz ing Past Studies,” IEEE Software 23 (November– December 2006), pp. 81–87. (Chapter 3) 





[Gamma, Helm, Johnson, and Vlissides, 1995] E. GAMMA, R. HELM, R. JOHNSON, AND J. VLISSIDES, Design Patterns: Elements of Reusable Object Oriented Software , Addison-Wesley, Reading, MA 1995. (Chapter 8) 





[Gane and Sarsen, 1979] C. GANE AND T. SARSEN, Structured Systems Analysis: Tools and Techniques , Prentice Hall, Englewood Cliffs, NJ, 1979. (Chapters 12 and 14) 





[Garman, 1981] J. R. GARMAN, “The ‘Bug’ Heard ’Round the World,” ACM SIGSOFT Software Engineering Notes 6 (October 1981), pp. 3–10. (Chapter 3) 





[Gelperin and Hetzel, 1988] D. GELPERIN AND B. HETZEL, “The Growth of Software Testing,” Communications of the ACM 31 (June 1988), pp. 687–95. (Chapter 6) 





[Gerald and Wheatley, 1999] C. F. GERALD AND P. O. WHEATLEY, Applied Numerical Analysis , 6th ed., Addison-Wesley, Reading, MA, 1999. (Chapter 7) 





[Ghezzi and Mandrioli, 1987] C. GHEZZI AND D. MAN DRIOLI, “On Eclecticism in Specifi cations: A Case Study Centered around Petri Nets,” Proceedings of the 





Fourth International Workshop on Software Specifi ca tion and Design , Monterey, CA, 1987, pp. 216–24. (Chapter 12) 





[Gifford and Spector, 1987] D. GIFFORD AND A. SPECTOR, “Case Study: IBM’s System/360-370 Architecture,” Communications of the ACM 30 (April 1987), pp. 292–307. (Chapter 8) 





[GJSentinel.com, 2003] “Sallie Mae’s Errors Double Some Bills,” www.gjsentinel.com/news/content/ coxnet/headlines/0522_salliemae.html, May 22, 2003. (Chapter 1) 





[Glinz, 2008] M. GLINZ, “A Risk-Based, Value-Oriented Approach to Quality Requirements,” IEEE Software 25 (March–April 2008), pp. 34–41. (Chapter 11) 





[Goldberg and Robson, 1989] A. GOLDBERG AND D. ROB-SON, Smalltalk-80: The Language, Addison-Wesley, Reading, MA, 1989. (Chapters 7 and 14) 





[Gomaa, 2000] H. GOMAA, Designing Concurrent, Distributed, and Real-time Applications with UML, Addison-Wesley, Reading, MA, 2000. (Chapter 14) 





[Goodenough, 1979] J. B. GOODENOUGH, “A Survey of Program Testing Issues,” in: Research Directions in Software Technology , P. Wegner (Editor), The MIT Press, Cambridge, MA, 1979, pp. 316–40. (Chapter 6) 





[Goodenough and Gerhart, 1975] J. B. GOODENOUGH AND S. L. GERHART, “Toward a Theory of Test Data Selection,” Proceedings of the Third International Conference on Reliable Software , Los Angeles, 1975, pp. 493–510; also published in IEEE Transactions on Software Engineering SE-1 (June 1975), pp. 156–73. Revised version: J. B. Goodenough and S. L. Gerhart, “Toward a Theory of Test Data Selection: Data Selection Criteria,” in: Current Trends in Programming Methodology, Vol. 2, R. T. Yeh (Editor), Prentice Hall, Englewood Cliffs, NJ, 1977, pp. 44–79. (Chapters 6 and 12) 





[Gordon, 1979] M. J. C. GORDON, The Denotational Description of Programming Languages: An Introduc tion , Springer-Verlag, New York, 1979. (Chapter 12) 





[Gorla and Lam, 2004] N. GORLA AND Y. W. LAM, “Who Should Work with Whom?” Communications of the ACM 47 (June 2004), pp. 79–82. (Chapter 4) 





[Goth, 2000] G. GOTH, “New Air Traffi c Control Software Takes an Incremental Approach,” IEEE Software 17 (July–August 2000), pp. 108–111. (Chapter 2) 





[Grady, 1992] R. B. GRADY, Practical Software Metrics for Project Management and Process Improvement , Prentice Hall, Englewood Cliffs, NJ, 1992. (Chapter 15) 





[Grady, 1994] R. B. GRADY, “Successfully Applying Soft ware Metrics,” IEEE Computer 27 (September 1994), pp. 18–25. (Chapter 1) 





[Gramlich, 1997] E. M. GRAMLICH, A Guide to Benefi t– Cost Analysis , 2nd ed., Waveland Books, Prospect Heights, IL, 1997. (Chapter 5) 





[Green, 2000] P. GREEN, “FW: Here’s an Update to the Simulated Kangaroo Story,” The Risks Digest 20 (January 23, 2000), catless.ncl.ac.uk/Risks/20.76. html. (Chapter 8) 





[Gregoriades and Sutcliffe, 2005] A. GREGORIADES AND A. SUTCLIFFE, “Scenario-Based Assessment of Nonfunctional Requirements,” IEEE Transactions on Software Engineering 31 (May 2005), pp. 392–409. (Chapter 11) 





[Griss, 1993] M. L. GRISS, “Software Reuse: From Library to Factory,” IBM Systems Journal 32 (No. 4 1993), pp. 548–66. (Chapter 8) 





[Guéhéneuc and Antoniol, 2008] Y.-G. GUÉHÉNEUC AND G. ANTONIOL, “DeMIMA: A Multilayered Approach for Design Pattern Identifi cation,” IEEE Transaction on Software Engineering 34 (September–October 2008), pp. 667–84. (Chapter 8) 





[Guerrero and Eterovic, 2004] F. GUERRERO AND Y. ETEROVIC, “Adopting the SW-CMM in a Small IT Organization,” IEEE Software 21 (July–August 2004), pp. 29–35. (Chapter 3) 





[Guha, Lang, and Bassiouni, 1987] R. K. GUHA, S. D. LANG, AND M. BASSIOUNI, “Software Specifi cation and Design Using Petri Nets,” Proceedings of the Fourth International Workshop on Software Specifi cation and Design , Monterey, CA, IEEE, April 1987, pp. 225–30. (Chapter 12) 





[Guimaraes, 1985] T. GUIMARAES, “A Study of Applica tion Program Development Techniques,” Commu nications of the ACM 28 (May 1985), pp. 494–99. (Chapter 15) 





[Guinan, Cooprider, and Sawyer, 1997] P. J. GUINAN, J. G. COOPRIDER, AND S. SAWYER, “The Effective Use of Automated Application Development Tools,” IBM Systems Journal 36 (No. 1, 1997), pp. 124–39. (Chapter 5) 





[Guttag, 1977] J. GUTTAG, “Abstract Data Types and the Development of Data Structures,” Communications of the ACM 20 (June 1977), pp. 396–404. (Chapter 7) 





[Hadar and Leron, 2008] I. HADAR AND U. LERON, “How Intuitive Is Object-Oriented Design?” Communications of the ACM 51 (May 2008), pp. 41–46. (Chapter 14) 





[Hagge and Lappe, 2005] L. HAGGE AND K. LAPPE, “Sharing Requirements Engineering Experience 





Using Patterns,” IEEE Software 22 (January–February 2005), pp. 24–31. (Chapter 8) 





[Hall, 1990] A. HALL, “Seven Myths of Formal Methods,” IEEE Software 7 (September 1990), pp. 11–19. (Chapter 12) 





[Hall and Chapman, 2002] A. HALL AND R. CHAPMAN, “Correctness by Construction: Developing a Commer cial Secure System,” IEEE Software 19 (January– February 2002), pp. 18–25. (Chapter 12) 





[Hanssen and Fægri, 2008] G. K. HANSSEN AND T. E. FÆGRI, “Process Fusion: An Industrial Case Study on Agile Software Product Line Engineering,” Journal of Systems and Software 81 (April 2008), pp. 502–16. (Chapter 8) 





[Hansson, Dittrich, Gustafsson, and Zarnak, 2006] C. HANS-SON, Y. DITTRICH, B. GUSTAFSSON, AND S. ZARNAK, “How Agile are Industrial Software Development Practices?” Journal of Systems and Software 79 (September 2006), pp. 1217–58. (Chapter 2) 





[Harel and Gery, 1997] D. HAREL AND E. GERY, “Executable Object Modeling with Statecharts,” IEEE Computer 30 (July 1997), pp. 31–42. (Chapters 12 and 13) 





[Harel et al., 1990] D. HAREL, H. LACHOVER, A. NAAMAD, A. PNUELI, M. POLITI, R. SHERMAN, A. SHTULL-TRAURING, AND M. TRAKHTENBROT, “STATEMATE: A Working Environment for the Development of Complex Reactive Systems,” IEEE Transactions on Software Engineering 16 (April 1990), pp. 403–14. (Chapters 12 and 15) 





[Harrison, 2004] W. HARRISON, “The Dangers of End-User Programming,” IEEE Software 21 (July–August 2004), pp. 5–7. (Chapter 15) 





[Harrold and Soffa, 1991] M. J. HARROLD AND M. L. SOFFA, “Selecting and Using Data for Integration Testing,” IEEE Software 8 (1991), pp. 58–65. (Chapter 15) 





[Harrold, McGregor, and Fitzpatrick, 1992] M. J. HAR-ROLD, J. D. MCGREGOR, AND K. J. FITZPATRICK, “Incremental Testing of Object-Oriented Class Structures,” Proceedings of the 14th International Conference on Software Engineering , Melbourne, Australia, IEEE, May 1992, pp. 68–80. (Chapter 15) 





[Harrold, Rosenblum, Rothermel and Weyuker, 2001] M. J. HARROLD, D. ROSENBLUM, G. ROTHERMEL, AND E. WEYUKER, “Empirical Studies of a Prediction Model for Regression Test Selection,” IEEE Transactions on Software Engineering 27 (March 2001), pp. 248–63. (Chapter 16) 





[Hatton, 1998] L. HATTON, “Does OO Sync with How We Think?” IEEE Software 15 (May–June 1998), pp. 46–54. (Chapter 1) 





[Hatton, 2008] L. HATTON, “Testing the Value of Check lists in Code Inspections,” IEEE Software 25 (July– August 2008), pp. 82–88. (Chapter 6) 





[Haxthausen and Peleska, 2000] A. E. HAXTHAUSEN AND J. PELESKA, “Formal Development and Verifi cation of a Distributed Railway Control System,” IEEE Transactions on Software Engineering 26 ( August 2000), pp. 687–701. (Chapter 12) 





[Hayes, 2004] F. HAYES, “Chaos Is Back,” Computerworld, www.computerworld.com/managementtopics management/project/story/0,10801,97283,00. html, November 8, 2004. (Chapter 2) 





[Heinemann, Kangasharju, Lyardet, and Mühlhäuser, 2003] A. HEINEMANN, J. KANGASHARJU, F. LYARDET, AND M. MÜHLHÄUSER, “iClouds— Peer-to-Peer Information Sharing in Mobile Environments,” Proceedings of the Internationa Conference on Parallel and Distributed Computing (Euro-Par 2003) , Klagenfurt, Austria, IEEE, August 2003. (Chapter 18) 





[Henry and Kafura, 1981] S. M. HENRY AND D. KAFURA, “Software Structure Metrics Based on Information Flow,” IEEE Transactions on Software Engineering SE-7 (September 1981), pp. 510–18. (Chapter 14) 





[Highsmith and Cockburn, 2001] J. HIGHSMITH AND A. COCKBURN, “Agile Software Development: The Busi ness of Innovation,” IEEE Computer 34 (Septembe 2001), pp. 120–22. (Chapter 2) 





[Hinchey et al., 2008] M. HINCHEY, M. JACKSON, P. COU SOT, B. COOK, J. P. BOWEN, AND T. MARGARIA, “Software Engineering and Formal Methods,” Communica tions of the ACM 51 (September 2008), pp. 54–59. (Chapters 6 and 12) 





[Hoare, 1969] C. A. R. HOARE, “An Axiomatic Basis fo Computer Programming,” Communications of the ACM 12 (October 1969), pp. 576–83. (Chapter 6) 





[Hoare, 1981] C. A. R. HOARE, “The Emperor’s Old Clothes,” Communications of the ACM 24 (February 1981), pp. 75–83. (Chapter 6) 





[Hoare, 1985] C. A. R. HOARE, Communicating Sequen tial Processes , Prentice Hall International, Englewood Cliffs, NJ, 1985. (Chapter 12) 





[Hoare, 1987] C. A. R. HOARE, “An Overview of Some Formal Methods for Program Design,” IEEE Computer 20 (September 1987), pp. 85–91. (Chapter 14) 





[Hoepman and Jacobs, 2007] J.-H. HOEPMAN AND B. JACOBS, “Increased Security through Open Source,” Communications of the ACM 50 (January 2007), pp. 79–83. (Chapter 1) 





[Holzinger, 2005] A. HOLZINGER, “Usability Engineering Methods for Software Developers,” Communications of the ACM 48 (January 2005), pp. 71–74. (Chapter 11) 





[Horgan, London, and Lyu, 1994] J. R. HORGAN, S. LON-DON, AND M. R. LYU, “Achieving Software Quality with Testing Coverage Measures,” IEEE Computer 27 ( 1994), pp. 60–69. (Chapter 15) 





[Howden, 1987] W. E. HOWDEN, Functional Program Testing and Analysis , McGraw-Hill, New York, 1987. (Chapter 15) 





[Hsueh, Chu, and Chu, 2008] N. HSUEH, P. CHU, AND W. CHU, “A Quantitative Approach for Evaluating the Quality of Design Patterns,” Journal of Systems and Software 81 (August 2008), pp. 1430–39. (Chapter 8) 





[Humphrey, 1989] W. S. HUMPHREY, Managing the Soft ware Process , Addison-Wesley, Reading, MA, 1989. (Chapter 3) 





[Humphrey, 1996] W. S. HUMPHREY, “Using a Defi ned and Measured Personal Software Process,” IEEE Soft ware 13 (May 1996), pp. 77–88. (Chapter 3) 





[Humphrey, Snider, and Willis, 1991] W. S. HUMPHREY, T. R. SNIDER, AND R. R. WILLIS, “Software Process Improvement at Hughes Aircraft,” IEEE Software 8 (July 1991), pp. 11–23. (Chapter 3) 





[Hwang, 1981] S.-S. V. HWANG, “An Empirical Study in Functional Testing, Structural Testing, and Code Read ing Inspection,” Scholarly Paper 362, Department of Computer Science, University of Maryland, College Park, 1981. (Chapter 15) 





[Iacovou and Nakatsu, 2008] C. L. IACOVOU AND R. NAKATSU, “A Risk Profi le of Offshore-Outsourced Development Projects,” Communications of the ACM 51 (June 2008), pp. 89–94. (Chapter 2) 





[IEEE 610.12, 1990] “A Glossary of Software Engineering Terminology,” IEEE 610.12-1990, Institute of Electrical and Electronic Engineers, Inc., 1990. (Chapters 1 and 6) 





[IEEE 1028, 1997] Standard for Software Reviews , IEEE 1028, Institute of Electrical and Electronic Engineers, New York, 1997. (Chapter 6) 





[IEEE 1058, 1998] “IEEE Standard for Software Project Management Plans.” IEEE Std. 1058-1998, Institute of Electrical and Electronic Engineers, New York, 1998. (Chapter 9) 





[IEEE Standards, 2003] “Products and Projects Status Report,” standards.ieee.org/db/status/status.txt June 3, 2003. (Chapter 1) 





[IEEE/ACM, 1999] “Software Engineering Code of Ethics and Professional Practice, Version 5.2, as Recommended by the IEEE-CS/ACM Joint Task Force on Software Engineering Ethics and Professional Prac tice,” www.computer.org/tab/seprof/code.htm, 1999. (Chapter 1) 





[IEEE/EIA 12207.0-1996, 1998] “IEEE/EIA 12207.0- 1996 Industry Implementation of International Standard ISO/IEC 12207:1995,” Institute of Electrical and Electronic Engineers, Electronic Industries Alliance, New York, 1998. (Chapters 1 and 3) 





[In, Baik, Kim, Yang, and Boehm, 2006] H. P. IN, J. BAIK, S. KIM, Y. YANG, AND B. BOEHM, “A Quality-Based Cost Estimation Model for the Product Line Life Cycle,” Communications of the ACM 49 (December 2006), pp. 85–88. (Chapter 9) 





[ISO 9000-3, 1991] “ISO 9000-3, Guidelines for the Ap plication of ISO 9001 to the Development, Supply, and Maintenance of Software,” International Organization for Standardization, Geneva, 1991. (Chapter 3) 





[ISO 9001, 1987] “ISO 9001, Quality Systems—Mode for Quality Assurance in Design/Development, Production, Installation, and Servicing,” Internationa Organization for Standardization, Geneva, 1987. (Chapter 3) 





[ISO/IEC 1539–1, 2004] Information Technology— Programming Languages—Fortran—Part 1: Base Language , ISO/IEC 1539–1, International Organization for Standardization, International Electrotechni cal Commission, Geneva, 2004. (Chapter 8) 





[ISO/IEC 1989, 2002] Information Technology— Programming Language COBOL , ISO 1989:2002 International Organization for Standardization, Inter national Electrotechnical Commission, Geneva, 2002. (Chapter 8) 





[ISO/IEC 8652, 1995] Programming Language Ada: Language and Standard Libraries , ISO/IEC 8652, International Organization for Standardization, International Electrotechnical Commission, Geneva, 1995. (Chapters 8 and 14) 





[ISO/IEC 12207, 1995] “ISO/IEC 12207:1995, Information Technology—Software Life-Cycle Processes,” International Organization for Standardization, International Electrotechnical Commission, Geneva, 1995. (Chapters 1, 2 and 3) 





[ISO/IEC 14882, 1998] Programming Language C++ , ISO/IEC 14882, International Organization for Standardization, International Electrotechnical Commission, Geneva, 1998. (Chapter 8) 





[IWSSD, 1986] Call for Papers, Fourth International Workshop on Software Specifi cation and Design, ACM SIGSOFT Software Engineering Notes 11 ( April 1986), pp. 94–96. (Chapter 12) 





[Jackson, 1975] M. A. JACKSON, Principles of Program Design , Academic Press, New York, 1975. (Chapter 14) 





[Jackson, 1995] M. JACKSON, Software Requirements and Specifi cations: A Lexicon of Practice, Principles and Prejudices, Addison-Wesley Longman, Reading, MA, 1995. (Chapter 11) 





[Jackson and Chapin, 2000] D. JACKSON AND J. CHAPIN, “Redesigning Air Traffi c Control: An Exercise in Software Design,” IEEE Software 17 (May–June 2000), pp. 63–70. (Chapter 14) 





[Jacobson, Booch, and Rumbaugh, 1999] I. JACOBSON, G. BOOCH, AND J. RUMBAUGH, The Unifi ed Software Development Process , Addison-Wesley, Reading, MA, 1999. (Chapters 2, 3, 11, 13, 15, 16) 





[Jacobson, Christerson, Jonsson, and Overgaard, 1992] I. JACOBSON, M. CHRISTERSON, P. JONSSON, AND G. OVERGAARD, Object-Oriented Software Engineering: A Use Case Driven Approach , ACM Press, New York, 1992. (Chapter 13) 





[Jalote, Palit, Kurien, and Peethamber, 2004] P. JALOTE, A. PALIT, P. KURIEN, AND V. T. PEETHAMBER, “Timeboxing: A Process Model for Iterative Software Development,” Journal of Systems and Software 70 (February 2004), pp. 117–27. (Chapter 2) 





[Jeffrey and Gupta, 2007] D. J N. G , “Im proving Fault Detection Capability by Selectively Retaining Test Cases during Test Suite Reduction,” IEEE Transactions on Software Engineering 33 (February 2007), pp. 108–23. (Chapter 16) 





[Jézéquel and Meyer, 1997] J.-M. JÉZÉQUEL AND B. MEYER, “Put It in the Contract: The Lessons of Ari ane,” IEEE Computer 30 (January 1997), pp. 129–30. (Chapter 8) 





[Jing, Sheng, and Kang, 2007] D. JING, Y. SHENG, AND Z. KANG, “Visualizing Design Patterns in Their Applications and Compositions,” IEEE Transactions on Software Engineering 32 (July 2007), pp. 433–53. (Chapter 8) 





[Johnson, 1979] S. C. JOHNSON, “A Tour through the Portable C Compiler,” 7th ed., UNIX Programmer’s Manual, Bell Laboratories, Murray Hill, NJ, January 1979. (Chapter 8) 





[Johnson, 2000] R. A. JOHNSON, “The Ups and Down of Object-Oriented System Development,” Commu nications of the ACM 43 (October 2000), pp. 69–73. (Chapters 1 and 7) 





[Johnson and Ritchie, 1978] S. C. JOHNSON AND D. M. RITCHIE, “Portability of C Programs and the UNIX System,” Bell System Technical Journal 57 (No. 6, Part 2, 1978), pp. 2021–48. (Chapter 8) 





[Jones, 1978] T. C. JONES, “Measuring Programming Quality and Productivity,” IBM Systems Journal 17 (No. 1, 1978), pp. 39–63. (Chapter 6) 





[Jones, 1984] T. C. JONES, “Reusability in Programming: A Survey of the State of the Art,” IEEE Transactions on Software Engineering SE-10 (September 1984), pp. 488–94. (Chapter 8) 





[Jones, 1986a] C. JONES, Programming Productivity McGraw-Hill, New York, 1986. (Chapter 9) 





[Jones, 1986b] C. B. JONES, Systematic Software Develop ment Using VDM , Prentice Hall, Englewood Cliffs, NJ, 1986. (Chapter 12) 





[Jones, 1987] C. JONES, Letter to the Editor, IEEE Com puter 20 (December 1987), p. 4. (Chapter 9) 





[Jones, 1994] C. JONES, “Software Metrics: Good, Bad, and Missing,” IEEE Computer 27 (September 1994) pp. 98–100. (Chapter 5) 





[Jones, 1996] C. JONES, Applied Software Measurement, McGraw-Hill, New York, 1996. (Chapter 3) 





[Jorgensen and Erickson, 1994] P. C. JORGENSEN AND C. ERICKSON, “Object-Oriented Integration Testing,” Communications of the ACM 37 (September 1994), pp. 30–38. (Chapter 15) 





[Jorgensen and Moløkken-Østvold, 2004] M. JORGENSEN AND K. MOLØKKEN-ØSTVOLD, “Reasons for Software Effort Estimation Error: Impact of Respondent Role, Information Collection Approach, and Data Analysis Method,” IEEE Transactions on Software Engineering 30 (December 2004), pp. 993–1007. (Chapter 9) 





[Jorgensen and Shepperd, 2007] M. JORGENSEN AND M. S , “A Systematic Review of Software Development Cost Estimation Studies,” IEEE Transactions on Software Engineering 32 (January 2007), pp. 33–53. (Chapter 9) 





[Josephson, 1992] M. JOSEPHSON, Edison, A Biography, John Wiley and Sons, New York, 1992. (Chapter 1) 





[Juran, 1988] J. M. JURAN, Juran on Planning for Quality, Macmillan, New York, 1988. (Chapter 3) 





[Juristo, Moreno, and López, 2000] N. JURISTO, A. M. MORENO, AND M. LÓPEZ, “How to Use Linguistic Instruments for Object-Oriented Analysis,” IEEE Software 17 (May–June 2000), pp. 80–89. (Chapter 13) 





[Juristo, Moreno, Vegas, and Solari, 2006] N. JURISTO, A. M. MORENO, S. VEGAS, AND M. SOLARI, “In Search of What We Experimentally Know about Unit Testing,” IEEE Software 23 (November–December 2006), pp. 72–80. (Chapter 15) 





[Kampen, 1987] G. R. KAMPEN, “An Eclectic Approach to Specifi cation,” Proceedings of the Fourth International Workshop on Software Specifi cation and Design , Monterey, CA, April 1987, pp. 178–82. (Chapter 12) 





[Kan et al., 1994] S. H. KAN, S. D. DULL, D. N. AMUND-SON, R. J. LINDNER, AND R. J. HEDGER, “AS/400 Software Quality Management,” IBM Systems Journal 33 (No. 1, 1994), pp. 62–88. (Chapter 1) 





[Karlsson and Ryan, 1997] J. KARLSSON AND K. RYAN, “A Cost-Value Approach for Prioritizing Requirements,” IEEE Software 14 (September–October 1997), pp. 67–74. (Chapter 11) 





[Karlström and Runeson, 2005] D. KARLSTRÖM AND P. RUNESON, “Combining Agile Methods with Stage-Gate Project Management,” IEEE Software 22 (May–June 2005), pp. 43–49. (Chapter 2) 





[Kazman, Bass, and Klein, 2006] R. KAZMAN, L. BASS, AND M. KLEIN, “The Essential Components of Software Architecture Design and Analysis,” Journal of Systems and Software 79 (August 2006), pp. 1207–16. (Chapter 8) 





[Keeni, 2000] G. KEENI, “The Evolution of Quality Pro cesses at Tata Consultancy Services,” IEEE Software 17 (July–August 2000), pp. 79–88. (Chapter 3) 





[Keil and Tiwana, 2005] M. KEIL AND A. TIWANA, “Beyond Cost: The Drivers of COTS Application Value,” IEEE Software 22 (May–June 2005), pp. 64–69. (Chapter 1) 





[Kelly and Sherif, 1992] J. C. KELLY AND J. S. SHERIF, “A Comparison of Four Design Methods for Real-Time Software Development,” Information and Software Technology 34 (February 1992), pp. 74–82. (Chapter 14) 





[Kelly, Sherif, and Hops, 1992] J. C. KELLY, J. S. SHERIF, AND J. HOPS, “An Analysis of Defect Densities Found 





during Software Inspections,” Journal of Systems and Software 17 (January 1992), pp. 111–17. (Chapters 1 and 6) 





[Kernighan and Plauger, 1974] B. W. KERNIGHAN AND P. J. PLAUGER, The Elements of Programming Style McGraw-Hill, New York, 1974. (Chapter 15) 





[Kernighan and Ritchie, 1978] B. W. KERNIGHAN AND D. M. RITCHIE, The C Programming Language , Prentice Hall, Englewood Cliffs, NJ, 1978. (Chapter 8) 





[Kiczales et al., 2001] G. KICZALES, E. HILSDALE, J. HU-GUNIN, M. KERSTEN, J. PALM, AND W. G. GRISWOLD, “An Overview of AspectJ,” in: J. L. Knudsen (Edition), European Conference on Object-oriented Program ming , Vol. 2072 of Lecture Notes in Computer Sci ence , Springer-Verlag, New York, 2001, pp. 327–53. (Chapter 18) 





[Kilpi, 2001] T. KILPI, “Implementing a Software Metrics Program at Nokia,” IEEE Software 18 (November– December 2001), pp. 72–76. (Chapter 5) 





[Kitchenham and Mendes, 2004] B. KITCHENHAM AND E. MENDES, “Software Productivity Measurement Using Multiple Size Measures,” IEEE Transactions on Software Engineering 30 (December 2004), pp. 1023–35. (Chapter 9) 





[Kitchenham, Pickard, and Linkman, 1990] B. A. KITCH-ENHAM, L. M. PICKARD, AND S. J. LINKMAN, “An Eval uation of Some Design Metrics,” Software Engineering Journal 5 (January 1990), pp. 50–58. (Chapter 14) 





[Kleinrock and Gail, 1996] L. KLEINROCK AND R. GAIL, Queuing Systems: Problems and Solutions , John Wiley and Sons, New York, 1996. (Chapter 12) 





[Klepper and Bock, 1995] R. KLEPPER AND D. BOCK, “Third and Fourth Generation Productivity Differ ences,” Communications of the ACM 38 (September, 1995), pp. 69–79. (Chapter 15) 





[Klunder, 1988] D. KLUNDER, “Hungarian Naming Con ventions,” Technical Report, Microsoft Corporation Redmond, WA, January 1988. (Chapter 15) 





[Knuth, 1968] D. E. KNUTH, The Art of Computer Programming, Vol. I , Fundamental Algorithms , Addison Wesley, Reading, MA, 1968. (Chapter 12) 





[Knuth, 1974] D. E. KNUTH, “Structured Programming with go to Statements,” ACM Computing Surveys 6 (December 1974), pp. 261–301. (Chapter 7) 





[Ko, Myers, Coblenz, and Aung, 2006] A. J. KO, B. A MYERS, M. J. COBLENZ, AND H. H. AUNG, “An Exploratory Study of How Developers Seek, Relate and Collect Relevant Information during Softwar 





Maintenance Tasks,” IEEE Transactions on Software Engineering 32 (December 2006), pp. 971–87. (Chapter 16) 





[Kobryn, 2000] C. KOBRYN, “Modeling Components and Frameworks with UML,” Communications of the ACM 43 (October 2000), pp. 31–38. (Chapter 8) 





[Kramer, 2007] J. KRAMER, “Is Abstraction the Key to Computing?” Communications of the ACM 50 (April 2007), pp. 36–42. (Chapter 7) 





[Krishnamurthy, Rolia, and Majumdar, 2006] D. KRISH-NAMURTHY, J. A. ROLIA, AND S. MAJUMDAR, “A Synthetic Workload Generation Technique for Stress Testing Session-Based Systems,” IEEE Transactions on Software Engineering 32 (November 2006), pp. 868–82. (Chapter 15) 





[Kruchten, Obbink, and Stafford, 2006] P. KRUCHTEN, H. OBBINK, AND J. STAFFORD, “The Past, Present, and Future for Software Architecture,” IEEE Software 23 (March–April 2006), pp. 22–30. (Chapter 8) 





[Kung, Hsia, and Gao, 1998] D. C. KUNG, P. HSIA, AND J. GAO, Testing Object-Oriented Software , IEEE Computer Society Press, Los Alamitos, CA, 1998. (Chapter 6) 





[Laddad, 2003] R. LADDAD, AspectJ in Action , Manning Publications, Greenwich, CT, 2003. (Chapter 18) 





[La Libre Online, 2007a] “Lalibre.be—Une erreur à 883 millions d’euros,” www.lalibre.be/index. php?view=article&art_id=305607. (Chapter 1) 





[La Libre Online, 2007b] “Lalibre.be—C’est la faute à l’informatique,” www.lalibre.be/index. php?view=article&art_id=307021. (Chapter 1) 





[Landwehr, 1983] C. E. LANDWEHR, “The Best Available Technologies for Computer Security,” IEEE Computer 16 (July 1983), pp. 86–100. (Chapter 6) 





[Lanergan and Grasso, 1984] R. G. LANERGAN AND C. A. GRASSO, “Software Engineering with Reusable Designs and Code,” IEEE Transactions on Software Engineering SE-10 (September 1984), pp. 498–501. (Chapter 8) 





[Lange, Chaudron, and Muskens, 2006] C. F. J. LANGE, M. R. V. CHAUDRON, AND J. MUSKENS, “In Practice: UML Software Architecture and Design Description,” IEEE Software 23 (March–April 2006), pp. 40–46. (Chapter 8) 





[LAPACK++, 2000] “LAPACK++: Linear Algebra Package in C++,” at math.nist.gov/lapack++, 2000. (Chapter 8) 





[Larman and Basili, 2003] C. LARMAN AND V. R. BASILI, “Iterative and Incremental Development: A Brief 





History,” IEEE Computer 36 (June 2003), pp. 47–56. (Chapter 2) 





[Lau and Wang, 2007] K.-K. LAU AND Z. WANG, “Soft ware Component Models,” IEEE Transactions on Software Engineering 33 (October 2007), pp. 709–24. (Chapter 8) 





[Leavenworth, 1970] B. LEAVENWORTH, Review #19420 Computing Reviews 11 (July 1970), pp. 396–97. (Chapters 6 and 12) 





[Leveson and Turner, 1993] N. G. LEVESON AND C. S. TURNER, “An Investigation of the Therac-25 Accidents,” IEEE Computer 26 (July 1993), pp. 18–41. (Chapter 1) 





[Li and Alshayeb, 2002] W. LI AND M. ALSHAYEB, “An Empirical Study of XP Effort,” Proceedings of the 17th International Forum on COCOMO and Software Cost Modeling , Los Angeles, IEEE, October 2002. (Chapter 2) 





[Li et al., 2008] J. LI, O. P. N. SLYNGSTAD, M. TORCHIANO, M. MORISIO, AND C. BUNSE, “A State-of-the-Practice Survey of Risk Management in Development with Off-the-Shelf Software Components,” IEEE Transactions on Software Engineering 34 (March–Apri 2008), pp. 271–86. (Chapters 1 and 2) 





[Li, Lu, Myagmar, and Zhou, 2006] Z. LI, S. LU, S. MYAGMAR, AND Y. ZHOU, “CP-Miner: Finding Copy Paste and Related Bugs in Large-Scale Software Code,” IEEE Transactions on Software Engineering 32 (March 2006), pp. 176–92. (Chapter 8) 





[Lieberman and Fry, 2001] H. LIEBERMAN AND C. FRY, “Will Software Ever Work?” Communications of the ACM 44 (March 2001), pp. 122–24. (Chapter 6) 





[Lientz, Swanson, and Tompkins, 1978] B. P. LIENTZ, E. B. SWANSON, AND G. E. TOMPKINS, “Characteristics of Application Software Maintenance,” Communications of the ACM 21 (June 1978), pp. 466–71. (Chapters 1 and 16) 





[Lim, 1994] W. C. LIM, “Effects of Reuse on Quality, Productivity, and Economics,” IEEE Software 11 (September 1994), pp. 23–30. (Chapters 8 and 9) 





[Lim, Jeong, and Schach, 2005] J. S. LIM, S. R. JEONG, AND S. R. SCHACH, “An Empirical Investigation of the Impact of the Object-Oriented Paradigm on the Maintainability of Real-World Mission-Critical Software,” Journal of Systems and Software 77 (August 2005), pp. 131–38. (Chapter 16) 





[Linger, 1994] R. C. LINGER, “Cleanroom Process Model,” IEEE Software 11 (March 1994), pp. 50–58. (Chapter 15) 





[Liskov and Zilles, 1974] B. LISKOV AND S. ZILLES, “Programming with Abstract Data Types,” ACM SIGPLAN Notices 9 (April 1974), pp. 50–59. (Chapter 7) 





[Liskov, Snyder, Atkinson, and Schaffert, 1977] B. LIS KOV, A. SNYDER, R. ATKINSON, AND C. SCHAFFERT, “Abstraction Mechanisms in CLU,” Communications of the ACM 20 (August 1977), pp. 564–76. (Chapter 8) 





[Little, 2006] T. LITTLE, “Schedule Estimation and Uncertainty Surrounding the Cone of Uncertainty,” IEEE Soft ware 23 (May–June 2006), pp. 48–54. (Chapter 9) 





[Liu, 2000] J. W. S. LIU, Real Time Systems , Prentice Hall, Upper Saddle River, NJ, 2000. (Chapter 14) 





[London, 1971] R. L. LONDON, “Software Reliability through Proving Programs Correct,” Proceedings of the IEEE International Symposium on Fault-Tolerant Computing, IEEE, March 1971. (Chapters 6 and 12) 





[Long and Morris, 1993] F. LONG AND E. MORRIS, “An Overview of PCTE: A Basis for a Portable Common Tool Environment,” Technical Report CMU/SEI–93– TR–1, Software Engineering Institute, Carnegie Mellon University, Pittsburgh, January 1993. (Chapter 15) 





[Longstaff, Chittister, Pethia, and Haimes, 2000] T. A. LONGSTAFF, C. CHITTISTER, R. PETHIA, AND Y. Y. HAIMES, “Are We Forgetting the Risks of Information Technology?” IEEE Computer 33 (December 2000), pp. 43–51. (Chapters 1 and 2) 





[Lotto, 1515] L. LOTTO, Giovanni Agostino della Torre and his Son, Niccolò , oil on canvas, 1515, www. nationalgallery.org.uk/cgi-bin/WebObjects.dll/ CollectionPublisher.woa/wa/largeImage?work Number=NG699. (Chapter 16) 





[Loukides and Oram, 1997] M. K. LOUKIDES AND A. ORAM, Programming with GNU Software , O’Reilly and Associates, Sebastopol, CA, 1997. (Chapters 5 and 16) 





[Louridas, 2006] P. LOURIDAS, “Version Control,” IEEE Software 23 (January–February 2006), pp. 104–107. (Chapter 5) 





[Luckham and von Henke, 1985] D. C. LUCKHAM AND F. W. VON HENKE, “An Overview of Anna, a Specifi cation Language for Ada,” IEEE Software 2 (March 1985), pp. 9–22. (Chapter 12) 





[Lui, Chan, and Nosek, 2008] K. M. LUI, K. C. C. CHAN, AND J. T. NOSEK, “The Effect of Pairs in Program Design Tasks,” IEEE Transactions on Software Engineering 34 (March–April 2008), pp. 197–211. (Chapters 4 and 14) 





[Luqi, Zhang, Berzins, and Qiao, 2004] LUQI, L. ZHANG, V. BERZINS, AND Y. QIAO, “Documentation Driven Development for Complex Real-Time Systems,” IEEE 





Transactions on Software Engineering 30 (December 2004), pp. 936–52. (Chapter 14) 





[Mackenzie, 1980] C. E. MACKENZIE, Coded Character Sets: History and Development , Addison-Wesley, Reading, MA, 1980. (Chapter 8) 





[Mackey, 1999] K. MACKEY, “Stages of Team Develop ment,” IEEE Software 16 (July–August 1999), pp. 90–91. (Chapter 4) 





[Madanmohan and De’, 2004] T. R. MADANMOHAN AND R. DE’, “Open Source Reuse in Commercial Firms,” IEEE Software 21 (November–December 2004), pp. 62–69. (Chapter 1) 





[Magee and Kramer, 1999] J. MAGEE AND J. KRAMER, Concurrency: State Models & Java Programs , John Wiley and Sons, New York, 1999. (Chapter 14) 





[Manna and Pnueli, 1992] Z. MANNA AND A. PNUELI, The Temporal Logic of Reactive and Concurrent Systems, Springer-Verlag, New York, 1992. (Chapter 6) 





[Manna and Waldinger, 1978] Z. MANNA AND R. WALDINGER, “The Logic of Computer Programming,” IEEE Transactions on Software Engineering SE-4 (1978), pp. 199–229. (Chapter 6) 





[Mantei, 1981] M. MANTEI, “The Effect of Programming Team Structures on Programming Tasks,” Communications of the ACM 24 (March 1981), pp. 106–13. (Chapter 4) 





[Manzoni and Price, 2003] L. V. MANZONI AND R. T. PRICE, “Identifying Extensions Required by RUP (Rational Unifi ed Process) to Comply with CMM (Capability Maturity Model) Levels 2 and 3,” IEEE Transactions on Software Engineering 29 (February 2003), pp. 181–92. (Chapter 3) 





[Maranzano et al., 2005] J. F. MARANZANO, S. A. ROZSYPAL, G. H. ZIMMERMAN, G. W. WARNKEN, P. E. WIRTH, AND D. M. WEISS, “Architecture Reviews: Practice and Experience,” IEEE Software 22 (March– April 2005), pp. 34–43. (Chapter 14) 





[Martin, 1985] J. MARTIN, Fourth-Generation Languages, Vols. 1, 2, and 3, Prentice Hall, Englewood Cliffs, NJ 1985. (Chapter 15) 





[Martin, 2007] R. C. MARTIN, “Professionalism and Test Driven Development,” IEEE Software 24 (May–June 2007), pp. 32–36. (Chapter 2) 





[Matsumoto, 1984] Y. MATSUMOTO, “Management of Industrial Software Production,” IEEE Computer 17 (February 1984), pp. 59–72. (Chapter 8) 





[Matsumoto, 1987] Y. MATSUMOTO, “A Software Factory: An Overall Approach to Software Production,” in: 





Tutorial: Software Reusability , P. Freeman (Editor), Computer Society Press, Washington, DC, 1987, pp. 155–78. (Chapter 8) 





[Maxwell and Forselius, 2000] K. D. MAXWELL AND P. FORSELIUS, “Benchmarking Software Development Productivity,” IEEE Software 17 (January–Februar 2000), pp. 80–88. (Chapter 9) 





[McBride, 2007] M. R. MCBRIDE, “The Software Architect,” Communications of the ACM 50 (May 2007), pp. 75–81. (Chapter 14) 





[McBride, 2008] T. MCBRIDE, “The Mechanisms of Project Management of Software Development,” Journal of Systems and Software 81 (December 2008), pp. 2386–95. (Chapter 9) 





[McCabe, 1976] T. J. MCCABE, “A Complexity Measure,” IEEE Transactions on Software Engineering SE-2 (December 1976), pp. 308–20. (Chapters 14 and 15) 





[McCabe and Butler, 1989] T. J. MCCABE AND C. W. BUT-LER, “Design Complexity Measurement and Testing,” Communications of the ACM 32 (December 1989), pp. 1415–25. (Chapter 15) 





[McConnell, 1993] S. MCCONNELL, Code Complete: A Practical Handbook of Software Construction, Micro soft Press, Redmond, WA, 1993. (Chapter 15) 





[McConnell, 2001] S. MCCONNELL, “The Nine Deadly Sins of Project Planning,” IEEE Software 18 (November–December 2001), pp. 5–7. (Chapter 9) 





[McGarry and Decker, 2002] F. MCGARRY AND B. DECKER, “Attaining Level 5 in CMM Process Maturity,” IEEE Software 19 (2002), pp. 87–96. (Chapter 3) 





[McGraw and Felten, 1999] G. MCGRAW AND E. FELTEN, Securing Java , John Wiley & Sons, New York, 1999. (Chapter 18) 





[MDA, 2008] “MDA,” www.omg.org/mda, 2008. (Chapter 18) 





[Mellor, 1994] P. MELLOR, “CAD: Computer-Aided Disaster,” Technical Report, Centre for Software Reliability, City University, London, July 1994. (Chapter 1) 





[Memon, Pollack, and Soffa, 2001] A. M. MEMON, M. E. POLLACK, AND M. L. SOFFA, “Hierarchical GUI Test Case Generation Using Automated Planning,” IEEE Transactions on Software Engineering 27 (February 2001), pp. 144–55. (Chapter 15) 





[Mens, 2002] T. MENS, “A State-of-the-Art Survey on Software Merging,” IEEE Transactions on Software Engineering 28 (May 2002), pp. 449–62. (Chapter 5) 





[Mens and Tourwe, 2004] T. MENS AND T. TOURWE, “A Survey of Software Refactoring,” IEEE Transactions 





on Software Engineering 30 (February 2004), pp. 126–39. (Chapter 2) 





[Menzies and Hihn, 2006] T. MENZIES AND J. HIHN, “Evidence-Based Cost Estimation for Better-Qualit Software,” IEEE Software 23 (July–August 2006), pp. 64–66. (Chapter 9) 





[Meyer, 1985] B. MEYER, “On Formalism in Specifi ca tions,” IEEE Software 2 (January 1985), pp. 6–26. (Chapter 12) 





[Meyer, 1986] B. MEYER, “Genericity versus Inheritance,” Proceedings of the Conference on Object-Oriented Programming Systems, Languages and Applications ACM SIGPLAN Notices 21 (November 1986), pp. 391–405. (Chapter 7) 





[Meyer, 1992] B. MEYER, “Applying ‘Design by Con tract’,” IEEE Computer 25 (October 1992), pp. 40–51. (Chapter 1) 





[Meyer, 2008] B. MEYER, “Design and Code Reviews in the Age of the Internet,” Communications of the ACM 51 (September 2008), pp. 66–71. (Chapters 6 and 15) 





[Miller, 1956] G. A. MILLER, “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,” The Psycholog ical Review 63 (March 1956), pp. 81–97; reprinted in www.well.com/user/smalin/miller.html. (Chapters 2, 3, and 5) 





[Miller and Yin, 2004] J. MILLER AND Z. YIN, “A Cognitive Based Mechanism for Constructing Software Inspection Teams,” IEEE Transactions on Software Engineering 30 (November 30), pp. 811–25. (Chapter 6) 





[Mills, Dyer, and Linger, 1987] H. D. MILLS, M. DYER, AND R. C. LINGER, “Cleanroom Software Engineer ing,” IEEE Software 4 (September 1987), pp. 19–25. (Chapter 15) 





[Modell, 1996] M. E. MODELL, A Professional’s Guide to Systems Analysis , 2nd ed., McGraw-Hill, New York, 1996. (Chapter 12) 





[Mohan, Xu, and Ramesh, 2008] K. MOHAN, P. XU, AND B. RAMESH, “Improving the Change-Management Process,” Communications of the ACM 51 (May 2008), pp. 59–64. (Chapter 5) 





[Moløkken-Østvold and Jorgensen, 2005] K. MOLØKKEN-ØSTVOLD AND M. JORGENSEN, “A Comparison of Software Project Overruns—Flexible versus Sequential Development Models,” IEEE Transactions on Software Engi neering 31 (September 2005), pp. 754–66. (Chapter 9) 





[Monarchi and Puhr, 1992] D. E. MONARCHI AND G. I. PUHR, “A Research Typology for Object-Oriented 





Analysis and Design,” Communications of the ACM 35 (September 1992), pp. 35–47. (Chapter 13) 





[Mooney, 1990] J. D. MOONEY, “Strategies for Supporting Application Portability,” IEEE Computer 23 (November 1990), pp. 59–70. (Chapter 8) 





[Morisio, Ezran, and Tully, 2002] M. MORISIO, M. EZRAN, AND C. TULLY, “Success and Failure Factors in Soft ware Reuse,” IEEE Transactions on Software Engineering 28 (April 2002), pp. 340–57. (Chapter 8) 





[Morisio, Tully, and Ezran, 2000] M. MORISIO, C. TULLY, AND M. EZRAN, “Diversity in Reuse Processes,” IEEE Software 17 (July–August 2000), pp. 56–63. (Chapter 8) 





[Murphy et al., 2001] G. C. MURPHY, R. J. WALKER, E. L. A. B , M. P. R , A. L , M. A. KERSTEN, “Does Aspect-Oriented Programming Work?” Communications of the ACM 44 (October 2001), pp. 75–78. (Chapters 7 and 18) 





[Murru, Deias, and Mugheddu, 2003] O. MURRU, R. DEIAS, AND G. MUGHEDDU, “Assessing XP at a European Internet Company,” IEEE Software 20 (May–June, 2003), pp. 37–43. (Chapters 2 and 4) 





[Murugappan and Keeni, 2003] M. MURUGAPPAN AND G. KEENI, “Blending CMM and Six Sigma to Meet Business Goals,” IEEE Software 20 (March–April 2003), pp. 42–48. (Chapter 3) 





[Musa and Everett, 1990] J. D. MUSA AND W. W. EVERETT, “Software-Reliability Engineering: Technology for the 1990s,” IEEE Software 7 (November 1990), pp. 36–43. (Chapter 15) 





[Musa, Iannino, and Okumoto, 1987] J. D. MUSA, A. IAN NINO, AND K. OKUMOTO, Software Reliability: Mea surement, Prediction, Application , McGraw-Hill, New York, 1987. (Chapter 15) 





[Musser and Saini, 1996] D. R. MUSSER AND A. SAINI, STL Tutorial and Reference Guide: C++ Programming with the Standard Template Library , Addison-Wesley, Reading, MA, 1996. (Chapter 8) 





[Myers, 1976] G. J. MYERS, Software Reliability: Principles and Practices, Wiley-Interscience, New York, 1976. (Chapter 15) 





[Myers, 1978a] G. J. MYERS, “A Controlled Experiment in Program Testing and Code Walkthroughs/Inspections,” Communications of the ACM 21 (September 1978), pp. 760–68. (Chapter 15) 





[Myers, 1978b] G. J. MYERS, Composite/Structured Design , Van Nostrand Reinhold, New York, 1978. (Chapter 7) 





[Myers, 1979] G. J. MYERS, The Art of Software Testing, John Wiley and Sons, New York, 1979. (Chapters 6 and 15) 





[Myers, 1992] W. MYERS, “Good Software Practices Pay Off—or Do They?” IEEE Software 9 (March 1992), pp. 96–97. (Chapter 5) 





[Myrtveit, Stensrud, and Shepperd, 2005] I. MYRTVEIT, E. STENSRUD, AND M. SHEPPERD, “Reliability and Validity in Comparative Studies of Software Prediction Mod els,” IEEE Transactions on Software Engineering 31 (May 2005), pp. 380–91. (Chapter 9) 





[NAG, 2003] “NAG The Numerical Algorithms Group Ltd,” at www.nag.co.uk, 2003. (Chapter 8) 





[Naur, 1964] P. NAUR, “The Design of the GIER ALGOL Compiler,” in: Annual Review in Automatic Program ming, Vol. 4, Pergamon Press, Oxford, UK, 1964, pp. 49–85. (Chapter 12) 





[Naur, 1969] P. NAUR, “Programming by Action Clusters,” BIT 9 (No. 3, 1969), pp. 250–58. (Chapters 6 and 12) 





[Naur, Randell, and Buxton, 1976] P. NAUR, B. RANDELL, AND J. N. BUXTON (Editors), Software Engineering: Concepts and Techniques: Proceedings of the NATO Conferences , Petrocelli-Charter, New York, 1976. (Chapter 1) 





[Nerur, Mahapatra, and Mangalaraj, 2005] S. NERUR, R. MAHAPATRA, AND G. MANGALARAJ, “Challenges of Migrating to Agile Methodologies,” Communications of the ACM 48 (May 2005), pp. 72–78. (Chapter 2) 





[Neumann, 1980] P. G. NEUMANN, Letter from the Editor, ACM SIGSOFT Software Engineering Notes 5 (Jul 1980), p. 2. (Chapter 1) 





[NIST 151, 1988] “POSIX: Portable Operating System Interface for Computer Environments,” Federal Infor mation Processing Standard 151, National Institute of Standards and Technology, Washington, DC, 1988. (Chapter 8) 





[Nix and Collins, 1988] C. J. NIX AND B. P. COLLINS “The Use of Software Engineering, Including the Z Notation, in the Development of CICS,” Quality Assurance 14 (September 1988), pp. 103–10 (Chapter 12) 





[Norden, 1958] P. V. NORDEN, “Curve Fitting for a Model of Applied Research and Development Scheduling,” IBM Journal of Research and Development 2 (July 1958), pp. 232–48. (Chapter 9) 





[Norušis, 2005] M. J. NORUŠIS, SPSS 13.0 Guide to Data Analysis, Prentice Hall, Upper Saddle River, NJ, 2005. (Chapter 8) 





[Norwig, 1996] P. NORWIG, “Design Patterns in Dynamic Programming,” norvig.com/design-patterns/ ppframe.htm/, 1996. (Chapter 8) 





[O’Keeffe and Ó Cinnéide, 2008] M. O’KEEFFE AND M. Ó CINNÉIDE, “Software Reliability Prediction by Soft Computing Techniques,” Journal of Systems and Soft ware 81 (April 2008), pp. 502–16. (Chapter 16) 





[Oest, 1986] O. N. OEST, “VDM from Research to Practice,” Proceedings of the IFIP Congress, Information Processing ’86, 1986, pp. 527–33. (Chapter 12) 





[Orr, 1981] K. ORR, Structured Requirements Defi nition , Ken Orr and Associates, Topeka, KS, 1981. (Chapter 14) 





[Ostrand, Weyuker, and Bell, 2005] T. J. OSTRAND, E. J. WEYUKER, AND R. M. BELL, “Predicting the Location and Number of Faults in Large Software Systems,” IEEE Transactions on Software Engineering 31 (April 2005), pp. 340–55. (Chapter 6) 





[Palshikar, 2001] G. K. PALSHIKAR, “Applying Formal Specifi cations to Real-World Software Development,” IEEE Software 18 (November–December 2001), pp. 89–97. (Chapter 12) 





[Parnas, 1971] D. L. PARNAS, “Information Distribution Aspects of Design Methodology,” Proceedings of the IFIP Congress , Ljubljana, Yugoslavia, 1971, IFIP, pp. 339–44. (Chapter 7) 





[Parnas, 1972a] D. L. PARNAS, “A Technique for Soft ware Module Specifi cation with Examples,” Com munications of the ACM 15 (May 1972), pp. 330–36. (Chapter 7) 





[Parnas, 1972b] D. L. PARNAS, “On the Criteria to Be Used in Decomposing Systems into Modules,” Communications of the ACM 15 (December 1972), pp. 1053–58. (Chapter 7) 





[Parnas, 1994] D. L. PARNAS, “Software Aging,” Proceedings of the 16th International Conference on Software Engineering , Sorrento, Italy, IEEE, May 1994, pp. 279–87. (Chapter 1) 





[Parnas, 1999] D. L. PARNAS, “Ten Myths about Y2K Inspections,” Communications of the ACM 42 (Ma 1999), p. 128. (Chapter 16) 





[Parnas and Lawford, 2003] D. L. PARNAS AND M. LAWFORD, “The Role of Inspection in Software Quality Assurance,” IEEE Transactions on Software Engineering 29 (August 2003), pp. 674–76. (Chapter 6) 





[Paulk, Weber, Curtis, and Chrissis, 1995] M. C. PAULK, C. V. WEBER, B. CURTIS, AND M. B. CHRISSIS, The Capability Maturity Model: Guidelines for Improving 





the Software Process , Addison-Wesley, Reading, MA 1995. (Chapter 3) 





[Paulson, Succi, and Eberlein, 2004] J. W. PAULSON, G. SUCCI, AND A. EBERLEIN, “An Empirical Study of Open-Source and Closed-Source Software Products,” IEEE Transactions on Software Engineering 30 (April 2004), pp. 246–56. (Chapter 1) 





[Payne and Landry, 2006] D. PAYNE AND B. J. L. LANDRY, “A Uniform Code of Ethics: Business and IT Profes sional Ethics,” Communications of the ACM 49 (November 2006), pp. 81–84. (Chapter 1) 





[Pendharkar, Subramanian, and Rodger, 2005] P. C. PEND-HARKAR, G. H. SUBRAMANIAN, AND J. A. RODGER, “A Probabilistic Model for Predicting Software Develop ment Effort,” IEEE Transactions on Software Engi neering 31 (July 2005), pp. 615–24. (Chapter 9) 





[Perry and Kaiser, 1990] D. E. PERRY AND G. E. KAISER, “Adequate Testing and Object-Oriented Programming,” Journal of Object-Oriented Programming 2 (January–February 1990), pp. 13–19. (Chapter 15) 





[Perry et al., 2002] D. E. PERRY, A. PORTER, M. W. WADE, L G. VOTTA, AND J. PERPICH, “Reducing Inspection Interval in Large-Scale Software Development,” IEEE Transactions on Software Engineering 28 (July 2002), pp. 695–705. (Chapter 6) 





[Peterson, 1981] J. L. PETERSON, Petri Net Theory and the Modeling of Systems , Prentice Hall, Englewood Cliffs, NJ, 1981. (Chapter 12) 





[Petri, 1962] C. A. PETRI, “Kommunikation mit Auto maten,” Ph.D. Dissertation, University of Bonn, Germany, 1962. [In German.] 





[Pigoski, 1996] T. M. PIGOSKI, Practical Software Maintenance: Best Practices for Managing Your Software Investment , John Wiley and Sons, New York, 1996. (Chapter 16) 





[Pitterman, 2000] B. PITTERMAN, “Telecordia Technologies: The Journey to High Maturity,” IEEE Software 17 (July–August 2000), pp. 89–96. (Chapter 3) 





[Pittman, 1993] M. PITTMAN, “Lessons Learned in Man aging Object-Oriented Development,” IEEE Software 10 (January 1993), pp. 43–53. (Chapter 9) 





[Pohl and Metzger, 2006] K. POHL AND A. METZGER, “Software Product Line Testing,” Communications of the ACM 49 (December 2006), pp. 78–81. (Chapter 8) 





[Pont and Banner, 2004] M. J. PONT AND M. P. BANNER, “Designing Embedded Systems Using Patterns: A Case Study,” Journal of Systems and Software 71 (May 2004), pp. 201–13. (Chapter 8) 





[Prechelt, Unger-Lamprecht, Philippsen, and Tichy, 2002] L. PRECHELT, B. UNGER-LAMPRECHT, M. PHILIPPSEN, AND W. F. TICHY, “Two Controlled Experiments in Assessing the Usefulness of Design Pattern Documen tation in Program Maintenance,” IEEE Transactions on Software Engineering 28 (June 2002), pp. 595–606. (Chapters 8 and 16) 





[Prechelt and Unger, 2000] L. PRECHELT AND B. UNGER, “An Experiment Measuring the Effects of Personal Software Process (PSP) Training,” IEEE Transactions on Software Engineering 27 (May 2000), pp. 465–72. (Chapter 3) 





[Procaccino and Verner, 2006] J. D. PROCACCINO AND J. M. VERNER, “How Agile Are Industrial Software Development Practices?” Journal of Systems and Software 79 (November 2006), pp. 1541–51. (Chapter 9) 





[Procaccino, Verner, and Lorenzet, 2006] J. D. PROCAC-CINO, J. M. VERNER, AND S. J. LORENZET, “Defi ning and Contributing to Software Development Success,” Communications of the ACM 49 (August 2006), pp. 79–83. (Chapter 1) 





[Putnam, 1978] L. H. PUTNAM, “A General Empirical Solution to the Macro Software Sizing and Estimating Problem,” IEEE Transactions on Software Engineering SE-4 (July 1978), pp. 345–61. (Chapter 9) 





[Qumer and Henderson-Sellers, 2008] A. QUMER AND B. HENDERSON-SELLERS, “A Framework to Support the Evaluation, Adoption and Improvement of Agile Methods in Practice,” Journal of Systems and Software 81 (November 2008), pp. 1899–1919. (Chapter 2) 





[Rajlich, 2006] V. RAJLICH, “Changing the Paradigm of Software Engineering,” Communications of the ACM 49 (August 2006) pp. 67–70. (Chapter 2) 





[Rajlich and Bennett, 2000] V. RAJLICH AND K. H. BENNETT, “A Staged Model for the Software Life Cycle,” IEEE Computer 33 (July 2000), pp. 66–71. (Chapter 2) 





[Rajlich, Wilde, Buckellew, and Page, 2001] V. RAJLICH, N. WILDE, M. BUCKELLEW, AND H. PAGE, “Software Cultures and Evolution,” IEEE Computer 34 (September 2001), pp. 24–28. (Chapter 16) 





[Rapps and Weyuker, 1985] S. RAPPS AND E. J. WEYUKER, “Selecting Software Test Data Using Data Flow Information,” IEEE Transactions on Software Engineering SE-11 (April 1985), pp. 367–75. (Chapter 15) 





[Rasmusson, 2003] J. RASMUSSON, “Introducing XP into Greenfi eld Projects: Lessons Learned,” IEEE Software 20 (May–June, 2003), pp. 21–29. (Chapter 2) 





[Ravichandran and Rothenberger, 2003] T. RAVICHAN DRAN AND M. A. ROTHENBERGER, “Software Reuse Strategies and Component Markets,” Communica tions of the ACM 46 (August 2003), pp. 109–14 (Chapter 8) 





[Raymond, 2000] E. S. RAYMOND, The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary , O’Reilly & Associates, Sebastopol, CA, 2000; also available at www.catb. org/~esr/writings/cathedral-bazaar/cathedral bazaar/. (Chapters 1 and 2) 





[Rech, Bogner, and Haas, 2007] J. RECH, C. BOGNER, AND V. HAAS, “Using Wikis to Tackle Reuse in Software Projects,” IEEE Software 24 (November–December 2007), pp. 99–104. (Chapter 8) 





[Reifer, 2000] D. J. REIFER, “Software Management: The Good, the Bad, and the Ugly,” IEEE Software 17 (March–April 2000), pp. 73–75. (Chapter 9) 





[Reifer, 2003] D. REIFER, “XP and the CMM,” IEEE Soft ware 20 (May–June 2003), pp. 14–15. (Chapter 4) 





[Reifer, Maurer, and Erdogmus, 2003] D. REIFER, F. MAU RER, AND H. ERDOGMUS, “Scaling Agile Methods,” IEEE Software 20 (July–August 2004), pp. 12–14. (Chapter 2) 





[Reiss, 2006] S. P. REISS, “Incremental Maintenance of Software Artifacts,” IEEE Transactions on Software Engineering 32 (September 2006), pp. 682–97. (Chapters 2, 5, and 16) 





[Rochkind, 1975] M. J. ROCHKIND, “The Source Code Control System,” IEEE Transactions on Software En gineering SE-1 (October 1975), pp. 255–65. (Chapters 5 and16) 





[Ropponen and Lyttinen, 2000] J. ROPPONEN AND K. LYTTINEN, “Components of Software Development Risk: How to Address Them? A Project Manager Sur vey,” IEEE Transactions on Software Engineering 26 (February 2000), pp. 96–111. (Chapter 2) 





[Ross, 1985] D. T. ROSS, “Applications and Extensions of SADT,” IEEE Computer 18 (April 1985), pp. 25–34. (Chapter 12) 





[Rothermel, Untch, Chu, and Harrold, 2001] G. ROTHER MEL, R. H. UNTCH, C. CHU, AND M. J. HARROLD, “Pri oritizing Test Cases for Regression Test Cases,” IEEE Transactions on Software Engineering 27 (October 2001), pp. 929–48. (Chapter 16) 





[Rout et al., 2007] T. P. ROUT, K. EL EMAM, M. FUSANI, D. GOLDENSON, AND H.-W. JUNG, “SPICE in Retrospect: Developing a Standard for Process Assessment,” 





Journal of Systems and Software 80 (September 2007), pp. 1483–93. (Chapter 3) 





[Royce, 1970] W. W. ROYCE, “Managing the Development of Large Software Systems: Concepts and Techniques,” 1970 WESCON Technical Papers, Western Electronic Show and Convention , Los Angeles, August 1970, pp. A/1-1–A/1-9; reprinted in: Proceedings of the 11th International Conference on Software Engineering , Pittsburgh, May 1989, IEEE, pp. 328–38. (Chapter 2) 





[Royce, 1998] W. ROYCE, Software Project Management: A Unifi ed Framework , Addison-Wesley, Reading, MA, 1998. (Chapters 2 and 4) 





[Royce, 2005] W. ROYCE, “Successful Software Management Style: Steering and Balance,” IEEE Software 22 (September–October 2005), pp. 40–47. (Chapter 9) 





[Rubenstein, 2007] D. RUBENSTEIN, “Standish Group Report: There’s Less Development Chaos Today,” www. sdtimes.com/content/article.aspx?ArticleID=30247, March 1, 2007. (Chapters 1 and 2) 





[Rumbaugh et al., 1991] J. RUMBAUGH, M. BLAHA, W. PREMERLANI, F. EDDY, AND W. LORENSEN, Object-Oriented Modeling and Design , Prentice Hall, Engle wood Cliffs, NJ, 1991. (Chapter 3) 





[Rumbaugh, Jacobson, and Booch, 1999] J. RUMBAUGH, I. JACOBSON, AND G. BOOCH, The Unifi ed Modeling Language Reference Manual , Addison-Wesley, Reading, MA, 1999. (Chapter 13) 





[Runeson et al., 2006] P. RUNESON, C. ANDERSSON, T. THELIN, A. ANDREWS, AND T. BERLING, “What Do We Know about Defect Detection Methods?” IEEE Software 23 (May–June 2006), pp. 82–90. (Chapter 15) 





[Ruthruff, Burnett, and Rothermel, 2006] J. R. RUTHRUFF, M. BURNETT, AND G. ROTHERMEL, “Interactive Fault Localization Techniques in a Spreadsheet Environment,” IEEE Transactions on Software Engineering 32 (April 2006), pp. 213–39. (Chapter 15) 





[Sackman, 1970] H. SACKMAN, Man–Computer Problem Solving: Experimental Evaluation of Time-Sharing and Batch Processing, Auerbach, Princeton, NJ, 1970. (Chapter 9) 





[Sackman, Erikson, and Grant, 1968] H. SACKMAN, W. J. ERIKSON, AND E. E. GRANT, “Exploratory Experimental Studies Comparing Online and Offl ine Program ming Performance,” Communications of the ACM 11 (January 1968), pp. 3–11. (Chapter 9) 





[Sakthivel, 2007] S. SAKTHIVEL, “Managing Risk in Off shore Systems Development,” Communications of the ACM 50 (April 2007), pp. 69–75. (Chapter 2) 





[Sammet, 1978] J. E. SAMMET, “The Early History of COBOL,” Proceedings of the History of Program ming Languages Conference , Los Angeles, ACM 1978, pp. 199–276. (Chapter 15) 





[Samoladas, Stamelos, Angelis, and Oikonomou, 2005] I. SAMOLADAS, I. STAMELOS, L. ANGELIS, AND A. OIKO-NOMOU, “Open Source Software Development Should Strive for Even Greater Code Maintainability,” Communications of the ACM 47 (October 2004), pp. 83–87. (Chapter 16) 





[Sarkar, Kak, and Rama, 2008] S. SARKAR, A. C. KAK, AND G. M. RAMA, “Metrics for Measuring the Qual ity of Modularization of Large-Scale Object-Oriented Software,” IEEE Transactions on Software Engineering 34 (September–October 2008), pp. 700–20. (Chapter 7) 





[Schach, 1992] S. R. SCHACH, Software Reuse: Past, Present, and Future , videotape, 150 min, US-VHS format, IEEE Computer Society Press, Los Alamitos, CA, November 1992. (Chapter 8) 





[Schach, 1994] S. R. SCHACH, “The Economic Impact of Software Reuse on Maintenance,” Journal of Software Maintenance—Research and Practice 6 (July–August 1994), pp. 185–96. (Chapters 8 and 9) 





[Schach, 1997] S. R. SCHACH, Software Engineering with Java , Richard D. Irwin, Chicago, 1997. (Chapter 8) 





[Schach and Stevens-Guille, 1979] S. R. SCHACH AND P. D. STEVENS-GUILLE, “Two Aspects of Computer-Aided Design,” Transactions of the Royal Society of South Africa 44 (Part 1, 1979), 123–26. (Chapter 7) 





[Schach and Wood, 1986] S. R. SCHACH AND P. T. WOOD, “An Almost Path-Free Very High-Level Interactive Data Manipulation Language for a Microcomputer Based Database System,” Software–Practice and Experience 16 (March 1986), pp. 243–68. (Chapter 11) 





[Schach et al., 2003a] S. R. SCHACH, B. JIN, DAVID R. WRIGHT, G. Z. HELLER, AND J. OFFUTT, “Quality Im pacts of Clandestine Common Coupling,” Software Quality Journal 11 (July 2003), pp. 211–18. (Chapter 7) 





[Schach et al., 2003b] S. R. SCHACH, B. JIN, G. Z. HELLER, L. YU, AND J. OFFUTT, “Determining the Distribution of Maintenance Categories: Survey versus Measurement,” Empirical Software Engineering 8 (December 2003), pp. 351–66. (Chapter 1) 





[Scheffer, Stone, and Rzepka, 1985] P. A. SCHEFFER, A H. STONE III, AND W. E. RZEPKA, “A Case Study of SREM,” IEEE Computer 18 (April 1985), pp. 47–54. (Chapter 12) 





[Schmerl et al., 2006] B. SCHMERL, J. ALDRICH, D. GAR-LAN, R. KAZMAN, AND H. YAN, “Discovering Architectures from Running Systems,” IEEE Transactions on Software Engineering 32 (July 2006), pp. 454–66. (Chapter 16) 





[Schrage, 2004] M. SCHRAGE, “Never Go to a Client Meeting without a Prototype,” IEEE Software 21 (2004), pp. 42–45. (Chapter 11) 





[Schricker, 2000] D. SCHRICKER, “Cobol for the Next Millennium,” IEEE Software 17 (March–April 2000), pp. 48–52. (Chapter 8) 





[Schwaber, 2001] K. SCHWABER, Agile Software Develop ment with Scrum , Prentice Hall, Upper Saddle River, NJ, 2001. (Chapter 2) 





[Schwartz and Delisle, 1987] M. D. SCHWARTZ AND N. M. DELISLE, “Specifying a Lift Control System with CSP,” Proceedings of the Fourth International Workshop on Software Specifi cation and Design , Monterey, CA, IEEE, April 1987, pp. 21–27. (Chapter 12) 





[Scott and Vessey, 2002] J. E. SCOTT AND I. VESSEY, “Managing Risks in Enterprise Systems Implementations,” Communications of the ACM 45 (April 2002), pp. 74–81. (Chapters 1 and 2) 





[Sedigh-Ali and Paul, 2001] S. SEDIGH-ALI AND R. A. PAUL, “Software Engineering Metrics for COTS-Based Systems,” IEEE Computer 34 (May 2001), pp. 44–50. (Chapter 5) 





[SEI, 2002] “CMMI Frequently Asked Questions (FAQ),” Software Engineering Institute, Carnegie Mellon University, Pittsburgh, June 2002. (Chapter 3) 





[Selby, 1989] R. W. SELBY, “Quantitative Studies of Software Reuse,” in: Software Reusability, Vol. 2, Applications and Experience , T. J. Biggerstaff and A. J. Perlis (Editors), ACM Press, New York, 1989, pp. 213–33. (Chapter 8) 





[Selby, 2005] R. W. SELBY, “Enabling Reuse-Based Software Development of Large-Scale Systems,” IEEE Transactions on Software Engineering 31 (June 2005), pp. 495–510. (Chapter 8) 





[Selic, Gullekson, and Ward, 1995] B. SELIC, G. GULLEK-SON, AND P. T. WARD, Real-Time Object-Oriented Modeling , John Wiley and Sons, New York, 1995. (Chapter 13) 





[Service, 2000] “Service. The American Heritage Dictionary of the English Language: Fourth Edition. 2000,” www.bartleby.com/61/68/S0286800.html, 2000. (Chapter 18) 





[Shapiro, 1994] F. R. SHAPIRO, “The First Bug,” Byte 19 (April 1994), p. 308. (Chapter 1) 





[Sharma and Rai, 2000] S. SHARMA AND A. RAI, “CASE Deployment in IS Organizations,” Communications of the ACM 43 (January 2000), pp. 80–88. (Chapter 5) 





[Shatnawi and Li, 2008] R. SHATNAWI AND W. LI, “The Effectiveness of Software Metrics in Identifying Error Prone Classes in Post-Release Software Evolution Pro cess,” Journal of Systems and Software 81 (November 2008), pp. 1868–82. (Chapter 16) 





[Shaw and Clements, 2006] M. SHAW AND P. CLEMENTS, “The Golden Age of Software Architecture,” IEEE Software 23 (March–April 2006), pp. 31–39. (Chapter 8) 





[Shaw and Garlan, 1996] M. SHAW AND D. GARLAN, Software Architecture: Perspectives on an Emerging Discipline , Prentice Hall, Upper Saddle River, NJ, 1996. (Chapter 8) 





[Shepperd and Ince, 1994] M. SHEPPERD AND D. C. INCE, “A Critique of Three Metrics,” Journal of Systems and Software 26 (September 1994), pp. 197–210. (Chapter 15) 





[Shepperd, 1990] M. SHEPPERD, “Design Metrics: An Empirical Analysis,” Software Engineering Journal 5 (January 1990), pp. 3–10. (Chapter 14) 





[Sherer, Kouchakdjian, and Arnold, 1996] S. W. SHERER A. KOUCHAKDJIAN, AND P. G. ARNOLD, “Experience Using Cleanroom Software Engineering,” IEEE Soft ware 13 (May 1996), pp. 69–76. (Chapter 15) 





[Shneiderman, 1980] B. SHNEIDERMAN, Software Psychol ogy: Human Factors in Computer and Information Systems , Winthrop Publishers, Cambridge, MA, 1980. (Chapter 1) 





[Shneiderman, 2003] B. SHNEIDERMAN, Designing the User Interface: Strategies for Effective Human-Computer Interaction, 4th ed., Addison-Wesley Longman, Reading, MA, 2003. (Chapter 11) 





[Shneiderman and Mayer, 1975] B. SHNEIDERMAN AND R. MAYER, “Towards a Cognitive Model of Programmer Behavior,” Technical Report TR-37, Indiana Univer sity, Bloomington, 1975. (Chapter 7) 





[Silberschatz, Galvin, and Gagne, 2002] A. SILBERSCHATZ, P. B. GALVIN, AND G. GAGNE, Operating System Con cepts, 6th ed., Addison-Wesley, Reading, MA, 2002. (Chapters 12 and 14) 





[Sillito, Murphy, and De Volder, 2008] J. SILLITO, G. C. MURPHY, AND K. DE VOLDER, “Asking and Answering Questions during a Programming Change Task,” IEEE Transactions on Software Engineering 34 (July– August 2008), pp. 434–51. (Chapter 16) 





[Smith, Hale, and Parrish, 2001] R. K. SMITH, J. E. HALE, AND A. S. PARRISH, “An Empirical Study Using Task Assignment Patterns to Improve the Accuracy of Software Effort Estimation,” IEEE Transactions on Software Engineering 27 (March 2001), pp. 264–71. (Chapter 9) 





[Sobel and Clarkson, 2002] A. E. K. SOBEL AND M. R. CLARKSON, “Formal Methods Application: An Empiri cal Tale of Software Development,” IEEE Transactions on Software Engineering 28 (March 2002), pp. 308–20. (Chapter 12) 





[Sobell, 1995] M. G. SOBELL, A Practical Guide to the UNIX System , 3rd ed., Benjamin/Cummings, Menlo Park, CA, 1995. (Chapter 5) 





[Softwaremag.com, 2004] “Standish: Project Success Rates Improved Over 10 Years,” www.softwaremag. com/L.cfm?Doc=newsletter/2004-01-15/ Standish, January 15, 2004. (Chapter 2) 





[Sparling, 2000] M. SPARLING, “Lessons Learned through Six Years of Component-Based Development,” Communications of the ACM 43 (October 2000), pp. 47–53. (Chapter 8) 





[Spiegel Online, 2004] “Rheinbrücke mit Treppe—54 Zentimeter Höhenunterschied,” www.spiegel.de/ panorama/0,1518,281837,00.html. (Chapter 1) 





[Spivey, 1990] J. M. SPIVEY, “Specifying a Real-Time Kernel,” IEEE Software 7 (September 1990), pp. 21–28. (Chapter 12) 





[Spivey, 1992] J. M. SPIVEY, The Z Notation: A Reference Manual , Prentice Hall, New York, 1992. (Chapter 2) 





[Spivey, 2001] J. M. SPIVEY, The Z Notation: A Reference Manual , 3rd ed., spivey.oriel.ox.ac.uk/~mike/zrm/, 2001. (Chapter 12) 





[St. Petersburg Times Online, 2003] “Thousands of Federal Checks Uncashable,” www.sptimes. com/2003/02/07/Worldandnation/Thousands_ of_federal_.shtml, February 07, 2003. (Chapter 1) 





[Standish, 2003] STANDISH GROUP INTERNATIONAL, “Introduction,” www.standishgroup.com/chaos introduction.pdf, 2003. (Chapter 2) 





[Stephens and Rosenberg, 2003] M. STEPHENS AND D. ROSENBERG, Extreme Programming Refactored: The Case against XP , Apress, Berkeley, CA, 2003. (Chapter 2) 





[Stephenson, 1976] W. E. STEPHENSON, “An Analysis of the Resources Used in Safeguard System Software Development,” Bell Laboratories, Draft Paper, August 1976. (Chapter 1) 





[Stevens and Pooley, 2000] P. STEVENS WITH R. POOLEY, Using UML: Software Engineering with Objects and Components , updated edition, Addison-Wesley, Upper Saddle River, NJ, 2000. (Chapter 17) 





[Stevens, Myers, and Constantine, 1974] W. P. STEVENS, G. J. MYERS, AND L. L. CONSTANTINE, “Structured Design,” IBM Systems Journal 13 (No. 2, 1974), pp. 115–39. (Chapters 5 and 7) 





[Stocks and Carrington, 1996] P. STOCKS AND D. CAR-RINGTON, “A Framework for Specifi cation-Based Test ing,” IEEE Transactions on Software Engineering 22 (November 1996), pp. 777–93. (Chapter 15) 





[Stolper, 1999] S. A. STOLPER, “Streamlined Design Approach Lands Mars Pathfi nder,” IEEE Software 16 (September–October 1999), pp. 52–62. (Chapter 14) 





[Stroustrup, 2003] B. STROUSTRUP, The C++ Standard: Incorporating Technical Corrigendum No. 1 , 2nd ed., John Wiley and Sons, New York, 2003. (Chapters 7 and 14) 





[Sykes and McGregor, 2000] D. A. SYKES AND J. D. MCGREGOR, Practical Guide to Testing Object-Oriented Software , Addison-Wesley, Reading, MA 2000. (Chapter 6) 





[Symons, 1991] C. R. SYMONS, Software Sizing and Estimating: Mk II FPA , John Wiley and Sons, Chichester UK, 1991. (Chapter 9) 





[Takahashi and Kamayachi, 1985] M. TAKAHASHI AND Y. KAMAYACHI, “An Empirical Study of a Model fo Program Error Prediction,” Proceedings of the Eighth International Conference on Software Engineering, London, IEEE, 1985, pp. 330–36. (Chapter 15) 





[Talby, Keren, Hazzan, and Dubinsky, 2006] D. TALBY, A KEREN, O. HAZZAN, AND Y. DUBINSKY, “Agile Software Testing in a Large-Scale Project,” IEEE Software 23 (July–August 2006), pp. 30–37. (Chapter 2) 





[Tanenbaum, 2002] A. S. TANENBAUM, Computer Net works, 4th ed., Prentice Hall, Upper Saddle River, NJ 2002. (Chapter 8) 





[Teichroew and Hershey, 1977] D. TEICHROEW AND E. A. HERSHEY III, “PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems,” IEEE Transaction on Software Engineering SE-3 (January 1977), pp. 41–48. (Chapter 12) 





[Thayer and Dorfman, 1999] R. H. THAYER AND M. DORF-MAN, Software Requirements Engineering , revised 2nd ed., IEEE Computer Society Press, Los Alamitos, CA, 1999. (Chapter 11) 





[Tichy, 1985] W. F. TICHY, “RCS—A System for Version Control,” Software—Practice and Experience 15 (July 1985), pp. 637–54. (Chapters 5 and 16) 





[Toft, Coleman, and Ohta, 2000] P. TOFT, D. COLEMAN, AND J. OHTA, “A Cooperative Model for Cross-Divisional Product Development for a Software Product Line,” in: Software Product Lines: Experience and Research Directions , P. Donohoe (Editor), Kluwer Academic Publishers, Boston, 2000, pp. 111–32. (Chapter 8) 





[Tomer and Schach, 2000] A. TOMER AND S. R. SCHACH, “The Evolution Tree: A Maintenance-Oriented Software Development Model,” in: Proceedings of the Fourth European Conference on Software Maintenance and Reengineering (CSMR 2000) , Zürich, Switzerland, February/March 2000, pp. 209–14. (Chapter 2) 





[Tomer and Schach, 2002] A. TOMER AND S. R. SCHACH, “A Three-Dimensional Model for System Design Evolution,” Systems Engineering 5 (No. 4, 2002), pp. 264–73. (Chapter 5) 





[Tomer et al., 2004] A. TOMER, L. GOLDIN, T. KUFLIK, E. KIMCHI, AND S. R. SCHACH, “Evaluating Software Reuse Alternatives: A Model and Its Application to an Industrial Case Study,” IEEE Transactions on Software Engineering 30 (September 2004), pp. 601–12. (Chapter 8) 





[Toth, 2006] K. TOTH, “Experiences with Open Source Software Engineering Tools,” IEEE Software 23 (November–December 2006), pp. 44–52. (Chapter 5) 





[Tracz, 1979] W. J. TRACZ, “Computer Programming and the Human Thought Process,” Software—Practice and Experience 9 (February 1979), pp. 127–37. (Chapter 5) 





[Tracz, 1994] W. TRACZ, “Software Reuse Myths Revisited,” Proceedings of the 16th International Conference on Software Engineering , Sorrento, Italy, IEEE, May 1994, pp. 271–72. (Chapter 8) 





[Trammel, Binder, and Snyder, 1992] C. J. TRAMMEL, L. H. BINDER, AND C. E. SNYDER, “The Automated Production Control Documentation System: A Case Study in Cleanroom Software Engineering,” ACM Transactions on Software Engineering and Methodology 1 (January 1992), pp. 81–94. (Chapter 15) 





[Tsantalis, Chatzigeorgiou, and Stephanides, 2005] N. TSANTALIS, A. CHATZIGEORGIOU, AND G. STEPHANIDES, “Predicting the Probability of Change in Object Oriented Systems,” IEEE Transactions on Software Engineering 31 (July 2005), pp. 601–14. (Chapter 14) 





[Tsantalis, Chatzigeorgiou, Stephanides, and Halkidis, 2006] N. TSANTALIS, A. CHATZIGEORGIOU, G. STEPHA-NIDES, AND S. T. HALKIDIS, “Design Pattern Detection Using Similarity Scoring,” IEEE Transactions on Soft ware Engineering 32 (November 2006), pp. 896–909. (Chapter 8) 





[Turner, 1994] C. D. TURNER, “State-Based Testing: A New Method for the Testing of Object-Oriented Programs,” Ph.D. thesis, Computer Science Division, University of Durham, Durham, UK, November 1994. (Chapter 15) 





[Tyran and George, 2002] C. K. TYRAN AND J. F. GEORGE, “Improving Software Inspections with Group Process Support,” Communications of the ACM 45 (September 2002), pp. 87–92. (Chapter 6) 





[Ulkuniemi and Seppanen, 2004] P. ULKUNIEMI AND V. SEPPANEN, “COTS Component Acquisition in an Emerging Market,” IEEE Software 21 (November– December 2004), pp. 76–82. (Chapter 1) 





[USNO, 2000] “The 21st Century and the Third Millennium—When Will They Begin?” U.S. Naval Obser vatory, Astronomical Applications Department, at aa.usno.navy.mil/AA/faq/docs/millennium.html, February 22, 2000. (Chapter 13) 





[van der Hoek, Carzaniga, Heimbigner, and Wolf, 2002] A. VAN DER HOEK, A. CARZANIGA, D. HEIMBIGNER, AND A. L. WOLF, “A Testbed for Confi guration Management Policy Programming,” IEEE Transactions on Software Engineering 28 (January 2002), pp. 79–99. (Chapter 5) 





[van der Poel and Schach, 1983] K. G. VAN DER POEL AND S. R. SCHACH, “A Software Metric for Cost Estimation and Effi ciency Measurement in Data Processing System Development,” Journal of Systems and Software 3 (September 1983), pp. 187–91. (Chapter 9) 





[van Solingen, 2004] R. VAN SOLINGEN, “Measuring the ROI of Software Process Improvement,” IEEE Software 21 (May–June 2004), pp. 32–38. (Chapters 3 and 5) 





[van Wijngaarden et al., 1975] A. VAN WIJNGAARDEN, B. J. MAILLOUX, J. E. L. PECK, C. H. A. KOSTER, M SINTZOFF, C. H. LINDSEY, L. G. L. T. MEERTENS, AND R. G. FISKER, “Revised Report on the Algorithmic Language ALGOL 68,” Acta Informatica 5 (1975), pp. 1–236. (Chapter 3) 





[Vander Wal, 2004] T. VANDER WAL, “Understanding the Personal Info Cloud: Using the Model of Attraction,” Presentation, University of Maryland, Baltimore, MD, June 2004. (Chapter 18) 





[Ven, Verelst, and Mannaert, 2008] K. VEN, I. VERELST, AND H. MANNAERT, “Should You Adopt Open Source Software?” IEEE Software 25 (May–June 2008), pp. 54–59. (Chapter 1) 





[Venugopal, 2005] C. VENUGOPAL, “Single Goal Set: A New Paradigm for IT Megaproject Success,” IEEE Software 22 (September–October 2005), pp. 48–53. (Chapter 9) 





[Vitharana, 2003] P. VITHARANA, “Risks and Challenges of Component-Based Software Development,” Com munications of the ACM 46 (August 2003), pp. 67–72. (Chapter 8) 





[Vitharana and Ramamurthy, 2003] P. VITHARANA AND K. RAMAMURTHY, “Computer-Mediated Group Support, Anonymity and the Software Inspection Process: An Empirical Investigation,” IEEE Transactions on Software Engineering 29 (March 2003), pp. 167–80. (Chapter 6) 





[Vokac, 2004] M. VOKAC, “Defect Frequency and Design Patterns: An Empirical Study of Industrial Code,” IEEE Transactions on Software Engineering 30 (December 2004), pp. 904–17. (Chapter 9) 





[Walrad and Strom, 2002] C. WALRAD AND D. STROM, “The Importance of Branching Models in SCM,” IEEE Computer 35 (September 2002), pp. 31–38. (Chapter 5) 





[Walsh, 1979] T. J. WALSH, “A Software Reliability Stud Using a Complexity Measure,” Proceedings of the AFIPS National Computer Conference , New York AFIPS, 1979, pp. 761–68. (Chapter 15) 





[Ward and Mellor, 1985] P. T. WARD AND S. MELLOR, Structured Development for Real-Time Systems, Vols. 1, 2 and 3, Yourdon Press, New York, 1985. (Chapter 14) 





[Warnier, 1976] J. D. WARNIER, Logical Construction of Programs , Van Nostrand Reinhold, New York, 1976. (Chapter 14) 





[Watson and McCabe, 1996] A. H. WATSON AND T. J. MCCABE, “Structured Testing: A Testing Methodology Using the Cyclomatic Complexity Metric,” NIST Special Publication 500–235, Computer Systems Laboratory, National Institute of Standards and Technology, Gaithersburg, MD, 1996. (Chapter 15) 





[Watson et al., 2008] R. T. WATSON, M.-C. BOUDREAU, P. T. YORK, M. E. GREINER. AND D. WYNN, “The Business of Open Source,” Communications of the ACM 51 (April 2008), pp. 41–46. (Chapter 1) 





[Weinberg, 1971] G. M. WEINBERG, The Psychology of Computer Programming , Van Nostrand Reinhold, New York, 1971. (Chapters 1 and 4) 





[Weinberg, 1992] G. M. WEINBERG, Quality Software Management: Systems Thinking , Vol. 1, Dorset House, New York, 1992. (Chapter 9) 





[Weinberg, 1993] G. M. WEINBERG, Quality Software Management: First-Order Measurement , Vol. 2, Dorset House, New York, 1993. (Chapter 9) 





[Weinberg, 1994] G. M. WEINBERG, Quality Software Management: Congruent Action , Vol. 3, Dorset House, New York, 1994. (Chapter 9) 





[Weinberg, 1997] G. M. WEINBERG, Quality Software Management: Anticipating Change , Vol. 4, Dorset House, New York, 1997. (Chapter 9) 





[Weller, 2000] E. F. WELLER, “Practical Applications of Statistical Process Control,” IEEE Software 18 (May– June 2000), pp. 48–55. (Chapter 3) 





[Wesselius, 2008] J. WESSELIUS, “The Bazaar inside the Cathedral: Business Models for Internal Markets,” IEEE Software 25 (May–June 2008), pp. 60–66. (Chapter 1) 





[Weyuker, 1988] E. J. WEYUKER, “An Empirical Study of the Complexity of Data Flow Testing,” Proceedings of the Second Workshop on Software Testing, Verifi cation, and Analysis , Banff, Canada, IEEE, July 1988, pp. 188–95. (Chapter 15) 





[Whittaker, 2000] J. A. WHITTAKER, “What Is Software Testing? And Why Is It So Hard?” IEEE Software 17 (January–February 2000), pp. 70–79. (Chapter 6) 





[Whittaker and Voas, 2000] J. A. WHITTAKER AND J. VOAS, “Toward a More Reliable Theory of Software Reliability,” IEEE Computer 33 (December 2000), pp. 36–42. (Chapter 6) 





[Wilde, Matthews, and Huitt, 1993] N. WILDE, P. MAT THEWS, AND R. HUITT, “Maintaining Object-Oriented Software,” IEEE Software 10 (January 1993), pp. 75–80. (Chapter 15) 





[Williams, 1996] J. D. WILLIAMS, “Managing Iteration in OO Projects,” IEEE Computer 29 (September 1996), pp. 39–43. (Chapter 13) 





[Williams, Kessler, Cunningham, and Jeffries, 2000] L. WILLIAMS, R. R. KESSLER, W. CUNNINGHAM, AND R. JEFFRIES, “Strengthening the Case for Pair Programming,” IEEE Software 17 (July–August 2000), pp. 19–25. (Chapters 2 and 4) 





[Wing, 1990] J. WING, “A Specifi er’s Introduction to For mal Methods,” IEEE Computer 23 (September 1990) pp. 8–24. (Chapter 12) 





[Wirfs-Brock, 2006] R. WIRFS-BROCK, “Designing fo Recovery,” IEEE Software 23 (July–August 2006), pp. 11–13. (Chapter 14) 





[Wirfs-Brock, Wilkerson, and Wiener, 1990] R. WIRFS-BROCK, B. WILKERSON, AND L. WIENER, Designing Object-Oriented Software , Prentice Hall, Englewood Cliffs, NJ, 1990. (Chapters 1 and 13) 





[Wirth, 1971] N. WIRTH, “Program Development by Stepwise Refi nement,” Communications of the ACM 14 (April 1971), pp. 221–27. (Chapters 5 and 6) 





[Wirth, 1975] N. WIRTH, Algorithms + Data Structures = Programs, Prentice Hall, Englewood Cliffs, NJ, 1975. (Chapter 5) 





[Woodcock, 1989] J. WOODCOCK, “Calculating Properties of Z Specifi cations,” ACM SIGSOFT Software Engineering Notes 14 (July 1989), pp. 43–54. (Chapter 12) 





[Woodward, Hedley, and Hennell, 1980] M. R. WOOD-WARD, D. HEDLEY, AND M. A. HENNELL, “Experience with Path Analysis and Testing of Programs,” IEEE Transactions on Software Engineering SE-6 (May 1980), pp. 278–86. (Chapter 15) 





[Yamaura, 1998] T. YAMAURA, “How to Design Practical Test Cases,” IEEE Software 15 (November–December 1998), pp. 30–36. (Chapter 15) 





[Yang, Bhuta, Boehm, and Port, 2005] Y. YANG, J. BHUTA, B. BOEHM, AND D. N. PORT, “Value-Based Processes for COTS-Based Applications,” IEEE Software 22 (July–August 2005), pp. 54–62. (Chapter 1) 





[Yoo et al., 2006] C. YOO, J. YOON, B. LEE, C. LEE, J. LEE, S. HYUN, AND C.WU, “A Unifi ed Model for the Implementation of Both ISO 9001:2000 and CMMI by ISO-Certifi ed Organizations,” Journal of Systems and Software 79 (July 2006), pp. 954–61. (Chapter 3) 





[Yourdon, 1989] E. YOURDON, Modern Structured Analysis, Yourdon Press, Englewood Cliffs, NJ, 1989. (Chapter 15) 





[Yourdon, 1992] E. YOURDON, The Decline and Fall of the American Programmer , Yourdon Press, Upper Saddle River, NJ, 1992. (Chapter 1) 





[Yourdon and Constantine, 1979] E. YOURDON AND L. L CONSTANTINE, Structured Design: Fundamentals of a Discipline of Computer Program and Systems Design, Prentice Hall, Englewood Cliffs, NJ, 1979. (Chapters 7, 12, and 14) 





[Yu, Schach, Chen, and Offutt, 2004] L. YU, S. R. SCHACH, K. CHEN, AND J. OFFUTT, “Categorization of Common Coupling and Its Application to the Main tainability of the Linux Kernel,” IEEE Transactions on Software Engineering 30 (October 2004), pp. 694–706. (Chapter 7) 





[Zage and Zage, 1993] W. M. ZAGE AND D. M. ZAGE, “Evaluating Design Metrics on Large-Scale Soft ware,” IEEE Software 10 (July 1993), pp. 75–81. (Chapter 14) 





[Zelkowitz, Shaw, and Gannon, 1979] M. V. ZELKOWITZ, A. C. SHAW, AND J. D. GANNON, Principles of Software Engineering and Design, Prentice Hall, Englewood Cliffs, NJ, 1979. (Chapter 1) 





[Zhou and Leung, 2006] Y. ZHOU AND H. LEUNG, “Empirical Analysis of Object-Oriented Design Metrics for Predicting High and Low Severity Faults,” IEEE Transactions on Software Engineering 32 (October 2006), pp. 771–89. (Chapter 15) 





[Zvegintzov, 1998] N. ZVEGINTZOV, “Frequently Begged Questions and How to Answer Them,” IEEE Software 15 (January/February 1998), pp. 93–96. (Chapter 1) 



# Term Project: Chocoholics Anonymous

Chocoholics Anonymous (ChocAn) is an organization dedicated to helping people addicted to chocolate in all its glorious forms. Members pay a monthly fee to ChocAn. For this fee they are entitled to unlimited consultations and treatments with health care professionals, namely, dietitians, internists, and exercise experts. Every member is given a plastic card embossed with the member’s name and a nine-digit member number and incorporating a magnetic strip on which that information is encoded. Each health care professional ( provider ) who provides services to ChocAn members has a specially designed ChocAn computer terminal, similar to a credit card device in a shop. When a provider’s terminal is switched on, the provider is asked to enter his or her provider number. 

To receive health care services from ChocAn, the member hands his or her card to the provider, who slides the card through the card reader on the terminal. The terminal then dials the ChocAn Data Center, and the ChocAn Data Center computer verifi es the member number. If the number is valid, the word Validated appears on the one-line display. If the number is not valid, the reason is displayed, such as Invalid number or Member suspended; the latter message indicates that fees are owed (that is, the member has not paid membership fees for at least a month) and member status has been set to suspended. 

To bill ChocAn after a health care service has been provided to the member, the provider again passes the card through the card reader or keys in the member number. When the word Validated appears, the provider keys in the date the service was provided in the format MM–DD–YYYY. The date of service is needed because hardware or other diffi culties may have prevented the provider from billing ChocAn immediately after providing the service. Next, the provider uses the Provider Directory to look up the appropriate six-digit service code corresponding to the service provided. For example, 598470 is the code for a session with a dietitian, whereas 883948 is the code for an aerobics exercise session. The provider then keys in the service code. To check that the service code has been correctly looked up and keyed in, the software product then displays the name of the service corresponding to the code (up to 20 characters) and asks the provider to verify that this is indeed the service that was provided. If the provider has entered a nonexistent code, an error message is printed. The provider also can enter comments about the service provided. 

The software product now writes a record to disk that includes the following fi elds: 

Current date and time (MM–DD–YYYY HH:MM:SS). 

Date service was provided (MM–DD–YYYY). 

Provider number (9 digits). 

Member number (9 digits). 

Service code (6 digits). 

Comments (100 characters) (optional). 

The software product next looks up the fee to be paid for that service and displays it on the provider’s terminal. For verifi cation purposes, the provider has a form on which to enter the current date and time, the date the service was provided, member name and number, service code, and fee to be paid. At the end of the week, the provider totals the fees to verify the amount to be paid to that provider by ChocAn for that week. 

At any time, a provider can request the software product for a Provider Directory, an alphabetically ordered list of service names and corresponding service codes and fees. The Provider Directory is sent to the provider as an e-mail attachment. 

At midnight on Friday, the main accounting procedure is run at the ChocAn Data Center. It reads the week’s fi le of services provided and prints a number of reports. Each report also can be run individually at the request of a ChocAn manager at any time during the week. 

Each member who has consulted a ChocAn provider during that week receives a list of services provided to that member, sorted in order of service date. The report, which is also sent as an e-mail attachment, includes: 

Member name (25 characters). 

Member number (9 digits). 

Member street address (25 characters). 

Member city (14 characters). 

Member state (2 letters). 

Member ZIP code (5 digits). 

For each service provided, the following details are required: 

Date of service (MM–DD–YYYY). 

Provider name (25 characters). 

Service name (20 characters). 

Each provider who has billed ChocAn during that week receives a report, sent as an e-mail attachment, containing the list of services he or she provided to ChocAn members. To simplify the task of verifi cation, the report contains the same information as that entered on the provider’s form, in the order that the data were received by the computer. At the end of the report is a summary including the number of consultations with members and the total fee for that week. That is, the fi elds of the report include: 

Provider name (25 characters). 

Provider number (9 digits). 

Provider street address (25 characters). 

Provider city (14 characters). 

Provider state (2 letters). 

Provider ZIP code (5 digits). 

For each service provided, the following details are required: 

Date of service (MM–DD–YYYY). 

Date and time data were received by the computer (MM–DD–YYYY HH:MM:SS). 

Member name (25 characters). 

Member number (9 digits). 

Service code (6 digits). 

Fee to be paid (up to $999.99). 

Total number of consultations with members (3 digits). 

Total fee for week (up to $99,999.99). 

A record consisting of electronic funds transfer (EFT) data is then written to a disk; banking computers will later ensure that each provider’s bank account is credited with the appropriate amount. 

A summary report is given to the manager for accounts payable. The report lists every provider to be paid that week, the number of consultations each had, and his or her total fee for that week. Finally, the total number of providers who provided services, the total number of consultations, and the overall fee total are printed. 

During the day, the software at the ChocAn Data Center is run in interactive mode to allow operators to add new members to ChocAn, to delete members who have resigned, and to update member records. Similarly, provider records are added, deleted, and updated. 

The processing of payments of ChocAn membership fees has been contracted out to Acme Accounting Services, a third-party organization. Acme is responsible for fi nancial procedures such as recording payments of membership fees, suspending members whose fees are overdue, and reinstating suspended members who have now paid what is owing. The Acme computer updates the relevant ChocAn Data Center computer membership records each evening at 9 P.M. 

Your organization has been awarded the contract to write only the ChocAn data processing software; another organization will be responsible for the communications software, for designing the ChocAn provider’s terminal, for the software needed by Acme Accounting Services, and for implementing the EFT component. The contract states that, at the acceptance test, the data from a provider’s terminal must be simulated by keyboard input and data to be transmitted to a provider’s terminal display must appear on the screen. A manager’s terminal must be simulated by the same keyboard and screen. Each member report must be written to its own fi le; the name of the fi le should begin with the member name, followed by the date of the report. The provider reports should be handled the same way. The Provider Directory must also be created as a fi le. None of the fi les should actually be sent as e-mail attachments. As for the EFT data, all that is required is that a fi le be set up containing the provider name, provider number, and the amount to be transferred. 

# Software Engineering Resources

There are two good ways to get more information on software engineering topics: by reading journals and conference proceedings, and via the Internet and World Wide Web. 

Journals dedicated exclusively to software engineering are available, such as IEEE Transactions on Software Engineering , as well as journals of a more general nature, such as Communications of the ACM , in which signifi cant articles on software engineering are published. For reasons of space, only a selection of journals of both classes follows. The journals have been chosen on a subjective basis, those I currently fi nd to be the most useful. 

ACM Computing Reviews 

ACM Computing Surveys 

ACM SIGSOFT Software Engineering Notes 

ACM Transactions on Computer Systems 

ACM Transactions on Programming Languages and Systems 

ACM Transactions on Software Engineering and Methodology 

Communications of the ACM 

Computer Journal 

Empirical Software Engineering 

IBM Systems Journal 

IEEE Computer 

IEEE Software 

IEEE Transactions on Software Engineering 

Journal of Systems and Software 

Software Engineering Journa 

Software—Practice and Experience 

Software Quality Journal 

In addition, proceedings of many conferences contain important articles on software engineering topics. Again, a subjective selection follows. Most of the conferences are referred to by their acronym or name of sponsoring organization; these appear in parentheses. 

ACM SIGPLAN Annual Conference (SIGPLAN) 

ACM SIGSOFT Symposium on the Foundations of Software Engineering (FSE) 

Conference on Human Factors in Computing Systems (CHI) 

Conference on Object-Oriented Programming Systems, Languages, and Applications (OOPSLA) 

International Computer Software and Applications Conference (COMPSAC) 

International Conference on Software Engineering (ICSE) 

International Conference on Software Maintenance (ICSM) 

International Conference on Software Reuse (ICSR) 

International Conference on the Software Process (ICSP) 

International Software Architecture Workshop (ISAW) 

International Symposium on Software Testing and Analysis (ISSTA) 

International Workshop on Software Confi guration Management (SCM) 

International Workshop on Software Specifi cation and Design (IWSSD) 

The Internet is another valuable source of information on software engineering. With regard to Usenet news groups, the following two have been consistently useful to me: 

comp.object 

comp.software-eng 

Other newsgroups that sometimes have items that I fi nd relevant include the following: 

comp.lang.c++.moderated 

comp.lang.java.programmer 

comp.risks 

comp.software.confi g-mgmt 

# Requirements Workfl ow: The MSG Foundation Case Study

The requirements workfl ow for the MSG Foundation case study appears in Chapter 10. 

# Structured Systems Analysis: The MSG Foundation Case Study

## Step 1. Draw the Data Flow Diagram See Figure 12.9.

Step 2. Decide What Sections to Computerize and How Computerize the complete pilot project online. However, if the weekly computation regarding availability of funds to purchase homes turns out to be time consuming, it may be better to perform it the night before it is required. 

## Step 3. Put in the Details of the Data Flows

investment_details investment_number (12 characters) investment_name (25 characters) expected_return (9 + 2 digits) date_expected_return_updated (8 characters) 

mortgage_details mortgage_number (12 characters) mortgage_name (21 characters) price (6 + 2 digits) date_mortgage_issued (8 characters) weekly_income (6 + 2 digits) date_weekly_income_was_updated (8 characters) annual_property_tax (5 + 2 digits) 

<table><tr><td>annual_insurance_premium</td><td>(5 + 2 digits)</td></tr><tr><td>mortgage_balance</td><td>(6 + 2 digits)</td></tr><tr><td>available_funds_for_week</td><td>(9 + 2 digits)</td></tr><tr><td>annual_operating_expenses</td><td>(9 + 2 digits)</td></tr><tr><td>update_request</td><td>(1 character)</td></tr></table>

## Step 4. Defi ne the Logic of the Processes

compute_availability_of_funds_and_generate_funds_report Determine the expected income for the week by adding the expected_return of each investment in INVESTMENT_DATA. Determine the expected mortgage payments for the week by adding the expected mortgage payment of each mortgage in MORTGAGE_DATA. Determine the expected grants for the week by adding the expected grant for each mortgage in MORTGAGE_DATA. Compute available_funds_for_week - expected income for the week  annual_operating_expenses / 52  expected mortgage payments for the week  expected grants for the week Display/print available_funds_for_week generate_listing_of_investments For each investment in INVESTMENT_DATA Print investment_details generate_listing_of_mortgages For each mortgage in MORTGAGE_DATA Print mortgage_details perform_selected_update Use the value of update_request to determine whether MORTGAGE_DATA, INVESTMENT_DATA, or EXPENSES_DATA are to be updated. Perform the update. 

## Step 5. Defi ne the Data Stores

EXPENSES_DATA annual_operating_expenses [defi ned in Step 3] INVESTMENT_DATA investment_details [defi ned in Step 3] MORTGAGE_DATA mortgage_details [defi ned in Step 3] ll fi les are sequential, and hence there is no DIAD. 

## Step 6. Defi ne the Physical Resources

EXPENSES DATA Sequential fi le Stored on disk INVESTMENT DATA Sequential fi le Stored on disk MORTGAGE DATA Sequential fi le Stored on disk 

Step 7. Determine the Input/Output Specifi cations Input screens are designed for the following processes: 

update_investment, update_mortgage, update_annual_operating_expenses, compute_availability_of_funds_and_generate_funds_report 

The following reports are displayed: 

list_of_investments, list_of_mortgages, available_funds_for_week 

The screens and reports of the rapid prototype will be used as a basis for the preceding. The exact format of all screens and reports is subject to approval by the MSG Foundation. 

Step 8. Perform Sizing Approximately 4 megabytes of storage are needed for the software. Each investment object requires approximately 50 bytes of storage. Each mortgage object requires approximately 90 bytes of storage. The storage requirements can be computed on the basis of the number of investments and mortgages owned by the MSG Foundation. 

## Step 9. Determine the Hardware Requirements

Desktop computer with hard disk, running Linux. 

Zip drive for backups. 

Laser printer for printing reports. 

# Analysis Workfl ow: The MSG Foundation Case Study

The analysis workfl ow is presented in Chapter 12. 

# Software Project Management Plan: The MSG Foundation Case Study

The plan presented here is for development of the MSG product by a small software organization consisting of three individuals: Almaviva, the owner of the company, and two software engineers, Bartolo and Cherubini. 

## 1 Overview.

## 1.1 Project Summary.

1.1.1 Purpose, Scope, and Objectives. The objective of this project is to develop a software product that will assist the Martha Stockton Greengage (MSG) Foundation in making decisions regarding home mortgages for married couples. The product will allow the client to add, modify, and delete information regarding the Foundation’s investments, operating expenses, and individual mortgage information. The product will perform the required calculations in these areas and produce reports listing investments, mortgages, and weekly operating expenses. 

## 1.1.2 Assumptions and Constraints. Constraints include the following:

The deadline must be met. 

The budget constraint must be met. 

The product must be reliable. 

The architecture must be open so that additional functionality may be added later. 

The product must be user-friendly. 

1.1.3 Project Deliverables. The complete product, including user manual, will be delivered 10 weeks after the project commences. 

1.1.4 Schedule and Budget Summary. The duration, personnel requirements, and bud get of each workfl ow are as follows: 

Requirements workfl ow (1 week, two team members, $3740) 

Analysis workfl ow (2 weeks, two team members, $7480) 

Design workfl ow (2 weeks, two team members, $7480) 

Implementation workfl ow (3 weeks, three team members, $16,830) 

Testing workfl ow (2 weeks, three team members, $11,220) 

The total development time is 10 weeks, and the total internal cost is $46,750. 

1.2 Evolution of the Project Management Plan. All changes in the project management plan must be agreed to by Almaviva before they are implemented. All changes should be documented to keep the project management plan correct and up to date. 

2 Reference Materials. All artifacts will conform to the company’s programming, documentation, and testing standards. 

3 Defi nitions and Acronyms. MSG—Martha Stockton Greengage; the MSG Foundation is our client. 

## 4 Project Organization.

4.1 External Interfaces. All the work on this project will be performed by Almaviva, Bartolo, and Cherubini. Almaviva will meet weekly with the client to report progress and discuss possible changes and modifi cations. 

4.2 Internal Structure. The development team consists of Almaviva (owner), Bartolo, and Cherubini. 

4.3 Roles and Responsibilities . Bartolo and Cherubini will perform the design workfl ow. Almaviva will implement the class defi nitions and report artifacts, Bartolo will construct the artifacts to handle investments and operating expenses, and Cherubini will develop the artifacts that handle mortgages. Each member is responsible for the quality of the artifacts he or she produces. Almaviva will oversee integration and the overall quality of the software product and will liaise with the client. 

## 5 Managerial Process Plans.

## 5.1 Start-up Plan.

5.1.1 Estimation Plan. As previously stated, the total development time is estimated to be 10 weeks and the total internal cost to be $46,750. These fi gures were obtained by expert judgment by analogy, that is, by comparison with similar projects. 

5.1.2 Staffi ng Plan. Almaviva is needed for the entire 10 weeks, for the fi rst 5 weeks in only a managerial capacity and the second 5 weeks as both manager and programmer. Bartolo and Cherubini are needed for the entire 10 weeks, for the fi rst 5 weeks as systems analysts and designers, and for the second 5 weeks as programmers and testers. 

5.1.3 Resource Acquisition Plan. All necessary hardware, software, and CASE tools for the project are already available. The product will be delivered to the MSG Foundation installed on a desktop computer that will be leased from our usual supplier. 

5.1.4 Project Staff Training Plan. No additional staff training is needed for this project. 

## 5.2 Work Plan.

## 5.2.1–2 Work Activities and Schedule Allocation.

Week 1. (Completed) Met with client, and determined requirements artifacts. Inspected requirements artifacts. 

Weeks 2, 3. (Completed) Produced analysis artifacts, and inspected analysis artifacts. Showed artifacts to client, who approved them. Produced software project management plan, and inspected software project management plan. 

Weeks 4, 5. Produce design artifacts, inspect design artifacts. 

Weeks 6–10. Implementation and inspection of each class, unit testing and documentation, integration of each class, integration testing, product testing, and documentation inspection. 

5.2.3 Resource Allocation. The three team members will work separately on their assigned artifacts. Almaviva’s assigned role will be to monitor the daily progress of the other two, oversee implementation, be responsible for overall quality, and interact with the client. Team members will meet at the end of each day and discuss problems and progress. Formal meetings with the client will be held at the end of each week to report progress and determine if any changes need to be made. Almaviva will ensure that schedule and budget requirements are met. Risk management will also be Almaviva’s responsibility. 

Minimizing faults and maximizing user-friendliness will be Almaviva’s top priorities. Almaviva has overall responsibility for all documentation and has to ensure that it is up to date. 

## 5.2.4 Budget Allocation. The budget for each workfl ow is as follows:

<table><tr><td>Requirements workflow</td><td>$ 3,740</td></tr><tr><td>Analysis workflow</td><td>7,480</td></tr><tr><td>Design workflow</td><td>7,480</td></tr><tr><td>Implementation workflow</td><td>16,830</td></tr><tr><td>Testing workflow</td><td>11,220</td></tr><tr><td>Total</td><td>$46,750</td></tr></table>

5.3 Control Plan. Any major changes that affect the milestones or the budget have to be approved by Almaviva and documented. No outside quality assurance personnel are involved. The benefi ts of having someone other than the individual who carried out the development task do the testing will be accomplished by each person testing another person’s work products. 

Almaviva will be responsible for ensuring that the project is completed on time and within budget. This will be accomplished through daily meetings with the team members. At each meeting, Bartolo and Cherubini will present the day’s progress and problems. 

Almaviva will determine whether they are progressing as expected and whether they are following the specifi cation document and the project management plan. Any major problems faced by the team members will immediately be reported to Almaviva. 

5.4 Risk Management Plan. The risk factors and the tracking mechanisms are as follows: 

There is no existing product with which the new product can be compared. Accordingly, it will not be possible to run the product in parallel with an existing one. Therefore, the product should be subjected to extensive testing. 

The client is assumed to be inexperienced with computers. Therefore, special attention should be paid to the analysis workfl ow and communication with the client. The product has to be made as user-friendly as possible. 

Because of the ever-present possibility of a major design fault, extensive testing will be performed during the design workfl ow. Also, each of the team members will initially test his or her own code and then test the code of another member. Almaviva will be responsible for integration testing and in charge of product testing. 

The information must meet the specifi ed storage requirements and response times. This should not be a major problem because of the small size of the product, but it will be monitored by Almaviva throughout development. 

There is a slim chance of hardware failure, in which case another machine will be leased. If there is a fault in the compiler, it will be replaced. These are covered in the warranties received from the hardware and compiler suppliers. 

5.5 Project Close-out Plan. Not applicable here. 

6 Technical Process Plans. 

6.1 Process Model. The Unifi ed Process will be used. 

6.2 Methods, Tools, and Techniques. The workfl ows will be performed in accordance with the Unifi ed Process. The product will be implemented in Java. 

6.3 Infrastructure Plan. The product will be developed using ArgoUML running under Linux on a personal computer. 

6.4 Product Acceptance Plan. Acceptance of the product by our client will be achieved by following the steps of the Unifi ed Process. 

7 Supporting Process Plan 

7.1 Confi guration Management Plan. CVS will be used throughout for all artifacts. 

7.2 Testing Plan. The testing workfl ow of the Unifi ed Process will be performed. 

7.3 Documentation Plan. Documentation will be produced as specifi ed in the Unifi ed Process. 

7.4–5 Quality Assurance Plan and Reviews and Audits Plan. Bartolo and Cherubini will test each other’s code, and Almaviva will conduct integration testing. Extensive product testing will then be performed by all three. 

7.6 Problem Resolution Plan. As stated in 5.3, any major problems faced by the team members will immediately be reported to Almaviva. 

## 7.7 Subcontractor Management Plan. Not applicable here.

7.8 Process Improvement Plan. All activities will be conducted in accord with the company plan to advance from CMM level 2 to level 3 within 2 years. 

## 8. Additional Plans . Additional components:

Security. A password will be needed to use the product. 

Training. Training will be performed by Almaviva at time of delivery. Because the product is straightforward to use, 1 day should be suffi cient for training. Almaviva will answer questions at no cost for the fi rst year of use. 

Maintenance. Corrective maintenance will be performed by the team at no cost for a period of 12 months. A separate contract will be drawn up regarding enhancement. 

# Design Workfl ow: The MSG Foundation Case Study

This appendix contains the fi nal version of the class diagram for the MSG Foundation case study (Figure G.1). The overall class diagram is followed by UML diagrams for the 10 component classes, in alphabetical order. These UML diagrams show the attributes and the methods. As explained in Section 17.2, the UML visibility prefi xes are – for private , + for public , and # for protected . The attributes and methods are shown in a PDL for Java. Accordingly, there is no Date Class (see Section 14.8). 


FIGURE G.1 The fi nal class diagram for the MSG Foundation case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/c1615aef-eb5a-442d-9862-08ddeee7799c/9e559d913d25f47960d33301ddbd2af04e15b027b51506f4e5d97c90a9082999.jpg)


<table><tr><td>«entity class»Asset Class</td></tr><tr><td># assetNumber : string</td></tr><tr><td>+ getAssetNumber ( ) : string+ setAssetNumber (a : string) : void+abstractread (fileName : RandomAccessFile) : void+abstractobtainNewData ( ) : void+abstractperformDeletion ( ) : void+abstractwrite (fileName : RandomAccessFile) : void+abstractsave ( ) : void+abstractprint ( ) : void+abstractfind (s : string) : Boolean+ delete ( ) : void+ add ( ) : void</td></tr></table>

```typescript
<<control class»
Estimate Funds for Week Class

+ <<static>> compute ( ) : void 
```

```txt
«boundary class»
Estimate Funds Report Class

+ <<static>> printReport ( ) : void 
```

```txt
«entity class»
Investment Class

- investmentName : string
- expectedAnnualReturn : float
- expectedAnnualReturnUpdated : string

+ getInvestmentName ( ) : string
+ setInvestmentName (n : string) : void
+ getExpectedAnnualReturn ( ) : float
+ setExpectedAnnualReturn (r : float) : void
+ getExpectedAnnualReturnUpdated ( ) : string
+ setExpectedAnnualReturnUpdated (d : string) : void
+ totalWeeklyReturnOnInvestment ( ) : float
+ find (findInvestmentID : string) : Boolean
+ read (fileName : RandomAccessFile) : void
+ write (fileName : RandomAccessFile) : void
+ save ( ) : void
+ print ( ) : void
+ printAll ( ) : void
+ obtainNewData ( ) : void
+ performDeletion ( ) : void
+ readInvestmentData ( ) : void
+ updateInvestmentName ( ) : void
+ updateExpectedReturn ( ) : void 
```

```txt
<<boundary class»
Investments Report Class

+ <<static>> printReport ( ) : void 
```

<table><tr><td>«control class»Manage an Asset Class</td></tr><tr><td></td></tr><tr><td>+ &lt;&gt; manageInvestment ( ) : void+ &lt;&gt; manageMortgage ( ) : void</td></tr></table>

```haskell
«entity class»
Mortgage Class

- mortgageeName : string
- price : float
- dateMortgageIssued : string
- currentWeeklyIncome : float
- weeklyIncomeUpdated : string
- annualPropertyTax : float
- annualInsurancePremium : float
- mortgageBalance : float
+ <<static final>> INTEREST_RATE : float
+ <<static final>> MAX_PER_OF_INCOME : float
+ <<static final>> NUMBER_OF_MORTGAGE_PAYMENTS : int
+ <<static final>> WEEKS_IN_YEAR : float
+ getMortgageeName ( ) : string
+ setMortgageeName (n : string) : void
+ getPrice ( ) : float
+ setPrice (p : float) : void
+ getDateMortgageIssued ( ) : string
+ setDateMortgageIssued (w : string) : void
+ getCurrentWeeklyIncome ( ) : float
+ setCurrentWeeklyIncome (i : float) : void
+ getWeeklyIncomeUpdated ( ) : string
+ setWeeklyIncomeUpdated (w : string) : void
+ getAnnualPropertyTax ( ) : float
+ setAnnualPropertyTax (t : float) : void
+ getAnnualInsurancePremium ( ) : float
+ setAnnualInsurancePremium (p : float) : void
+ getMortgageBalance ( ) : float
+ setMortgageBalance (m : float) : void
+ totalWeeklyNetPayments ( ) : float
+ find (findMortgageID : string) : Boolean
+ read (fileName : RandomAccessFile) : void
+ write (fileName : RandomAccessFile) : void
+ obtainNewData ( ) : void
+ performDeletion ( ) : void
+ print ( ) : void
+ <<static>> printAll ( ) : void 
```

```txt
+ save ( ) : void
+ readMortgageData ( ) : void
+ updateBalance ( ) : void
+ updateDate ( ) : void
+ updateInsurancePremium ( ) : void
+ updateMortgageeName ( ) : void
+ updatePrice ( ) : void
+ updatePropertyTax ( ) : void
+ updateWeeklyIncome ( ) : void 
```

«boundary class» 

Mortgages Report Class 

+ <<static>> printReport ( ) : void 

## «entity class»

## MSG Application Class

− <<static>> estimatedFundsForWeek : fl oat 

− <<static>> getAnnualOperatingExpenses ( ) : fl oa 

− <<static>> setAnnualOperatingExpenses (e : fl oat) : void 

+ <<static>> main ( ) 

## «boundary class»

## User Interface Class

+ <<static>> clearScreen ( ) : void 

+ <<static>> pressEnter ( ) : void 

+ <<static>> displayMainMenu ( ) : void 

+ <<static>> displayInvestmentMenu ( ) : void 

+ <<static>> displayMortgageMenu ( ) : void 

+ <<static>> displayReportMenu ( ) : void 

+ <<static>> getChar ( ) : char 

+ <<static>> getString ( ) : string 

+ <<static>> getInt ( ) : int 

# Implementation Workfl ow: The MSG Foundation Case Study (C++ Version)

The complete C++ source code for the MSG Foundation product is available on the World Wide Web at www.mhhe.com/schach. 

# Implementation Workfl ow: The MSG Foundation Case Study (Java Version)

The complete Java source code for the MSG Foundation product is available on the World Wide Web at www.mhhe.com/schach. 

# Test Workfl ow: The MSG Foundation Case Study

The test workfl ow of the MSG Foundation case study is presented in four sections: 

Section 11.11 (requirements) 

Section 13.17 (analysis) 

Section 14.11 (design) 

Section 15.23 (implementation) 

This page intentionally left blank 

This index includes only authors cited in the actual text. 

## A

Abrial, J.-R., 388 Ackerman, A. F., 161 Albrecht, A. J., 273 Alexander, C., 235 Alford, M., 374 Alshayeb, M., 61, 541 Andersson, C., 534 Arisholm, E., 61, 118 Arlow, J., 594 Atkinson, R., 253 Avrahami, M., 100 

## B

Babich, W. A., 144 Baker, F. T., 111, 112, 113 Balzer, R., 392 Banks, J., 361 Basili, V. R., 44, 527, 529 Bassiouni, M., 385, 387 Beck, K., 59, 60, 118 Beizer, B., 487 Berners-Lee, T., 597 Berry, D. M., 172, 190 Binder, L. H., 529 Binkley, A. B., 491, 541 Blaha, M. R., 213 Blythe, J., 220 Boehm, B. W., 11, 12, 14, 62, 63, 64 66, 269, 278, 279, 280, 281, 29 Booch, G., 44, 61, 77, 90, 91, 92, 31 404, 405, 458, 539, 552, 571 Brady, J. M., 376 Briand, L. C., 198 Brooks, F. P., 7, 95, 101, 108, 110, 352, 492 Brown, W. J., 236 Bruegge, B., 220 Buchwald, L. S., 161 Budd, T., 20 Bush, M., 161 Buxton, J. N., 4 

## C

## D

Dahl, O.-J., 184, 211 Daly, E. B., 11, 12 Daly, J., 198 Dart, S. A., 373 Date, C. J., 503 Dawood, M., 99 Delisle, N., 390, 392 DeMarco, T., 364, 365 Deming, W. E., 96 DeRemer, F., 138 Devenny, T., 270 Dhamija, R., 598 Diaz, M., 100 Dijkstra, E. W., 132, 163, 171, 591 Dion, R., 99 Doolan, E. P., 393 Dooley, J. W. M., 141 Drobka, J., 59 Dunn, R. H., 528 Dybå, T., 61, 118 Dyer, M., 529 

## E

Ellison, R. J., 373 Elshoff, J. L., 11 Endres, A., 534 Erdogmus, H., 61 Erikson, W. J., 271 

## F

Fagan, M. E., 12, 159, 160, 161, 393 Feiler, P. H., 373 Feldman, S. I., 147 Felten, E., 598 Ferguson, J., 101 Fitzpatrick, J., 532 Flanagan, D., 211, 233, 476 Forselius, P., 275 Fowler, M., 236 Fowler, P. J., 161 Fuggetta, A., 137 

## G

Gagne, G., 382, 489 Gail, R., 361 Galin, D., 100 Gallis, H., 61, 118 Galvin, P. B., 382, 489 Gamma, E., 234, 235, 236, 239, 244, 245, 248 Gane, C., 364, 365, 373 Gannon, J. D., 11 Garlan, D., 236, 390 Garman, J. R., 93 Gerald, C. F., 186 Gerhart, S. L., 171, 363 Ghezzi, C., 387 Gifford, D., 251 Goldberg, A., 211, 476 Gomaa, H., 490 Goodenough, J. B., 163, 164, 166, 171, 363 

Gordon, M. J. C., 392 

Grady, R. B., 11, 533 

Grant, E. E., 271 

Grasso, C. A., 230 

Green, P., 229 

Griss, M. L., 228 

Guha, R. K., 385, 387 

Guimaraes, T., 502 

Guinan, P. J., 148 

## H

Habermann, A. N., 373 

Hall, A., 390, 391 

Harel, D., 382, 539 

Harrold, M. J., 532 

Hatton, L., 11, 18 

Hayes, F., 50 

Hearst, M., 598 

Hedley, D., 526 

Hefl ey, W. E., 119 

Heinemann, A., 597 

Helm, R., 234, 235, 236, 239, 244, 245, 248 

Hennell, M. A., 526 

Henry, S. M., 491 

Hershey, E. A., 373 

Hoare, C. A. R., 174, 389, 392 

Hops, J., 14, 161 

Howden, W. E., 522, 523 

Huitt, R., 531 

Humphrey, W. S., 95, 99 

Hunter, J. C., 219 

Hutchens, D. H., 527 

Hwang, S.-S. V., 528 

Iannino, A., 528 

## I

Ince, D. C., 528 

## J

Jackson, J., 220 

Jackson, M. A., 475 

Jacobson, I., 44, 77, 90, 91, 92, 314, 404, 405, 458, 539, 552, 571 

Jalote, P., 60 

James, M. F., 219 

Jeffries, R., 59, 61, 118 

Jézéquel, J.-M., 231, 232 

Johnson, R., 219, 234, 235, 236, 239, 244, 245, 248 

Johnson, S. C., 254, 257 

Jones, C., 100, 161, 227, 274, 275, 291 

Jones, C. B., 392 

Josephson, M., 25 

Juran, J. M., 96 

## K

Kafura, D. G., 491 

Kaiser, G. E., 532 

Kamayachi, Y., 527 

Kampen, G. R., 377, 378, 380, 382 

Kan, S. H., 13 

Kangasharju, J., 597 

Keeni, G., 100 

Kelly, J. C., 14, 161 

Kemerer, C. F., 491, 541 

Kernighan, B. W., 254 

Kessler, R. R., 59, 61, 118 

Kiczales, G., 593 

Kitchenham, B. A., 491 

Kleinrock, L., 361 

Klunder, D., 505 

Knuth, D. E., 196, 378 

Kron, H. H., 138 

Kurien, P., 60 

## L

Laddad, R., 593 

Landwehr, C. E., 172 

Lanergan, R. G., 230 

Lang, S. D., 385, 387 

Larman, V., 44 

Leavenworth, B., 171, 363 

Leveson, N. G., 3 

Lewski, F. H., 161 

Li, W., 61, 541 

Lientz, B. P., 8 

Lim, W. C., 228, 229, 290 

Linger, R. C., 529, 530 

Linkman, S. J., 491 

Liskov, B., 253 

Liu, J. W. S., 490 

London, R. L., 171, 363 

Long, F., 540 

Loukides, M., 146, 565 

Luckham, D. C., 392 

Lyardet, F., 597 

## M

Mackenzie, C. E., 250 Mandrioli, D., 387 Manna, Z., 172, 173 Mantei, M., 110 Martin, J., 502 Matsumoto, Y., 229 Matthews, P., 531 Maurer, F., 61 Maxwell, K. D., 275 Mayer, R., 188 McCabe, T. J., 491, 527, 528 McGraw, G., 598 McGregor, J. D., 532 Mellor, P., 3 Mellor, S., 490 Meyer, B., 20, 211, 231, 232, 363 Miller, G. A., 44, 93 Miller, S. A., 119 Mills, H. D., 529 Mooney, J. D., 250 Morris, E., 540 Mühlhäuser, M., 597 Musa, J. D., 528 Musser, D. R., 227 Myers, G. J., 133, 175, 184, 186, 187, 188, 514, 519, 528, 533, 534 Myers, W., 147 

## N

Naur, P., 4, 171, 363 

Nelson, B. L., 361 

Neumann, P. G., 2 

Neustadt, I., 594 

New, R., 158 

Nichol, D. M., 361 

Nix, C. J., 391 

Noftz, D., 59 

Norden, P. V., 282 

Northrop, L., 236 

Norusis, M. J., 227 Norwig, P., 248 Nygaard, K., 184, 211 

## O

Oest, O. N., 392 Offutt, A. J., 198 Ohta, J., 237 Okumoto, K., 528 Oram, A., 146, 565 Orr, K., 475 

## P

Palit, A., 60 Parnas, D. L., 184, 209, 559 Paulk, M. C., 95 Peethamber, V. T., 60 Perry, D. E., 532 Peterson, J. L., 383, 384 Petri, C. A., 383 Pickard, L. M., 491 Pigorski, T., 556 Pittman, M., 290 Pnueli, A., 172 Porter, V., 198 Premerlani, W. J., 213 Putnam, L. H., 283 

## R

Raghu, R., 59 Randell, B., 4 Rapps, S., 526 Raymond, E. S., 23, 58 Reifer, D. J., 61 Ritchie, D. M., 254, 257 Robson, D., 211, 476 Rochkind, M. J., 146, 565 Ross, D. T., 374 Roussopoulos, N., 386 Royce, W. W., 41, 53 Rubenstein, D., 4, 50 Rumbaugh, J., 44, 77, 90, 91, 92, 213, 314, 404, 405, 458, 539, 552, 571 Runeson, P., 529, 534 Rzepka, W. E., 374, 393, 395 

## S

Sackman, H., 271 Saini, A., 227 Sammet, J. E., 500 Sarsen, T., 364, 365, 373 Sawyer, S., 148 Schach, S. R., 8, 38, 135, 141, 194, 198, 249, 253, 272, 273, 290, 491, 541 Schaffert, C., 253 Scheffer, P. A., 374, 393, 395 Schricker, D., 254 Schwaber, K., 60 Schwartz, M., 392 Selby, R. W., 62, 117, 130, 229, 52 Shapiro, F. R., 25 Shaw, A. C., 11 Shaw, M., 236 Sheard, S., 101 Shepperd, M., 491, 528 Sherif, J. S., 14, 161 Shneiderman, B., 188 Shufelt, J., 220 Silberschatz, A., 382, 489 Sjøberg, D. I. K., 61, 118 Sligo, J., 100 Snider, T. R., 99 Snyder, A., 253 Snyder, C. E., 529 Sobell, M. G., 138, 140 Spector, A., 251 Spivey, J. M., 54, 387, 390 Stephenson, W. E., 12 Stevens, W. P., 133, 184, 186 Stevens-Guille, P. D., 194 Stone, A. H., 374, 393, 395 Stroustrup, B., 211, 476 Swanson, E. B., 8 Symons, C. R., 275 

## T

Takahashi, M., 527 Tanenbaum, A. S., 257 Teichroew, D., 373 Tichy, W. F., 146, 565 Toft, P., 237 Tomer, A., 38, 135, 236 Tompkins, G. E., 8 Tracz, W., 228 

Trammel, C. J., 529 Turner, C. S., 3 Turner, R., 62 Tygar, J. D., 598 

## V

van der Poel, K. G., 272, 273 van Wijngaarden, A., 86 Vander Wal, T., 597 Vlissides, J., 234, 235, 236, 239, 244, 245, 248 von Henke, F. W., 392 

## W

Waldinger, R., 173 Walsh, T. J., 528 Ward, P. T., 490 Warnier, J. D., 475 Watson, A. H., 528 Weber, C. V., 95 Weinberg, G. M., 109 Weiss, D. M., 529 Weyuker, E. J., 526 Wheatley, P. O., 186 Wiener, L., 20, 413 Wilde, N., 531 Wilkerson, B., 20, 413 Williams, L., 59, 61, 118 Willis, R. R., 99 Wing, J. M., 172 Wirfs-Brock, R., 20, 413 Wirth, N., 130 Wood, P. T., 350 Woodcock, J., 391 Woodward, M. R., 526 Wüst, J., 198 

## Y

Yourdon, E., 11, 18, 184, 364, 365, 539 Yu, L., 198 

## Z

Zelkowitz, M. V., 11 

1-800-fl owers.com, 21 

## A

abstract class, 239 abstract data type, 191, 207–208, 209, 530 abstract data type design, 476 abstract factory design pattern, 241–244 abstract initial state, 389 abstract method, 239, 561 abstract noun, 411 abstraction, 201–207, 466 acceptance criteria, 36 acceptance testing, 7, 86, 158, 535, 536–537 accessor, 482 accidental reuse, 226 action, defi nition, 582 activation box, 579 activity, 137, 283, 582 defi nition, 582 diagram, 583–585, 587 actor, 318–319, 323–325, 408, 457, 577, 587 defi nition, 318 elevator problem case study, 408 MSG Foundation case study, 323–325 Ada (language), 195, 254, 255, 275, 370, 392, 476, 540 Ada 83 (language), 255 Ada 95 (language), 255, 476 Ada, Countess of Lovelace, 254 Ada Joint Program Offi ce (AJPO), 25 Ada reference manual, 255 Ada standard, 255 adapter design pattern, 235, 240 adaptive maintenance, 8, 142, 553, 554–555, 558, 563 defi nition, 553 ADF, 502 advice, 591 aggregate, 241 aggregation, 213, 573 Agile Alliance, 60 

agile processes, 59–62, 118 Alexander, Christopher, 235 ALGOL, 254 algorithm, 328–329 all-defi nition-use-path coverage, 526–527 alpha release, 86 alpha testing, 86–87, 535 verb, 193 ambiguity, 81, 362 analysis. See analysis workfl ow; classical analysis phase; object oriented analysis analysis artifacts, 84–85 review, 84 analysis fault, 12–14, 553 analysis phase. See classical analysis phase analysis testing, 84–85 analysis workfl ow, 22, 44–47, 80–82, 404–459, 636 challenges, 459 elevator problem case study, 407–424 MSG Foundation case study, 425–455, 636 Analyst/Designer, 395, 490, 539 analytic network modeling, 361 Anna, 392 ANSI X3. 159, 254 ANSI/IEEE 754, 252 ANSI/IEEE 829, 291 ANSI/MIL-STD-1815A, 255 Ant, 147 antipattern, 236 Apache project, 147 Apache Web server, 23 application composition model, 281 application domain, 76, 78, 314, 315–316 application framework, 234 application programming interface (API), 227 architect, 486 architectural design, 7, 21, 82, 466–470 architecture, 49, 90. See also software architecture 

architecture pattern, 236–237 ArgoUML, 353, 459, 490 Ariane 5 rocket, 231–232 artifact, 18, 41, 135 ASCII, 250 aspect, 591 AspectJ, 593 aspect-oriented programming (AOP), 220, 591–593 aspect-oriented programming language, 592 aspect-oriented software development (AOSD), 593 aspect-oriented technology, 591–593 assembler, 257, 275, 501, 534, 564 assert statement, 174, 232 assertion, 168, 170, 174 association, 214, 576 association class, 57 assumptions, 131 asterisk, 575 AT&T Bell Laboratories, 252 ATM, 278 attribute, 18–22, 212, 411, 531 

## B

Babbage, Charles, 254 back-end CASE tool, 136, 490 backtrack, 342, 430 backup programmer, 111–112, 113 bag, 383 baseline, 41, 145–146, 284, 559 Beethoven, Ludwig van, 226 behavioral design pattern, 246 behavioral testing, 517 Belgian budget, 3 beta release, 86, 92 beta testing, 86–87, 535 binding, 186 BlackBerry, 316 black-box testing, 289, 517. See also black-box unit testing origin of term, 517 

black-box unit testing, 520–525, 528–530 

Caesar, Julius, 132 

CICS, 391 

California Institute of Technology, 378 

clandestine common coupling, 194 

blog, 596 

Clarke, Edmund M., 59 

Boccalini, Traiano, 132 capability maturity model (CMM), 95–101, 120, 148, 540 

class, 82, 202–220, 466, 530–53 

Booch’s method, 77 

Borland, 23 

bottom-up integration, 513 strengths, 513 weaknesses, 513 

capital, 320 

CASE, 124, 134–148, 227, 276, 292, 352, 353, 394–395, 457, 458–459, 490, 535, 537–541, 560, 563, 565 

class diagram, 411–412, 419, 422, 428–429, 477–478, 572–577, 587 elevator problem case study 411–412, 419, 422, 477–478 MSG Foundation case study, 428–429 

boundary class, 424, 434–435 defi nition, 405 MSG Foundation case study, 434–435 

scope, 137–141 

tools for analysis workfl ow, 458–459 

class library, 227 

class testing, 530 

boundary value analysis, 521–522 

bounds checking, 174 classical analysis phase, 7, 22, 218, 360–396 challenges, 396 test workfl ow, 393–39 

branch coverage, 526–527 tools for implementation workfl ow, 537–541 

bridge design pattern, 240–241 

tools for management, 292 

Brooks’s Law, 108 

classical analysis technique, 360–393 comparison, 392–393 

browser, 138, 227, 594 tools for object-oriented analysis, 458–459 

budget, 82, 270, 284 tools for planning and estimating, 292 

bug, 25, 109 fi rst use in computer context, 25 classical chief programmer team, 110–113 impracticality, 113 

Bugzilla, 541, 565 tools for postdelivery maintenance, 565 

classical design phase, 7, 22, 466–476 

classical implementation phase, 7 

build tool, 146–147, 565 tools for requirements workfl ow, 353 

classical life cycle, 6–7 

business case, 79, 90–92 

classical maintenance, 9, 10 

business logic tier, 237 

business model, 89, 316–319, 322–32 defi nition, 316 MSG Foundation case study, 322–325 

tools for test workfl ow, 540–541 

tools for the complete life cycle, 537–541 

classical paradigm, 1–15, 18, 25, 215, 217–220, 289, 347–352, 360–396, 466–476 

business-oriented environment, 539–540 

case study. See elevator problem case study; MSG Foundation case study study; MSG Foundation case study 

CCC, 565 

classical phase, 6–7 

Byron, Lord Alfred, 254 classical requirements phase, 7, 218, 347–352 

## C

class-responsibility-collaboration (CRC) card, 413–414, 417–418 elevator problem case study, 417–424 challenges of the analysis workfl ow, 459 of classical analysis, 396 of the design workfl ow, 491–492 of the implementation workfl ow, 542 of object-oriented analysis, 459 of postdelivery maintenance, 566 of the requirements workfl ow, 354–355 

C, 147, 174, 184, 196, 202, 213, 214, 252–253, 254–255, 257, 476, 500, 501, 539, 540 history, 252 

Cleanroom, 529–530 

clickware, 23 

client, 23 

client–server, 236 

C standard, 254–255 

closing costs, 322 

CHAOS Report, 50, 51 

cloud technology, 597–598 

C/SD. See composite/structured design C#, 593 

chat room, 596 

chief programmer, 111–117 

CLU, 253 

CMM. See capability maturity mode 

C++, 10, 25, 138, 140, 143, 147, 166, 174, 184, 196, 202–211, 213, 214, 215, 227, 230, 252–253, 254, 255, 472, 476, 498, 500–501, 507, 509, 515, 516, 531–532, 537, 539, 593 history, 252–253 popularity, 500–501 

chief programmer team, 110–117 classical, 110–113 modern, 113–117 

CMMI, 95 

Cobble, 593 

ChocAn. See Chocoholics Anonymous 

Chocoholics Anonymous, 627–629 

C++ standard, 255 

choice of programming language, 484, 538–539 

C <sup>3</sup> I, 374 

Chrome, 138 

chunk, 130 

COBOL 2002, 254 

COBOL program logic structure, 230 

COBOL standard, 253–254 

Coca-Cola, 156 

Cocoa, 227 

COCOMO, 278–282, 290, 292 example, 279–280 experimentation, 280 

COCOMO II, 281–282, 292 

CODASYL, 254 

code artifact, 83, 516 

code generator, 539–540 

code inspection, 352, 528–530 

code reuse, 232–237, 510 

code review, 85, 113 

code walkthrough, 528–530 

code-and-fi x model, 52–53, 218 

coding. See implementation 

coding fault, 553 

coding standard, 509–510 

coding tool, 138 

cohesion, 186, 187–192, 218, 468–475, 490 example, 191–192 

coincidental cohesion, 187–188, 192, 509 

collaboration diagram, 436–452, 587 MSG Foundation case study, 436–452 

collection, 241 

comments, 506–507 

commercial off-the-shelf software. See COTS 

common coupling, 193–195, 198, 203 

Communicating Sequential Processes (CSP), 392 

communicational cohesion, 190, 469 

compiler, 253–255 incompatibility, 253–255 

complexity, 20, 527 

component, 83, 226–228, 516 reusable, 226–228 

component diagram, defi nition, 586 

component-based software engineering, 237, 594 

component-based technology, 594, 595–596 

composite/structured design (C/SD), 133, 186–199, 232, 468 

composition, 575–576, 592, 594 

computer crime, 194, 196 

computer security, 598 

computer-aided software engineering. See CASE 

conceptual independence, 20, 133, 202, 232, 560 concern, 591 cone of uncertainty, 269 confi guration, 143 confi guration control, 143–147, 565 during maintenance, 145–146 during postdelivery maintenance, 565 confi guration-control tool, 143, 145, 538, 565 consistency checker, 136, 538, 539 consistent variable names, 504–505 constraints, 79, 83, 165, 360–361, 488, 489, 536, 537 deadline, 79, 83, 361 hard time, 165, 488 parallel running, 361, 537 portability, 361 reliability, 79, 361 response time, 536 security, 536 size of object code, 79 storage, 536 timing, 361, 489 construction phase, 89, 92 container, 241 content coupling, 192–193 contract software development, 23 contradiction, 81 control class, 406, 424, 435 defi nition, 406 MSG Foundation case study, 435 control coupling, 195, 198 core assets, 236 core concern, 591 core workfl ows, 78 corrective maintenance, 8, 142, 528, 553, 554, 555, 558, 560, 563 defi nition, 8, 553 correctness, 166 necessity, 166 suffi ciency, 166 correctness proof, 167–174, 363–364 example, 167–170 mini case study, 172, 363–364 strengths, 173–174 and testing, 171 weaknesses, 173 correctness testing, 86, 166–167, 536, 537 cost, 79, 133, 134, 268–272, 275–282 external, 271 internal. 271 

cost estimate, 270–27 cost estimation, 81–82, 268–272, 275–282 algorithmic models, 277–282 bottom-up approach, 277 expert judgment by analogy, 276–277 tracking, 282 cost–benefi t analysis, 130–131, 173, 257, 364, 533 example, 130–131 COTS, 23, 62, 86–87, 228, 405, 535 coupling, 186, 192–199, 203, 218, 468–475, 490 example, 197–198 importance, 198–199 CppUnit, 540 CRC card. See class-responsibility collaboration card creational design pattern, 245 Cresti, Domenico, 349 cross-cutting concerns, 591 cursor, 241 Cutter Consortium, 5 CVS, 146 cyclomatic complexity, 491, 527–528, 541 strengths, 491 weaknesses, 491 

## D

dancing pigs problem, 598 data abstraction, 202, 208, 214 data access logic tier, 237 data coupling, 196–197, 198 data dictionary, 136–137, 368, 394, 490, 538, 539 data encapsulation, 199–206 and development, 201–202 and maintenance, 202–206 data fl ow (structured systems analysis), 365 data fl ow analysis (DFA), 18, 467–473, 490 mini case study, 468–472 data fl ow diagram (DFD), 365–367, 394, 467–473 data immediate access diagram (DIAD), 370 data processing, 230–231, 273, 499 

data store (structured systems analysis), 365 data-driven testing, 517 data-oriented design, 465 date and time stamp, 147 DB2, 503 dbx tool, 141 debugging, 140–141, 175, 533 decision tree, 369 defect, terminology, 25, 155, 554 defect report, 557–558 defect tracking, 565 defect-tracking tool, 565 defensive programming, 512, 513, 514 defi ned level, 96 deliberate reuse, 226 deliverables, 82, 89, 91, 92 della Torre, Giovanni Agostino, 552 della Torre, Niccolò, 552 Delphi technique, 276 delta, 145 democratic team, 109–110, 113–117 strengths, 110 weaknesses, 110 Department of Defense (DoD), 98, 500 Department of Redundant Information Department, 278 deployment diagram, defi nition, 586 deposit, 320 derivation, 144 derived class, 212 design, 465–492. See also classical design phase; design workfl ow; object-oriented design of real-time systems, 488–490 design artifacts, 85 design by contract, 20 design document, 7, 563 design fault, 12–14, 85, 487, 553 design inspection. 352 design pattern, 232–249 abstract factory , 241–244 adapter , 235, 240 behavioral, 246 bridge , 240–24 creational, 245 iterator , 241 strengths, 247 structural, 245 weaknesses, 248 design phase. See classical design phase design reuse, 232–237 

design walkthrough, 487 design workfl ow, 22, 44–47, 82–83, 477–480, 488–492, 642–646 challenges, 491–492 elevator problem case study, 477–480 MSG Foundation case study, 488–490, 642–646 desk checking, 175 detailed design, 7, 21, 82, 466, 470–472, 479, 483, 488 elevator problem case study, 479 formal techniques, 488 MSG Foundation case study, 483 developers, 23 development, 20 development-then-maintenance model, 9 DFD. See data fl ow diagram direct observation, 317 discriminator, 576 distributed software, 489 divide-and-conquer, 132 documentation, 24, 45, 54–55, 74, 75, 82, 86, 87, 88, 91, 137–138, 258, 291, 536, 537, 554, 558, 559, 563, 564 checking, 537 documentation fault, 553 documentation phase, 17 documentation standard, 258, 291 doghouse, 61 domain, 78, 314, 315–316. See also application domain door (elevator), 381 DOS/VS, 534 Doxygen, 565 driver, 240, 511–513 defi nition, 511 DTSTTCPW, 60 duration, 134, 268–272, 275–282 duration estimate, 270–271 duration estimation, 81–82, 268–272, 275–282 tracking, 282 dynamic binding, 215–217, 220, 561–562 dynamic model, 414–417, 430–432 elevator problem case study 414–417 MSG Foundation case study, 430-432 

dynamic modeling, 406, 414–417, 430–432 defi nition, 406 elevator problem case study, 414–417 MSG Foundation case study, 430–432 

## E

early aspects, 593 early design model, 281 EBCDIC, 250 Eclipse, 538, 541 e-Components, 234 economics, 5–6 Edison, Thomas Alva, 25 effi ciency, 273 effort, 134 egoless programming, 109–110 elaboration phase, 89, 91–92 element access, 241 element traversal, 241 elephant, 108 elevator button, 378 elevator controller, 380 elevator door malfunction, 419 elevator problem, history, 378 elevator problem case study, 378–382, 385–387, 388–390, 407–424, 477–480 class diagram, 411–412, 419, 422, 477–478 class-responsibility-collaboration (CRC) card, 417–424 constraints, 378, 385–387, 389 detailed design, 479 dynamic modeling, 414–417 entity class modeling, 410–414 fi nite state machine, 378–382 functional modeling, 407–410 noun extraction, 411 object-oriented analysis, 407–424 object-oriented design, 477–480 Petri nets, 385–387 scenarios, 408–410 statechart, 414–417, 422 statement of problem, 378, 407 test workfl ow, 417–424 use case, 408 use-case diagram, 408, 419 Z, 388–390 

e-mail, 138, 596 embedded software, 165 Emeraude, 540 Emerson, E. Allen, 598 enable (Petri net), 384 encapsulation, 20, 133, 199–206, 232, 560 end-user programming, 503 enhancement, 8, 560 Enterprise JavaBeans, 234 entity class, defi nition, 405 entity class modeling, 406, 410–414, 425–435 defi nition, 406 elevator problem case study, 410–414 MSG Foundation case study, 425–435 entity-relationship diagram, 374–376 entity-relationship model (ERM), 374–376, 394, 410 environment, 137, 538–540. See also CASE potential problems, 540 equivalence class, defi nition, 521 equivalence testing, 521–522 error, terminology, 25, 155 escrow account, 321 estimation. See cost estimation; duration estimation; size estimation ethics, 26–27 European Space Agency, 231–232 European Strategic Programme for Research in Information Technology (ESPRIT), 540 event, 431 event (fi nite state machine), 377 event (UML), 581 evolution, 552 evolution-tree model, 40–42, 43, 47–48 Excel, 292 exception, 231 exception scenario, 408 executable load image, 147 execution-based testing, 155, 162–167, 176, 516–530 who should perform it, 175–176 experimentation, 161, 271, 274, 280, 528–529 on COCOMO, 280 on function points, 274 

on inspection, 161 on programmer performance, 271 on unit testing, 528–529 extend relationship, 578 extended fi nite state machine, 377–382 external cost, 271 extreme programming, 59–60, 117–118 

## F

Facebook, 596 failure, terminology, 25, 155 fan-in, 491 fan-out, 491 fault, terminology, 25, 155 fault density, 162 fault detection, 157–164, 166–167, 529–533 fault detection effi ciency, 162 fault detection rate, 162 fault distribution, 528, 534 fault isolation, 190, 511–513 fault statistics, 160–161, 289, 541, 566 faults, maximum permitted number, 535 feature creep, 43 FFP metric, 273, 275 strengths, 273 weaknesses, 273, 275 fi eld, 26 fi nite state machine (FSM), 374, 376–382, 414 defi nition, 376–377 elevator problem case study, 378–382 Firefox Web browser, 23, 56, 58 fi rst-generation language, 501, 539 Flickr, 596 Flintstock Life Insurance Company (FLIC) mini case study, 238–239 fl oating-point standard, 252 fl oor button, 378 FLOW, 141 fl owchart, 55, 130, 563 fl owchart cohesion, 190 Focus, 501 follow-up, 160 fork, 584, 585 defi nition, 584 formal method, 539 formal specifi cation, 54, 363, 376–392 formal technique, 376–392, 414, 488, 539 formatter, 138 

forms, 317 Fortran, 253, 254, 476 spelling, 254 Fortran 2003, 253, 254 Fortran standard, 254 forward engineering, 563 fourth-generation language (4GL), 272, 349, 500, 501–503, 539 potential danger, 503 FoxBASE, 529 fragile base class problem, 219, 562 framework, 234, 236 freeze, 145 front-end CASE tool, 135, 490 function points, 273–275, 290 experimentation, 274 strengths, 275 weaknesses, 275 functional analysis, 523 functional cohesion, 187, 190–191, 232, 469 functional modeling, 407–410, 425–427 defi nition, 406 elevator problem case study, 407–410 MSG Foundation case study, 425–427 functional module, 230 functional requirement, 486 defi nition, 320 functional testing, 517, 522–525 

## G

Gang of Four, 235 general design, 466 generalization, 213, 319, 576 Generic Coverage Tool, 526 Gist, 392 given set, 388 glass-box testing, origin of term, 517 glass-box unit testing, 525–530 glossary, 315, 322 MSG Foundation case study, 322 God class, 419 good programming practice, 203, 504–509 Google Docs, 594, 595 Gosling, James, 252, 253 graphical user interface (GUI), 219, 233, 258, 350, 535, 539 graphical user interface (GUI) generator, 539 

Gregorian calendar, 413 GTE, 12 guard, 580–583 defi nition, 580 GUI, 431 guillemet, 578 

## H

hardware, 250–251, 371 incompatibility, 250–251 Hayakawa, S. I., 314 Hewlett-Packard, 11, 228, 237 hierarchy, 111 high-level design, 466 high-level language, 256, 257, 501 history of C, 252 of C++, 252–253 of COBOL, 500 of elevator problem, 378 of Java, 252–253 of reuse, 227 Hopper, Grace Murray, 25, 500 horizontal schema defi nition, 389 hot spot, 234 How to Perform equivalence testing, 522 object-oriented analysis, 458 requirements workfl ow, 355 sandwich integration, 515 structured systems analysis, 371 transaction analysis, 474 HTML, 349, 352 Hughes Aircraft, 99 human factors, 271, 349–351 human–computer interface (HCI), 349–351 Hungarian Naming Conventions, 505 Hypertext Markup Language. See HTML 

## I

IBM, 12, 13, 112, 161, 219, 251, 253, 257, 391, 502, 503, 540 IBM Rational ClearCase, 565 IBM Rational ClearQuest, 565 IBM Rational Functional Tester, 541 IBM Rational Purify, 541 

IBM Rational Rose, 353, 459, 490, 539, 565 IBM Websphere, 593 IEEE 1028, 159, 160 IEEE 1058, 284 IEEE 610, 12, 155 IEEE/EIA 12207, 101 illuminated (button), 379 implementation, 138–141, 498–542. See also classical implementation phase; implementation workfl ow implementation artifacts, 85–87 implementation phase. See classical implementation phas implementation testing. See unit testing implementation workfl ow, 22, 44–47, 83–84, 516, 647, 648 challenges, 542 MSG Foundation case study, 647, 648 inception phase, 89–91 include relationship, 345, 578 incompleteness, 8 incrementation, 43–52, 429 management, 51–52 infeasible path, 527 informal specifi cation, 362–364 example, 362–363 information hiding, 19, 20, 133, 184, 209–211, 232, 240, 530–531, 559, 560 informational cohesion, 187, 191, 201, 232 inheritance, 211–220, 319, 411, 530, 531–532, 560–561 inhibitor arc, 385 initial level, 95 initial requirements, 319–320, 326–327 input (fi nite state machine), 377 input function (Petri net), 383 input specifi cation, 166, 168–173 input/output-driven testing, 517 inspection, 159–162, 289, 393, 487, 528–530 code, 528–530 comparison with walkthrough, 161–162 experimentation, 161 possible danger, 161 strength, 162 transaction-driven, 487 weakness, 162 inspection rate, 162 

instance variable, 25 instant messaging, 596 insurance premium, 32 integrated environment, 290, 538–539 integration, 7, 85–87, 510–516, 535–537 of object-oriented products, 514 integration testing, 86, 92, 510–514, 535–537, 563 interaction diagram, 436–452, 587 MSG Foundation case study, 436–452 interactive source-level debugger, 140 interconnection diagram, 511 interface, 188 internal cost, 271 internal software development, 23 International Organization for Standardization (ISO), 10, 98 interview, 316–317, 353 JPD-CMM. 95 isA relationship, 213 ISO. See International Organization fo Standardization ISO 9000-3, 98 ISO 9001, 98 ISO/IEC 12207, 10 ISO/IEC 14882, 255 ISO/IEC 1539-1, 253, 254 ISO/IEC 15504 (SPICE), 99 ISO/IEC 1989, 254 ISO/IEC 8652, 255, 476 iteration. 43. 48–52. 429. 476 management, 51–52 iterative-and-incremental life-cycle model, 43–52, 76, 338, 406, 587 strengths, 49–50 iterator, 24 iterator design pattern, 241 

## J

Jackpot Source Code Metrics, 541 Jackson system development (JSD), 18, 538 Java, 10, 140, 143, 174, 184, 211, 227, 252–253, 254, 255, 352, 500, 501, 504, 507, 509, 515, 516, 537, 539 history, 252–253 origin of name, 252 Java Abstract Windowing Toolkit, 233 Java interpreter, 15 

Java loader, 15 JavaBeans, 234 JBoss, 593 JBuilder, 138 job control language (JCL), 111, 251 Johannesburg, 504 join, 584, 585 defi nition, 584 Julian Day, 413 JUnit, 540 Just in Case You Wanted to Know, 3, 4, 8, 10, 21, 24, 25, 38, 51, 75, 77, 93, 101, 109, 132, 135, 136, 156, 165, 174, 184, 196, 203, 210, 226, 229, 235, 236, 252–253, 254, 278, 279, 314, 321, 349, 351, 378, 388, 405, 410, 413, 419, 500, 502, 504, 505, 514, 517, 535, 539, 552, 556, 575, 591, 596 

## K

kangaroos, 229 KDSI. See lines of code key process area (KPA), 97–98, 119 Kleene star, 575, 580 Kleene, Stephen, 575 KLOC. See lines of code Knuth, Donald E., 196 Kokomo, Indiana, 278 

## L

learning curve, 219 legacy system, 10, 405, 563 levels of abstraction, 539, 564 librarian, 112 library, 233–234 life cycle, 6, 12–14, 21 life-cycle model, 6, 37–67 agile processes, 59–62 code-and-fi x, 52–53 comparison, 66–67 evolution-tree, 40–42 extreme programming, 59–60 iterative-and-incremental, 48–52 open source, 56–59 rapid prototyping, 55–56 spiral, 62–66 synchronize-and-stabilize, 62 waterfall, 41 

lift problem, 378 Lilio, Luigi, 413 Lincoln Center, 502 linear path sequences, 526 line-editing problem. See textprocessing problem lines of code (LOC, KLOC, KDSI), 133, 272, 274, 278, 527, 528, 541 LinkedIn, 596 lint , 15, 254, 541 Linus’s Law, 23, 24 Linux, 23, 49, 244, 258 LISP, 213, 253, 272, 349, 499, 504 LOC. See lines of code logic artifact, 511–514 defi nition, 511 logical cohesion, 188, 191, 195, 474 logical data fl ow, 365 logical design, 466 logic-driven testing, 517 lookahead, 129 loop invariant, 169–171, 172–173 Lotto, Lorenzo, 552 Lotus 1-2-3, 292 lowerCASE tool, 136, 490 low-level design, 466 

## M

Mac OS, 244 Mac OS X, 227 Machiavelli, Niccolò, 132 Macintosh, 351, 538 MacProject, 292 maintainability, 553, 559 techniques, 559 maintenance, 6–12, 18, 20, 75, 87, 142, 188, 190, 197, 219, 528, 551–566 adaptive maintenance, 8, 142, 553, 554–555, 558, 563 classical, 9 corrective maintenance, 8, 142, 528, 553, 554, 555, 558, 560, 563 modern, 10 operational defi nition, 10 perfective maintenance, 8, 142, 553, 554–555, 558, 563 postdelivery, 75, 87, 551–566 temporal defi nition, 9 maintenance programmer, 505–506, 553–559 maintenance team, 145–146 

maintenance testing, 87 maintenance tool, 565 make tool, 147 managed level, 96 management, 75, 158–159, 282–291, 515–516, 533, 557–560. See also software project management plan of integration, 515–516 of postdelivery maintenance, 557–560 of unit testing, 533 of walkthrough, 158–159 managerial independence, 156 Manifesto for Agile Software Development , 60, 6 manual. See documentation manual pages, 138 marked Petri net, 384 marking, defi nition, 384 maturity, 95 maturity level, 95–101, 120 MDA. See model-driven architecture mean time between failures, 133, 164 mean time to repair, 164 meaningful variable names, 504–505 MEASL. See million equivalent assembler source lines media site, 596 member, 26 member function, 26 menu, 431 message, 19, 218, 514, 560 method, 19, 531, 539 multiple meanings, 539 method-based environment, 539 methodology, correct meaning, 24 metrics, 133–134, 162, 187–199, 270–282, 353–354, 395, 459, 490–491, 527–528, 541, 566 for classical analysis, 395 cohesion, 187–192 complexity, 491, 527–528 cost, 134, 270–282 coupling, 192–199 cyclomatic complexity, 527–528 for design, 490–491 duration, 134, 270–272, 275–282 effort, 134, 395 for implementation, 527–528, 541 for inspections, 162 object-oriented, 491 for object-oriented analysis, 459 

for planning, 270–282 for postdelivery maintenance, 566 quality, 134, 395, 459, 490 for requirements, 353–354 size, 134, 272–275, 395, 459, 490 Microsoft, 23, 62, 117, 505, 541 Microsoft Project, 292 Microsoft Word, 594 milestone, 82, 284 millennium bug, 405 Miller’s Law, 44, 78, 93, 124–125 million equivalent assembler source lines (MEASL), 100 Milstar satellite, 93 mini case study. See correctness proof mini case study; data fl ow analysis mini case study; Flintstock Life Insurance Company mini case study; postdelivery maintenance min case study; Sally’s Software Store mini case study; stepwise refi nement mini case study; Teal Tractors mini case study; Winburg mini case study; word counting mini case study mistake, terminology, 25, 155 mitigate risk. See risk mitigation Mk II function points, 275 modal logic, 172, 173 model (UML), 318 model checking, 174, 598–599 model, life cycle. See life-cycle model model, UML, 76 model-driven architecture (MDA), 259, 593–594 model-driven technology, 593–594 model-view-controller (MVC) architecture pattern, 133, 237 modern chief programmer team, 113–117 modern maintenance, 10 modular design, 466 module, 7, 82, 184–220, 232, 466 context, 186 defi nition, 184 interface, 82 logic, 186 operation, 186 money, 284 mortgage, 320–322 pronunciation, 321 Motif, 258 

Motorola, 100 moving target problem, 43, 559–560 Mozart, Wolfgang Amadeus, 226 MSG Foundation case study, 320–347, 372–373, 425–457, 476, 481–483, 484, 486, 516, 523–525, 537, 566, 632–649 actors, 323–325 algorithm, 328–329 analysis workfl ow, 425–455, 636 black-box test cases, 523–525 boundary classes, 434–435 business model, 322–325 C++ implementation, 647 class diagram, 428–429 class extraction, 425–435 classical analysis phase, 372–373 collaboration diagrams, 435–452 control classes, 435 design workfl ow, 481–483, 642–646 detailed design, 483 dynamic model, 430–432 entity classes, 425–435 functional model, 425–427 glossary, 322 implementation workfl ow, 516, 647, 648 initial business model, 322–325 initial class diagram, 428–429 initial dynamic model, 430–432 initial functional model, 425–427 initial glossary, 322 initial requirements, 326–327 initial understanding of the domain, 320–322 interaction diagrams, 435–452 Java implementation, 648 noun extraction, 428 object-oriented analysis (OOA), 425–455 object-oriented design, 481–483 postdelivery maintenance, 566 requirements workfl ow, 320–347, 632 scenarios, 435–452 sequence diagrams, 435–452 software project management plan, 637–641 statechart, 430–432 structured systems analysis, 372–373, 633–635 test workfl ow, 456, 537, 649 

understanding of the domain, 320–322 use cases, 425–430, 435–452 use-case diagram, 330–345, 429 use-case realizations, 435–454 multiplicity, 574–575 multiset, 383 mutator, 482 MySpace, 596 

## N

NAG, 227 NASA, 14 Natural, 501 natural language, 362 Naur, Peter, 171, 363–364 navigation triangle, 214, 576 negotiation, 354 nested if statement, 507–509 networking site, 596 New York Times . See The New York Times NIST 151, 258 No Silver Bullet , 101, 492 nominal effort, 278 non-execution-based testing, 155, 157–162, 167–174, 516, 528–530 nonfunctional requirement, 320, 486 nonprocedural language, 502, 503 normal scenario, 408 not invented here (NIH) syndrome, 228 note, 213, 577 noun extraction, 411, 428 elevator problem case study, 411 MSG Foundation case study, 428 numerical software, incompatibility, 251 

## O

object, 18–22, 191, 211–220, 232, 514, 530–533, 560 advantages, 214 object code, 146–147 Object Management Group (OMG), 77, 571 object points, 281 object testing, 530–533 

object-oriented analysis (OOA), 22, 404–459, 466. See also analysis workfl ow elevator problem case study 407–424 MSG Foundation case study, 425–455 

object-oriented architecture, 236 

object-oriented CASE tool, 458–459, 539 

object-oriented COBOL, 254 

object-oriented design (OOD), 20, 410, 466, 476–483, 490. See also design workfl ow elevator problem case study, 477–480 MSG Foundation case study, 481–483 

object-oriented Fortran, 254 

object-oriented language, 476 

object-oriented metrics, 491 

object-oriented paradigm, 18–22, 25, 187, 202–220, 232, 277, 289–290, 314–346, 404–459, 500–501, 514, 516, 530–533, 539, 560–562 

strengths, 22, 217–220 

weaknesses, 22, 217–220, 560–562 

object-oriented programming language, 500–501, 514, 515 hybrid, 501, 515 pure, 501, 515 

Objectory, 77 

OMT, 77 

one-dimensional life-cycle model, 92. See also waterfall model 

online documentation, 137–138, 141 

online interface checker, 139, 141 

open-ended design, 83 

open-source CASE tool, 146, 147, 353, 459, 490, 538, 540, 541, 565 

ArgoUML, 353, 459, 490 

Bugzilla, 541, 565 

CppUnit, 540 

CVS, 146, 538, 565 

Doxygen, 565 

open-source life-cycle model, 56–59 

open-source software, 23, 147 open-source software development, 56–59 operating system, 257 incompatibility, 251, 258 operating system front end, 139–140, 141 operation, 18–22 operational artifact, 511–514 defi nition, 511 operation-oriented design, 465, 466–476 operations, 389 opportunistic reuse, 226 optimization, 196 optimizing level, 96 Oracle, 503 Oracle Developer Suite, 540 OS/370, 534 OS/VS2, 188 output function (Petri net), 383 output specifi cation, 166, 168–173 overview, 159 

## P

P & I. See principal and interest package, 132, 486, 585 defi nition, 585 pair programming, 59, 61, 118 Palm Pilot, 316 paradigm, correct meaning, 24 parameter, 507 Parasoft, 541 part–whole relationship, 573 Pascal (language), 184, 254, 501 Pascal, Blaise, 254 path coverage, 520, 526–527 path-oriented testing, 517 Patriot missile, 3 pattern, 232–249 architecture, 236–237 pattern language for architecture, 235 pcc compiler front end, 254 P–CMM, 95, 120 PCTE. See portable common tool environment PDL. See pseudocode people capability maturity model. See P–CMM perfective maintenance, 8, 142, 553, 554–555, 558, 563 

performance appraisal, 113–114, 159 161 

performance testing, 165–166, 536, 537 

Perl, 349 

personal profi le site, 596 

person-month, defi nition, 133 

Petri net, 382–387, 394, 538 

elevator problem case study, 385–387 

phase. See also classical analysis phase; classical design phase; classical implementation phase; classica requirements phase; construction phase; elaboration phase; inception phase; transition phase classical, 6–7, 16–17 

Phillip II of Macedon, 132 

physical design, 466 

physical independence, 20, 133, 232, 560 

PIN, 278 

pipes and fi lters, 236, 538 

PL/I, 112–113, 253 

place (Petri net), 383 

planning, 16, 45, 91, 98, 268–291 

planning phase, 16 

platform constraint, 32 

platform-independent model (PIM), 593 

platform-specifi c model (PSM), 593 

point and click, 350 

point of highest abstraction of input, 467–473 

point of highest abstraction of output, 467–473 

pointcut, 591 

points, 322 

polymorphism, 215–217, 220, 561–562 

portability, 250–259, 484, 486, 539 defi nition, 250 description, 226 impediments, 256, 259 strengths, 256, 259 

portable application software, 257–258 

portable common tool environment (PCTE), 540 

portable compiler, 255 

portable data, 258–259 

portable database, 258 

portable numerical software, 251 

portable operating system, 257 portable operating system interface for computer environments (POSIX), 258 portable system software, 257 POSIX. See portable operating system interface for computer environments postarchitecture model, 281 postcondition, 390 postdelivery maintenance, 6–12, 20, 75, 87, 145–146, 249–250, 551–566. See also maintenance attitude toward, 556 challenges, 566 diffi culty, 554–555 management of, 557–560 mini case study, 556–557 of object-oriented software, 560–562 repeated, 559–560 scope, 552 skills, 563 thanklessness, 555 postdelivery maintenance testing, 564–565 PowerBuilder, 503 statement, 232 precondition, 390 predicate (fi nite state machine), 377 predicate calculus, 172 PREfast, 541 PREfi x, 541 preparation, 159 presentation logic tier, 237 pretty printer, 138, 563, 564 price, 271 principal, 320 principal and interest (P & I), 321 private visibility modifi er, 210 private workspace, 145, 559 procedural abstraction, 202, 208 procedural cohesion, 189 procedural language, 502 process. See software process process (structured systems analysis), 365 process improvement, 94–101 process integration, 538–539 process maturity level, 95–101 process metric, 133 product, terminology, 24 product line, 236–237 product metric, 133 

product testing, 86, 92, 289, 535–536, 563 productivity, 147–148, 231, 232, 272, 273, 274, 502 program, 24 program description language. See pseudocode (PDL) programming language, choice of, 538–539 programming languages. See specifi c languages programming secretary, 111, 112, 113 programming team, 15, 470 programming workbench, 141 programming-in-the-large, 138 programming-in-the-many, 138, 139, 498 programming-in-the-small, 138 project function, 283 Prolog, 349 prologue comments, 506–507, 558 proof of correctness. See correctness proof proof-of-concept prototype, 45, 63, 91 prototype, 62–64, 91, 361. See also rapid prototype pseudocode (PDL), 130, 471, 492 PSL/PSA, 373 public tool infrastructure, 540 public visibility modifi er, 193, 208, 210 pun, 136 PureCoverage, 526 PVCS, 146, 538 

## Q

QARun, 535 quality. See software quality terminology, 156 quality requirement, 320 questionnaire, 317 

## R

rapid prototype, 55–56, 63, 348–349, 351–352 purpose, 348 reuse of, 351–352 rapid-prototyping model, 55–56, 348–349, 351–352 

Rational, 77 Rational Unifi ed Process, 77 Rayleigh distribution, 282 Raytheon, 99, 230–231, 234 rcs tool, 146, 565 readability, 505, 507 reader, 160 real-time software, 93, 166 real-time system. 11. 163. 166, 488–490 diffi culties, 489 real-time system design, 488–490 extension of non-real-time techniques, 490 recorder, 160 reengineering, 563 refactoring, 60, 564 refi ne, 319, 434, 457 defi nition, 316 regression fault, 20, 43, 53, 197, 218 554, 560, 566 regression testing, 54, 87, 176, 554, 558, 559, 564–565 reliability, 164, 320, 486 reliability analysis, 533 reliability testing, 164 repeatable level, 96 report generator, 136, 457, 490 requirements, 313–355 requirements analysis, 315, 348 requirements artifacts, 84 requirements capture, 315 requirements elicitation, 315, 316–317, 348 requirements engineering, 315 requirements fault, 14 requirements management, 98 requirements workfl ow, 44–47, 78–80, 314–347, 353–355, 632 actors, 318–319 business model, 316–319 challenges, 354–355 intial requirements, 319–320 MSG Foundation case study, 632 understanding the domain, 315–316 use cases, 318–319 RequisitePro, 137 resources, 282, 283 response time, 320, 371 responsibility-driven design, 20, 21, 408, 477 restructuring, 564 retirement, 8, 88, 176 

return, 580 

reusable component, 226–228 

reuse, 21, 188, 189, 190, 193, 194, 218, 226–250, 259, 290, 475, 484, 510, 512, 514 

case studies, 229–232 

code, 232–237, 510 

description, 226 

design, 232–237 

history, 227 

impediments, 228, 259 

review, 84, 85. See also walkthrough; inspection 

revision, 141–142 and postdelivery maintenance, 249–250 

rework, 160 

Rhapsody, 382, 539 

risk, 50, 62–66, 87, 90 

risk analysis, 499 

reverse engineering, 563–564 

risk mitigation, 63 

Ritchie, Dennis, 252 

robustness, 49, 86, 90, 165, 486, 536 

robustness testing, 86, 165, 537 

role, 457 

Romeo and Juliet , 226 

Romney, George, 314 

## S

SADT, 374 

Salesforce.com, 596 

Sallie Mae, 3 

schema, 388 

Sally’s Software Shop mini case study, 364–371 

San Francisco (framework), 234 

scheduling tool, 292 

sandwich integration, 513–514 origin of term, 514 

SBC Communications, 253 

Scaliger, Joseph, 413 

Scaliger, Julius Caesar, 413 

sccs tool, 146, 565 

scenario, 406, 408–410, 435–452 elevator problem case study, 408–410 MSG Foundation case study, 435–452 

screen generator, 136–137, 457, 490 

Schubert, Franz, 226 

Scud missile, 3 

SDRTS, 490 

scientifi c software, 233 

scratch, 38 

secretary, 112 

SEI. See Software Engineering Institute self-call, 580 

self-documenting code, 505 

Semantic Web, 598 

semiformal specifi cation, 364–375, 404 

semiformal technique, 414 

separate implementation and integration, 510–511 

sequence diagram, 435–452, 587 MSG Foundation case study 435–452 

separation of concerns, 20, 132–133, 186, 191, 197, 201, 209, 591 

service, 595 

service providers, 595 

Shoo-Bug, 109 

Shakespeare, William, 226 

Sifakis, Joseph, 598 

shrink-wrapped software, 23 

service-oriented technology, 594–596 

SilkTest, 535, 541 

Simula 67 (language), 184, 211 

simulator, 164 

size, 272–275 

size estimation, 272–275 

sizing, hardware, 371 

SLAM, 541 

Smalltalk, 211, 227, 349, 476, 498, 500 

social computing, 596 

software, 24 

software architecture, 236–237 

software crisis, 4–5 fi nancial implications, 4–5 

software depression, 5 

software development effort multipliers, 278 

software development environment. See CASE 

software engineering defi nition, 2 economic aspects, 5–6 historical aspects, 4–5 maintenance aspects, 6–12 requirements, analysis and design aspects, 12–14 

scope of, 1–15 

software process improvement, 94–101 costs and benefi ts, 99–101 

team development aspects, 15 

software process, 5, 74–101 

Software Engineering Institute (SEI), 95–98 

software production, terminology, 24 software product line, 236–237 software engineering resources, 630–631 

MSG Foundation case study, 637–641 

components, 282–284 software project management plan (SPMP), 7, 16, 81–82, 282–292, 393, 516, 536, 637–641 

terminology, 282–284 

IEEE standard, 282, 286–288 

testing, 292 

software quality, 17, 133, 134, 155–157, 173 

software quality assurance (SQA), 62, 98, 156–157, 559 

software quality assurance (SQA) group, 17, 53, 81, 84–85, 141, 158, 160, 175, 289, 506, 509, 535–537, 558 

software repair, 8 

Software through Pictures, 137, 353, 395, 490, 539 

software tool. See CASE; tool 

software update, 8 

solution strategy, 361–36 

sort (in typesetting), 136 

source code, 146–147, 554 

source computer, 25 

source or destination of data (structured systems analysis), 365 

source-level debugger, 140–141 

SourceSafe, 146, 538 

Soyuz TMA-1 spaceship, 93 

space shuttle, 93 

specialization, 111, 213, 319 

specifi cation document, 7, 54, 80–81, 84, 166–167, 173, 360–361, 456–457, 490, 563 

ambiguity, 81, 362 

contradiction, 81 

correctness, 166–167, 173 

feasibility, 84 

incompleteness, 81 MSG Foundation case study, 456–457 specifi cation inspection, 393 specifi cation phase. See classical analysis phase specifi cation walkthrough, 393 SPICE. See ISO/IEC 15504 spiral model, 62–66 strengths, 64–65, 66 weaknesses, 66 spreadsheet, 138 SPSS, 227 SQA. See software quality assurance SREM, 374, 393, 395 stabilize, 62 stamp coupling, 195–196, 198 Standish Group, 4, 50, 51 stand-up meeting, 60 state (attribute value), 418 state (fi nite state machine), 377 state defi nition (Z), 388 state transition diagram (STD), 376, 379–381, 414 state variable, 418, 531 statechart, 414–417, 422, 430–432, 539, 581–583, 587 elevator problem case study, 414–417, 422 MSG Foundation case study, 430–432 statement coverage, 526–527 statistical-based testing, 533 stepwise refi nement, 44, 124–130, 201–202, 366–370, 468, 488 mini case study, 125–130 stereotype, 577–578 defi nition, 406 stories, 59 strength, 186 stress testing, 536 Stroustrup, Bjarne, 253 structural analysis, 374 structural design pattern, 245 structural testing, 517, 526 structure chart, 468 structure editor, 138–141 structured interview, defi nition, 316 structured paradigm, 501, 531. See also classical paradigm structured programming, 18, 191, 193 structured systems analysis, 18, 364 373, 404, 467, 490, 538, 633–635 

MSG Foundation case study, 372–373, 633–635 Sally’s Software Shop mini case study, 364–371 structured testing, 18, 528 stub, 510–514 defi nition, 510 subclass, 212 subsystem, 132, 486 Sun Microsystems, 252, 255 Sun ONE Studio, 141 superprogrammer, 113 superstate, 583 SW–CMM, 95–98 swimlane, defi nition, 585 synchronization, 489 synchronize, 62 synchronize-and-stabilize model, 62, 117 synchronize-and-stabilize team, 117 system, terminology, 24 System Architect, 353, 395, 413, 490 systematic reuse, 226 systematic testing, 175 systems analysis, 218 defi nition, 24 systems design, defi nition, 24 systems engineering, 135 

## T

Tacitus, Publius Cornelius, 132 target computer, 250 task, 59, 118, 283 Teal Tractors mini case study, 42–43 team, 107–120 team leader, 114–117 team manager, 114–117 team organization, 107–120 communication channels, 108 comparison, 120 managerial aspects, 108, 113–118 technical complexity factor, 274 technique, 25 technique-based environment, 538, 539, 540 technology, 184 Temperate Fruit Committee, 556–557 temporal cohesion, 189 temporal logic, 172 terminology, 23–26 test, 594 

test case, 176 successful, 175 test case selection, 517–527 test driven development, 59 test plan, 288–289, 531 test workfl ow, 44–47, 84–87, 91, 393–394, 417–424, 456, 516–528, 535–537, 540–541, 559, 564–565, 649 during analysis, 456 analysis artifacts, 84–85 during classical analysis, 393–394 design artifacts, 85 elevator problem case study, 417–424 graphical user interface (GUI), 535 during implementation, 516–528, 535–537 implementation artifacts, 85–87 during integration, 535–537 MSG Foundation case study, 456, 537, 649 during postdelivery maintenance, 559, 564–565 requirements artifacts, 84 testing, 16–17, 45, 62, 75, 84–85, 86–87, 91, 154–176, 510–514, 516–528, 530–533. See also test workfl ow classes, 530 destructiveness, 175 execution-based, 155, 162–167, 176 during implementation, 516–528 during integration, 510–514 non-execution-based, 155, 157–162 167–174 objects, 530–533 when it stops, 176 testing fault rate, 530 testing phase, 16–17 testing to code, 517, 518–520 feasibility, 518–520 reliability, 519, 520 validity, 520 testing to specifi cations, 517, 518–520 feasibility, 518–520 text-processing problem, 171–172 363–364, 391 The Cloud, 597 The New York Times , 112–113 theorem prover, 172–173 Therac-25, 3 third-generation language, 501, 539 

Three Amigos! , 77 three-tier architecture, 133, 237 time. See duration timeboxing, 60 timeout, 380 Together, 353, 459, 490, 565 token (Petri net), 384 tool, 135–137, 538. See also CASE tool integration, 538 toolkit, 233–234, 236 top-down integration, 511–512 strengths, 511–512 weaknesses, 512 Torvalds’ Truism, 24 Torvalds, Linus, 23, 24 traceability, 84, 85, 289 tracing, 140 trade-offs, 486 traditional paradigm. See classica paradigm training, 290–291 transaction, defi nition, 473 transaction analysis, 473–475, 490 transaction-driven inspection, 487 transition, 431 transition (Petri net), 383 transition (UML), 582 defi nition, 581 transition function (fi nite state machine), 377 transition phase, 89 transition rule (fi nite state machine), 377 TRW, 12 two-dimensional life-cycle model, 93–94. See also evolution-tree model; iterative-and-incremental life-cycle model typesetting, 136 

## U

U.S. Air Force, 98 UML, 76, 77–78, 212–217, 315, 405–457, 571–587 aggregation, 213 association, 214 inheritance, 213 navigation triangle, 214 not a methodology, 571–572 note, 213 unadjusted function points, 273 underscore, 18 n understanding the domain, 315–316, 320–322 MSG Foundation case study, 320–322 Unifi ed Modeling Language. See UML Unifi ed Process, 76–94, 155, 284, 314–346, 404–406, 456–457, 516, 539, 552, 553, 572, 587 analysis workfl ow, 404–406, 456–457 construction phase, 92 elaboration phase, 91–92 history, 77 implementation workfl ow, 516 inception phase, 89–91 requirements workfl ow, 314–346 unit testing, 7, 85, 92, 516, 528–529, 533, 535, 516–535 comparison, 528–529 experimentation, 528–529 statistical techniques, 533 UNIX, 49, 138, 140, 146, 147, 236, 254, 257, 258, 468, 538, 540, 565 UNIX Programmer’s Workbench, 538 unstructured interview, defi nition, 316 upperCASE tool, 135, 136, 490 upward compatibility, 256 urban myth, 229 use case, 318–319, 323, 408, 425–430, 435–452, 457, 577, 587 defi nition, 407 elevator problem case study, 408 MSG Foundation case study, 425–430, 435–452 use-case description, 323 use-case diagram, 325, 330–345, 408, 419, 429, 577, 587 elevator problem case study, 408, 419 MSG Foundation case study, 325, 330–345, 429 use-case realization, 435–452, 454 defi nition, 435 MSG Foundation case study, 435–452, 454 user, 23 user interface, 431, 457 user interface integration, 538 user-friendliness, 350–351 utility, 164 utility testing, 164, 165 

## V

V & V, 155 validation, 17, 155 variable names consistent, 504–505 meaningful, 504–505 variation, 144–145 multiple, 144–145 VAX/VMS, 257 Vegetius, 132 verifi cation, 17, 155, 167 version, 141–147, 559–560 version control, 143–147, 565 version-control tool, 143–144, 146 vertical schema defi nition, 389 videotape, 317 Vienna defi nition method (VDM), 392 virtual method, 215 Visual Basic .NET, 25 Visual C++, 138, 147 Visual Java, 147 VM/370, 257 volume testing, 536 

## W

walkthrough, 158–159, 161–162, 528–530 code, 528–530 comparison with inspection, 161–162 possible danger, 159 strength, 162 weakness. 162 WarGames , 2 waterfall life-cycle model. See waterfall model waterfall model, 7, 41, 49, 51, 41 strengths, 54 weaknesses, 54–55 weaver, 592 Web 2.0, 598 Web 3.0, 598 Web engineering, 596–597 WebSphere, 234 West Side Story , 226 white-box testing, 517 widget, 241 wiki, 596 Wikipedia, 596 Win32, 227 

Winburg mini case study, 38–42, 44, 47–48, 50 

Windows, 244, 258 

word counting mini case study, 468–472 

word processor, 138 

work package, 284 

work product, 283 

workbench, 137, 538. See also CASE worker, 457 

workfl ow, 44, 76. See also analysis workfl ow; core workfl ows; design workfl ow; implementation workfl ow; requirements workfl ow; test workfl ow 

World Wide Web, 248–249 YAGNI, 60 and reuse, 248–249 YouTube, 596 

wrapper, 235 WWMCCS, 2 

## X

X Window, 350 X11, 258 XRunner, 535 

Y2K problem, 405 

## Y

## Z

Z, 387–392 elevator problem case study, 388–390 strengths, 390–39 weaknesses, 390–391 Zermelo, Ernst Friedrich Ferdinand, 388 