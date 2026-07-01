
FIGURE 12.16 The STD for a fl oor button [Kampen 1987]. (© 1987 IEEE)


<table><tr><td rowspan="2">FBOFF (d, f)</td><td>FBP (d, f)</td></tr><tr><td>EFHAF (1..n, f)</td></tr><tr><td colspan="2">FBON (d, f)</td></tr></table>

FBP (d, f): Floor Button (d, f) Pressed 

EHAF (1. . n, f): Elevator 1 or . . . or n Has Arrived at Floor f 

(12.9) 

Note the use of 1 . . n to denote disjunction. Throughout this section an expression such as $\mathsf { P } ( \mathsf { a } , 1 \ldots \mathsf { n } , \mathsf { b } )$ denotes 

$$
P (a, 1, b) \text { or } P (a, 2, b) \text { or } \dots \text { or } P (a, n, b)\tag{12.10}
$$

To define the state transition rules connecting these events and states, a predicate again is needed. In this case, it is ${ \mathsf { S } } \left( { \mathsf { d } } , { \mathsf { e } } , { \mathsf { f } } \right)$ , which is defi ned as follows: 

S (d, e, f): Elevator e is visiting fl oor f and the direction 

in which it is about to move is either up (d  U), 

(12.11) 

down (d  D), or no requests are pending (d = N) 

This predicate actually is a state. In fact, the formalism allows both events and states to be treated as predicates. 

Using ${ \mathsf { S } } \left( { \mathsf { d } } , { \mathsf { e } } , { \mathsf { f } } \right)$ , the formal transition rules are 

FBOFF (d, f) and FBP (d, f) and not ${ \mathsf { S } } \left( { \mathsf { d } } , 1 \ldots { \mathsf { n } } , { \mathsf { f } } \right) \Rightarrow$ 

FBON (d, f), 

$$
\begin{array}{l} \text {FBON (d,f) and EHAF (1..n,f) and S (d, 1..n,f)} \Rightarrow \\ \text {FBOFF (d,f), d = U or D} \end{array}\tag{12.12}
$$

That is, if the fl oor button at fl oor f for motion in direction d is off and the button is pushed and none of the elevators currently is visiting fl oor f about to move in direction d, then the fl oor button is turned on. Conversely, if the button is on and at least one elevator has arrived at fl oor f and the elevator is about to move in direction d, then the button is turned off. The notation 1 . . n in ${ \mathsf { S } } \left( { \mathsf { d } } , 1 \ldots { \mathsf { n } } , { \mathsf { f } } \right)$ and EHAF $( 1 \ldots \mathsf { n , f } )$ was defi ned in defi nition (12.10). The predicate V (e, f) of defi nition (12.5) can be defi ned in terms of S (d, e, f) as follows: 

$$
V (e, f) = S (U, e, f) \text {or} S (D, e, f) \text {or} S (N, e, f)\tag{12.13}
$$

The states of the elevator button and fl oor button were straightforward to defi ne. Turning to the elevators, complications arise. The state of an elevator essentially con sists of a number of component substates. Kampen [1987] identifi es several, such as the elevator slowing and stopping, the door opening, the door open with a timer running, or the door closing after a timeout . He makes the reasonable assumption that the elevator controller (the mechanism that directs the motion of the elevator) initiates a state such as ${ \mathsf { S } } \left( { \mathsf { d } } , { \mathsf { e } } , { \mathsf { f } } \right)$ and that the controller then moves the elevator through the substates. Three elevator states can be defi ned, one of which, S (d, e, f), was defi ned in defi nition (12.11) but is included here for completeness. 


FIGURE 12.17 The STD for the elevator [Kampen, 1987]. (© 1987 IEEE)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/d3772f34626a67172a0ae4b0a54ee4f7391dade45dddd3303143ae3acbd7b374.jpg)


M (d, e, f): Elevator e is M oving in direction d (fl oor f is next) 

S (d, e, f): Elevator e is S topped (d-bound) at fl oor f 

(12.14) 

W (e, f): Elevator e is W aiting at fl oor f (door closed) 

These states are shown in Figure 12.17 . Note that the three stopped states S (U, e, f), S (N, e, f), and S (D, e, f) have been grouped into one larger state to simplify the diagram and to reduce the overall number of states. 

The events that can trigger state transitions are DC (e, f), the closing of the door of elevator e at fl oor f; ST (e, f), which occurs when the sensor on the elevator is triggered as it nears fl oor f and the elevator controller must decide whether to stop the elevator at that fl oor; and RL, which occurs whenever an elevator button or a fl oo button is pressed and enters its ON state: 

DC (e, f): Door Closed for elevator e, at fl oor f 

ST (e, f): Sensor Triggered as elevator e nears fl oor f 

(12.15) 

RL: Request Logged (button pressed) 

These events are indicated in Figure 12.17. 

Finally, the state transition rules for an elevator can be presented. They can be deduced from Figure 12.17 , but in some cases, additional predicates are necessary. 

To be more precise, Figure 12.17 is nondeterministic; among other reasons, the predicates are necessary to make the STD deterministic. The interested reader should consult [Kampen, 1987] for the complete set of rules; for the sake of brevity, the only rules presented here are those that declare what happens when the door closes. The elevator moves up, down, or enters a wait state, depending on the current state: 

$$
S (U, e, f) \text { and } D C (e, f) \Rightarrow M (U, e, f + 1)
$$

$$
S (D, e, f) \text { and } D C (e, f) \Rightarrow M (D, e, f - 1)
$$

$$
S (N, e, f) \text { and } D C (e, f) \Rightarrow W (e, f)\tag{12.16}
$$

The fi rst rule states that, if elevator e is in state ${ \mathsf { S } } \left( \mathsf { U } , { \mathsf { e } } , { \mathsf { f } } \right)$ , that is, stopped at fl oor f about to go up, and the doors close, then the elevator moves up toward the next fl oor. The second and third rules correspond to the cases of the elevator about to go down or with no requests pending. 

The format of these rules refl ects the power of fi nite state machines for specifying complex products. Instead of having to list a complex set of preconditions that have to hold for the product to do something and then having to list all the conditions that hold after the product has done it, the specifi cations take the simple form 

## current state and event and predicate next state

This type of specifi cation is easy to write, easy to validate, and easy to convert into a design and into code. In fact, it is straightforward to construct a CASE tool that will translate a fi nite state machine specifi cation directly into source code. Maintenance is achieved by replay. That is, if new states or events are needed, the specifi cations are modifi ed and a new version of the product is generated directly from the new specifi cations. 

The FSM approach is more precise than the graphical technique of Gane and Sarsen presented in Section 12.3.1, but it is almost as easy to understand. It has a drawback, in that for large systems, the number of ( state, event, predicate) triples can grow rapidly. Also, like Gane and Sarsen’s technique, timing considerations are not handled in Kampen’s formalism. 

These problems can be solved using statecharts, an extension of FSMs [Harel et al., 1990]. Statecharts are extremely powerful and are supported by a CASE work bench, Rhapsody. The approach has been successfully used for a number of large real-time systems. 

Another formal technique that can handle timing issues is Petri nets. 

## 12.8 Petri Nets

A major diffi culty with specifying concurrent systems is coping with timing. This diffi culty can manifest itself in many different ways, such as synchronization problems, race condi tions, and deadlock [Silberschatz, Galvin, and Gagne, 2002]. Although timing problems can arise as a consequence of a poor design or a faulty implementation, such designs and implementations often are the consequence of poor specifi cations. If specifi cations are not properly drawn up, there is a very real risk that the corresponding design and implementation will be inadequate. One powerful technique for specifying systems with potential timing problems is Petri nets. A further advantage of this technique is that it can be used for the design as well 

FIGURE 12.18 A Petri net. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/46a11bff0c5ba4de95607eb5af8f472447f142975ac237540cbedd177f1d2ffb.jpg)


Petri nets were invented by Carl Adam Petri [Petri, 1962]. Originally of interest only to automata theorists, Petri nets have found wide applicability in computer science, being used in such fi elds as performance evaluation, operating systems, and software engineering. In particular, Petri nets have proven to be useful for describing concurrent interrelated activities. But, before the use of Petri nets for specifi cations can be demonstrated, a brief introduction to Petri nets is given for those readers who may be unfamiliar with them. 

A Petri net consists of four parts: a set of places, $\mathsf { P } ;$ a set of transitions, ${ \sf T } ;$ an input function, I; and an output function, O. Consider the Petri net shown in Figure 12.18. 

The set of places, P, is $\{ { \mathsf p } _ { 1 } , { \mathsf p } _ { 2 } , { \mathsf p } _ { 3 } , { \mathsf p } _ { 4 } \}$ 

The set of transitions, T, is $\{ \mathfrak { t } _ { 1 } , \mathfrak { t } _ { 2 } \}$ 

The input functions for the two transitions, represented by the arrows from places to transitions, are 

$$
I \left(t _ {1}\right) = \left\{p _ {2}, p _ {4} \right\}
$$

$$
I \left(t _ {2}\right) = \{p _ {2} \}
$$

The output functions for the two transitions, represented by the arrows from transitions to places, are 

$$
O \left(t _ {1}\right) = \left\{p _ {1} \right\}
$$

$$
O \left(t _ {2}\right) = \left\{p _ {3}, p _ {3} \right\}
$$

Note the duplication of ${ \mathsf { p } } _ { 3 } ;$ there are two arrows from $\mathfrak { t } _ { 2 }$ to ${ \mathsf p } _ { 3 }$ . 

More formally [Peterson, 1981], a Petri net structure is a 4-tuple, ${ \mathsf C } = ( { \mathsf P } , { \mathsf T } , { \mathsf I } , { \mathsf O } )$ 

$\mathsf { P } = \{ \mathsf { p } _ { 1 } , \mathsf { p } _ { 2 } , \ldots \ldots , \mathsf { p } _ { \mathsf { n } } \}$ is a fi nite set of places , ${ \mathsf n } \geq 0$ 

$\mathsf { T } = \{ \mathrm { t } _ { 1 } , \mathrm { t } _ { 2 } , \hdots \hdots , \mathrm { t } _ { \mathrm { m } } \}$ is a fi nite set of transitions, $\mathsf m \ge 0$ , with P and T disjoint. 

$1 : \mathsf T \to \mathsf P ^ { \infty }$ is the input function , a mapping from transitions to bags of places. 

0 $) : \mathsf { T } \to \mathsf { P } ^ { \infty }$ is the output function , a mapping from transitions to bags of places. 

(A bag , or multiset , is a generalization of a set that allows for multiple instances of an element.) 


FIGURE 12.19 A marked Petri net.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/6f681c6570d0acdcbebfe12a45b75f72a553a48225f1cb319dac5d57703ade3e.jpg)



FIGURE 12.20 The Petri net of Figure 12.19 after transition $\mathrm { t } _ { 1 }$ fi res.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/0ca07b87c249206c407c199347a22ba0cef8ad121457ffdac9bb474366577ad0.jpg)


Marking a Petri net is the assignment of tokens to that Petri net. Figure 12.19 contains four tokens: one in $\mathsf { p } _ { 1 }$ , two in $\mathsf { p } _ { 2 } ,$ , none in $\mathsf { p } _ { 3 } ,$ , and one in ${ \mathsf { p } } _ { 4 }$ . The marking can be represented by the vector (1, 2, 0, 1). Transition $\mathfrak { t } _ { 1 }$ is enabled (ready to fire), because there are tokens in ${ \mathsf p } _ { 2 }$ and in $\mathsf { p } _ { 4 } ;$ in general, a transition is enabled if each of its input places has as many tokens in it as there are arcs from the place to that transition. $\mathrm { I f } \mathbf { t } _ { 1 }$ were to fi re, one token would be removed from ${ \mathsf p } _ { 2 }$ and one from $\mathsf { p } _ { 4 } ,$ , and one new token would be placed in $\mathsf { p } _ { 1 }$ . The number of tokens is not conserved—two tokens are removed, but only one new one is placed in $\mathsf { p } _ { 1 }$ In Figure 12.19 , transition $\mathfrak { t } _ { 2 }$ also is enabled, because there are tokens in ${ \mathsf p } _ { 2 }$ . If t  were to fi re, one token would be removed from $\mathsf { p } _ { 2 } ,$ , and two new tokens would be placed in ${ \mathsf p } _ { 3 }$ 

Petri nets are nondeterministic; that is, if more than one transition can fi re, then any one of them can be fi red. Figure 12.19 has marking (1, 2, 0, 1); both $\mathfrak { t } _ { 1 }$ and $\mathfrak { t } _ { 2 }$ are enabled. Suppose that $\mathfrak { t } _ { 1 }$ fi res. The resulting marking (2, 1, 0, 0) is shown in Figure 12.20 , where only $\mathfrak { t } _ { 2 }$ is enabled. It fi res, the enabling token is removed from ${ \mathsf p } _ { 2 }$ , and two new tokens are placed in ${ \mathsf p } _ { 3 }$ . The marking now is (2, 0, 2, 0), as shown in Figure 12.21. 

More formally [Peterson, 1981], a marking, M, of a Petri net $\mathsf { C } = ( \mathsf { P } , \mathsf { T } , \mathsf { I } , \mathsf { O } )$ , is a function from the set of places, P, to the set of nonnegative integers: 

$$
\mathsf {M}: \mathsf {P} \to \{0, 1, 2, \dots \}
$$

A marked Petri net then is a 5-tuple (P, T, I, O, M). 


FIGURE 12.21 The Petri net of Figure 12.20 after transition $\mathfrak { t } _ { 2 }$ fi res.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/bc098d0dd0ef8c9bc665759a32f7b5ce93eacce6e954ee88417305c90fc1e625.jpg)



FIGURE 12.22 A Petri net with an inhibitor arc.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/d96df3a0d15343c31e3800ee70e293cb7e85990690628889a1d70094ec032b0d.jpg)


An important extension to a Petri net is an inhibitor arc . In Figure 12.22 , the inhibitor arc is marked by a small circle rather than an arrowhead. Transition $\mathfrak { t } _ { 1 }$ is enabled because a token is in ${ \mathsf p } _ { 3 }$ but no token is in $\mathsf { p } _ { 2 } .$ . In general, a transition is enabled if at least one token is on each of its (normal) input arcs and no tokens are on any of its inhibitor input arcs. This extension is used in the Petri net specifi cation of the elevator problem case study of Section 12.7.1 [Guha, Lang, and Bassiouni, 1987]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/fa6a39696d2da7af7b485b88eb84679b9c5388938e42db6c2d364a297aa719bc.jpg)


## Petri Nets: The Elevator Problem Case Study12.8.1

Recall that an n elevator system is to be installed in a building with m fl oors. In this Petri net specifi cation, each fl oor in the building is represented by a place, $\mathsf { F } _ { \mathsf { f } } , 1 \leq \mathsf { f } \leq$ m, in the Petri net; an elevator is represented by a token. A token in $\mathsf { F } _ { \mathsf { f } }$ denotes that an elevator is at fl oor f. 

First Constraint 

Each elevator has a set of m buttons, one for each fl oor. These illuminate when pressed and cause the elevator to visit the corresponding fl oor. The illumination is canceled when the corresponding fl oor is visited by the elevator. 


FIGURE 12.23 A Petri net representation of an elevator button [Guha, Lang, and Bassiouni, 1987]. (© 1987 IEEE.)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/ebe38348ed4db9d2955970741aee374742cd90e4b947370df85189fa03cb1826.jpg)


To incorporate this into the specifi cation, additional places are needed. The elevator button for fl oor f is represented in the Petri net by place $\mathsf { E B } _ { \mathsf { f } } , 1 \le \mathsf { f } \le \mathsf { m }$ . More precisely, because there are n elevators, the place should be denoted $\mathsf { E B } _ { \mathsf { f } , \mathsf { e } }$ with $\rceil \leq$ $\mathsf { f } \leq \mathsf { m } , 1 \leq \mathsf { e } \leq \mathsf { n }$ . But, for the sake of simplicity of notation, the subscript e representing the elevator is suppressed. A token in $\mathsf { E B } _ { \mathsf { f } }$ denotes that the elevator button for fl oor f is illuminated. Because the button must be illuminated the fi rst time the button is pressed and subsequent button presses must be ignored, this is specifi ed using a Petri net as shown in Figure 12.23 . First, suppose that button $\mathsf { E B } _ { \mathsf { f } }$ is not illuminated. Accordingly no token is in place and, because of the presence of the inhibitor arc, transition $\mathsf { E B } _ { \mathsf { f } }$ pressed is enabled. The button now is pressed. The transition fi res and a new token is placed in $\mathsf { E B } _ { \mathsf { f } } ,$ as shown in Figure 12.23 . Now, no matter how many times the button is pressed, the combination of the inhibitor arc and the presence of the token means that transition $\mathsf { E B } _ { \mathsf { f } }$ pressed cannot be enabled. Therefore, no more than one token can ever be in place $\mathsf { E B } _ { \mathsf { f } } .$ 

Furthermore, suppose that the elevator is to travel from fl oor g to fl oor f. Because the elevator is at fl oor g, a token is in place $\mathsf { F } _ { \mathsf { g } } ,$ as shown in Figure 12.23 . Transition Elevator in action is enabled and fi res. The tokens in $\mathsf { E B } _ { \mathsf { f } }$ and $\mathsf { F } _ { \mathsf { g } }$ are removed, turning off button $\mathsf { E B } _ { \mathsf { f } } ,$ and a new token appears in $\mathsf { F } _ { \mathsf { f } } ;$ the fi ring of this transition brings the elevator from fl oor g to fl oor f. 

This motion from fl oor g to fl oor f cannot take place instantaneously. To handle this and similar issues, such as the physical impossibility for a button to illuminate at the very instant it is pressed, timing must be added to the Petri net model. That is, whereas in classical Petri net theory, transitions are instantaneous, in practical situations, such as the elevator problem case study, timed Petri nets [Coolahan and Roussopoulos, 1983] are needed to associate a nonzero time with a transition. 

## Second Constraint

Each fl oor, except the fi rst fl oor and top fl oor, has two buttons, one to request an up-elevator and one to request a down-elevator. These buttons illuminate when pressed. The illumination is canceled when an elevator visits the fl oor and then moves in the desired direction. 

The fl oor buttons are represented by places $\mathsf { F B } _ { \mathsf { f } } ^ { \mathsf { u } }$ and $\mathsf { F B } _ { \mathrm { ~ f ~ } } ^ { \mathsf { d } }$ representing the buttons for requesting up- and down-elevators, respectively. More precisely, fl oor 1 has a button $F B ^ { \boldsymbol { \mathsf { u } } } { } _ { 1 }$ , fl oor m has a button $\mathsf { F B } _ { \mathsf { m } } ^ { \mathsf { d } } ,$ and the intermediate fl oors each have two buttons, $F B _ { f } ^ { \mathrm { u } }$ and $\mathsf { F B } _ { \mathsf { f } } ^ { \mathsf { d } } , 1 < \mathsf { f } < \mathsf { m }$ . The situation when an elevator reaches fl oor f from 

FIGURE 12.24 A Petri net representation of fl oor buttons. [Guha, Lang, and Bassiouni, 1987]. (© 1987 IEEE.) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/cd7ad0f6d2cfb8a3f597df6a578e8472b59bf3a46a1b9c948c39eb91fabeda33.jpg)


fl oor g with one or both buttons illuminated is shown in Figure 12.24 . In fact, that fi gure needs further refi nement, because if both the buttons are illuminated, one is turned off on a nondeterministic basis. To ensure that the correct button is turned off requires a Petri net model too complicated to present here; see, for example, [Ghezzi and Mandrioli, 1987]. 

Third Constraint 

When an elevator has no requests, it remains at its current fl oor with its doors closed. 

This is achieved easily: If there are no requests, no Elevator in action transition is enabled. 

Not only can Petri nets be used to represent the specifi cations, they can be used for the design as well [Guha, Lang, and Bassiouni, 1987]. However, even at this stage of the devel opment of the product, it is clear that Petri nets possess the expressive power necessary for specifying the synchronization aspects of concurrent systems. 

## 12.9 Z

A formal specifi cation language gaining widely in popularity is Z [Spivey, 2001]. (For the correct pronunciation of the name Z , see Just in Case You Wanted to Know Box 12.2.) Use of Z requires knowledge of set theory, functions, and discrete mathematics, including fi rst-order logic. Even for users with the necessary background (and this includes most computer science majors), Z initially is diffi cult to learn because, in addition to the usual set theoretic and logic symbols like , , and , it uses many unusual special symbols, such as , , | , and | . 

For insight into how Z is used to specify a product, the elevator problem case study of Section 12.7.1 is considered again. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/ee7a95da0387eb56b94933ffdd8a5774123c88094536c5203049e8782451e172.jpg)


The name Z was given to the formal specifi cation language by its inventor Jean-Raymond Abrial in honor of the great set theorist Ernst Friedrich Ferdinand Zermelo (1871–1953). Because it was developed at Oxford University [Abrial, 1980], the name Z is properly pronounced “zed,” the way the British pronounce the 26th letter of the alphabet. 

Lately, however, moves are afoot to acknowledge that Z is named after a German mathematician and to pronounce it the German way, “tzet.” In response, Francophiles and Francophones point out that Abrial is a Frenchman and that the letter Z is pronounced “zed” in French, too. 

The one totally unacceptable pronunciation is the American style, that is, “zee.” The reason is that Z (pronounced “zee”) is the name of an American fourth-generation language (see Section 15.2). However, we cannot trademark a single letter of the alphabet. Furthermore, we are free to pronounce the letter Z the way we wish. Nevertheless, within the programming language context, the pronunciation “zee” refers to the 4GL, not the formal specifi cation language. 

Watch this space for the next round in the Z pronunciation wars. 

## Case Study

## Z: The Elevator Problem Case Study12.9.1

In its simplest form, a Z specifi cation consists of four sections: 

1. Given sets, data types, and constants. 

2. State defi nition. 

3. Initial state. 

4. Operations. 

Each of these sections is examined in turn. 

## 1. Given Sets

A Z specifi cation begins with a list of given sets , that is, sets that need not be defined in detail. The names of any such sets appear in brackets. For the elevator problem case study, the given set will be called Button, the set of all buttons. The Z specifi cation therefore begins 

## [Button]

## 2. State Defi nition

A Z specifi cation consists of a number of schemata (plural of schema ). Each schema consists of a group of variable declarations together with a list of predicates that constrain the possible values of the variables. The format of a schema S is shown in Figure 12.25 . 

In the elevator problem case study, there are four subsets of Button: the fl oor buttons, the elevator buttons, buttons (the set of all buttons in the elevator problem case study), and pushed (the set of those buttons that have been pushed and therefore are on). Figure 12.26 depicts the schema Button_State , a state defi nition. 

<table><tr><td>Push_Button</td></tr><tr><td>ΔButton_State</td></tr><tr><td>button?: Button</td></tr><tr><td>(button? ∈ buttons) ∧</td></tr><tr><td>(((button?∉ pushed) ∧ (pushed&#x27; = pushed ∪ {button?})) ∨</td></tr><tr><td>((button? ∈ pushed) ∧ (pushed&#x27; = pushed)))</td></tr></table>

schema S. 

floor_buttons, elevator_buttons : P Button 

floor_buttons  elevator_buttons  

floor_buttons  elevator_buttons  buttons 

The symbol P denotes the power set (the set of all subsets of a given set). The constraints, that is, the statements below the horizontal line, assert that the set of fl oor_ buttons and elevator_buttons are disjoint and that together they constitute the set of buttons. (The sets fl oor_buttons and elevator_buttons are not needed in what follows; they are included in Figure 12.26 only to demonstrate the power of Z.) 

## 3. Initial State

The abstract initial state describes the state when the system fi rst is turned on. The abstract initial state for the elevator problem case study is 

Button_Init <sup>^</sup> = [ Button_State′ | pushed′ = ∅] 

This is a vertical schema defi nition , as opposed to a horizontal schema defi - nition , such as Figure 12.26 . The vertical schema asserts that, when the elevator system is fi rst turned on, the set pushed initially is empty; that is, all the buttons are off. 

## 4. Operations

If a button is pushed for the fi rst time, then that button is turned on. The button is added to the set pushed. This is depicted in Figure 12.27 , in which operation Push_Button is defi ned. The Δ in the fi rst line of the schema denotes that this operation changes the state of Button_State . The operation has one input variable, button?. As in various other languages (such as CSP [Hoare, 1985]), the question mark (?) denotes an input variable, whereas an exclamation mark (!) denotes an output variable. 


FIGURE 12.28 A Z specifi cation of operation Floor_Arrival .


<table><tr><td colspan="2">Floor_Arrival</td></tr><tr><td colspan="2">ΔButton_State</td></tr><tr><td colspan="2">button?: Button</td></tr><tr><td colspan="2">(button? ∈ buttons) ∧</td></tr><tr><td colspan="2">((button? ∈ pushed) ∧ (pushed&#x27; = pushed \ {button?})) ∨</td></tr><tr><td colspan="2">((button?∉ pushed) ∧ (pushed&#x27; = pushed)))</td></tr></table>

The predicate part of an operation consists of a group of preconditions that must hold before the operation is invoked and postconditions that must hold after the operation has completed execution. Provided the preconditions are met, the postconditions hold after completing execution. However, if the operation is invoked without the preconditions being satisfi ed, unspecifi ed (and therefore unpredictable) results occur. 

The fi rst precondition of Figure 12.27 states that button? must be a member of buttons, the set of all buttons in this elevator system. If the second precondition, button? ∉ pushed, is met (that is, if the button is not on), then the set of pushed buttons is updated to include button?. In Z, the new value of a variable is denoted by a prime (′). Therefore, the postcondition says that, after operation Push_Button has been performed, button? must be added to the set pushed. There is no need to turn on the button explicitly; it is suffi cient that button? is now an element of pushed. 

The other possibility is that an already pushed button is pushed again. Because button? pushed, the third precondition holds <sup>1</sup> and, as required, nothing happens. This is indicated by the statement pushed′  pushed; the new state of pushed i the same as the old state. 

Now, suppose an elevator arrives at a fl oor. If the corresponding fl oor button is on, then it must be turned off, and similarly for the corresponding elevator button. That is, if button? is an element of pushed, then it must be removed from the set, as shown in Figure 12.28 . (The symbol \ denotes set difference.) However, if a button is not on, then set pushed is unchanged. 

The solution presented in this section is an oversimplifi cation in that it does not distinguish between up and down fl oor buttons. Nevertheless, it gives an indication how Z can be used to specify the behavior of the buttons in the elevator problem case study. 

## 12.9.2 Analysis of Z

Z has been used successfully in a wide variety of projects, including CASE tools [Hall, 1990], a real-time kernel [Spivey, 1990], and an oscilloscope [Delisle and Garlan, 1990]. 

Z has also been used to specify large portions of a release of CICS, the IBM transaction processing system [Nix and Collins, 1988]. 

These successes perhaps are somewhat surprising, in view of the fact that, even for the simplifi ed version of the elevator problem case study, it is clear that Z is not straightforward to use. First is the problem caused by the notation; a new user has to learn the set of symbols and their meanings before being able to read Z specifi cations, let alone write them. Second, not every software engineer has the required training in mathematics to be able to use Z (although recent graduates of almost all computer science programs either know enough mathematics to use Z or could learn what they still need to know with little diffi culty). 

Z perhaps is the most widely used formal language of its type. Why is this, and why has Z been so successful, especially on large-scale projects? A number of different reasons have been put forward: 

• It has been found that it is easy to find faults in specifi cations written in Z, especially during inspections of the specifi cations themselves and inspections of designs or code against the formal specifi cations [Nix and Collins, 1988; Hall, 1990]. 

• Writing Z specifications requires the specifi er to be extremely precise; as a result of this need for exactness, there appear to be fewer ambiguities, contradictions, and omissions than with informal specifi cations. 

• As a formal language, Z allows developers to prove specifi cations correct when necessary. Accordingly, although some organizations rarely do any correctness proving of Z, such proofs have been done, even for such practical specifi cations as the CICS storage manager [Woodcock, 1989]. 

• It has been suggested that software professionals with only high-school mathematics can be taught to write Z specifi cations in a relatively short period of time [Hall, 1990]. Clearly such individuals cannot prove the resulting specifi cations to be correct, but then formal specifi cations do not necessarily have to be proven to be correct. 

• The use of Z has decreased the cost of software development. No doubt more time has to be spent on the specifications themselves than when informal techniques are used, but the overall time for the complete development process is decreased. 

• The problem that the client cannot understand specifi cations written in Z has been solved in a number of ways, including rewriting the specifi cations in natural language. The resulting natural language specifi cations have been found to be clearer than informal specifi cations constructed from scratch. (This also was the experience with Meyer’s English paraphrase of his formal specifi cation for Naur’s text-processing problem, described in Section 12.2.1.) 

The bottom line is that, notwithstanding the arguments to the contrary, Z has been successfully used in the software industry for a number of large-scale projects. Although the vast majority of specifi cations continue to be written in languages considerably less formal than Z, there is a growing global trend toward the use of formal specifi cations. The use of such formal specifi cations traditionally has been largely a European practice. However, more and more organizations in the United States are employing formal specifi cations of one sort or another. The extent to which Z and similar languages will be used in the future remains to be seen. 

## 12.10 Other Formal Techniques

Many other formal techniques have been proposed. These techniques are extremely varied. For example, Anna [Luckham and von Henke, 1985] is a formal specifi cation language for Ada. Some formal techniques are knowledge based, such as Gist [Balzer, 1985]. Gist was designed so users could describe processes in a way as close as possible to the way we think about processes. This was to be achieved by formalizing the constructs used in natural languages. In practice, Gist specifi cations are as hard to read as most other formal specifi cations, so much so that a paraphraser from Gist to English has been implemented. 

Vienna defi nition method (VDM) [Jones, 1986b] is a technique based on denotational semantics [Gordon, 1979]. The VDM can be applied, not just to the specifi cations, but also to the design and implementation. The VDM has been used successfully in a number of projects, most spectacularly in the Dansk Datamatik Center development of the DDC Ada Compiler System [Oest, 1986]. 

A different way of looking at specifi cations is to view them in terms of sequences of events, where an event is either a simple action or a communication that transfers data into or out of the system. For example, in the elevator problem case study, one event consists of pushing the elevator button for fl oor f on elevator e and its resulting illumination. Another event is elevator e leaving fl oor f in a downward direction and canceling the illumination of the corresponding fl oor button. The language Communicating Sequential Processes (CSP), invented by Hoare [1985], is based on the idea of describing the behavior of a system in terms of such events. In CSP, a process is described in terms of the sequences of events in which the process engages with its environment. Processes interact with each other by sending messages to one another. CSP allows processes to be combined in a wide variety of ways, such as sequentially, in parallel, or interleaved nondeterministically. 

The power of CSP lies in the executable nature of CSP specifi cations [Delisle and Schwartz, 1987]; as a result, they can be checked for internal consistency. In addition, CSP provides a framework for going from specifi cations to design to implementation in a sequence of steps that preserve validity. In other words, if the specifi cations are correct and the transformations are performed correctly, then the design and implementation are correct as well. Going from design to implementation is particularly straightforward if the implementation language is Ada. 

However, CSP also has its weaknesses. In particular, like Z, it is not an easy language to learn. An attempt was made to include a CSP specifi cation for the elevator problem case study [Schwartz and Delisle, 1987] in this book. But the quantity of essential preliminary material and the level of detail of explanation needed to describe each CSP statement adequately were simply too great to permit inclusion in a book as general as this one. The relationship between the power of a specifi cation language and its diffi culty of use is expanded in Section 12.11. 

## 12.11 Comparison of Classical Analysis Techniques

The main lesson of this chapter is that every development organization has to decide what type of specifi cation language is appropriate for the product about to be developed. An informal technique is easy to learn but lacks the power of a semiformal or formal technique. 

Conversely, each formal technique supports a variety of features that may include executability, correctness proving, or transformability to design and implementation through a series of correctness-preserving steps. Although generally the more formal the technique, the greater its power, formal techniques can be diffi cult to learn and use. Also, a formal specifi cation can be diffi cult for the client to understand. In other words, there is a trade-off between ease of use and the power of a specifi cation language. 

In some circumstances, the choice of specifi cation language type is easy. For example, if the vast majority of the members of the development team have no training in computer science, then it is virtually impossible to use anything other than an informal or semiformal specifi ca tion technique. Conversely, where a mission-critical real-time system is being built in a research laboratory, the power of a formal specifi cation technique almost certainly is required. 

An additional complicating factor is that many of the newer formal techniques have not been tested under practical conditions. Considerable risk is involved in using such a technique. Large sums of money are needed to pay for training the relevant members of the development team, and more money will be spent while the team adjusts from using the language in the classroom to using it on the actual project. Furthermore, the language’s supporting software tools might not work properly, as happened with SREM [Scheffer, Stone, and Rzepka, 1985], resulting in additional expense and time slippage. But, if everything works and the software project management plan takes into account the additional time and money needed when a new technology is used on a nontrivial project for the fi rst time, huge gains are possible. 

Which analysis technique should be used for a specifi c project? It depends on the project, the development team, the management team, and myriad other factors, such as the client insisting that a specifi c method be used (or not used). As with so many other aspects of software engineering, trade-offs have to be made. Unfortunately, there is no simple rule for deciding which analysis technique to use. 

Figure 12.29 is a summary of the ideas of this section. 

## 12.12 Testing during Classical Analysis

During classical analysis, the functionality of the proposed product is expressed precisely in the specifi cation document. It is vital to verify that the specifi cation document is correct. One way to do this is by means of a walkthrough of the document (Section 6.2.1). 

A more powerful mechanism for detecting faults in specifi cation documents is an inspection (Section 6.2.3). A team of inspectors reviews the specifi cations against a checklist. Typical items on a specifi cation inspection checklist are these: Have the required hardware resources been specifi ed? Have the acceptance criteria been specifi ed? 

Inspections were suggested fi rst by Fagan [1976] in the context of testing the design and the code. Fagan’s work is described in detail in Section 6.2.3. However, inspections also have proven to be of considerable use in testing specifi cations. For example, Doolan [1992] used inspections to validate the specifi cations of a product that, when built, consisted of over 2 million lines of Fortran. From data on the cost of fi xing faults in the product, he could deduce that each hour invested in inspections saved 30 hours of execution-based fault detection and correction 

When a specifi cation has been drawn up using a formal technique, other testing techniques can be applied. For example, correctness-proving methods (Section 6.5) can be employed. Even if formal proofs are not performed, informal proof techniques such as 

FIGURE 12.29 A summary of the classical analysis methods discussed in this chapter and the section in which each is described. 

<table><tr><td>Classical Analysis Method</td><td>Category</td><td>Strengths</td><td>Weaknesses</td></tr><tr><td>Natural language (Section 12.2)</td><td>Informal</td><td>Easy to learnEasy to useEasy for the client to understand</td><td>ImpreciseSpecifications can be ambiguous, contradictory, or incomplete</td></tr><tr><td>Entity-relationship modeling (Section 12.6)PSL/PSA (Section 12.5)SADT (Section 12.5)SREM (Section 12.5)Structured systems analysis (Section 12.3)</td><td>Semiformal</td><td>Can be understood by the clientMore precise than informal techniques</td><td>Not as precise as formal techniquesGenerally cannot handle timing</td></tr><tr><td>Anna (Section 12.10)CSP (Section 12.10)Extended finite state machines (Section 12.7)Gist (Section 12.10)Petri nets (Section 12.8)VDM (Section 12.10)Z (Section 12.9)</td><td>Formal</td><td>Extremely preciseCan reduce analysis faultsCan reduce development cost and effortCan support correctness proving</td><td>Hard for the development team to learnHard to useAlmost impossible for most clients to understand</td></tr></table>

those used in Section 6.5.1 can be an extremely useful way of highlighting specifi cation faults. In fact, the product and its proof should be developed in parallel. In this way, faults are detected quickly. 

## 12.13 CASE Tools for Classical Analysis

Two classes of CASE tools are particularly helpful during classical analysis. The fi rst is a graphical tool. Whether a product is represented using data fl ow diagrams, Petri nets, entity-relationship diagrams, or any of the many other representations omitted from this book simply for reasons of space, drawing the entire product by hand is a lengthy process. In addition, making substantial changes can result in having to redraw everything from scratch. A drawing tool therefore is a great time saver. Tools of this type exist for the analysis techniques described in this chapter, as well as many other graphical representations for specifi cations. A second tool needed during this phase is a data dictionary. As described in Section 5.7 and summarized in Section 10.8, this tool stores the name and representation (format) of every component of every data item in the product, including data fl ows and their components, data stores and their components, and processes (operations) and their internal variables. ( Figure 12.5 shows typical information that would be stored in a data dictionary for Sally’s Software Shop.) Again, a wide selection of data dictionaries run on a variety of hardware–operating system combinations. 

What really is needed is not a separate graphical tool and a separate data dictionary. Instead, the two tools should be integrated, so that any change made to a data component is refl ected automatically in the corresponding part of the specifi cation document. Among the many examples of this type of tool are Analyst/Designer, Software through Pictures, and System Architect. Furthermore, many such tools also incorporate an automatic consistency checker that ensures consistency between the specifi cation document and the corresponding design document. For example, it is possible to check that every item in the specifi cation document is carried forward to the design document and that everything mentioned in the design has been declared in the data dictionary. 

An analysis technique is unlikely to receive widespread acceptance unless a tool-rich CASE environment supports that technique. For example, SREM (Section 12.5) probably would be used far more widely today had REVS, its associated CASE tool set, performed better in the U.S. Air Force tests [Scheffer, Stone, and Rzepka, 1985]. It is not easy to specify a system correctly, even for experienced software professionals. It is only reasonable to provide specifi ers with a set of state-of-the-art CASE tools to assist them in every way possible. 

## 12.14 Metrics for Classical Analysis

As in all other phases, during classical analysis it is necessary to measure the fi ve fundamental metrics: size, cost, duration, effort, and quality. One measure of the size of a specifi cation is the number of pages in the specifi cation document. If the same technique is used to specify a number of similar products, then differences in specifi cation size may be signifi cant predictors of the effort needed to build the various products. 

Turning to quality, a vital aspect of specifi cation inspections is the record of fault statistics. Noting the number of faults of each type found during an inspection is an integral part of the inspection process. Also, the rate at which faults are detected can give a measure of the effi ciency of the inspection process. 

Metrics for predicting the size of the target product include the number of items in the data dictionary. Several different counts should be taken, including the number of fi les, data items, and processes (operations). This information can give management a preliminary estimate regarding the effort required to build the product. It is important to note that this information is tentative at best. After all, during the classical design phase, a process in a DFD may be broken down into a number of different modules. Conversely, a number of processes together may constitute a single module. Nevertheless, metrics derived from the data dictionary can give management an early clue as to the eventual size of the target product. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/8bfd1dea2b0737509efa27ac75a17d977efec76c63fd252cb30d04bc1c3183df.jpg)


## 12.15 Software Project Management Plan: The MSG Foundation Case Study

Now that the specifi cations are complete, the software project management plan (SPMP) is drawn up, including estimates of cost and duration (see Chapter 9 ). Appendix F contains a software project management plan for development of the MSG Foundation product by a small (three-person) software organization. This plan fi ts the IEEE SPMP format (Section 9.5). 

## 12.16 Challenges of Classical Analysis

A repeated theme of this chapter is that a specifi cation document must be simultaneously informal enough for the client to understand and formal enough for the development team to use as the sole description of the product to be built. A major challenge of classical analysis is to resolve this contradiction. There are no easy answers. On the contrary, a permanent confl ict lies between the two competing objectives, and the development team must simply do its best to steer safely between Scylla and Charybdis. 

A second challenge of classical analysis is that the boundary line between analysis (what) and design (how) is all too easy to cross. The specifi cation document should describe what the product must do; it must never say how the product is to do it. For example, suppose that the client requires a response time of no more than 0.05 seconds whenever a certain network routing computation is performed. The specifi cation document should state exactly this—and nothing more. In particular, the specifi cation document should not state which algorithm must be used to achieve this response time. That is, a specifi cation document has to list all constraints, but it must never state how those constraints are to be achieved. 

Another example of this potential pitfall arises from data fl ow diagrams (Section 12.3.1). A box with rounded ends denotes a process; it does not denote a module. As explained in Section 12.14, a process in a DFD may be broken down into a number of different modules and, conversely, a number of processes may be combined into a single module. The key point is that this refi nement of processes into modules must take place during the classical design phase, not the classical analysis phase. The specifi cation document has to describe the operations of the target process. It must never specify how those operations are to be implemented, not even the modules to which each is assigned. The design team’s task is to study the specifi cations as a whole and decide on a design that will result in an optimal implementation of those specifi cations; this is described in Chapter 14 . Until the product as a whole has been decomposed into modules, it is premature to try to assign operations to specifi c modules; the result is almost certain to be suboptimal. 

## Chapter Review

Specifi cations (Section 12.1) can be expressed informally (Section 12.2), semiformally (Sections 12.3 through 12.5), or formally (Sections 12.6 through 12.10). 

The major theme of this chapter is that informal techniques are easy to use but imprecise; this is demonstrated by a mini case study (Section 12.2.1). Conversely, formal techniques are powerful but require a nontrivial investment in training time (Section 12.11). One semiformal technique, Gane and Sarsen’s structured systems analysis, is described in some detail (Section 12.3), followed by its application to the MSG Foundation case study (Section 12.4). Other semiformal techniques are then described (Section 12.5), including entity-relationship modeling (Section 12.6). Formal techniques presented in this chapter include fi nite state machines (Section 12.7), Petri nets (Section 12.8), and Z (Section 12.9). Other formal techniques are outlined in Section 12.10. Material on specifi cation reviews appears in Section 12.12. Next follows a description of CASE tools (Section 12.13) and metrics (Section 12.14) for classical analysis. The software project management plan for the MSG Foundation case study (Section 12.15) is presented next. The chapter ends with a discussion of the challenges of classical analysis (Section 12.16). 

An overview of the MSG Foundation case study for Chapter 12 appears in Figure 12.30 , and for the elevator problem in Figure 12.31. 

<table><tr><td>Structured systems analysis</td><td>Section 12.4, Appendix D</td></tr><tr><td>Data flow diagram</td><td>Figure 12.9</td></tr><tr><td>Software project management plan</td><td>Section 12.15, Appendix F</td></tr></table>

<table><tr><td>Requirements</td><td>Section 12.7.1</td></tr><tr><td>Finite state machine analysis</td><td>Section 12.7.1</td></tr><tr><td>Petri net analysis</td><td>Section 12.8.1</td></tr><tr><td>Z analysis</td><td>Section 12.9.1</td></tr></table>

## For Further Reading

The classic texts on structured systems analysis are the books by DeMarco [1978], Gane and Sarsen [1979], and Yourdon and Constantine [1979]. These ideas have been updated in [Modell, 1996]. SADT is described in [Ross, 1985], and PSL/PSA is described in [Teichroew and Hershey, 1977]. Two sources of information on SREM are [Alford, 1985] and [Scheffer, Stone, and Rzepka, 1985]. 

Six formal techniques are described in [Wing, 1990]. An outstanding collection of papers on formal techniques can be found in the September 1990 issues of IEEE Transactions on Software Engineering, IEEE Computer , IEEE Software, and ACM SIGSOFT Software Engineering Notes . Of particular interest is [Hall, 1990]; the paper should be read in its entirety. [Bowen and Hinchey, 1995b] is a sequel to Hall’s seminal article, and [Bowen and Hinchey, 1995a] is a list of guidelines for use of formal techniques. Additional articles on formal techniques can be found in the August 2000 issue of IEEE Transactions on Software Engineering . An empirical study comparing different types of formal techniques is presented in [Sobel and Clarkson, 2002]. Haxthausen and Peleska [2000] have applied formal verifi cation to a distributed railway control system. Palshikar [2001] describes the practical use of formal specifi cations in real-world software development. Hall and Chapman [2002] describe the construction of a commercial secure system using formal techniques. Three dif ferent attitudes to formal methods appear in [Hinchey et al., 2008]. 

An early reference to the fi nite state machine approach is [Naur, 1964], where unfortunately it is referred to as the Turing machine approach . Statecharts are a powerful extension of FSMs; they are described in [Harel et al., 1990]. Object-oriented extensions of statecharts appear in [Harel and Gery, 1997]. 

[Peterson, 1981] is an excellent introduction to Petri nets and their applications. The use of Petri nets in prototyping is described in [Bruno and Marchetto, 1986]. Timed Petri nets are described in [Coolahan and Roussopoulos, 1983]. 

With regard to Z, [Diller, 1994] is a good introductory text. For the reference manual with full details about the specifi cation language, see [Spivey, 2001]. Using the results of an experiment in reading Z specifi cations, Finney [1996] questions whether Z specifi cations are as easy to read as has been claimed by some Z proponents. 

The proceedings of the International Workshops on Software Specifi cation and Design are a preeminent source for research ideas regarding specifi cations. 

## Key Terms

abstract initial state 389 Anna 392 bag 383 Communicating Sequential Processes (CSP) 392 constraint 360 data fl ow 365 data fl ow diagram (DFD) 365 data immediate-access diagram (DIAD) 370 data store 365 enable 384 entity-relationship modeling (ERM) 374 event 377 extended fi nite state machine 378 fi nal state 377 fi nite state machine (FSM) 376 formal specifi cation 376 Gist 392 given set 388 

horizontal schema defi nition 389 informal specifi cation 362 inhibitor arc 385 initial state 377 input 377 input function 383 logical data fl ow 365 marked Petri net 384 marking 384 multiset 383 natural language 362 operation 390 output function 383 Petri net 383 place 383 predicate 377 process 365 PSL/PSA 373 SADT 374 schema 388 semiformal specifi cation 373 solution strategy 361 source or destination of data 365 specifi cation document 360 SREM 374 state 377 state defi nition 388 state transition diagram (STD) 376 structural analysis (SA) 374 structured systems analysis 365 token 384 transition 383 transition function 377 transition rule 377 vertical schema defi nition 389 Vienna defi nition method (VDM) 392 

Case Study button 378 elevator button 378 illumination 379 Key Terms door 381 elevator controller 380 timeout 380 elevator 378 fl oor button 378 

## Problems

12.1 Why should the following constraints not appear in a specifi cation document? 

(i) The product must signifi cantly reduce transportation expenses that arise from distributing our beer in central Queensland. 

(ii) The credit card database must be set up at a reasonable cost. 

12.2 Why is it so important that the specifi cation document should have no omissions, contradictions, or ambiguities? 

12.3 Consider the following recipe for grilled pockwester. Ingredients: 

1 large onion 2 medium-sized eggplants 

${ } ^ { 1 } / _ { 2 }$ cup Pouilly Fuissé 

1 garlic 

Milk 4 free-range eggs 

3 medium-sized shallots 

The night before, take one lemon, squeeze it, strain the juice, and freeze it. Take one large onion and three shallots, dice them, and grill them in a skillet. When clouds of black smoke start to come off, add 2 cups of fresh orange juice. Stir vigorously. Slice the lemon into paper-thin slices and add to the mixture. In the meantime, coat the mushrooms in fl our, dip them in milk, and then shake them in a paper bag with the bread crumbs. In a saucepan, heat 1/2 cup of Pouilly Fuissé. When it reaches 170°, add the sugar and continue to heat. When the sugar has caramelized, add the mushrooms. Blend the mixture for 10 minutes or until all lumps have been removed. Add the eggs. Now take the pockwester, and kill it by sprinkling it with frobs. Skin the pockwester, break it into bite-sized chunks, and add it to the mixture. Bring to a boil and simmer, uncovered. The eggs previously should have been vigorously stirred with a wire whisk for 5 minutes. When the pockwester is soft to the touch, place it on a serving platter, sprinkle with Parmesan cheese, and broil for not more than 4 minutes. 

Determine the ambiguities, omissions, and contradictions in the preceding specifi cation. (For the record, a pockwester is an imaginary sort of fi sh and frobs is slang for generic hors d’oeuvres.) 

12.4 Correct the specifi cation paragraph of Section 12.2 to refl ect the client’s wishes more accurately. 

12.5 Use mathematical formulas to represent the specifi cation paragraph of Section 12.2. Compare your answer with your answer to Problem 12.4. 

12.6 What are the strengths of informal specifi cations? 

12.7 What are the weaknesses of informal specifi cations? 

12.8 Write a precise English specifi cation for the product to determine whether a bank statement is correct (Problem 8.8). 

12.9 Draw a data fl ow diagram for the specifi cation you drew up for Problem 12.8. Ensure that your DFD simply refl ects the fl ow of data and that no assumptions regarding computerization have been made. 

12.10 Consider the automated library circulation system of Problem 8.7. Write down precise specifi cations for the library circulation system. 

12.11 Draw a data fl ow diagram showing the operation of the library circulation system of Problem 8.7. 

12.12 Complete the specifi cation document for the library circulation system of Problem 8.7 using Gane and Sarsen’s technique. Where data have not been specifi ed (for example, the total number of books checked in and out each day), make your own assumptions, but make sure that they are indicated clearly. 

12.13 A fi xed-point binary number consists of an optional sign followed by one or more bits, followed by a binary point, followed by one or more bits. Examples of fi xed-point binary numbers include 

11010.1010, 0.000001, and 1101101.0 

More formally, this can be expressed as 

<sign> 

<bitstring> 

<binary point> 

<bit> 

(The notation [ . . . ] denotes an optional item, and a | b denotes a or b.) 

Specify a fi nite state machine that will take as input a string of characters and determine whether or not that string constitutes a valid fi xed-point binary number. 

12.14 A fl oating-point binary number consists of an optional sign followed by one or more bits, followed by the letter E, followed by another optional sign, followed by one or more bits. Examples of fl oating-point binary numbers include 11010E–1010, –100101E11101, and +1E0. 

More formally, this can be expressed as 

<fl oating-point binary> :: [<sign>] <bitstring> E [<sign>] <bitstring> <sign> ::  |  <bitstring> :: <bit> [<bitstring>] <bit> :: 0 | 1 

(The notation [. . .] denotes an optional item, and a | b denotes a or b.) 

Specify a fi nite state machine that will take as input a string of characters and determine whether that string constitutes a valid fl oating-point binary number. 

12.15 Use the fi nite state machine approach to specify the library circulation system of Problem 8.7. 

12.16 Show how your solution to Problem 12.15 can be used to design and implement a menu-driven product for the library circulation system (Problem 8.7). 

12.17 Use a Petri net to specify the circulation of a single book through the library of Problem 8.7. Include operations H , C , and R in your specifi cation. 

12.18 You are a software engineer working for a large company that specializes in computerizing library systems. Your manager asks you to specify the complete library circulation system of Problem 8.7 using Z. What is your reaction? 

12.19 Why are many software organizations reluctant to use formal specifi cations? 

12.20 (Term Project) Using the technique specifi ed by your instructor, draw up a specifi cation document for the Chocoholics Anonymous product described in Appendix A. 

12.21 (Term Project) Draw up a software project management plan for the Chocoholics Anonymous product described in Appendix A. 

12.22 (Case Study) Draw up the requirements of the MSG Foundation product using the fi nite state machine approach. 

12.23 (Case Study) Use the Petri net technique to specify the states through which a married couple in the MSG Foundation product passes. 

12.24 (Case Study) Specify a portion of the MSG Foundation product using the Z constructs of Section 12.9. 

12.25 (Case Study) The software project management plan of Section 12.15 is for a small software engineering organization consisting of three software engineers. Modify the plan so that it is appropriate for a medium-sized organization with over 1000 software engineers. 

12.26 (Case Study) In what way would the software project management plan of Section 12.15 have to be modifi ed if the MSG Foundation product had to be completed in only 8 weeks? 

12.27 (Readings in Software Engineering) Your instructor will distribute copies of [Hinchey et al., 2008]. For each of the three principal co-authors (Jackson, Cousot, and Cook), state whether or not you agree with their views, giving careful reasons for your answers. 

## References



[Abrial, 1980] J.-R. ABRIAL , “The Specifi cation Language Z: Syntax and Semantics,” Oxford University Computing Laboratory, Programming Research Group, Oxford, UK, April 1980. 





[Alford, 1985] M. ALFORD , “SREM at the Age of Eight; The Distributed Computing Design System,” IEEE Computer 18 (April 1985), pp. 36–46. 





[Balzer, 1985] R. BALZER , “A 15 Year Perspective on Automatic Programming,” IEEE Transactions on Software Engineering SE-11 (November 1985), pp. 1257–68. 





[Banks, Carson, Nelson, and Nichol, 2010] J. BANKS , J. S. CARSON , B. L. NELSON, AND D. M. NICHOL , Discrete-Event System Simulation, 5th ed., Prentice Hall, Upper Saddle River, NJ, 2010. 





[Bowen and Hinchey, 1995a] J. P. BOWEN AND M. G. HINCHEY , “Ten Commandments of Formal Methods,” IEEE Computer 28 (April 1995), pp. 56–63. 





[Bowen and Hinchey, 1995b] J. P. BOWEN AND M. G. HINCHEY , “Seven More Myths of Formal Methods,” IEEE Software 12 (July 1995), pp. 34–41. 





[Brady, 1977] J. M. BRADY , The Theory of Computer Science , Chapman and Hall, London, 1977. 





[Bruno and Marchetto, 1986] G. BRUNO AND G. MARCHETTO , “Process-Translatable Petri Nets for the Rapid Prototyping of Process Control Systems,” IEEE Transactions on Software Engineering SE-12 (February 1986), pp. 346–57. 





[Chen, 1976] P. CHEN , “The Entity-Relationship Model—Towards a Unifi ed View of Data,” ACM Transactions on Database Systems 1 (March 1976), pp. 9–36. 





[Coolahan and Roussopoulos, 1983] J. E. COOLAHAN, JR., AND N. ROUSSOPOULOS , “Timing Requirements for Time-Driven Systems Using Augmented Petri Nets,” IEEE Transactions on Software Engineering SE-9 (September 1983), pp. 603–16. 





[Dart, Ellison, Feiler, and Habermann, 1987] S. A. DART , R. J. ELLISON , P. H. FEILER, AND A. N. HABERMANN , “Software Development Environments,” IEEE Computer 20 (November 1987), pp. 18–28. 





[Delisle and Garlan, 1990] N. DELISLE AND D. GARLAN , “A Formal Description of an Oscilloscope,” IEEE Software 7 (September 1990), pp. 29–36. 





[Delisle and Schwartz, 1987] N. DELISLE AND M. SCHWARTZ , “A Programming Environment for CSP,” Proceedings of the Second ACM SIGSOFT/SIGPLAN Software Engineering Symposium on Practical Software Development Environments, ACM SIGPLAN Notices 22 (January 1987), pp. 34–41. 





[DeMarco, 1978] T. DEMARCO , Structured Analysis and System Specifi cation , Yourdon Press, New York, 1978. 





[Diller, 1994] A. DILLER , Z: An Introduction to Formal Methods , 2nd ed., John Wiley and Sons, Chichester, UK, 1994. 





[Doolan, 1992] E. P. DOOLAN , “Experience with Fagan’s Inspection Method,” Software—Practice and Experience 22 (February 1992), pp. 173–82. 





[Fagan, 1976] M. E. FAGAN , “Design and Code Inspections to Reduce Errors in Program Development,” IBM Systems Journal 15 (No. 3, 1976), pp. 182–211. 





[Finney, 1996] K. FINNEY , “Mathematical Notation in Formal Specifi cation: Too Diffi cult for the Masses?” IEEE Transactions on Software Engineering 22 (1996), pp. 158–59. 





[Gane and Sarsen, 1979] C. GANE AND T. SARSEN , Structured Systems Analysis: Tools and Techniques , Prentice Hall, Englewood Cliffs, NJ, 1979. 





[Ghezzi and Mandrioli, 1987] C. GHEZZI AND D. MANDRIOLI , “On Eclecticism in Specifi cations: A Case Study Centered around Petri Nets,” Proceedings of the Fourth International Workshop on Software Specifi cation and Design , Monterey, CA, IEEE, 1987, pp. 216–24. 





[Goodenough and Gerhart, 1975] J. B. GOODENOUGH AND S. L. GERHART , “Toward a Theory of Test Data Selection,” Proceedings of the Third International Conference on Reliable Software , Los Angeles, IEEE, 1975, pp. 493–510; also published in: IEEE Transactions on Software Engineering SE-1 ( June 1975), pp. 156–73. Revised version: J. B. Goodenough, and S. L. Gerhart, “Toward a Theory of Test Data Selection: Data Selection Criteria,” in: Current Trends in Programming Methodology, Vol. 2, R. T. Yeh (Editor), Prentice Hall, Englewood Cliffs, NJ, 1977, pp. 44–79. 





[Gordon, 1979] M. J. C. GORDON , The Denotational Description of Programming Languages: An Introduction , Springer-Verlag, New York, 1979. 





[Guha, Lang, and Bassiouni, 1987] R. K. GUHA , S. D. LANG, AND M. BASSIOUNI , “Software Specifi cation and Design Using Petri Nets,” Proceedings of the Fourth International Workshop on Software Specifi cation and Design , Monterey, CA, IEEE, April 1987, pp. 225–30. 





[Hall, 1990] A. HALL , “Seven Myths of Formal Methods,” IEEE Software 7 (September 1990), pp. 11–19. 





[Hall and Chapman, 2002] A. HALL AND R. CHAPMAN , “Correctness by Construction: Developing a Commercial Secure System,” IEEE Software 19 (January–February 2002), pp. 18–25. 





[Harel and Gery, 1997] D. HAREL AND E. GERY , “Executable Object Modeling with Statecharts,” IEEE Computer 30 (July 1997), pp. 31–42. 





[Harel et al., 1990] D. HAREL , H. LACHOVER , A. NAAMAD , A. PNUELI , M. POLITI , R. SHERMAN , A. SHTULL-TRAURING, AND M. TRAKHTENBROT , “STATEMATE: A Working Environment for the Development of Complex Reactive Systems,” IEEE Transactions on Software Engineering 16 (April 1990), pp. 403–14. 





[Haxthausen and Peleska, 2000] A. E. HAXTHAUSEN AND J. PELESKA , “Formal Development and Verifi cation of a Distributed Railway Control System,” IEEE Transactions on Software Engineering 26 ( August 2000), pp. 687–701. 





[Hinchey et al., 2008] M. HINCHEY , M. JACKSON , P. COUSOT , B. COOK , J. P. BOWEN, AND T. MARGARIA , “Software Engineering and Formal Methods,” Communications of the ACM 51 (September 2008), pp. 54–59. 





[Hoare, 1985] C. A. R. HOARE , Communicating Sequential Processes , Prentice Hall International, Englewood Cliffs, NJ, 1985. 





[IWSSD, 1986] Call for Papers, Fourth International Workshop on Software Specifi cation and Design, ACM SIGSOFT Software Engineering Notes 11 ( April 1986), pp. 94–96. 





[Jones, 1986b] C. B. JONES , Systematic Software Development Using VDM , Prentice Hall, Englewood Cliffs, NJ, 1986. 





[Kampen, 1987] G. R. KAMPEN , “An Eclectic Approach to Specifi cation,” Proceedings of the Fourth International Workshop on Software Specifi cation and Design , Monterey, CA, April 1987, pp. 178–82. 





[Kleinrock and Gail, 1996] L. KLEINROCK AND R. GAIL , Queuing Systems: Problems and Solutions , John Wiley and Sons, New York, 1996. 





[Knuth, 1968] D. E. KNUTH , The Art of Computer Programming, Vol. I , Fundamental Algorithms , Addison-Wesley, Reading, MA, 1968. 





[Leavenworth, 1970] B. LEAVENWORTH , Review #19420, Computing Reviews 11 ( July 1970), pp. 396–97. 





[London, 1971] R. L. LONDON , “Software Reliability through Proving Programs Correct,” Proceedings of the IEEE International Symposium on Fault-Tolerant Computing, Pasadena, CA, March 1971. 





[Luckham and von Henke, 1985] D. C. LUCKHAM AND F. W. VON HENKE , “An Overview of Anna, a Specifi cation Language for Ada,” IEEE Software 2 (March 1985), pp. 9–22. 





[Meyer, 1985] B. MEYER , “On Formalism in Specifi cations,” IEEE Software 2 (January 1985), pp. 6–26. 





[Modell, 1996] M. E. MODELL , A Professional’s Guide to Systems Analysis , 2nd ed., McGraw-Hill, New York, 1996. 





[Naur, 1964] P. NAUR , “The Design of the GIER ALGOL Compiler,” in: Annual Review in Automatic Programming, Vol. 4, Pergamon Press, Oxford, UK, 1964, pp. 49–85. 





[Naur, 1969] P. NAUR , “Programming by Action Clusters,” BIT 9 ( No. 3, 1969), pp. 250–58. 





[Nix and Collins, 1988] C. J. NIX AND B. P. COLLINS , “The Use of Software Engineering, Including the Z Notation, in the Development of CICS,” Quality Assurance 14 (September 1988), pp. 103–10. 





[Oest, 1986] O. N. OEST , “VDM from Research to Practice,” Proceedings of the IFIP Congress, Information Processing ’86, IFIP, 1986, pp. 527–33. 





[Palshikar, 2001] G. K. PALSHIKAR , “Applying Formal Specifi cations to Real-World Software Development,” IEEE Software 18 (November–December 2001), pp. 89–97. 





[Peterson, 1981] J. L. PETERSON , Petri Net Theory and the Modeling of Systems , Prentice Hall, Englewood Cliffs, NJ, 1981. 





[Petri, 1962] C. A. PETRI , “Kommunikation mit Automaten,” Ph.D. Dissertation, University of Bonn, Germany, 1962. [In German.] 





[Ross, 1985] D. T. ROSS , “Applications and Extensions of SADT,” IEEE Computer 18 (April 1985), pp. 25–34. 





[Scheffer, Stone, and Rzepka, 1985] P. A. SCHEFFER , A. H. STONE III, AND W. E. RZEPKA , “A Case Study of SREM,” IEEE Computer 18 (April 1985), pp. 47–54. 





[Schwartz and Delisle, 1987] M. D. SCHWARTZ AND N. M. DELISLE , “Specifying a Lift Control System with CSP,” Proceedings of the Fourth International Workshop on Software Specifi cation and Design , Monterey, CA, April 1987, pp. 21–27. 





[Silberschatz, Galvin, and Gagne, 2002] A. SILBERSCHATZ , P. B. GALVIN, AND G. GAGNE , Operating System Concepts, 6th ed., Addison-Wesley, Reading, MA, 2002. 





[Sobel and Clarkson, 2002] A. E. K. SOBEL AND M. R. CLARKSON , “Formal Methods Application: An Empirical Tale of Software Development,” IEEE Transactions on Software Engineering 28 (March 2002), pp. 308–20. 





[Spivey, 1990] J. M. SPIVEY , “Specifying a Real-Time Kernel,” IEEE Software 7 (September 1990), pp. 21–28. 





[Spivey, 2001] J. M. SPIVEY , The Z Notation: A Reference Manual , 3rd ed., spivey.oriel.ox.ac.uk ∼mike/zrm/, 2001. 





[Teichroew and Hershey, 1977] D. TEICHROEW AND E. A. HERSHEY III, “PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems,” IEEE Transactions on Software Engineering SE-3 (January 1977), pp. 41–48. 





[Wing, 1990] J. WING , “A Specifi er’s Introduction to Formal Methods,” IEEE Computer 23 (September 1990), pp. 8–24. 





[Woodcock, 1989] J. WOODCOCK , “Calculating Properties of Z Specifi cations,” ACM SIGSOFT Software Engineering Notes 14 (July 1989), pp. 43–54. 





[Yourdon and Constantine, 1979] E. YOURDON AND L. L. CONSTANTINE , Structured Design: Fundamentals of a Discipline of Computer Program and Systems Design , Prentice Hall, Englewood Cliffs, NJ, 1979. 



# Object-Oriented Analysis

Learning Objectives 

After studying this chapter, you should be able to 

• Perform the analysis workfl ow. 

• Extract the boundary, control, and entity classes. 

• Perform functional modeling. 

• Perform class modeling. 

• Perform dynamic modeling. 

• Perform use-case realization. 

In Chapter 12 , we examined various classical analysis techniques. This chapter is the object-oriented counterpart of Chapter 12 . 

Object-oriented analysis (OOA) is a semiformal analysis technique for the objectoriented paradigm. In Chapter 12 , we pointed out that a number of different techniques are used for structured systems analysis, all essentially equivalent. Similarly, well over 60 different techniques have been put forward for OOA. Again, all the techniques are largely equivalent. The “For Further Reading” section of this chapter includes references to a wide variety of techniques, as well as to published comparisons of different techniques. 

However, as explained in Section 3.1, today the Unifi ed Process [Jacobson, Booch, and Rumbaugh, 1999] is almost always the methodology of choice for object-oriented software production. For this reason, the fi rst and last parts of this chapter are devoted to the analysis workfl ow of the Unifi ed Process. 

Object-oriented analysis is a key component of the object-oriented paradigm. When this workfl ow is performed, the classes are extracted. The use cases and the classes are the basis 

Most of the major advances in the object-oriented paradigm were made between 1990 and 1995. Because it usually takes some 15 years for new technology to become accepted, widespread adoption of the object-oriented paradigm should have started no sooner than 2005. However, the millennium bug or Y2K problem changed the expected timetable. 

In the 1960s, when computers fi rst started to be used for business on a widespread basis, hardware was far more expensive than it is today. As a result, the vast majority of software products of that vintage represented a date using only the last two digits for a year; the leading 19 was understood. The problem with this scheme is that the year 00 is then interpreted as 1900, not 2000. 

When hardware became cheaper in the 1970s and 1980s, few managers saw any point in spending large sums of money rewriting existing software products with four-digit dates. After all, by the time the year 2000 arrived, it would be someone else’s problem. As a result, legacy systems remained year-2000 noncompliant. However, as the deadline of January 1, 2000, neared, software organizations were forced to work against the clock to fi x their software products; there was no way to postpone the arrival of Y2K. 

Problems facing the maintenance programmers included a lack of documentation for many legacy software products, as well as software products implemented in programming languages that were now obsolete. When modifying an existing software product was impossible, the only alternative was to start again from scratch. Some companies decided to use COTS technology (Section 1.11). Others decided that new custom software products were needed. For obvious reasons, managers wanted these software products to be developed using modern technology that had already been shown to be cost effective, and that meant using the object-oriented paradigm. The Y2K problem was therefore a signifi cant catalyst for the widespread acceptance of the object-oriented paradigm. 

of the object-oriented software product to be developed. (For more insight into the objectoriented paradigm, see Just in Case You Wanted to Know Box 13.1.) 

## 13.1 The Analysis Workfl ow

The analysis workfl ow of the Unifi ed Process [Jacobson, Booch, and Rumbaugh, 1999] has two overall aims. From the viewpoint of the requirements workfl ow (the preceding workfl ow), the aim of the analysis workfl ow is to obtain a deeper understanding of the requirements. Conversely, from the viewpoint of the design and implementation workfl ows (the workfl ows that follow the analysis workfl ow), the aim of the analysis workfl ow is to describe those requirements in such a way that the resulting design and implementation are easy to maintain. 

The Unifi ed Process is use-case driven. During the analysis workfl ow, the use cases are described in terms of the classes of the software product. The Unifi ed Process has three types of classes: entity classes, boundary classes, and control classes. An entity class models information that is long lived. In the case of a banking software product, Account Class is an entity class because information on accounts has to stay in the software product. For the MSG Foundation software product, Investment Class is an entity class; again, information on investments has to be long lived. 

A boundary class models the interaction between the software product and its actors. Boundary classes are generally associated with input and output. For example, in the MSG 

FIGURE 13.1 UML stereotypes (extensions of UML) for representing an entity class, a boundary class, and a control class. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/40d456037f283aa5514711eed29f39543e19c1a7b2b7dae3f06d9127c19f2c53.jpg)



Entity Class


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/cf3be3d6ae5e13b740965512c47975e4c71eb63fcb333cd1f06402965274d4af.jpg)



Boundary Class


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/54b371c0d7e36cebc8d2062f4cce25576fad39fed7b6ae03fc696bb2bd093b38.jpg)



Control Class


Foundation software product, reports have to be printed listing the investments of the Foundation, as well as all the mortgages currently held. This means that boundary classes Investments Report Class and Mortgages Report Class are needed. 

A control class models complex computations and algorithms. In the case of the MSG Foundation software product, the algorithm for estimating the funds available for the week is a control class, namely, Estimate Funds for Week Class . 

The UML notation for these three types of classes is shown in Figure 13.1 . These are stereotypes , that is, extensions of UML. A strength of UML is that it allows additional constructs to be defi ned that are not part of UML but may be needed to model a specifi c system accurately. 

As stated at the beginning of this section, during the analysis workflow, the use cases are described in terms of the classes of the software product. The Unified Process itself does not describe how classes are to be extracted because users of the Unified Process are expected to have a background in object-oriented analysis and design. Accordingly, this discussion of the Unified Process is temporarily suspended so that an explanation can be given of how classes are extracted; we return to the Unified Process in Section 13.15. 

Entity classes, that is, classes that model long-lived information, are considered fi rst. 

## 13.2 Extracting the Entity Classes

Entity class extraction consists of three steps that are carried out iteratively and incrementally: 

1. Functional modeling . Present scenarios of all the use cases (a scenario is an instance of a use case). 

2. Entity class modeling . Determine the entity classes and their attributes. Then, determine the interrelationships and interactions between the entity classes. Present this information in the form of a class diagram. 

3. Dynamic modeling . Determine the operations performed by or on each entity class or subclass. Present this information in the form of a statechart. 

However, as with all iterative and incremental processes, the three steps are not necessarily always performed in this order; a change in one model frequently triggers corresponding revisions of the other two models. 

To show how this is done, we now extract the entity classes of the elevator problem case study. 

## 13.3 Object-Oriented Analysis: The Elevator Problem Case Study

The elevator problem case study is described in Chapter 12 . For ease of reference, the problem is repeated here. 

A product is to be installed to control n elevators in a building with m fl oors. The problem concerns the logic required to move elevators between fl oors according to the following constraints: 

1. Each elevator has a set of m buttons, one for each fl oor. These illuminate when pressed and cause the elevator to visit the corresponding fl oor. The illumination is canceled when the corresponding fl oor is visited by the elevator. 

2. Each fl oor, except the fi rst fl oor and the top fl oor, has two buttons, one to request an up-elevator and one to request a down-elevator. These buttons illuminate when pressed. The illumination is canceled when an elevator visits the fl oor and then moves in the desired direction. 

3. When an elevator has no requests, it remains at its current fl oor with its doors closed. 

The fi rst step in OOA is to model the use cases. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/ee05fcab9b2a2040736d4d0ae3f450a2b340b43b154a568c0746a91e241e4b7c.jpg)


## Functional Modeling: The Elevator Problem Case Study

A use case describes the interaction between the product to be constructed and the actors , that is, the external users of that product. The only interactions possible between a user and an elevator are the user pressing an elevator button to summon an elevator or the user pressing a fl oor button to request the elevator to stop at a specifi c fl oor, hence, two use cases, Press an Elevator Button and Press a Floor Button. The two use cases are shown in the use-case diagram (Section 11.7) of Figure 13.2. 

## FIGURE 13.2

Use-case diagram for the elevator problem case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/a0371125c6f22c3f836baaedb79298364c2a9b4de947f306e7bfbf1f737dc368.jpg)



FIGURE 13.3 The first iteration of a normal scenario (the missing responsibilities and the use of the passive voice will be corrected in the next iteration).


<table><tr><td>1. User A presses the Up floor button at floor 3 to request an elevator. User A wishes to go to floor 7.</td></tr><tr><td>2. The Up floor button is turned on.</td></tr><tr><td>3. An elevator arrives at floor 3. It contains User B, who has entered the elevator at floor 1 and pressed the elevator button for floor 9.</td></tr><tr><td>4. The elevator doors open.</td></tr><tr><td>5. The timer starts.User A enters the elevator.</td></tr><tr><td>6. User A presses the elevator button for floor 7.</td></tr><tr><td>7. The elevator button for floor 7 is turned on.</td></tr><tr><td>8. The elevator doors close after a timeout.</td></tr><tr><td>9. The Up floor button is turned off.</td></tr><tr><td>10. The elevator travels to floor 7.</td></tr><tr><td>11. The elevator button for floor 7 is turned off.</td></tr><tr><td>12. The elevator doors open to allow User A to exit from the elevator.</td></tr><tr><td>13. The timer starts.User A exits from the elevator.</td></tr><tr><td>14. The elevator doors close after a timeout.</td></tr><tr><td>15. The elevator proceeds to floor 9 with User B.</td></tr></table>

A use case provides a generic description of the overall functionality; a scenario is a specifi c instantiation of a use case, just as an object is an instantiation of a class. In general, there are a large number of scenarios, each representing one specifi c set of interactions. In this section, we consider the scenario of Figure 13.3 , which incorporates instantiations of both use cases. 

Figure 13.3 depicts a normal scenario ; that is, a set of interactions between users and elevators that corresponds to the way we understand elevators should be used. Figure 13.3 was constructed after carefully observing different users interacting with elevators (or, more precisely, with elevator buttons and fl oor buttons). The 15 numbered events describe in detail the two interactions between User A and the buttons of the elevator system (event 1 and event 6) and the operations performed by the components of the elevator system (events 2 through 5 and 7 through 15). Two items, User A enters the elevator and User A exits from the elevator , are unnumbered. Such items essentially are comments; User A does not interact with the components of the elevator when entering or leaving an elevator. 

In contrast, Figure 13.4 is an exception scenario . It depicts what happens when a user presses the Up button at floor 3 but actually wants to go down to fl oor 1. This scenario, too, was constructed by observing the actions of many users in elevators; it is unlikely that someone who has never used an elevator would realize that users sometimes press the wrong button. 

There is a serious mistake throughout Figures 13.3 and 13.4 . Recall that, as stated in Section 1.9, responsibility-driven design is a feature of the object-oriented paradigm. From the very beginning of the life cycle, that is, from the requirements workfl ow onward, it is essential to specify the responsibility for each action. Consider event 2 in Figure 13.3 , The Up fl oor button is turned on . This statement does not specify who is responsible for turning on the button. Instead, the scenario should have stated, “The system turns on the Up fl oor button.” Similarly, event 4 states, The elevator doors open . But who or what is responsible for opening the doors? Is it a manual elevator in which the users have to open and close the doors? Or is it an automatic elevator in which the system is responsible for opening and closing the doors? Accordingly, in use cases and scenarios (instantiations of use cases), the responsibil ity for each action must be explicitly stated. 


FIGURE 13.4 An exception scenario (the missing responsibilities and the use of the passive voice will be corrected in the next iteration).


<table><tr><td>1. User A presses the Up floor button at floor 3 to request an elevator. User A wishes to go to floor 1.</td></tr><tr><td>2. The Up floor button is turned on.</td></tr><tr><td>3. An elevator arrives at floor 3. It contains User B, who has entered the elevator at floor 1 and pressed the elevator button for floor 9.</td></tr><tr><td>4. The elevator doors open.</td></tr><tr><td>5. The timer starts.User A enters the elevator.</td></tr><tr><td>6. User A presses the elevator button for floor 1.</td></tr><tr><td>7. The elevator button for floor 1 is turned on.</td></tr><tr><td>8. The elevator doors close after a timeout.</td></tr><tr><td>9. The Up floor button is turned off.</td></tr><tr><td>10. The elevator travels to floor 9.</td></tr><tr><td>11. The elevator button for floor 9 is turned off.</td></tr><tr><td>12. The elevator doors open to allow User B to exit from the elevator.</td></tr><tr><td>13. The timer starts.User B exits from the elevator.</td></tr><tr><td>14. The elevator doors close after a timeout.</td></tr><tr><td>15. The elevator proceeds to floor 1 with User A.</td></tr></table>

Furthermore, it is bad practice to use the passive voice in a use case, a scenario, or in any other UML diagram that specifi es actions. For example, event 2, The Up fl oor button is turned on , should not be in the passive voice. A use case describes an inter action between the software product and the user; for clarity, an action should be described in the active voice. Furthermore, a use case should be written from the user’s perspective, that is, what the user does and how the software product responds. Finally, it should be written in the present tense, to give a sense of immediacy. 

In summary, statements in a use case or scenario should take the form, “A user does this and the software product responds by doing that.” In view of the fact that the use cases will eventually be refi ned into the run-time behavior of the product, statements in that form are easy to test, easy to document, and easy to modify. The mistakes in the scenarios of Figures 13.3 and 13.4 are corrected in a subsequent iteration, in Section 13.7. 

As explained at the beginning of Chapter 7 , the object-oriented paradigm did not suddenly appear out of nowhere. Instead, it evolved out of the classical paradigm, in response to perceived shortcomings in the classical paradigm. 

Entity class modeling is an example of this evolution. It is an extension of the classical technique of entity-relationship modeling. As described in Section 12.6, entity-relationship modeling has been used for database modeling since 1976. 

The scenarios of Figures 13.3 and 13.4 , plus innumerable others, are specifi c instances of the use cases shown in Figure 13.2 . The OOA team should study suffi cient scenarios to gain a comprehensive insight into the behavior of the system being modeled. This information is used in the next step, entity class modeling, to determine the entity classes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/8089e67c2bbfc3aff4c0888d04792a7342cced74282a5fbba6d685dcf64ee33c.jpg)


## 13.5 Entity Class Modeling: The Elevator Problem Case Study

In this step, the entity classes and their attributes are extracted and represented in a UML class diagram (see Just in Case You Wanted to Know Box 13.2). Only the attributes of an entity class are determined at this time, not the methods; the latter are assigned to the classes during the object-oriented design (OOD) workfl ow. 

A characteristic of the whole object-oriented paradigm is that the various steps rarely are easy to carry out. Fortunately, the benefi ts of using objects make the effort worthwhile. So it should not come as a surprise that the fi rst part of the analysis workfl ow, extracting entity classes and their attributes, usually is diffi cult to get right the fi rst time. 

One method of determining the entity classes is to deduce them from the use cases. That is, the developers carefully study all the scenarios, both normal and exception, and identify the components that play a role in the use cases. From just the scenarios of Figures 13.3 and 13.4 , candidate entity classes are elevator buttons, fl oor buttons, elevators, doors, and timers. As we will see, these candidate entity classes are close to the actual classes extracted during entity class modeling. In general, however, there are many scenarios and, consequently, a large number of potential classes. An inexperienced developer may be tempted to infer too many candidate entity classes from the scenarios. This has a deleterious effect on the entity class modeling, because it is easier to add a new entity class than to remove a candidate entity class that should not have been included. 

Another approach to determining the entity classes, which is effective when the developers have domain expertise, is CRC cards (Section 13.5.2). However, if the developers have little or no experience in the application domain, then it is advisable to use noun extraction, described in Section 13.5.1. 

## 13.5.1 Noun Extraction

For developers with no domain expertise, a good way to proceed is to use the following two-stage noun-extraction method to extract candidate entity classes and then to refi ne the solution: 

Stage 1. Describe the Software Product in a Single Paragraph. One possible way to do this for the elevator problem case study is as follows: 

Buttons in elevators and on the fl oors control the movement of n elevators in a build ing with m fl oors. Buttons illuminate when pressed to request the elevator to stop at a specifi c fl oor; the illumination is canceled when the request has been satisfi ed. When an elevator has no requests, it remains at its current fl oor with its doors closed. 

## Stage 2. Identify the Nouns.

Identify the nouns in the informal strategy (excluding those that lie outside the problem boundary); then use these nouns as candidate entity classes. The informal strategy i now reproduced, but this time with the identifi ed nouns printed in a sans serif typeface. 

Buttons in elevators and on the fl oors control the movement of n elevators in a building with m fl oors. Buttons illuminate when pressed to request an elevator to stop at a specifi c fl oor ; the illumination is canceled when the request has been satisfi ed. When an elevator has no requests , it remains at its current fl oor with its doors closed. 

There are eight different nouns: button, elevator, fl oor, movement, build ing, illumination, request, and door . Three of these nouns— fl oor, building, and door —lie outside the problem boundary and therefore may be ignored. Three of the remaining nouns— movement, illumination , and request —are abstract nouns ; that is, they identify things that have no physical existence. A useful rule of thumb is that abstract nouns rarely end up corresponding to classes. Instead, they frequently are attributes of classes. For example, illumination is an attribute of button. 

This leaves two nouns and, therefore, two candidate entity classes: Elevator Class and Button Class . (The UML convention is to use boldface for class names and capitalize the initial letter of each word in a class name.) 

The resulting class diagram is shown in Figure 13.5 . Button Class has the Boolean attribute illuminated to model events 2, 7, 9, and 11 of the scenarios of Figures 13.3 and 13.4 . The problem specifi es two types of buttons, so two subclasses of Button Class are defi ned: Elevator Button Class and Floor Button Class (the open triangle denotes inheritance in UML). Each instance of Elevator Button Class and Floor Button Class communicates with the instance of Elevator Class . The latter class has the Boolean attribute doors open to model events 4, 8, 12, and 14 of the two scenarios. 

Unfortunately, this is not a good beginning. In a real elevator, the buttons do not directly communicate with the elevators; some sort of elevator controller is needed, if only to decide which elevator to dispatch in response to a particular request. However, the problem statement makes no mention of a controller, so it was not selected as an entity class during the noun-extraction process. In other words, the technique of this section for fi nding candidate entity classes provides a starting point but certainly should not be relied on to do more than that. 


FIGURE 13.5 The fi rst iteration of the class diagram for the elevator problem case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/5615245a25301a34d11ff7c7d33d5788a6f6277ac583a384636a118ed1fa52d1.jpg)


Adding the Elevator Controller Class to Figure 13.5 yields Figure 13.6. This certainly makes more sense. Furthermore, there are now one-to-many relationships in Figure 13.6 , as opposed to the hard to model many-to-many relationship of Figure 13.5 . It therefore seems reasonable to go on to stage 3 at this point, bearing in mind that it is possible to return to entity class modeling at any time, even as 

FIGURE 13.6 The second iteration of the class diagram for the elevator problem case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/d530245d57c8b5ddb0d80126e9d041e462f03785a31ef8a6fe3a73df1f52e3b9.jpg)


How do we fi nd the number of days between February 21, 1999, and August 16, 2007? Such subtractions are needed in many fi nancial computations, such as calculating an interest payment or determining the present value of a future cash fl ow. The usual way this is done is to convert each date into an integer, the number of days since a specifi ed starting date. The problem is that we cannot agree what starting date to use. 

Astronomers use Julian days, the number of days since noon GMT on January 1, 4713, B.C.E. This system was invented in 1582 by Joseph Scaliger, who named it for his father, Julius Caesar Scaliger. (If you really, really have to know why January 1, 4713 B.C.E. was chosen, consult [USNO, 2000].) 

A Lilian date is the number of days since October 15, 1582, the fi rst day of the Gregorian calendar, introduced by Pope Gregory XIII. Lilian dates are named for Luigi Lilio, a leading proponent of the Gregorian calendar reform. Lilio was responsible for deriving many of the algorithms of the Gregorian calendar, including the rule for leap years. 

Turning to software, COBOL intrinsic functions use January 1, 1600, as the starting date for integer dates. Almost all spreadsheets, however, use January 1, 1900, following the lead of Lotus 1-2-3. 

late as the implementation workfl ow. However, before proceeding with the dynamic modeling, a different technique for entity class modeling is considered. 

## 13.5.2 CRC Cards

For a number of years, class–responsibility–collaboration (CRC) cards have been utilized during the object-oriented analysis workfl ow [Wirfs-Brock, Wilkerson, and Wiener, 1990]. For each class, the software development team fi lls in a card showing the name of the class, its functionality (responsibility), and a list of the othe classes it invokes to achieve that functionality (collaboration). 

This approach subsequently has been extended. First, a CRC card often explicitly contains the attributes and methods of the class, rather than just its “responsibility” expressed in some natural language. Second, the technology has changed. Instead of using cards, some organizations put the names of the classes on Post-it notes, which they move around on a white board; lines are drawn between the Post-it notes to denote collaboration. Nowadays the whole process can be automated; CASE tools like System Architect include components for creating and updating CRC “cards” on the screen. 

The strength of CRC cards is that, when utilized by a team, the interaction among the members can highlight missing or incorrect fi elds in a class, whether attributes or methods. Also, the relationships between classes are clarifi ed when CRC cards are used. One especially powerful technique is to distribute the cards among the team members, who then act out the responsibilities of their classes. Consequently, someone might say, “I am the Date Class , and my responsibility is to create new date objects.” Another team member might then interject that he or she needs additional functionality from the Date Class , such as converting a date from the conventional format to an integer, the number of days from January 1, 1900, so that fi nding the number of days between any two dates can be computed easily by subtracting the corresponding two integers (see Just in Case You Wanted to Know Box 13.3). Accordingly, acting out the responsibilities of CRC cards is an effective means of verifying that the class diagram is complete and correct. 

A weakness of CRC cards is that this approach generally is not a good way of identifying entity classes unless the team members have considerable experience in the relevant application domain. On the other hand, once the developers have determined many of the classes and have a good idea of their responsibilities and collaborations, CRC cards can be an excellent way of completing the process and making sure that everything is correct. This is described in Section 13.7. First, however, we need to perform the dynamic modeling. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/36402793353b30a81f6fcc78728069c5e7ac48388c0ba39d8ff6fda0d98873d1.jpg)


## Dynamic Modeling:13.6 The Elevator Problem Case Study

The aim of dynamic modeling is to produce a statechart , a description of the target product similar to a finite state machine, for each class. First, consider Elevator Controller Class . For simplicity, only one elevator is considered. The relevant statechart for Elevator Controller Class is in Figure 13.7 . 

The notation is somewhat similar to that of the fi nite state machine (FSM) of Section 12.7, but there is a signifi cant difference. An FSM as presented in Chapter 12 is an example of a formal technique. The state transition diagrams themselves are not a complete representation of the product to be built. Instead, the model consists of a set of transition rules of the form given in equation (12.2): 

## current state and event and predicate ⇒ next state

Formality is achieved by presenting the model in the form of a set of mathematical rules. 

In contrast, the representation of a UML statechart is somewhat less formal. The three aspects of a state machine (state, event, and predicate) are distributed over the UML diagram. For example, the state Going Into Wait State in Figure 13.7 is entered if the present state is Elevator Event Loop and the event elevator stopped, no requests pending is true. When the state Going Into Wait State has been entered, operation Close elevator doors after timeout is to be carried out. Current versions of OOA are semiformal (graphical) techniques, and the intrinsic lack of formality of the statechart accordingly is no problem. However, when the object-oriented paradigm matures, it is likely that more formal versions will be developed and the corresponding dynamic models will be somewhat closer to fi nite state machines. 

To see the equivalence of the statechart of Figure 13.7 and the STDs of Figures 12.15 through 12.17 , consider various scenarios. For example, consider the fi rst part of the scenario of Figure 13.3 . Event 1 is User A presses the Up fl oor button at fl oor 3. 

First consider the STD of Figure 12.16 . If the fl oor button is off, then the button is turned on. Now consider the statechart of Figure 13.7 . The solid circle denotes the start state, which takes the system into state Elevator Event Loop . Following the leftmost vertical line, if the button was turned off when it is pushed, the system enters state Processing New Request of Figure 13.7 , and the button is turned on. The following state is Elevator Event Loop . 


FIGURE 13.7 The first iteration of the statechart for the Elevator Controller Class.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/770f59755a2e1df28462840947218299cc3634b26edb6e14463332c9f46c5df4.jpg)


Next, the elevator nears fl oor 3. First consider the STD approach. In Figure 12.17 , the elevator goes into state S (U, 3) ; that is, it stops at fl oor 3, about to go up. (Because the simplifying assumption has been made of only one elevator, the argument e in Figure 12.17 is suppressed here.) Now the doors close ( Figure 12.17 ), the Up fl oor button is turned off ( Figure 12.16 ), and the elevator starts to move toward fl oor 4. 

Returning to the statechart of Figure 13.7 , consider what happens when the elevator nears fl oor 3. Because the elevator is in motion, the next state entered i Determining If Stop Requested . The requests are checked and, because User A has requested the elevator to stop there, the next state is Stopping At Floor . The elevator stops at fl oor 3, the doors open, and the timer starts. The elevator button for fl oor 3 has not been pressed, so state Elevator Event Loop is next. 

User A enters and presses the elevator button for fl oor 7. Therefore, the next state is again Processing New Request , followed again by Elevator Event Loop. The elevator has stopped and two requests are pending, so state Closing Elevator Doors is next and the doors close after a timeout. The fl oor button at fl oor 3 was pressed by User A, so Turning Off Floor Button is the following state, and the fl oor button is turned off. State Processing Next Request is next, and the elevator starts to move toward fl oor 4. The relevant aspects of the corresponding diagrams clearly are equivalent with respect to this scenario; you may wish to consider other possible scenarios as well. 

From the preceding discussion, it should come as no surprise to learn that Figure 13.7 was constructed from the scenarios. More precisely, the specifi c events of the scenarios were generalized. For example, consider the fi rst event of the scenario of Figure 13.3 , User A presses the Up fl oor button at fl oor 3 . This specifi c event is generalized to an arbitrary button (fl oor button or elevator button) being pushed. Then, there are two possibilities. Either the button already is turned on (in which case nothing happens) or the button is turned off (in which case action must be taken to process the user’s request). 

To model this event, the Elevator Event Loop state is drawn in Figure 13.7. The case of an already turned on button is modeled by the do-nothing loop with event button pushed, button turned on in the top left-hand corner of Figure 13.7 . The other case, a turned-off button, is modeled by the arrow labeled with the event button pushed, button turned off leading to state Processing New Request. From event 2 of the scenario it is clear that the operation Turn on button is needed in this state. Furthermore, the purpose of the user’s action of pressing an arbitrary button is to request an elevator (fl oor button) or request an elevator to move to a specifi c fl oor (elevator button), so operation Update requests also must be carried out in the state Processing New Request. 

Now consider event 3 of the scenario, An elevator arrives at fl oor 3 . This was generalized to the concept of an arbitrary elevator moving between fl oors. The motion of the elevator is modeled by the event elevator moving in direction d, fl oor f is next and the state Determining If Stop Requested . But there again are two possibilities, either a request to stop at fl oor f or no such request. In the former case, corresponding to event no request to stop at fl oor f, the elevator simply must be in the state of Continuing Moving one more fl oor in direction d . In the latter case (corresponding to event user has requested stop at fl oor f ), from the sce nario of Figure 13.3 it is clear that it is necessary to Stop elevator (from event 3), and then Open doors and start timer (from events 4 and 5); state Stopping At Floor is needed to perform these actions. Also, similar to the Processing New Request state, it becomes apparent that it is necessary also to Update requests in state Stopping At Floor . In addition, generalizing event 9 of the scenario leads to the realization that the fl oor button has to be turned off if it is turned on. This is modeled by state Turning Off Floor Button , together with the two events above the box representing that state. Similarly, generalizing event 11 of the scenario implies that the elevator button has to be turned off if it is turned on. This is modeled by state Turning Off Elevator Button , together with the two events above the box rep resenting that state. 

Generalizing event 8 of the scenario of Figure 13.3 yields state Closing Elevator Doors ; generalizing event 10 yields state Processing Next Request . However, the need for the state Going Into Wait State and the event no requests pending, doors closed is deduced by generalizing an event of a different scenario, one in which the user exits from the elevator but no buttons remain turned on. 

## 13.7 The Test Workfl ow: Object-Oriented Analysis

At this point, the functional, entity class, and dynamic models appear to be complete and the test workfl ow resumes. The next step is to review the analysis workfl ow to date. One component of this review, as suggested in Section 13.5.2, is to use CRC cards. 

Accordingly, CRC cards are fi lled in for each of the entity classes, Button Class, Elevator Button Class, Floor Button Class, Elevator Class , and Elevator Controller Class . The CRC card for Elevator Controller Class , shown in Figure 13.8 , is deduced from the class diagram of Figure 13.5 and the statechart of Figure 13.6 . In more detail, the RESPONSIBILITY of Elevator Controller Class is obtained by listing all the operations in the statechart for Elevator Controller Class ( Figure 13.7 ). The COLLABORATION of the Elevator Controller Class is determined by examining the class diagram of Figure 13.6 and noting that classes Elevator Button Class, Floor Button Class , and Elevator Class interact with class Elevator Controller Class . 

## CLASS Elevator Controller Class RESPONSIBILITY

1. Turn on elevator button 

2. Turn off elevator button 

3. Turn on floor button 

4. Turn off floor button 

5. Move elevator up one floor 

6. Move elevator down one floo 

7. Open elevator doors and start timer 

8. Close elevator doors after timeout 

9. Check requests 

10. Update requests 

## COLLABORATION

1. Elevator Button Class 

2. Floor Button Class 

3. Elevator Class 

FIGURE 13.9 The second iteration of the CRC card for the Elevator Controller Class. 

This CRC card highlights two major problems with the fi rst iteration of the objectoriented analysis. 

1. Consider responsibility 1. Turn on elevator button. This command is totally out of place in the object-oriented paradigm. From the viewpoint of responsibility-driven design (Section 1.9), objects (instances) of Elevator Button Class are responsible for turning themselves on or off. Also, from the viewpoint of information hiding (Section 7.6), the Elevator Controller Class should not have the knowledge of the internals of Elevator Button Class needed to turn on a button. The correct responsibility is this: Send a message to Elevator Button Class to turn itself on. Similar changes are needed for responsibilities 2 through 6 in Figure 13.8 . These six corrections are refl ected in Figure 13.9 , the second iteration of the CRC card for the Elevator Controller Class. 

2. A class has been overlooked. Returning to Figure 13.8 , consider responsibility 7. Open elevator doors and start timer. The key concept here is the notion of state . The attributes of a class sometimes are termed state variables . The reason for this terminology is that, in most object-oriented implementations, the state of the product is determined by the values of the attributes of the various component objects. The statechart has many features in common with a fi nite state machine. Accordingly, it is not surprising that the concept of state plays an important role in the object-oriented paradigm. This concept can be used to help determine whether a component should be modeled as a class. If the component in question possesses a state that is changed during execution of the implementation, then it probably should be modeled as a class. Clearly, the doors of the elevator possess a state (open or closed), and Elevator Doors Class therefore should be a class. 

<table><tr><td>CLASSElevator Controller Class</td></tr><tr><td>RESPONSIBILITY1. Send message to Elevator Button Class to turn on button2. Send message to Elevator Button Class to turn off button3. Send message to Floor Button Class to turn on button4. Send message to Floor Button Class to turn off button5. Send message to Elevator Class to move up one floor6. Send message to Elevator Class to move down one floor7. Send message to Elevator Doors Class to open8. Start timer9. Send message to Elevator Doors Class to close after timeout10. Check requests11. Update requests</td></tr><tr><td>COLLABORATION1. Elevator Button Class (subclass)2. Floor Button Class (subclass)3. Elevator Doors Class4. Elevator Class</td></tr></table>

Some years ago, I was on the 10th fl oor of a building, waiting impatiently for an elevator. The doors opened, I started to step forward—only no elevator was there. What saved my life was the total blackness I saw as I was about to step into the elevator shaft, and I instinctively realized that something was wrong. 

Perhaps, if that elevator control system had been developed using the object-oriented paradigm, the inappropriate opening of the doors on the 10th fl oor might have been avoided. 

There is another reason why Elevator Doors Class should be a class. The objectoriented paradigm allows the state to be hidden within an object and hence protected from unauthorized change. If there is an Elevator Doors Class object, the only way that the doors of the elevator can be opened or shut is by sending a message to that Elevator Doors Class object. Serious accidents can be caused by opening or closing the doors of an elevator at the wrong time; see Just in Case You Wanted to Know Box 13.4. Therefore, for certain types of products, safety considerations should be added to the other strengths of objects listed in Chapters 7 and 8 . 

Adding Elevator Doors Class means that responsibilities 7 and 8 in Figure 13.8 need to be changed analogously to responsibilities 1 through 6. That is, messages should be sent to instances of the Elevator Doors Class to open and close themselves. But there is an additional complication. 

Recall that responsibility 7 is Open elevator doors and start timer. This must be split into two separate responsibilities. A message must indeed be sent to Elevator Doors Class to open. However, the timer is part of the Elevator Controller Class, and starting the timer therefore is the responsibility of the Elevator Controller Class itself. The second iteration of the CRC card for Elevator Controller Class ( Figure 13.9 ) shows that this separation of responsibilities has been achieved satisfactorily. 

In addition to the two major problems highlighted by the CRC card of Figure 13.8, responsibilities Check requests and Update requests of Elevator Controller Class require the attribute requests be added to Elevator Controller Class . At this stage, requests are defi ned simply to be of type requestType ; a data structure for requests will be chosen during the design workfl ow. 

The corrected class diagram is shown in Figure 13.10 . Having modifi ed the class diagram, we must reexamine the use-case diagram and statecharts to see if they, too, need further refi nement. The use-case diagram clearly is still adequate. However, the operations in the statechart of Figure 13.7 must be modifi ed to refl ect the responsibilities of Figure 13.9 (the second iteration of the CRC card) and not Figure 13.8 (the fi rst iteration). Also, the set of statecharts must be extended to include the additional class. The scenarios need to be updated to refl ect these changes; Figure 13.11 shows the second iteration of the scenario of Figure 13.3 . 

There is a serious problem in Figure 13.10 , the third iteration of the class diagram. The Elevator Controller Class is running the entire show—this is an example of a socalled God class, a class that is exposed to too much information and has too much control. This type of architecture is a well-known antipattern, or pattern to be avoided (see Just in Case You Wanted to Know Box 8.4). To solve this problem, instead of having one central elevator controller, we distribute the control. Each of the n elevators now has its own elevator subcontroller, and each of the m fl oors has its own fl oor subcontroller. The m + n subcontrollers all communicate with a scheduler, which processes requests. The resulting fourth iteration of the class diagram is shown in Figure 13.12 . This diagram refl ects a distributed, decentralized architecture, characteristic of the object-oriented paradigm. 


FIGURE 13.10 The third iteration of the class diagram for the elevator problem case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/9c21f9aaa33df3e30d50909a29cd73a8ce8e60cc57d50d235a955a4c32788c84.jpg)


Now, when a user presses a Floor Button Class object, the Floor Button Class object sends a message to the corresponding Floor Subcontroller Class object informing it that the button has been pressed. The Floor Subcontroller Class object sends a message back to the Floor Button Class object to ask whether its light is on. If not, it sends a message to that Floor Button Class object to turn itself on, and it also informs the Scheduler Class object of the new request that has been made by a user. 

Similarly, when a user presses an Elevator Button Class object, the Elevator Button Class object sends a message to the corresponding Elevator Subcontroller Class object informing it that the button has been pressed. The Elevator Subcontroller Class object sends a message back to the Elevator Button Class object to ask whether its light is on. If not, it sends a message to that Elevator Button Class object to turn itself on, and it also informs the Scheduler Class object of the new request that has been made. 

Now, there is a sensor just above and just below each fl oor in each elevator shaft, for a total of 2m – 2 sensors per shaft. When an Elevator Class object nears a fl oor (moving up or down), the corresponding Sensor Class object sends an appropriate message to the corresponding Elevator Subcontroller Class object. The Elevator Subcontroller Class object then sends a message to the Scheduler Class object informing it that the 

FIGURE 13.11 The second iteration of a normal scenario for the elevator problem case study. 



1. User A presses the Up floor button at floor 3 to request an elevator. User A wishes to go to floor 7. 





2. The floor button informs the elevator controller that the floor button has been pushed. 





3. The elevator controller sends a message to the Up floor button to turn itself on 





4. The elevator controller sends a series of messages to the elevator to move itself up to floor 3. The elevator contains User B, who has entered the elevator at floor 1 and pressed the elevator button for floor 9. 





5. The elevator controller sends a message to the elevator doors to open themselves. 





6. The elevator controller starts the timer. User A enters the elevator. 





7. User A presses elevator button for floor 7. 





8. The elevator button informs the elevator controller that the elevator button has been pushed. 





9. The elevator controller sends a message to the elevator button for floor 7 to turn itself on. 





10. The elevator controller sends a message to the elevator doors to close themselves after a timeout. 





11 The elevator controller sends a message to the Up floor button to turn itself off.. 





12. The elevator controller sends a series of messages to the elevator to move itself up to floor 7. 





13. The elevator controller sends a message to the elevator button for floor 7 to turn itself off. 





14. The elevator controller sends a message to the elevator doors to open themselves to allow User A to exit from the elevator. 





15. The elevator controller starts the timer. User A exits from the elevator. 





16. The elevator controller sends a message to the elevator doors to close themselves after a timeout. 





17. The elevator controller sends a series of messages to the elevator to move itself up to floor 9 with User B. 



Elevator Class object is nearing that fl oor. The Scheduler Class object now checks whether there is a request to stop at that fl oor. If not, it sends a message to the Elevator Subcontroller Class object, which then sends a message to the appropriate Elevator Class object to move itself one further fl oor in the same direction. But if there is a request to stop, the Scheduler Class object informs the Elevator Subcontroller Class object accordingly, and then updates its request list appropriately. The Elevator Subcontroller Class object then sends a message to the relevant Elevator Button Class object to ask whether its light is off. If not, it sends a subsequent message to that Elevator Button Class object to turn itself off. 

When an Elevator Class object stops at a fl oor, the corresponding Elevator Subcontroller Class object sends a message to the appropriate Elevator Doors Class object to open itself; it then starts its timer. After a time-out, it sends the appropriate message to that Elevator Doors Class object to close itself. 


FIGURE 13.12 The fourth iteration of the class diagram for the elevator problem case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/c4d61c0d2c8fa54515fb0c781d07d206399a583e28a64ba642fb9c4a2fa9f5b3.jpg)


Finally, when an Elevator Class object leaves a fl oor (moving up or down), the appropriate Sensor Class object informs the corresponding Elevator Subcontroller Class object that the elevator has left the fl oor. The Elevator Subcontroller Class object sends a message to the corresponding Floor Subcontroller Class object informing it that the elevator has left that fl oor, and the direction in which it is moving. The Floor Subcontroller Class object then sends a message to the corresponding Floor Button Class object to determine if its light is on and, if so, sends a subsequent message to turn itself off. 

The various UML diagrams now need to be updated to refl ect the fourth iteration of the class diagram of Figure 13.12 . The fi rst iteration of the statechart for the Elevator Subcontroller Class is shown in Figure 13.13 . The fi rst iteration of the CRC card for the Elevator Subcontroller Class is shown in Figure 13.14 . Updating the other UML diagrams is left as an exercise (Problems 13.1–13.5). 


F I G U RE 1 3 1 3 Th<sub>e</sub> fi<sub>rs</sub>t it<sub>era</sub>ti<sub>on o</sub>f th<sub>e s</sub>t<sub>a</sub>t<sub>ec</sub>h<sub>ar</sub>t f<sub>or</sub> th<sub>e</sub> Elevator Su bcontrol ler Class


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/ce1dcc8556e1576fd00b98a86db45030445859646d6a4b62557d21a2add58cc5.jpg)


<table><tr><td>CLASSElevator Subcontroller Class</td></tr><tr><td>RESPONSIBILITY1. Send message to Elevator Button Class to check if it is turned on2. Send message to Elevator Button Class to turn itself on3. Send message to Elevator Button Class to turn itself off4. Send message to Elevator Doors Class to open themselves5. Start timer6. Send message to Elevator Doors Class to close themselves after timeout7. Send message to Elevator Class to move itself up one floor8. Send message to Elevator Class to move itself down one floor9. Send message to Scheduler Class that a request has been made10. Send message to Scheduler Class that a request has been satisfied11. Send message to Scheduler Class to check if the elevator is to stop at the next floor12. Send message to Floor Subcontroller Class that elevator has left floor</td></tr><tr><td>COLLABORATION1. Elevator Button Class (subclass)2. Sensor Class3. Elevator Doors Class4. Elevator Class5. Scheduler Class6. Floor Subcontroller Class</td></tr></table>

Even after all these changes have been made and checked (including the modifi ed CRC cards), it still may be necessary during the object-oriented design workfl ow to return to the object-oriented analysis workfl ow and revise one or more of the analysis artifacts. However, at this stage it appears that the entity classes for the elevator problem case study have been correctly extracted. 

## 13.8 Extracting the Boundary and Control Classes

Unlike entity classes, boundary classes are usually easy to extract. In general, each input screen, output screen, and printed report is modeled by its own boundary class. Recall that a class incorporates attributes (data) and operations. The boundary class modeling (say) a printed report incorporates all the various data items that can be included in the report and the various operations carried out to print the report. 

Control classes are usually as easy to extract as boundary classes. In general, each nontrivial computation is modeled by a control class. 

FIGURE 13.15 The seventh iteration of the use-case diagram of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/073feab5668f917934b51170ef8a6c822cc61345847630bd16f4fab000377d12.jpg)


We now illustrate entity, boundary, and control class extraction and obtain further insights into the Unifi ed Process by extracting the classes of the MSG Foundation case study. The starting point is the use-case diagram of Figure 11.42 , reproduced here as Figure 13.15. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/d3784ce11696beb72d8d985c2029521415f8a4b7f5cac4d4a684af2f713743fe.jpg)


## 13.9 The Initial Functional Model: The MSG Foundation Case Study

As described in Section 13.2, functional modeling consists of fi nding the scenarios of the use cases. Recall that a scenario is an instance of a use case. Consider the use case Manage a Mortgage ( Figures 11.32 and 11.33 ). One possible scenario is shown in Figure 13.16 . There is a change in the annual real-estate tax to be paid on a home for which the MSG Foundation has provided a mortgage. Because the borrowers pay this tax in equal weekly payments, any change in the real-estate tax must be entered in the relevant mortgage record, so that the total weekly installment (and perhaps the grant) can be adjusted accordingly. The normal portion of the extended scenario models an MSG staff member accessing the relevant mortgage record and changing the annual real-estate tax. Sometimes, however, the staff member may not be able to locate the correct mortgage stored in the software product because he or she has entered the mortgage number incorrectly. This possibility is modeled by the exception portion of the scenario. 


FIGURE 13.16 An extended scenario of managing a mortgage.


<table><tr><td>An MSG Foundation staff member wants to update the annual real-estate tax on a home for which the Foundation has provided a mortgage.</td></tr><tr><td>1. The staff member enters the new value of the annual real-estate tax.</td></tr><tr><td>2. The information system updates the date on which the annual real-estate tax was last changed.</td></tr><tr><td>Possible Alternative</td></tr><tr><td>A. The staff member enters the mortgage number incorrectly.</td></tr></table>


FIGURE 13.17 Another extended scenario of managing a mortgage.


<table><tr><td>There is a change in the weekly income of a couple who have borrowed money from the MSG Foundation. They wish to have their weekly income updated in the Foundation records by an MSG staff member so that their mortgage payments will be correctly computed.1. The staff member enters the new value of the weekly income.2. The information system updates the date on which the weekly income was last changed.Possible AlternativesA. The staff member enters the mortgage number incorrectly.B. The borrowers do not bring documentation regarding their new income.</td></tr></table>

A second scenario corresponding to the Manage a Mortgage use case ( Figures 11.32 and 11.33 ) is shown in Figure 13.17 . Here the borrowers’ weekly income has changed. They would like this information to be refl ected in the MSG Foundation records so that their weekly installment can be correctly computed. The normal portion of this extended scenario shows this operation proceeding as expected. The abnormal portion of this scenario shows two possibilities. First, as in the previous scenario, the staff member may enter the mortgage number incorrectly. Second, the borrowers may not bring with them adequate documentation to support their claim regarding their income, in which case the requested change is not implemented. 

A third scenario ( Figure 13.18 ) is an instance of use case Estimate Funds Available for Week ( Figure 11.42 ). This scenario is directly derived from the description of the use case ( Figure 11.43 ). 

The scenarios of Figures 13.19 and 13.20 are instances of use case Produce a Report. Again, these scenarios are directly derived from the corresponding description of the use case ( Figure 11.39 ). The remaining scenarios are equally straightforward and are therefore left as an exercise (Problems 13.12 and 13.13). 

An MSG Foundation staff member wishes to determine the funds available for mortgages this week. 

1. For each investment, the information system extracts the estimated annual return on that investment. It sums the separate returns and divides the result by 52 to yield the estimated investment income for the week. 

2. The information system then extracts the estimated annual MSG Foundation operating expenses and divides the result by 52. 

3. For each mortgage: 

3.1 The information system computes the amount to be paid this week by adding the principal and interest payment to $\frac { 1 } { 5 2 }$ nd of the sum of the annual real-estate tax and the annual homeowner’s insurance premium. 

3.2 It then computes 28 percent of the couple’s current gross weekly income. 

3.3 If the result of Step 3.1 is greater than the result of Step 3.2, then it determines the mortgage payment for the week as the result of Step 3.2, and the amount of the grant for this week as the difference between the result of Step 3.1 and the result of Step 3.2. 

3.4 Otherwise, it takes the mortgage payment for this week as the result of Step 3.1, and there is no grant for the week. 

4. The information system sums the mortgage payments of Steps 3.3 and 3.4 to yield the estimated total mortgage payments for the week. 

5. It sums the grant payments of Step 3.3 to yield the estimated total grant payments for the week. 

6. The information system adds the results of Steps 1 and 4 and subtracts the results of Steps 2 and 5. This is the total amount available for mortgages for the current week. 

7. Finally, the software product prints the total amount available for new mortgages during the current week. 

FIGURE 13.19 A scenario of the Produce a Report use case. 

An MSG staff member wishes to print a list of all mortgages. 

1. The staff member requests a report listing al mortgages. 

## FIGURE 13.20 Another scenario of the Produce a Report use case.

An MSG staff member wishes to print a list of all investments. 

1. The staff member requests a report listing al investments. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/54ace6595085269bd52640c5fa9f94d21675237a8c7fa05ae9339d4d63c96350.jpg)


# The Initial Class Diagram: The MSG Foundation Case Study

The second step is class modeling. The aim of this step is to extract the entity classes, determine their interrelationships, and fi nd their attributes. The best way to start this step is usually to use the two-stage noun extraction method (Section 13.5.1). 

In Stage 1 we describe the software product in a single paragraph. In the case of the MSG Foundation case study, a way to do this is 

Weekly reports are to be printed showing how much money is available for mortgages. In addition, lists of investments and mortgages must be printed on demand. 

In Stage 2 we identify the nouns in this paragraph. For clarity, the nouns are printed in sans serif type. 

Weekly reports are to be printed showing how much money is available for mortgages. In addition, lists of investments and mortgages must be printed on demand. 

The nouns are report, money, mortgage, list, and investment . Nouns report and list are not long lived, so they are unlikely to be entity classes ( report will surely turn out to be a boundary class), and money is an abstract noun. This leaves two candidate entity classes, namely, Mortgage Class and Investment Class, as shown in Figure 13.21 , the fi rst iteration of the class diagram. 

Now we consider interactions between these two entity classes. Looking at the descriptions of use cases Manage an Investment and Manage a Mortgage ( Figures 11.31 and 11.33 , respectively) it appears that the operations performed on the two entity classes are likely to be very similar, namely, insertions, deletions, and modifi cations. Also, the second iteration of the description of use case Produce a Report ( Figure 11.39 ) shows all the members of both entity classes have to be printed on demand. In other words, Mortgage Class and Investment Class should probably be subclasses of some superclass. We will call that superclass Asset Class , because mortgages and investments are both assets of the MSG Foundation. The resulting second iteration of the class diagram is shown in Figure 13.22. 


FIGURE 13.21 The first iteration of the class diagram of the MSG Foundation case study.


<table><tr><td>Mortgage Class</td></tr><tr><td></td></tr></table>

<table><tr><td>Investment Class</td></tr><tr><td></td></tr></table>

FIGURE 13.22 The second iteration of the class diagram of the MSG Foundation case study. 

FIGURE 13.23 The eighth iteration of the use-case diagram of the MSG Foundation case study. The new use case, Manage an Asset, is shaded. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/4628ba0a5744778688f181ec2dc7a6f214594d4fb52acbdc96ea4f4def2488ab.jpg)


A useful side effect of constructing this superclass is that we can once again reduce the number of use cases. As shown in Figure 13.15 , we currently have fi ve use cases, including Manage a Mortgage and Manage an Investment. However, if we consider a mortgage or an investment to be a special case of an asset, we can combine the two use cases into a single use case, Manage an Asset. The eighth iteration of the use-case diagram is shown in Figure 13.23 . The new use case is shaded. Now the attributes are added, as shown in Figure 13.24. 

The phrase “iteration and in crementation” also includes the possibility of the need for a de crementation in what has been developed to date. There are two reasons for such a decrease. First, if a mistake is made, the best way to correct it may be to backtrack to an earlier version of the software product and fi nd a better way of performing the step that was incorrectly carried out. When backtracking, everything that was added in the course of the incorrect step now has to be removed. Second, as a consequence of reorganizing the models to date, one or more artifacts may have become superfl uous. Developing a software product is hard. It is therefore important to remove superfl uous use cases or other artifacts as soon as possible. 


FIGURE 13.24 Attributes added to the second iteration of the class diagram of the MSG Foundation case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/58befd52c63c42ed069718ff47039f8ae0543eb2714d7ec424491682093f2d97.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/48a84bfd32c95caf2a1ca58071d0b40c6c32ba2275628a6cbeef4345d2aa75de.jpg)


## The Initial Dynamic Model: The MSG Foundation Case Study

The third step in object-oriented analysis is dynamic modeling. In this step, a statechart is drawn that refl ects all the operations performed by or to that system, indi cating the events that cause the transition from state to state. The major source of information regarding the relevant operations is the scenarios. 

The statechart of Figure 13.25 refl ects the operations of the complete MSG Foundation case study. The solid circle on the top left represents the initial state, the starting point of the statechart. The arrow from the initial state leads us to the state labeled MSG Foundation Event Loop ; states other than the initial and fi nal states are represented by rectangles with rounded corners. In state MSG Foundation Event Loop , one of fi ve events can occur. In more detail, an MSG staff member can issue one of fi ve commands: estimate funds for the week, manage an asset, update esti mated annual operating expenses, produce a report, or quit. These possibilities are indicated by the fi ve events estimate funds for the week selected, manage an asset selected, update estimated annual operating expenses selected, produce a report selected, and quit selected . (An event causes a transition between states.) 


FIGURE 13.25 The initial statechart of the MSG Foundation case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/9e2945069070ba40b71f8462cd254e747557f408372812f8598b47806c2ba739.jpg)


When the system is in state MSG Foundation Event Loop , any one of the fi ve events may occur, depending on which option the MSG staff member selects from the menu, shown in Figure 13.26 , that will be incorporated in the target software product. [The C++ and Java implementations of the MSG Foundation case study given in Appendices H and I, respectively, use a textual interface rather than a graphical user interface (GUI). That is, instead of clicking on a box, as shown in Figure 13.26 , the user types in a choice, as shown in Figure 13.27 . For example, the user types 1 to Estimate funds available for week, 2 to Manage an asset , and so on. The reason the implementations in Appendices H and I use a textual interface, such as Figure 13.27 , is that a textual interface can be run on all computers; a GUI generally needs special software.] 

Suppose that the MSG staff member clicks on the choice Manage an asset in the menu of Figure 13.26 . The event manage an asset selected (second from the left below the MSG Foundation Event Loop box in Figure 13.25 ) has now occurred, so the system moves from its current state, MSG Foundation Event Loop , to the state Managing An Asset . The operations that the MSG staff member can perform in this state, namely, Add, delete, or modify a mortgage or investment , appear below the line in the box with rounded corners. 

FIGURE 13.26 Menu in the target MSG Foundation case study. 

FIGURE 13.27 Textual version of the menu of Figure 13.26 . 

Click on your choice: 

MAIN MENU 

Estimate funds for the week 

MARTHA STOCKTON GREENGAGE FOUNDATION 

Manage an asset 

1. Estimate funds available for week 

2. Manage an asset 

Update estimated annual operating expenses 

3. Update estimated annual operating expenses 

4. Produce a report 

Produce a report 

5. Quit 

Quit 

Type your choice and press <ENTER>: 

Once the operation has been performed, the system returns to the state MSG Foundation Event Loop , as shown by the arrows. The behavior of the rest of the statechart is equally straightforward. 

In summary, the software product moves from state to state. In each state, the MSG staff member can perform the operations supported by that state, as listed below the line in the box with rounded corners that represents the state. This continues until the MSG staff member clicks on menu choice Quit when the software product is in the state MSG Foundation Event Loop . At this time the software product enters the fi nal state (represented by the white circle containing the small black circle). When this state is entered, execution of the statechart terminates; recall that the statechart is a model of the execution of the target software product. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/2aebee1d95f35fb8bce51556d49494990a4bd22d7a8843d3b8a424c8170b1c9c.jpg)


## Revising the Entity Classes: The MSG Foundation Case Study

The initial functional model, the initial class diagram, and the initial dynamic model have now been completed. However, a check of all three models reveals that something has been overlooked. 

Look at the initial statechart of Figure 13.25 and consider state Updating Estimated Annual Operating Expenses with operation Update the estimated annual operating expenses . This operation has to be performed on data, namely, the current value of the estimated annual operating expenses. But where is the value of the estimated annual operating expenses to be found? Looking at Figure 13.24 , it would have been a serious error to have it as an attribute of Asset Class or either of its subclasses. On the other hand, currently there is only one class Asset Class ) and its two subclasses. This means that the only way a value can be stored on a long-term basis is as an attribute of an instance of that class or its subclasses. 

The solution is obvious: Another entity class is needed in which the value of the estimated annual operating expenses can be stored. In fact, other values need to be stored as well; the result is shown in Figure 13.28 . A new class, MSG Application Class , has been introduced in which the various attributes shown in the top box in the fi gure can be stored. In addition, the MSG Application Class will be assigned the task of starting the execution of the rest of the software product. 

Now the class diagram of Figure 13.28 is redrawn to refl ect the stereotypes. This is shown in Figure 13.29 . All four classes are entity classes. The entity classes seem to be correct, at least for now. The next step is to determine the boundary classes and control classes. 


FIGURE 13.28 The third iteration of the class diagram of the MSG Foundation case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/7186c8613dc33ff0111a499abdcbb7a2ea290c4d9cef83bdb6302e73b52586ac.jpg)


FIGURE 13.29 Figure 13.28 redrawn to show the stereotypes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/44889beb05f210e09e4a107c56bfc0681dc206aa18dc77c3791d1490eec72a56.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/ef841527c2d4463fc0ca44a90ca86ebbc83252ef4eaaa4e5749a28f09ba25243.jpg)


# Extracting the Boundary Classes:13.13 The MSG Foundation Case Study

Extracting entity classes is usually considerably harder than extracting boundary classes. After all, entity classes generally have interrelationships, whereas each input screen, output screen, and printed report is usually modeled by an (independent) boundary class, as pointed out in Section 13.8. 

In view of the fact that the target MSG Foundation software product appears to be relatively straightforward (at least at this early stage of the Unifi ed Process), it is reasonable to try to have just one screen that the MSG staff member can use for all four use cases: Estimate Funds Available for Week, Manage an Asset, Update Estimated Annual Operating Expenses, and Produce a Report. As more is learned about the MSG Foundation, it is certainly possible that this one screen may have to be refi ned into two or more screens. But the initial clas extraction has just the one screen class, User Interface Class. 

There are three reports that have to be printed, the estimated funds for the week report and the two asset reports, namely, the complete listing of all mortgages or of all investments. Each of these has to be modeled by a separate boundary class because the content of each report is different. The four corresponding initial bound ary classes are then User Interface Class, Estimated Funds Report Class, Mortgages Report Class , and Investments Report Class . These four classes are displayed in Figure 13.30 . 

FIGURE 13.30 The initial boundary classes of the MSG Foundation case study. 

User Interface Class Estimated Funds Report Class Mortgages Report Class Investments Report Class 

Estimate Funds for Week Class 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/5d9718634b69212582ebb67c4d681d0db14c51dfeddcdf94863319f2cf1608a9.jpg)


## Extracting the Control Classes:13.14 The MSG Foundation Case Study

Control classes are generally as easy to extract as boundary classes because each nontrivial computation is almost always modeled by a control class, as stated in Section 13.8. For the MSG Foundation case study, there is just one computation, namely, estimating the funds available for the week. This yields the initial control class Estimate Funds for Week Class shown in Figure 13.31. 

The next step is to check all three sets of classes: entity classes, boundary classes, and control classes. Careful examination of the classes yields no obvious discrepan cies. Having completed class extraction, we now return to the Unifi ed Process. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/c91204cd7a577ba497bec97461fda832622eeacbf3709384a462325a3d10c279.jpg)


## Use-Case Realization:13.15 The MSG Foundation Case Study

A use case is a description of an interaction between an actor and the software product. Use cases are fi rst utilized at the beginning of the software life cycle, that is, in the requirements workfl ow. During the analysis and design workfl ows, more details are added to each use case, including a description of the classes involved in carrying out the use case. This process of extending and refi ning use cases is called use-case realization . Finally, during the implementation workfl ow, the use cases are implemented in code. 

This terminology is somewhat confusing, because the verb realize can be used in at least three different senses: 

• Understand (“Harvey slowly began to realize that he was in the wrong classroom”). 

• Receive (“Ingrid will realize a profit of $45,000 on the stock transaction”). 

• Accomplish (“Janet hopes to realize her dream of starting a software development organization”). 

In the phrase realize a use case , the word realize is used in this last sense; that is, it means to accomplish (or achieve ) the use case. 

An interaction diagram (sequence diagram or communication diagram) depicts the realization of a specifi c scenario of the use case. We fi rst consider the use case Estimate Funds Available for Week. 

FIGURE 13.32 The Estimate Funds Available for Week use case. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/869eb8922860cad2d7b809e3785e9646b80a386058c9a81b4e529a3aa730bf2a.jpg)


13.15.1 Estimate Funds Available for Week Use Case The use-case diagram of Figure 13.23 shows all the use cases. These include Estimate Funds Available for Week, which is shown separately in Figure 13.32 . The description of that use case was given in Figure 11.43 , which is reproduced here as Figure 13.33 for convenience. From the description we deduce that, as refl ected in the class diagram of Figure 13.34 , the classes that enter into this use case are User Interface Class , which models the user interface; Estimate Funds for Week Class , the control class that models the computation of the estimate of the funds that are available to fund mortgages during that week; Mortgage Class , which models the estimated grants and payments for the week; Investment Class , which mod els the estimated return on investments for the week; MSG Application Class , which models the estimated operating expenses for the week; and Estimated Funds Report Class, which models the printing of the report. 

Figure 13.34 is a class diagram. That is, it shows the classes that participate in the realization of the use case and their relationships. A working software product, on the other hand, uses objects rather than classes. For example, a specifi c mortgage cannot be represented by Mortgage Class but rather by an object, a specifi c instance of Mortgage Class , denoted by : Mortgage Class . Also, the class diagram of Figure 13.34 shows the participating classes in the use case and their relationships; it does not show the sequence of events as they occur. Something more is needed to model a specifi c scenario such as the scenario of Figure 13.18 , reproduced here as Figure 13.35 . 

Now consider Figure 13.36 . This fi gure is a communication diagram (“collaboration diagram” in older versions of UML). It therefore shows the objects that interact as well as the messages that are sent, numbered in the order in which they are sent. A communication diagram depicts a realization of a specifi c scenario of a use case. In this case, Figure 13.36 depicts the scenario of Figure 13.35 . In more detail, in the scenario the staff member wants to compute the funds available for the week. This is represented by message 1: Request estimate of funds available for week from MSG Staff Member to : User Interface Class , an instance of User Interface Class . 

Next, this request is passed on to : Estimate Funds for Week Class , an instance of the control class that actually performs the calculation. This is represented by message 2: Transfer request. 

Four separate fi nancial estimates are now determined by : Estimate Funds for Week Class . In step 1 of the scenario ( Figure 13.35 ), the estimated annual return on investments is summed for each investment and the result divided by 52. Thi extraction of the estimated weekly return is modeled in Figure 13.36 by message 3: Request estimated return on investments for week from : Estimate Funds for Week Class to : Investment Class followed by message 4: Return estimated weekly return on investments in the reverse direction, that is, back to the object that is controlling the computation. 


FIGURE 13.33 The description of the Estimate Funds Available for Week use case.


<table><tr><td>Brief DescriptionThe Estimate Funds Available for Week use case enables an MSG Foundation staff member to estimate how much money the Foundation has available that week to fund mortgages.</td></tr><tr><td>Step-by-Step Description1. For each investment, extract the estimated annual return on that investment.Summing the separate returns and dividing the result by 52 yields the estimated investment income for the week.2. Determine the estimated MSG Foundation operating expenses for the week by extracting the estimated annual MSG Foundation operating expenses and dividing by 52.3. For each mortgage:3.1 The amount to be paid this week is the total of the principal and interest payment and <eq>\frac{1}{52}</eq>nd of the sum of the annual real-estate tax and the annual homeowner’s insurance premium.3.2 Compute 28 percent of the couple’s current gross weekly income.3.3 If the result of Step 3.1 is greater than the result of Step 3.2, then the mortgage payment for this week is the result of Step 3.2, and the amount of the grant for this week is the difference between the result of Step 3.1 and the result of Step 3.2.3.4 Otherwise, the mortgage payment for this week is the result of Step 3.1, and there is no grant this week.4. Summing the mortgage payments of Steps 3.3 and 3.4 yields the estimated total mortgage payments for the week.5. Summing the grant payments of Step 3.3 yields the estimated total grant payments for the week.6. Add the results of Steps 1 and 4 and subtract the results of Steps 2 and 5. This is the total amount available for mortgages for the current week.7. Print the total amount available for new mortgages during the current week.</td></tr></table>

In step 2 of the scenario ( Figure 13.35 ), the weekly operating expenses are estimated by taking the estimated annual operating expenses and dividing by 52. This extraction of the weekly return is modeled in Figure 13.36 by message 5: Request estimated operating expenses for week from : Estimate Funds for Week Class to : MSG Application Class followed by message 6: Return estimated operating expenses for week in the other direction. 

In steps 3, 4, and 5 of the scenario ( Figure 13.35 ), two estimates are determined, namely the estimated grants for the week and the estimated payments for the week. This is modeled in Figure 13.36 by message 7: Request estimated grants and 

FIGURE 13.34 Class diagram showing the classes that realize the Estimate Funds Available for Week use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/b9fb0479435f98a58a4b9ad74ba19ac8e0584c14387c00371d4dcafe03810f54.jpg)



FIGURE 13.35 A scenario of the Estimate Funds Available for Week use case.


<table><tr><td>An MSG Foundation staff member wishes to determine the funds available for mortgages this week.</td></tr><tr><td>1. For each investment, the information system extracts the estimated annual return on that investment. It sums the separate returns and divides the result by 52 to yield the estimated investment income for the week.</td></tr><tr><td>2. The information system then extracts the estimated annual MSG Foundation operating expenses and divides the result by 52.</td></tr><tr><td>3. For each mortgage:</td></tr><tr><td>3.1 The information system computes the amount to be paid this week by adding the principal and interest payment to <eq>\frac{1}{52}</eq>nd of the sum of the annual real-estate tax and the annual homeowner’s insurance premium.</td></tr><tr><td>3.2 It then computes 28 percent of the couple’s current gross weekly income.</td></tr><tr><td>3.3 If the result of Step 3.1 is greater than the result of Step 3.2, then it determines the mortgage payment for the week as the result of Step 3.2, and the amount of the grant for this week as the difference between the result of Step 3.1 and the result of Step 3.2.</td></tr><tr><td>3.4 Otherwise, it takes the mortgage payment for this week as the result of Step 3.1, and there is no grant for the week.</td></tr><tr><td>4. The information system sums the mortgage payments of Steps 3.3 and 3.4 to yield the estimated total mortgage payments for the week.</td></tr><tr><td>5. It sums the grant payments of Step 3.3 to yield the estimated total grant payments for the week.</td></tr><tr><td>6. The information system adds the results of Steps 1 and 4 and subtracts the results of Steps 2 and 5. This is the total amount available for mortgages for the current week.</td></tr><tr><td>7. Finally, the software product prints the total amount available for new mortgages during the current week.</td></tr></table>

FIGURE 13.36 A communication diagram of the realization of the scenario of Figure 13.35 of the Estimate Funds Available for Week use case of the MSG Application case study 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/32cb5a853d7e88178231fedeb27c8a6e0c6db6209d23e1f10f2da12c84a0a224.jpg)


payments for week from : Estimate Funds for Week Class to : Mortgage Class and by message 8: Return estimated grants and payments for week in the reverse direction. 

Now the arithmetic computation of step 6 of the scenario is performed. This is mod eled in Figure 13.36 by message 9: Compute estimated amount available for week. This is a self call, that is, : Estimate Funds for Week Class tells itself to perform the calculation. The result of the computation is stored in : MSG Application Class by message 10: Transfer estimated amount available for week . 

Next, the result is printed in step 7 of the scenario ( Figure 13.35 ). This is modeled in Figure 13.36 by message 11: Print estimated amount available from : MSG Application Class to : Estimated Funds Report Class. 

Finally, an acknowledgment is sent to the MSG staff member that the task has been successfully completed. This is modeled in Figure 13.36 by messages 12: Send successful completion message, 13: Send successful completion message, 14: Transfer successful completion message, and 15: Display successful completion message . 

FIGURE 13.37 The flow of events of the communication diagram of Figure 13.36 of the realization of the scenario of Figure 13.35 of the Estimate Funds Available for Week use case of the MSG Application case study. 

An MSG staff member requests an estimate of the funds available for mortgages for the week (1, 2). The information system estimates the return on investments for the week (3, 4), the operating expenses for the week (5, 6), and the grants and payments for the week (7, 8). Then it estimates (9), stores (10), and prints out (11–15) the funds available for the week. 

No client is going to approve the specifi cation document unless he or she understands precisely what the proposed software product will do. For this reason, a written description of the communication diagram is essential. This is shown in Figure 13.37 , the flow of events . Finally, the equivalent sequence diagram of the realization of the scenario is shown in Figure 13.38 . When constructing a software product, either a communication diagram or a sequence diagram may prove to give better insight of a realization of a use case. In some situations, both are needed to get a full under standing of a specifi c realization of a given use case. That is why, in this chapter, every communication diagram is followed by the equivalent sequence diagram. The sequence diagram of Figure 13.38 is fully equivalent to the communication diagram of Figure 13.36 , so its fl ow of events is also shown in Figure 13.37 . 

The strength of a sequence diagram is that it shows the fl ow of messages unambiguously. The order of the messages is particularly clear, as are the sender and receiver of each individual message. So, when the transfer of information is the focus of attention (which is the case for much of the time when performing the analysis workfl ow), a sequence diagram is superior to a communication diagram. On the other hand, the similarity between a sequence diagram (such as Figure 13.38 ) and the communication diagram that realizes the relevant scenario (such as Figure 13.36 ) is strong. Accordingly, on those occasions when the developers are concentrating on the classes, a communication diagram is generally more useful than the equivalent sequence diagram. 

Summarizing, Figures 13.32 through 13.38 do not depict a random collection of UML artifacts. On the contrary, these fi gures depict a use case and artifacts derived from that use case. In more detail: 

• Figure 13.32 depicts the use case Estimate Funds Available for Week. That is, Figure 13.32 models all possible sets of interactions, between the actor MSG Staff Member (an entity that is external to the software product) and the MSG Foundation software product itself, that relate to the action of estimating funds available for the week. 

• Figure 13.33 is the description of that use case; that is, it provides a written account of the details of the Estimate Funds Available for Week use case of Figure 13.32 . 

• Figure 13.34 is a class diagram showing the classes that realize the Estimate Funds Available for Week use case. The class diagram depicts the classes that are needed to model all possible scenarios of the use case, together with their interactions. 

FIGURE 13.38 A sequence diagram of the realization of the scenario of Figure 13.35 of the Estimate Funds Available for Week use case of the MSG Application case study. This sequence diagram is fully equivalent to the communication diagram of Figure 13.36, so its fl ow of events is also shown in Figure 13.37. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/b46fa17bb347f3efc6c95bf9cba1883761680e6df34207beb48ea6c24df8955a.jpg)


FIGURE 13.39 The Manage an Asset use case. 

• Figure 13.35 is a scenario, that is, one specific instance of the use case of Figure 13.32 . 

• Figure 13.36 is a communication diagram of the realization of the scenario of Figure 13.35 ; that is, it depicts the objects and the messages sent between them in the realization of that one specifi c scenario. 

• Figure 13.37 is the flow of events of the communication diagram of the realization of the scenario of Figure 13.35 . That is, just as Figure 13.33 is a written description of the Estimate Funds Available for Week use case of Figure 13.32 , Figure 13.37 is a written description of the realization of the scenario of Figure 13.35. 

• Figure 13.38 is the sequence diagram that is fully equivalent to the communication diagram of Figure 13.36 . That is, the sequence diagram depicts the objects and the messages sent between them in the realization of the scenario of Figure 13.35 . Its fl ow of events is therefore also shown in Figure 13.37 . 

It has been stated many times in this book that the Unifi ed Process is use-case driven. These bulleted items explicitly state the precise relationship between each of the artifacts of Figures 13.33 through 13.38 and the use case of Figure 13.32 that underlies each of them. 

## 13.15.2 Manage an Asset Use Case

The Manage an Asset use case is shown in Figure 13.39 and its description in Figure 13.40 . A class diagram showing the classes that realize the Manage an Asset use case is shown in Figure 13.41 . Initially it was assumed that only one control 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/222a65027de6e24952081e62ac5b8845424ce0f9787bf4e1a6a70ace87b90c68.jpg)


## Brief Description

The Manage an Asset use case enables an MSG Foundation staff member to add and delete assets and manage the portfolio of assets (investments and mortgages). Managing a mortgage includes updating the weekly income of a couple who have borrowed money from the Foundation. 

## Step-by-Step Description

1. Add, modify, or delete an investment or mortgage, or update the borrower's weekly income 

FIGURE 13.41 A class diagram showing the classes that realize the Manage an Asset use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/fd2d1037abe76574d74800273403057eec0fdf41db2a3b7301c3928aa0dfe021.jpg)


FIGURE 13.42 A scenario of the Manage an Asset use case. 

An MSG Foundation staff member wants to update the annual real-estate tax on a home for which the Foundation has provided a mortgage. 

1. The staff member enters the new value of the annual realestate tax. 

2. The information system updates the date on which the annua real-estate tax was last changed. 

class was needed (see Figure 13.31 ). However, Figure 13.41 shows that a second control class, Manage an Asset Class , is required; additional control classes may have to be added in subsequent iterations. 

The normal part of the extended scenario of Figure 13.16 of the use case Manage a Mortgage (and hence of Manage an Asset) is reproduced as Figure 13.42 . In this scenario, an MSG staff member updates the annual realestate tax on a mortgaged home and the software product updates the date on which the tax was last changed. Figure 13.43 is the communication diagram of this scenario. Notice that object : Investment Class does not play an active role in this communication diagram because the scenario of Figure 13.42 does not 

FIGURE 13.43 A communication diagram of the realization of the scenario of Figure 13.42 of the Manage an Asset use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/ba65ca0aa8d349b16f9e2396bd293acd503b8884d523b89746f440a4a3d42827.jpg)


involve an investment, only a mortgage. Also, the Borrowers do not play a role in this scenario either. The fl ow of events is left as an exercise (Problem 13.14). The sequence diagram equivalent to the communication diagram of Figure 13.43 is shown in Figure 13.44 . 

Now consider a different scenario of the use case Manage an Asset ( Figure 13.39 ), namely, the extended scenario of Figure 13.17 , the normal part of which is repro duced here as Figure 13.45 . In this scenario, at the request of the borrowers, the MSG staff member updates the weekly income of a couple who have an MSG mortgage. As explained in Section 11.7, the scenario is initiated by the Borrowers , and their data are entered into the software product by the MSG Staff Member , as stated in the note in the communication diagram of Figure 13.46 . The fl ow of events is again left as an exercise (Problem 13.15). The equivalent sequence diagram is shown in Figure 13.47 . 

FIGURE 13.44 A sequence diagram of the realization of the scenario of Figure 13.42 of the Manage an Asset use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/3e86b0b926fb0fc88aa3751f7c3110d82d0e9c73ce15650ea44a89a8ccf56f37.jpg)



FIGURE 13.45 A second scenario of the Manage an Asset use case.


There is a change in the weekly income of a couple who have borrowed money from the MSG Foundation. They wish to have their weekly income updated in the Foundation records by an MSG staff member so that their mortgage payments will be correctly computed. 

1. The staff member enters the new value of the weekly income. 

2. The information system updates the date on which the weekly income was last changed. 

Comparing the interaction diagrams of Figures 13.43 and 13.46 (or, equivalently, the sequence diagrams of Figures 13.44 and 13.47 ), we see that, other than the actors involved, the only other difference between the two diagrams is that messages 1, 2, and 3 involve annual real-estate tax in the case of Figure 13.43 (or Figure 13.44 ) and weekly income in the case of Figure 13.46 (or Figure 13.47 ). This example highlights the difference between a use case, scenarios (instances of the use case), and communication or sequence diagrams of the realization of different scenarios of that use case. 

Boundary class User Interface Class appears in all the realizations considered so far. In fact, the same screen will be used for all commands of the software product. 

FIGURE 13.46 A communication diagram of the realization of the scenario of Figure 13.45 of the Manage an Asset use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/94de0c9016fd318657b1dfe2938b5ebf805d00954d4dc8f2ff84e3861bd18c82.jpg)


An MSG staff member clicks on the appropriate operation in the revised menu of Figure 13.48 . (The corresponding textual interface, as implemented in Appendices H and I, is given in Figure 13.49 .) 

## 13.15.3 Update Estimated Annual Operating Expenses Use Case

The use case Update Estimated Annual Operating Expenses is shown in Figure 11.17 with a description in Figure 11.18 . A class diagram showing the classes that realize the Update Estimated Annual Operating Expenses use case appears in Figure 13.50 and a communication diagram of a realization of a scenario of the use case in Figure 13.51 . The equivalent sequence diagram is shown in Figure 13.52 . Details of the scenario and the fl ow of events are left as an exercise (Problems 13.16 and 13.17). 

FIGURE 13.47 A sequence diagram of the realization of the scenario of Figure 13.45 of the Manage an Asset use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/b996e9e98c8fde4818775f24ac77ccda8801e75586a52aed33ace3b5f300884f.jpg)



FIGURE 13.49 Textual version of the revised menu of Figure 13.48.


MARTHA STOCKTON GREENGAGE FOUNDATION 

1. Estimate funds available for week 

2. Manage a mortgage 

3. Manage an investment 

4. Update estimated annual operating expenses 

5. Produce a mortgages report 

6. Produce an investments report 

7. Quit 

Type your choice and press <ENTER>: 

FIGURE 13.50 A class diagram showing the classes that realize the Update Estimated Annual Operating Expenses use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/fd5413493bcf8fe609ab19eaef2f423999c129872f76e09d57d015c4a17ce081.jpg)


FIGURE 13.51 A communication diagram of the realization of a scenario of the Update Estimated Annual Operating Expenses use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/58b20ad854d94ea9f81229021d6091d4454fd7158ebebd42d24397de92bceb2c.jpg)


FIGURE 13.52 A sequence diagram of the realization of a scenario of the Update Estimated Annual Operating Expenses use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/52ede9ae71f9fe28178292fc8377899aa653ed2ccba6a9ca5fad6f16b05bb94e.jpg)


## 13.15.4 Produce a Report Use Case

Use case Produce a Report is shown in Figure 13.53 . The description of use case Produce a Report of Figure 11.39 is reproduced here as Figure 13.54 . A class diagram showing the classes that realize the Produce a Report use case is shown in Figure 13.55. 

FIGURE 13.53 The Produce a Report use case. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/d0f433d785f61856e5e7d1ce3a7fa40f97975e42b652574b3f46701ce8c4dc8f.jpg)



FIGURE 13.54 Description of the Produce a Report use case.


<table><tr><td>Brief DescriptionThe Produce a Report use case enables an MSG Foundation staff member to print a listing of all investments or all mortgages.</td></tr><tr><td>Step-by-Step Description1. The following reports must be generated:1.1 Investments report—printed on demand:The information system prints a list of all investments. For each investment,the following attributes are printed:Item numberItem nameEstimated annual returnDate estimated annual return was last updated1.2 Mortgages report—printed on demand:The information system prints a list of all mortgages. For each mortgage,the following attributes are printed:Account numberName of mortgageesOriginal price of homeDate mortgage was issuedPrincipal and interest paymentCurrent combined gross weekly incomeDate current combined gross weekly income was last updatedAnnual real-estate taxDate annual real-estate tax was last updatedAnnual homeowner&#x27;s insurance premiumDate annual homeowner&#x27;s insurance premium was last updated</td></tr></table>

FIGURE 13.55 A class diagram showing the classes that realize the Produce a Report use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/6e159a156216f08f6617b3784064b25f4a5d93fc932557091e66c763cbf2b799.jpg)


First consider the scenario of Figure 13.19 for listing all mortgages, reproduced here as Figure 13.56 . A communication diagram of the realization of this scenario is shown in Figure 13.57 . This realization models the listing of all mortgages. Accordingly, object : Investment Class , an instance of the other subclass of Asset Class , plays no role in this realization, and neither does : Investments Report Class . The fl ow of events is left as an exercise (Problem 13.18). The equivalent sequence diagram is shown in Figure 13.58. 

Now consider the scenario of Figure 13.20 for listing all investments, reproduced here as Figure 13.59 . A communication diagram of the realization of this scenario is shown in Figure 13.60 . As opposed to the previous realization, Figure 13.60 models 

FIGURE 13.56 A scenario of the Produce a Report use case. 

An MSG staff member wishes to print a list of al mortgages. 

1. The staff member requests a report listing all mortgages. 


FIGURE 13.57 A communication diagram of the realization of the scenario of Figure 13.56 of the Produce a Report use case of the MSG Foundation case study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/ce7c07493eaa051e755f5770eb4422e55a629bfa11213a45bc23ef4111eb1284.jpg)


FIGURE 13.58 A sequence diagram of the realization of the scenario of Figure 13.56 of the Produce a Report use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/0489dca5b2b6d26499cde496808aca5cb45f6d7e3e86ab0b364c00a5384a18ef.jpg)



FIGURE 13.59 Another scenario of the Produce a Report use case.


An MSG staff member wishes to print a list of all investments. 

1. The staff member requests a report listing al investments. 

the listing of the investments; mortgages are ignored here. The equivalent sequence diagram is shown in Figure 13.61. 

This concludes the realization of the four use cases of Figure 13.23 , the eighth iteration of the use-case diagram of the MSG Foundation case study. 

FIGURE 13.60 A communication diagram of the realization of the scenario of Figure 13.59 of the Produce a Report use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/f1784b85d53f3fc01edc8a296e59638c2a66bd628f1303d9d8f205eb4dc65f2a.jpg)


FIGURE 13.61 A sequence diagram of the realization of the scenario of Figure 13.59 of the Produce a Report use case of the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/19a0e7650f0237317576f9012aec61700c81b6683191e00961091fa9a5a72b14.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/0151b7893eeb6126ff74a5d11c916b64aad35dfa398fc7bf863950b69da082ff.jpg)


# Incrementing the Class Diagram: The MSG Foundation Case Study

The entity classes were extracted in Sections 13.9 through 13.12, yielding Figure 13.29, which shows four entity classes. The boundary classes were extracted in Section 13.13 and the control classes in Sections 13.14 and 13.15.2. In the course of realizing the various use cases in Section 13.15, interrelationships between many of the classes became apparent; these interrelationships are refl ected in the class diagrams of Figures 13.34 , 13.41 , 13.50 , and 13.55 . Figure 13.62 combines these class diagrams. 

Now the class diagrams of Figures 13.29 and 13.62 are combined to yield the fourth iteration of the class diagram of the MSG Foundation case study, shown in 

FIGURE 13.62 Class diagram combining the class diagrams of 13.34, 13.41, 13.50, and 13.55. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/83300e91b22ce37c435502af712cee231ce1744403ab0f1cf2532324bc85ca35.jpg)


FIGURE 13.63 The fourth iteration of the class diagram of the MSG Foundation case study, obtained by combining the class diagrams of Figures 13.29 and 13.62. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/02943c9a416b4899406c93e9e5d0af248c6c089dad2727c707829387748c681b.jpg)


Figure 13.63 . More specifi cally, starting with Figure 13.62 , Asset Class of Figure 13.29 is added. Then the two inheritance (generalization) relationships in Figure 13.29 are drawn in; they are shown with dashed lines to distinguish them. The result, Figure 13.63, the fourth iteration of the class diagram, is the class diagram at the end of the analysis workfl ow. 

The last step of the analysis workfl ow of the MSG Foundation case study is to draw up the software project management plan (this is done during the elaboration phase; see Section 3.10.2). Appendix F contains a software project management plan for the development of the MSG Foundation product by a small (three-person) software organization. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/9be822c38db27a3e2b7dac8d101b6b74a882b46b31b44e037572c8a1d30beec8.jpg)


# The Test Workfl ow: The MSG Foundation Case Study

The analysis workfl ow of the MSG Foundation case study is checked in two ways. First the entity classes are checked using CRC cards, as described in Section 13.7. Then all the artifacts of the analysis workfl ow are inspected (Section 6.2.3). This concludes the analysis workfl ow of the MSG Foundation case study. 

## 13.18 The Specifi cation Document in the Unifi ed Process

A primary goal of the analysis workfl ow is to produce the specifi cation document , but at the end of Section 13.17 it was claimed that the analysis workfl ow is now complete. The obvious question is, Where is the specifi cation document? 

The short answer is, the Unifi ed Process is use-case driven. In more detail, the use cases and the artifacts derived from them contain all the information that, in the traditional paradigm, appears in the specifi cation document in text form, and more. 

For example, consider the use case Estimate Funds Available for Week. When the requirements workfl ow is performed, the Estimate Funds Available for Week use case ( Figure 11.27 ) and its description ( Figure 11.40 ) are shown to the client, the trustees of the MSG Foundation. The developers must be meticulous in ensuring that the trustees fully understand these two artifacts and agree that these artifacts accurately model the software product the Foundation needs. Then, during the analysis workfl ow, the trustees are shown the use case Estimate Funds Available for Week ( Figure 13.32 ), its description ( Figure 13.33 ), the class diagram showing the classes that realize the use case ( Figure 13.34 ), a scenario of the use case ( Figure 13.35 ), the interaction diagrams of the realization of a scenario of the use case ( Figures 13.36 and 13.38 ), and the fl ow of events of these interaction diagrams ( Figure 13.37 ). 

The set of artifacts just listed all appertain to only the use case Estimate Funds Available for Week. As shown in Figure 13.23 , there are four use cases altogether. The same set of artifacts are produced for each of the scenarios of each of the use cases. The resulting collection of artifacts, some diagrammatic and some textual, convey to the client more information more accurately than the purely textual specifi cation document of the traditional paradigm possibly could. 

The traditional specifi cation document usually plays a contractual role. That is, once it has been signed by both the developers and the client, it essentially constitutes a legal document. If the developers build a software product that satisfi es the specifi cation document, the client is obligated to pay for the software product, and conversely, if the product does not conform to its specifi cation document, the developers are required to fi x it if they want to get paid. In the case of the Unifi ed Process, the collection of artifacts of all the scenarios of all the use cases similarly constitutes a contract. Therefore, as claimed at the end of Section 13.17, the analysis workfl ow of the MSG Foundation case study i indeed complete. 

As stated before, the Unifi ed Process is use-case driven. When using the Unifi ed Process, instead of constructing a rapid prototype, the use cases, or more precisely, interaction diagrams refl ecting the classes that realize the scenarios of the use cases, are shown to the client. The client can understand how the target software product will behave just as well from the interaction diagrams and their written fl ow of events as from a rapid prototype. After all, a scenario is a particular execution sequence of the proposed software product, as is each execution of the rapid prototype. The difference is that the rapid prototype is generally discarded, whereas the use cases are successively refi ned, with more information added each time. 

However, there is one area where a rapid prototype is superior to a scenario, the user interface. This does not mean that a rapid prototype should be built just so that specimen screens and reports can be examined by the client and users. But specimen screens and reports need to be constructed, as described in Section 11.13, preferably with the aid of CASE tools such as screen generators and report generators (Section 5.5). 

In Section 13.19, methods for determining actors and use cases are provided. 

## 13.19 More on Actors and Use Cases

As stated in Section 11.4.3, a use case depicts an interaction between the software product itself and the actors (the users of that software product). Now that a number of examples of actors and use cases have been presented, it is appropriate to describe how to fi nd actors and use cases. 

To fi nd the actors, we have to consider every role in which an individual can interact with the software product. For example, consider a couple who wish to obtain a mortgage from the MSG Foundation. When they apply for the mortgage, they are Applicants , whereas after their application has been approved and money to buy their home loaned to them, they become Borrowers . In other words, actors are not so much individuals as roles played by those individuals. In our example, the actors are not the couple, but rather fi rst the couple playing the role of Applicants and then the couple playing the role of Borrowers . This means that merely listing all the individuals who will use the software product is not a satisfactory way of fi nding the actors. Instead, we need to fi nd all the roles played by each user (or group of users). From the list of roles we can extract the actors. 

In the terminology of the Unifi ed Process, the term worker is used to denote a particular role played by an individual. This is a somewhat unfortunate term, because the word worker usually refers to an employee. In the terminology of the Unifi ed Process, in the case of a couple with a mortgage, Applicants and Borrowers are two different workers. In this book, in the interests of clarity the word role is used in place of worker . 

Within a business context, the task of fi nding the roles is generally straightforward. The use-case business model usually displays all the roles played by the individuals who interact with the business, thereby highlighting the business actors. We then fi nd the subset of 

## How to Perform Object-Oriented Analysis

## • Iterate

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/38d116e64d8d9c28cb21792912fba9ec18fa0a9f21a97aa0d38b0c087643fc65.jpg)


• Extract the boundary classes and control classes. 

• Refi ne the use cases. 

• Perform use-case realization. 

the use-case business model that corresponds to the use-case model of the requirements. In more detail, 

1. Construct the use-case business model by fi nding all the roles played by the individuals who interact with the business 

2. Find the subset of the use-case diagram of the business model that models the software product we wish to develop. That is, consider only those parts of the business model that correspond to the proposed software product. 

Once the actors have been determined, fi nding the use cases is generally straightforward. For each role, there are one or more use cases. So, the starting point in fi nding the use cases of the requirements is fi nding the actors, as described in this section. 

How to Perform Box 13.1 summarizes object-oriented analysis. 

## 13.20 CASE Tools for the Object-Oriented Analysis Workfl ow

Bearing in mind the role played by diagrams in object-oriented analysis, it is not surprising that a number of CASE tools have been developed to support object-oriented analysis. In its basic form, such a tool is essentially a drawing tool that makes it easy to perform each of the modeling steps. More important, it is far simpler to modify a diagram constructed with a drawing tool than to attempt to change a hand-drawn fi gure. Accordingly, a CASE tool of this type supports the graphical aspects of object-oriented analysis. In addition, some tools of this type not only draw all the relevant diagrams but CRC cards as well. A strength of these tools is that a change to the underlying model is refl ected automatically in all the affected diagrams; after all, the various diagrams are merely different views of the underlying model. 

On the other hand, some CASE tools support not just object-oriented analysis but a considerable portion of the rest of the object-oriented life cycle as well. Nowadays virtually all of these tools support UML [Rumbaugh, Jacobson, and Booch, 1999]. Examples of such tools include IBM Rational Rose and Together. ArgoUML is a typical open-source CASE tool of this type. 

## 13.21 Metrics for the Object-Oriented Analysis Workfl ow

As with the other core workfl ows, during object-oriented analysis it is essential to measure the fi ve fundamental metrics: size, cost, duration, effort, and quality. One measure of the size of the object-oriented analysis is the number of pages of UML diagrams; this metric can be used to compare different projects. 

With regard to quality, as with classical analysis, it is essential to keep accurate fault statistics. Also, the rate at which faults are detected can give a measure of the effi ciency of the inspection process. 

## 13.22 Challenges of the Object-Oriented Analysis Workfl ow

Object-oriented analysis is a specifi c approach to analysis, so the challenges of classical analysis described in Section 12.16 apply equally to object-oriented analysis. In particular, the second challenge listed in that section is that it is easy to cross the boundary line between specifi cations (what) and design (how). This danger is especially acute in the case of object-oriented analysis. 

Recall that, as described in Section 1.9, the transition from object-oriented analysis to object-oriented design is far smoother than the transition in the classical paradigm from the analysis phase to the design phase. In the classical paradigm, an initial task of the design phase is to decompose the product into modules. In contrast, the classes, the “modules” of the object-oriented design workfl ow, are extracted during the object-oriented analysis workfl ow, ready for refi nement during the object-oriented design workfl ow. The presence of classes from early in the OOA workfl ow means that the temptation to carry the OOA too far can be extremely strong. 

For example, consider the issue of allocation of methods to classes. One task of the classical analysis phase is to determine the data and operations of the target product. However, allocation of the various operations to specifi c modules should be delayed until the classical design phase, because as pointed out in Section 12.16, we fi rst have to determine how the product as a whole is broken down into modules. 

In the object-oriented paradigm, however, this latter task is part of the analysis workfl ow. That is, during the object-oriented analysis workfl ow, we determine the modules (classes) and their interactions; the result is depicted in the class diagram. Therefore, there is no apparent reason why we should wait until the object-oriented design workfl ow before allocating methods to classes. 

Nevertheless, it is important to remember that object-oriented analysis is an iterative process. In the course of refi ning the various models, frequently large portions of the class diagram have to be reorganized. Reallocating the methods then results in unnecessary additional rework 

At each step of the OOA process it is a good idea to minimize the information that would have to be reorganized during iteration. Therefore, allocation of methods to classes should wait until the design workfl ow, no matter how tempting it may be to go just a little further during the object-oriented analysis workfl ow. 

Object-oriented analysis is introduced (Section 13.1). Extracting entity classes is described in Section 13.2. The technique is then applied to the elevator problem case study (Section 13.3); functional modeling, entity class modeling, and dynamic modeling are performed in Sections 13.4, 13.5, and 13.6, respectively. Next, object-oriented analysis aspects of the test workfl ow are covered in Section 13.7. Extraction of boundary and control classes is the subject of Section 13.8. The class extraction of the MSG Foundation case study is described in Section 13.9 (the initial functional model), Section 13.10 (the initial class diagram), Section 13.11 (the initial dynamic model), Section 13.12 (revision of the entity classes), Section 13.13 (extraction of the boundary classes), and Section 13.14 (extraction of the control classes). Application of the Unifi ed Process to the MSG Foundation case study resumes in Section 13.15 (realization of the use cases), Section 13.16 (class diagram incrementation), and Section 13.17 (test workfl ow). The specifi cation document for the Unifi ed Process is discussed in Section 13.18. Additional information regarding actors and use cases appears in Section 13.19. CASE tools and metrics for object-oriented analysis are described in Sections 13.20 and 13.21, respectively. The chapter concludes with a discussion of the challenges of the object-oriented analysis workfl ow (Section 13.22). 

An overview of the MSG Foundation case study for Chapter 13 appears in Figure 13.64 , and for the elevator problem in Figure 13.65. 


FIGURE 13.64 Overview of the MSG Foundation case study for Chapter 13.


<table><tr><td>Initial functional model</td><td>Section 13.9</td></tr><tr><td>Seventh iteration of the use-case diagram</td><td>Figure 13.15</td></tr><tr><td>Initial class diagram</td><td>Section 13.10</td></tr><tr><td>First iteration of the class diagram</td><td>Figure 13.21</td></tr><tr><td>Second iteration of the class diagram</td><td>Figure 13.22</td></tr><tr><td>Eighth iteration of the use-case diagram</td><td>Figure 13.23</td></tr><tr><td>Second iteration of the class diagram, with attributes added</td><td>Figure 13.24</td></tr><tr><td>Initial dynamic model</td><td>Section 13.11</td></tr><tr><td>Initial statechart</td><td>Figure 13.25</td></tr><tr><td>Revising the entity classes</td><td>Section 13.12</td></tr><tr><td>Third iteration of the class diagram</td><td>Figure 13.28</td></tr><tr><td>Extracting the boundary classes</td><td>Section 13.13</td></tr><tr><td>Extracting the control classes</td><td>Section 13.14</td></tr><tr><td>Use-case realization</td><td>Section 13.15</td></tr><tr><td>Estimate Funds Available for Week use case</td><td>Section 13.15.1</td></tr><tr><td>Manage an Asset use case</td><td>Section 13.15.2</td></tr><tr><td>Update Estimated Annual Operating Expenses use case</td><td>Section 13.15.3</td></tr><tr><td>Produce a Report use case</td><td>Section 13.15.4</td></tr><tr><td>Incrementing the class diagram</td><td>Section 13.16</td></tr><tr><td>Fourth iteration of the class diagram</td><td>Figure 13.63</td></tr></table>


FIGURE 13.65 Overview of the elevator problem case study for Chapter 13.


<table><tr><td>Object-oriented analysis</td><td>Section 13.3</td></tr><tr><td>Functional modeling</td><td>Section 13.4</td></tr><tr><td>Entity class modeling</td><td>Section 13.5</td></tr><tr><td>First iteration of the class diagram</td><td>Figure 13.5</td></tr><tr><td>Second iteration of the class diagram</td><td>Figure 13.6</td></tr><tr><td>Dynamic modeling</td><td>Section 13.6</td></tr><tr><td>First iteration of the statechart for the elevator controller</td><td>Figure 13.7</td></tr><tr><td>Test workflow</td><td>Section 13.7</td></tr><tr><td>Third iteration of the class diagram</td><td>Figure 13.10</td></tr><tr><td>Fourth iteration of the class diagram</td><td>Figure 13.12</td></tr><tr><td>First iteration of the statechart for the elevator subcontroller</td><td>Figure 13.13</td></tr></table>

## For Further Reading

Fusion [Coleman et al., 1994] is a second-generation OOA technique, a combination (or fusion) of a number of fi rst-generation techniques, including OMT [Rumbaugh et al., 1991] and Objectory [Jacobson, Christerson, Jonsson, and Overgaard, 1992]. The Unifi ed Software Development Process unifi es the work of Jacobson, Booch, and Rumbaugh [1999]. Catalysis is another important object-oriented methodology [D’Souza and Wills, 1999]. 

ROOM is an object-oriented methodology for real-time software [Selic, Gullekson, and Ward, 1995]. Further information on real-time object-oriented technologies can be found in [Awad, Kuusela, and Ziegler, 1996]. 

Full details regarding UML can be found in [Booch, Rumbaugh, and Jacobson, 1999] and [Rumbaugh, Jacobson, and Booch, 1999]. The October 1999 issue of Communications of the ACM contains a broad variety of papers on the use of UML. UML is now under the control of the Object Management Group; the latest version of UML will be found at the OMG Website, www.omg.org. 

The noun-extraction technique used in this chapter to extract candidate classes is formalized in [Juristo, Moreno, and López, 2000]. CRC cards were fi rst put forward in [Beck and Cunningham, 1989]. [Wirfs-Brock, Wilkerson, and Wiener, 1990] is a good source of information on CRC cards. 

A number of comparisons of object-oriented analysis techniques have been published, including [de Champeaux and Faure, 1992], [Monarchi and Puhr, 1992], and [Embley, Jackson, and Woodfi eld, 1995]. A comparison of both object-oriented and classical analysis techniques appears in [Fichman and Kemerer, 1992]. 

Management of iteration in object-oriented projects is described in [Williams, 1996]. Statecharts are described in [Harel and Gery, 1997]. The reuse of specifi cations in the object-oriented paradigm is described in [Bellinzona, Fugini, and Pernici, 1995]. 

A variety of papers on formal techniques for object-oriented software appear in the July 2000 issue of IEEE Transactions on Software Engineering. 

## Key Terms

abstract noun 411 entity class modeling 406 role 457 actor 407 event 431 scenario 406 analysis workfl ow 405 exception scenario 408 sequence diagram 435 attribute 411 fl ow of events 440 specifi cation backtrack 430 functional modeling 406 document 456 boundary class 405 interaction diagram 435 state 418 class diagram 411 legacy system 405 state variable 418 class–responsibility– millennium bug 405 statechart 414 collaboration (CRC) normal scenario 408 stereotype 406 cards 413 noun-extraction method 411 test workfl ow 417 communication object-oriented analysis transition 431 diagram 435 (OOA) 404 use case 407 control class 406 realize (in the Unifi ed Theory use-case realization 435 dynamic modeling 406 context) 435 worker 457 entity class 405 responsibility-driven design 408 Y2K problem 405 

## Problems <sup>1</sup>

13.1 Modify the scenario of Figure 13.11 to refl ect the fourth iteration of the class diagram of the elevator problem case study ( Figure 13.12 ). 

13.2 Develop a statechart for the Button Class shown in Figure 13.12 . 

13.3 Develop a statechart for the Elevator Class shown in Figure 13.12 . 

13.4 Develop a statechart for the Elevator Doors Class shown in Figure 13.12 . 

13.5 Construct a CRC card for the Floor Subcontroller Class shown in Figure 13.12 . 

13.6 Why must the fi nite state machine formalism of Section 12.7 be changed when used for objectoriented analysis? 

13.7 What is the latest point in the analysis workfl ow in which classes can be introduced without adversely affecting the project? 

13.8 What is the earliest point in the Unifi ed Process in which classes can meaningfully be introduced? 

13.9 Is it possible to represent the dynamic model using a formalism other than the statechart described in this chapter? Explain your answer. 

13.10 Why are the attributes of the classes but not the methods determined during object-oriented analysis? 

13.11 A noun-extraction process is described in Section 13.5.1. Why do we not also extract the verbs? And what about the other six parts of speech (adjectives, adverbs, conjunctions, interjections, prepositions, and pronouns)? 

13.12 Give an extended scenario of the use case Manage an Investment of Figures 11.30 and 11.31 . 

13.13 Give an extended scenario of the use case Update Estimated Annual Operating Expenses of Figures 11.17 and 11.18 . 

13.14 Give the fl ow of events of the interaction diagrams of Figures 13.43 and 13.44 . 

13.15 Give the fl ow of events of the interaction diagrams of Figures 13.46 and 13.47 . 

13.16 Check that your answer to Problem 13.13 is a possible scenario for the interaction diagrams of Figures 13.51 and 13.52 . If not, modify your scenario. 

<sup>1</sup> Problem 12.16 (Term Project) and Problems 12.20 and 12.21 (Case Study) can be done at the end of either Chapter 12 or Chapter 13. 

13.17 Give the fl ow of events of the interaction diagrams of Figures 13.51 and 13.52 . 



13.18 Give the fl ow of events of the interaction diagrams of Figures 13.57 and 13.58 . 



13.19 (Analysis and Design Project) Perform the analysis workfl ow of the library software product of Problem 8.7. 

13.20 (Analysis and Design Project) Perform the analysis workfl ow of the product for determining whether a bank statement is correct of Problem 8.8. 

13.21 (Analysis and Design Project) Perform the analysis workfl ow of the automated teller machine of Problem 8.9. There is no need to consider the details of the constituent hardware components such as the card reader, printer, and cash dispenser. Instead, simply assume that, when the ATM sends commands to those components, they are correctly executed. 

13.22 (Term Project) Perform the analysis workfl ow of the Chocoholics Anonymous product described in Appendix A. 

13.23 (Case Study) Add Report Class to the analysis workfl ow of the MSG Foundation case study (Sections 13.9 through 13.16). Is this an improvement or an unnecessary complication? 

13.24 (Case Study) Determine what happens when object-oriented analysis starts with dynamic modeling. Start with the statechart of Figure 13.25 and complete the object-oriented analysis process for the MSG Foundation case study. 

13.25 (Case Study) Compare and contrast the structured systems analysis of the MSG Foundation case study of Section 12.4 with the object-oriented analysis workfl ow of Sections 13.9 through 13.11. 

13.26 (Readings in Software Engineering) Your instructor will distribute copies of [Juristo, Moreno, and López, 2000]. What is your opinion of their approach to object-oriented analysis? 

## References



[Awad, Kuusela, and Ziegler, 1996] M. AWAD, J. KUUSELA, AND J. ZIEGLER, Object-Oriented Technology for Real-Time Systems: A Practical Approach Using OMT and Fusion, Prentice Hall, Upper Saddle River, NJ, 1996. 





[Beck and Cunningham, 1989] K. BECK AND W. CUNNINGHAM, “A Laboratory for Teaching Object-Oriented Thinking,” Proceedings of OOPSLA ’89, ACM SIGPLAN Notices 24 (October 1989), pp. 1–6. 





[Bellinzona, Fugini, and Pernici, 1995] R. BELLINZONA, M. G. FUGINI, AND B. PERNICI, “Reusing Specifi cations in OO Applications,” IEEE Software 12 (March 1995), pp. 656–75. 





[Booch, Rumbaugh, and Jacobson, 1999] G. BOOCH, J. RUMBAUGH, AND I. JACOBSON, The UML Users Guide , Addison-Wesley, Reading, MA, 1999. 





[Coleman et al., 1994] D. COLEMAN, P. ARNOLD, S. BODOFF, C. DOLLIN, H. GILCHRIST, F. HAYES, AND P. JEREMAES, Object-Oriented Development: The Fusion Method , Prentice Hall, Englewood Cliffs, NJ, 1994. 





[D’Souza and Wills, 1999] D. D’SOUZA AND H. WILLS, Objects, Components, and Frameworks with UML: The Catalysis Approach , Addison-Wesley, Reading, MA, 1999. 





[de Champeaux and Faure, 1992] D. DE CHAMPEAUX AND P. FAURE, “A Comparative Study of Object-Oriented Analysis Methods,” Journal of Object-Oriented Programming 5 (March–April 1992), pp. 21–33. 





[Embley, Jackson, and Woodfi eld, 1995] D. W. EMBLEY, R. B. JACKSON, AND S. N. WOODFIELD, “OO Systems Analysis: Is It or Isn’t It?” IEEE Software 12 (July 1995), pp. 18–33. 





[Fichman and Kemerer, 1992] R. G. FICHMAN AND C. F. KEMERER, “Object-Oriented and Conventional Analysis and Design Methodologies: Comparison and Critique,” IEEE Computer 25 (October 1992), pp. 22–39. 





[Harel and Gery, 1997] D. HAREL AND E. GERY, “Executable Object Modeling with Statecharts,” IEEE Computer 30 (July 1997), pp. 31–42. 





[Jacobson, Booch, and Rumbaugh, 1999], I. JACOBSON, G. BOOCH, AND J. RUMBAUGH, The Unifi ed Software Development Process , Addison-Wesley, Reading, MA, 1999. 





[Jacobson, Christerson, Jonsson, and Overgaard, 1992] I. JACOBSON, M. CHRISTERSON, P. JONSSON, AND G. OVERGAARD, Object-Oriented Software Engineering: A Use Case Driven Approach , ACM Press, New York, 1992. 





[Juristo, Moreno, and López, 2000] N. JURISTO, A. M. MORENO, AND M. LÓPEZ, “How to Use Linguistic Instruments for Object-Oriented Analysis,” IEEE Software 17 (May–June 2000), pp. 80–89. 





[Monarchi and Puhr, 1992] D. E. MONARCHI AND G. I. PUHR, “A Research Typology for Object-Oriented Analysis and Design,” Communications of the ACM 35 (September 1992), pp. 35–47. 





[Rumbaugh et al., 1991] J. RUMBAUGH, M. BLAHA, W. PREMERLANI, F. EDDY, AND W. LORENSEN, Object-Oriented Modeling and Design, Prentice Hall, Englewood Cliffs, NJ, 1991. 





[Rumbaugh, Jacobson, and Booch, 1999] J. RUMBAUGH, I. JACOBSON, AND G. BOOCH, The Unifi ed Modeling Language Reference Manual, Addison-Wesley, Reading, MA, 1999. 





[Selic, Gullekson, and Ward, 1995] B. SELIC, G. GULLEKSON, AND P. T. WARD, Real-Time Object-Oriented Modeling , John Wiley and Sons, New York, 1995. 





[USNO, 2000] “The 21st Century and the Third Millennium—When Will They Begin?” U.S. Naval Observatory, Astronomical Applications Department, at aa.usno.navy.mil/AA/faq/docs/ millennium.html , February 22, 2000. 





[Williams, 1996] J. D. WILLIAMS, “Managing Iteration in OO Projects,” IEEE Computer 29 (September 1996), pp. 39–43. 





[Wirfs-Brock, Wilkerson, and Wiener, 1990] R. WIRFS-BROCK, B. WILKERSON, AND L. WIENER, Designing Object-Oriented Software , Prentice Hall, Englewood Cliffs, NJ, 1990. 



# Design

Learning Objectives 

After studying this chapter, you should be able to 

• Perform the design workfl ow. 

• Perform object-oriented design. 

• Perform data fl ow analysis and transaction analysis. 

Over the past 40 or so years, hundreds of design techniques have been put forward. Some are variations on existing techniques; others are radically different from anything previously proposed. A few design techniques have been used by tens of thousands of software engineers; many have been used by only their authors. Some design strategies, particularly those developed by academics, have a fi rm theoretical basis. Others, including many drawn up by academics, are more pragmatic in nature; they were put forward because their authors found that they worked well in practice. Most design techniques are manual, but automation increasingly is becoming an important aspect of design, if only to assist in the management of documentation. 

Notwithstanding this plethora of design techniques, a certain underlying pattern emerges. A major theme of this book is that two essential aspects of a product are its operations and the data on which the operations act. Therefore, the two basic ways of designing a product are operation-oriented design and data-oriented design. In operation-oriented design, the emphasis is on the operations. An example is data fl ow analysis (Section 14.3), where the objective is to design modules with high cohesion (Section 7.2). In data-oriented design, the data are considered fi rst. For example, in Jackson’s technique (Section 14.5), the structure of the data is determined fi rst, and then the procedures are designed to conform to the struc ture of the data. 

A weakness of operation-oriented design techniques is that they concentrate on the operations; the data are of only secondary importance. Data-oriented design techniques similarly emphasize the data, to the detriment of the operations. The solution is to use object-oriented techniques, which give equal weight to operations and data. In this chapter, operation- and data-oriented design are described fi rst, and then object-oriented design. Just as an object incorporates both operations and data, so object-oriented design combines features of operation-oriented and data-oriented design. Therefore, a basic understanding of operation- and data-oriented design is needed to get a full understanding of objectoriented design. 

Before specifi c design techniques are examined, some general remarks must be made regarding design. 

## 14.1 Design and Abstraction

The classical design phase consists of three activities: architectural design, detailed design, and design testing. The input to the design process is the specifi cation document, a description of what the product is to do. The output is the design document, a description of how the product is to achieve this. 

During architectural design (also known as general design , logical design , or high-level design ), a modular decomposition of the product is developed. That is, the specifications are carefully analyzed, and a module structure that has the desired functionality is produced. The output from this activity is a list of the modules and a description of how they are to be interconnected. From the viewpoint of abstraction, during architectural design, the existence of certain modules is assumed; the design then is developed in terms of those modules. 

When the object-oriented paradigm is used, however, as explained in Section 1.9, the architectural design activity is performed during the object-oriented analysis workfl ow ( Chapter 12 ). This is because the fi rst step in the analysis workfl ow is to determine the classes. Because a class is a type of module, the modular decomposition has been performed during the analysis workfl ow. 

The next activity in the classical design phase and a major activity of the object-oriented design workfl ow is detailed design , also known as modular design , physical design , or low-level design , during which each module (or class) is designed in detail. For example, specifi c algorithms are selected and data structures are chosen. Again, from the viewpoint of abstraction, during this activity the fact that the modules (or classes) are to be interconnected to form a complete product is ignored. 

It was stated previously that the classical design phase has three activities and that the third activity is testing. The word activity was used, rather than stage or step , to emphasize that testing is an integral part of design, just as it is an integral part of the entire software development and maintenance process. Testing is not something performed only after the architectural design and detailed design have been completed. Similarly, in the case of object-oriented design, the test workfl ow is performed concurrently with the design workfl ow. 

A variety of design techniques are now described, fi rst operation-oriented techniques, then data-oriented techniques, and fi nally object-oriented techniques. 

## 14.2 Operation-Oriented Design

Sections 7.2 and 7.3 made a theoretical case for decomposing a product into modules with high cohesion and low coupling. We now describe two practical classical techniques for achieving this design objective, data fl ow analysis (Section 14.3) and transaction analysis (Section 14.4). In theory, data fl ow analysis can be applied whenever the specifi cations can be represented by a data fl ow diagram, and because (at least in theory) every product can be represented by a DFD, data fl ow analysis is universally applicable. In practice, however, in a number of situations, there are more appropriate design techniques, specifi cally for designing products where the fl ow of data is secondary to other considerations. Examples where other design techniques are indicated include rule-based systems (expert systems), databases, and transaction-processing products. (Transaction analysis, described in Section 14.4, is a good way of decomposing transaction-processing products into modules.) 

## 14.3 Data Flow Analysis

Data fl ow analysis (DFA) is a classical design technique for achieving modules with high cohesion. It can be used in conjunction with most analysis techniques. Here, DFA is presented in conjunction with structured systems analysis (Section 12.3). The input to the technique is a data fl ow diagram. A key point is that, once the DFD has been completed, the software designer has precise and complete information regarding the input to and output from the product 

Consider the fl ow of data in the product represented by the DFD of Figure 14.1 . The product somehow transforms input into output. At some point in the DFD, the input ceases to be input and becomes some sort of internal data. Then, at some further point, these internal data take on the quality of output. This is shown in more detail in Figure 14.2 . The point at which the input loses the quality of being input and simply becomes internal data operated on by the product is termed the point of highest abstraction of input . The point of highest abstraction of output is similarly the fi rst point in the fl ow of data at which the output can be identifi ed as such, rather than as some sort of internal data. 

Using the points of highest abstraction of input and output, the product is decomposed into three modules: input_module, transform_module , and output_module . Now each module is taken in turn, its points of highest abstraction found, and the module decomposed again. This procedure is continued stepwise until each module performs a single operation; that is, the design consists of modules with high cohesion. Consequently, stepwise refi nement, the foundation of so many other software engineering techniques, also underlies data fl ow analysis 


FIGURE 14.1 A data flow diagram showing fl ow of data and operations of product.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/17dc7375f3b32b14f7f65201472758351000d41725130e3452693844ec4f06fd.jpg)



FIGURE 14.2 Points of highest abstraction of input and output.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/893142323613b7098c4c2144d2d5af266a61040621dbfc1ac7a035ce2df01087.jpg)


In fairness, it should be pointed out that minor modifi cations might have to be made to the decomposition to achieve the lowest possible coupling. Data fl ow analysis is a way of achieving high cohesion. The aim of composite/structured design is high cohesion but also low coupling. To achieve the latter, sometimes it is necessary to make minor modifi cations to the design. For example, because DFA does not take coupling into account, control coupling may arise inadvertently in a design constructed using DFA. In such a case, all that is needed is to modify the two modules involved so that data, and not control, are passed between them 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/ff789c7d1d271bf77f945195bcf0d6af7c77a73caf3c7599a3af9a49cb85c2fa.jpg)


## 14.3.1

## Mini Case Study Word Counting

Consider the problem of designing a product that takes as input a fi le name and returns the number of words in that fi le, similarly to the UNIX wc utility. 

Figure 14.3 depicts the data fl ow diagram. There are fi ve modules. Module read_fi le_name reads the name of the fi le, which then is validated by validate_fi le_ name . The validated name is passed to count_number_of_words , which does precisely that. The word count is passed on to format_word_count , and the formatted word count fi nally is passed to display_word_count for output. 

Examining the data fl ow, the initial input is fi le_name . When this becomes validated_fi le_name , it still is a fi le name and therefore has not lost its quality of being input data. But consider module count_number_of_words . Its input is validated_ fi le_name , and its output is word_count . The output from this module is totally different in quality from the input to the product as a whole. It is clear that the point of highest abstraction of input is as indicated on Figure 14.3 . Similarly, even though the output from count_number_of_words undergoes some sort of formatting, it is essentially output from the time it emerges from module count_number_of_words. The point of highest abstraction of output therefore is as shown in Figure 14.3 . 

The result of decomposing the product using these two points of highest abstraction is shown in the structure chart of Figure 14.4 . This fi gure also reveals that the data 


FIGURE 14.3 The fi rst refi nement of the data fl ow diagram.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/a172898749c8ca7696268a31000ccf2780bffe6085fc5674720d52eb1f9ee368.jpg)


FIGURE 14.4 The fi rst refi nement of the structure chart. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/b26b397b14a05b89ed38b03096eb4e903240f27a4113a8c0f4d770c43d4cdb01.jpg)



FIGURE 14.5 The second refinement of the structure chart.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/5a20acd53b55afe9468247c9131544659cf9b4b6e878984760741cd55c712c1f.jpg)


fl ow diagram of Figure 14.3 is somewhat too simplistic. The DFD does not show the logical fl ow corresponding to what happens if the fi le specifi ed by the user does not exist. Module read_and_validate_fi le_name must return a status_fl ag to perform_ word_count . If the name is invalid, then it is ignored by perform_word_count and an error message of some sort is printed. But, if the name is valid, it is passed on to count_number_of_words . In general, wherever there is a conditional data fl ow, a corresponding control fl ow is needed. 

As explained in Section 7.2.5, a module has communicational cohesion if it performs a series of operations related by the sequence of steps to be followed by the product and if all the operations are performed on the same data. In Figure 14.4 , two modules have communicational cohesion: read_and_validate_fi le_name and format_and_display_word_count . These must be decomposed further. The fi nal result is shown in Figure 14.5 . All eight modules have functional cohesion, with either data coupling (Section 7.3.5) or no coupling between them. 

Now that the architectural design has been completed, the next step is the detailed design. Here, data structures are chosen and algorithms selected. The detailed design of each module then is handed to a programmer for implementation. Just as with virtually every other phase of software production, time constraints usually require that the implementation be done by a team, rather than having a single programmer responsible for coding all the modules. For this reason, the detailed design of each module must be presented so it can be understood without reference to any other module. The detailed design of four of the eight modules appears in Figure 14.6 ; the other four modules are presented in a different format. 


FIGURE 14.6 The detailed design of four modules of the example.


<table><tr><td>Module name</td><td>read_file_name</td></tr><tr><td>Module type</td><td>Function</td></tr><tr><td>Return type</td><td>string</td></tr><tr><td>Input arguments</td><td>None</td></tr><tr><td>Output arguments</td><td>None</td></tr><tr><td>Error messages</td><td>None</td></tr><tr><td>Files accessed</td><td>None</td></tr><tr><td>Files changed</td><td>None</td></tr><tr><td>Modules called</td><td>None</td></tr><tr><td>Narrative</td><td>The product is invoked by the user by means of the command stringword_countUsing an operating system call, this module accesses the contents of the command string input by the user, extracts, and returns it as the value of the module.</td></tr></table>

<table><tr><td>Module name</td><td>validate_file_name</td></tr><tr><td>Module type</td><td>Function</td></tr><tr><td>Return type</td><td>Boolean</td></tr><tr><td>Input arguments</td><td>file_name : string</td></tr><tr><td>Output arguments</td><td>None</td></tr><tr><td>Error messages</td><td>None</td></tr><tr><td>Files accessed</td><td>None</td></tr><tr><td>Files changed</td><td>None</td></tr><tr><td>Modules called</td><td>None</td></tr><tr><td>Narrative</td><td>This module makes an operating system call to determine whether file file_name exists. The module returns true if the file exists and false otherwise.</td></tr><tr><td>Module name</td><td>count_number_of_words</td></tr><tr><td>Module type</td><td>Function</td></tr><tr><td>Return type</td><td>integer</td></tr><tr><td>Input arguments</td><td>validated_file_name : string</td></tr><tr><td>Output arguments</td><td>None</td></tr><tr><td>Error messages</td><td>None</td></tr><tr><td>Files accessed</td><td>None</td></tr><tr><td>Files changed</td><td>None</td></tr><tr><td>Modules called</td><td>None</td></tr><tr><td>Narrative</td><td>This module determines whether validated_file_name is a text file, that is, divided into lines of characters. If so, the module returns the number of words in the text file; otherwise, the module returns -1.</td></tr></table>

<table><tr><td>Module name</td><td>produce_output</td></tr><tr><td>Module type</td><td>Function</td></tr><tr><td>Return type</td><td>void</td></tr><tr><td>Input arguments</td><td>word_count : integer</td></tr><tr><td>Output arguments</td><td>None</td></tr><tr><td>Error messages</td><td>None</td></tr><tr><td>Files accessed</td><td>None</td></tr><tr><td>Files changed</td><td>None</td></tr><tr><td>Modules called</td><td>format_word_countarguments: word_count : integerformatted_word_count : stringdisplay_word_countarguments: formatted_word_count : string</td></tr><tr><td>Narrative</td><td>This module takes the integer word_count passed to it by the calling module and calls format_word_count to have that integer formatted according to the specifications. Then it calls display_word_count to have the line printed.</td></tr></table>

The design of Figure 14.6 is independent of the programming language. However, if management decides on an implementation language before the detailed design is started, the use of a program description language (PDL) for representing the detailed design is an attractive alternative ( pseudocode is an earlier name for PDL). PDL essentially consists of comments connected by the control statements of the chosen implementation language. Figure 14.7 shows a detailed design for the remaining four modules of the product written in a PDL with the flavor of C++ or Java. A PDL has the advantage that it generally is clear and concise, and the implementation step usually consists merely of translating the comments into the relevant programming language. The weakness is that sometimes there is a tendency for the designers to go into too much detail and produce a complete code implementation of a module rather than a PDL detailed design. 

```c
void perform_word_count ()
{
    String validated_file_name;
    int word_count;

    if (get_input (validated_file_name) is null)
    print "error 1: file does not exist";
    else 
    {
    set word_count equal to count_number_of_words (validated_file_name);
    if (word_count is equal to -1)
    print "error 2: file is not a text file";
    else 
    produce_output (word_count);
    }
}

String get_input ()
{
    String file_name;

    file_name = read_file_name ();
    if (validate_file_name (file_name) is true)
    {
    return file_name;
    }
    else 
    return null;
}

void display_word_count (String formatted_word_count)
{
    print formatted_word_count, left justified;
}

String format_word_count (int word_count);
{
    return "File contains" word_count "words";
} 
```

After it has been fully documented and successfully tested, the detailed design is handed over to the implementation team for coding. The product then proceeds through the remaining phases of the classical software life cycle. 

## How to Perform Data Flow Analysis

Box 14.1 

## • Iterate

Find the point of highest abstraction of input of each input stream. 

Find the point of highest abstraction of output of each output stream. 

Decompose the data fl ow diagram using these points of highest abstraction. 

• Until the resulting modules have high cohesion. 

• If a resulting coupling is too high, adjust the design. 

FIGURE 14.8 The data fl ow diagram with multiple input and output streams. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/463c06d93bb799748e88987a40a020f14791d5745047cf118aacf821634a334e.jpg)


## 14.3.2 Data Flow Analysis Extensions

The reader may well feel that this mini case study is somewhat artifi cial, in that the data fl ow diagram ( Figure 14.3 ) has only one input stream and one output stream. To see what happens in more complex situations, consider Figure 14.8 . Now there are four input streams and fi ve output streams, a situation that corresponds more closely to reality. 

When there are multiple input and output streams, the way to proceed is to fi nd the point of highest abstraction of input for each input stream and the point of highest abstraction of output for each output stream. Use these points to decompose the given data fl ow diagram into modules with fewer input–output streams than the original. Continue this way until each resulting module has high cohesion. Finally, determine the coupling between each pair of modules and make any necessary adjustments. 

Data fl ow analysis is summarized in How to Perform Box 14.1. 

## 14.4 Transaction Analysis

A transaction is an operation from the viewpoint of the user of the product, such as “process a request” or “print a list of today’s orders.” Data fl ow analysis is inappropriate for the transaction-processing type of product, in which a number of related operations, similar in outline but differing in detail, must be performed. A typical example is the software controlling an automated teller machine. The customer inserts a card with a magnetic strip into a slot, keys in a password, and then performs operations such as deposit to a checking, savings, or credit card account; withdraw from an account; or determine the balance in an account. This type of product is depicted in Figure 14.9 . A good way to design such a product is to break it into two pieces, the analyzer and the dispatcher. The analyzer determines the transaction type and passes this information to the dispatcher, which performs the transaction 

<table><tr><td>How to Perform Transaction Analysis</td><td>Box 14.2</td></tr><tr><td colspan="2">Design the architecture in terms of two components:The analyzer.The dispatcher.For each set of related operationsDesign one basic module and instantiate it as many times as necessary.</td></tr></table>

As explained in Section 7.2.2, a module has logical cohesion when it performs a series of related operations, one of which is selected by the calling module. The design shown in Figure 14.10 is undesirable, because it has two modules with logical cohesion (Section 7.2.2), edit_any_transaction and update_any_fi le . On the other hand, it seems a waste of effort to have fi ve very similar edit modules and fi ve very similar update modules. The 


FIGURE 14.9 A typical transaction-processing system


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/faa33210c18b019ad0f51e62807d086b369a75eb37e26cb8b8610c7a2b417c6f.jpg)


FIGURE 14.10 A poor design of transactionprocessing system. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/0dbf4cfcd4460f5531bae24461288a7f5a42e2a3545f3a3c4044ce1eed69e7b7.jpg)


solution is software reuse (Section 8.1): A basic edit module should be designed, coded, documented, tested, and then instantiated fi ve times. Each version is slightly different, but the differences are small enough to make this approach worthwhile. Similarly, a basic update module can be instantiated fi ve times and slightly modifi ed to cater to the fi ve dif ferent update types. The resulting design has high cohesion and low coupling. 

Transaction analysis is summarized in How to Perform Box 14.2. 

## 14.5 Data-Oriented Design

The basic principle behind data-oriented design is to design the product according to the structure of the data on which it is to operate. That is, fi rst the structure of the data is determined. Then each procedure is given the same structure as the data on which it operates. There are a number of data-oriented techniques of this type; the most well known are those of Michael Jackson [1975], Warnier [1976], and Orr [1981]. The three techniques share many similarities. 

Data-oriented design was never as popular as operation-oriented design and, with the rise of the object-oriented paradigm, it has largely fallen out of fashion. For reasons of space, data-oriented design is not discussed further in this book; the interested reader should consult the references cited in the previous paragraph. 

## 14.6 Object-Oriented Design

As previously stated, the Unifi ed Process assumes previous knowledge of objectoriented design (OOD). Accordingly, we now describe OOD and then discuss the design workfl ow of the Unifi ed Process in Section 14.9. 

The aim of OOD is to design the product in terms of objects, that is, instantiations of the classes and subclasses extracted during object-oriented analysis. Classical languages, such as C, and older (pre-2000) versions of COBOL and Fortran do not support objects as such. This might seem to imply that OOD is accessible only to users of object-oriented languages like Smalltalk [Goldberg and Robson, 1989], C++ [Stroustrup, 2003], Ada 95 [ISO/IEC 8652, 1995], and Java [Flanagan, 2005]. 

That is not the case. Although OOD as such is not supported by classical languages, a large subset of OOD can be used. As explained in Section 7.7, a class is an abstract data type with inheritance and an object is an instance of a class. When using an implementation language that does not support inheritance, the solution is to utilize those aspects of OOD that can be achieved in the programming language used in the project, that is, to use abstract data type design . Abstract data types can be implemented in virtually any language that supports type statements. Even in a classical language that does not support type statements as such, and hence cannot support abstract data types, it still may be possible to implement data encapsulation. Figure 7.28 depicts a hierarchy of design concepts starting with modules and ending with objects. In those cases where full OOD is not possible, the developers should endeavor to ensure that their design uses the highest possible concept in the hierarchy of Figure 7.28 that their implementation language supports. 

The two key steps of OOD are to complete the class diagram and perform the detailed design. With regard to the fi rst step, completing the class diagram , the formats of the attributes need to be determined, and the methods need to be assigned to the relevant classes. The formats of the attributes can generally be deduced directly from the analysis artifacts. For example, in the United States the specifi cations may state that a date such as December 3, 1947, shall be represented as 12/03/1947 ( mm/dd/yyyy format) or in Europe as 03/12/1947 ( dd/mm/yyyy format). But, irrespective of which date convention is used, a total of 10 characters is needed. 

The information for determining the formats is obtained during the analysis workfl ow, so the formats could certainly be added to the class diagram at that time. However, the object-oriented paradigm is iterative. Each iteration results in a change to what has already been completed. For practical reasons, then, information should be added to UML models as late as possible. Consider, for example, Figures 13.21 and 13.22, which show the fi rst two iterations of the class diagram of the MSG Foundation case study. Neither of those two iterations shows the attributes of the classes. If the attributes had been determined earlier, they would probably have had to be modifi ed, as well as possibly moved from class to class, until the analysis team was satisfi ed with the class diagram. Instead, all that had to be modifi ed was the classes themselves. In general, it makes little sense to add an item to a class diagram (or any other UML diagram) before it is absolutely essential to do so, because adding the item will make the next iteration unnecessarily burdensome. In particular, it makes little sense to specify formats before they are strictly needed. 

The other major component of the fi rst step of OOD is to assign methods (implementations of operations) to classes. Determination of all the operations of the product is performed by examining the interaction diagrams of every scenario. This is straightforward. The hard part is to determine how to decide which methods should be associated with each class. 

A method can be assigned either to a class or to a client that sends a message to an object of that class. (A client of an object is a program unit that sends a message to that object.) One principle that can be employed to assist in deciding how to assign an operation is information hiding (Section 7.6). That is, the state variables of a class should be declared private (accessible only within an object of that class) or protected (accessible only within an object of that class or a subclass of that class). Accordingly, operations performed on state variables must be local to that class. 

A second principle is that, if a particular operation is invoked by a number of different clients of an object, it makes sense to have a single copy of that operation implemented as a method of the object, rather than have a copy in each client of that object. 

A third principle that can be employed to assist in deciding where to locate a method is to use responsibility-driven design. As explained in Section 1.9, responsibility-driven design is a key aspect of the object-oriented paradigm. If a client sends a message to an object, then that object is responsible for every aspect of carrying out the request of the client. The client does not know how the request will be carried out and is not permitted to know. Once the request has been carried out, control returns to the client. At that point, all the client knows is that the request has been carried out; it still has no idea how this was achieved 

To see how these principles are utilized, we now illustrate OOD by means of two examples. As before, the elevator problem case study is presented, with just one elevator for simplicity. Then, we return to the MSG Foundation case study. By using the same examples, you can compare different approaches without having to worry about the ramifi cations of the problem itself. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/98e132cc0e52e90890b23a119c74d6f6356d6bde8cb35eb2c8707c72a7e6d8e1.jpg)


## 14.7 Object-Oriented Design: The Elevator Problem Case Study

## Step 1. Complete the Class Diagram

A design workflow detailed class diagram ( Figure 14.11 ) is obtained by adding the operations (methods) to the class diagram of Figure 13.12. In the case of a Java implementation, two additional classes are needed. Elevator 


FIGURE 14.11 The detailed class diagram for the elevator problem case study. For clarity, only those methods that cause an object to change its state are shown.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/04b6a9ef111e98889e7139a9313b14c38047d002b372c49080baa6a7e9a4ad55.jpg)


Application Class corresponds to the C++ main function, and Elevator Utilities Class contains the Java routines that correspond to the C++ functions declared external to the C++ classes. (For clarity, methods of the form Send message to C Class . . . have been omitted from Figure 14.11 ; but see Problems 14.7–14.12.) 

Consider the fi rst iteration of the CRC card for the elevator subcontroller (Figure 13.14). The responsibilities fall into two groups. One responsibility— 5. Start timer —is assigned to the elevator controller on the basis of responsibility-driven design; that task is carried out by the elevator controller itself. 

On the other hand, the remaining eleven responsibilities (events 1 through 4 and 6 through 12) have the form “Send a message to another class to tell it to do something.” This again implies that responsibility-driven design should be used in assigning the relevant method to classes. In addition, because of safety concerns, the principle of information hiding is equally applicable in all eleven cases. 

For these two reasons, methods closeDoors and openDoors are assigned to Elevator Doors Class . That is, a client of Elevator Doors Class (in this case, an object of Elevator Subcontroller Class ) sends a message to an object of Elevator Doors Class to close or open the doors of the elevator, and that request is then carried out by the relevant method. Every aspect of those two methods is encapsulated within Elevator Doors Class . In addition, information hiding results in a truly independent Elevator Doors Class , instances of which can undergo detailed design and implementation independently and be reused later in other products. 

The same two design principles are applied to methods moveDownOneFloor and moveUpOneFloor , and they are assigned to Elevator Class . There is no need for an explicit instruction to cause an elevator to stop. If neither of its two methods is invoked, an elevator cannot move; there is no way to change the state of an elevator other than by invoking one of its two methods. 

Finally, methods turnOffButton and turnOnButton are assigned to both Elevator Button Class and Floor Button Class . The reasoning here is the same as for the methods assigned to Elevator Doors Class and Elevator Class. First, the principle of responsibility-driven design requires that the buttons have full control over whether they are on or off. Second, the principle of information hiding requires the internal state of a button to be hidden. The methods that turn an elevator button on or off therefore must be local to Elevator Button Class , and similarly for Floor Button Class . To make use of polymorphism and dynamic binding, methods turnOffButton and turnOnButton are declared abstract ( virtual ) in the base class Button Class for the reasons stated in Section 7.8. At run time, the correct version of method turnOffButton or turnOnButton wil then be invoked. 

## Step 2. Perform the Detailed Design

A detailed design now is developed for all the classes. Any suitable technique may be used, such as the stepwise refi nement described in Chapter 5 . The detailed design of method elevatorSubcontrollerEventLoop is shown in Figure 14.12 . Here PDL (pseudocode) was used, but a tabular representation (such as that of Figure 14.6 ) can be equally effective. 

Figure 14.12 is constructed from the statechart of Figure 13.13. For example, the events elevator button pushed and elevator button turned off is implemented by the two nested if statements at the beginning of Figure 14.12 . The two operations of the state Processing New Request then follow. The else-if condition cor responds to the next event leading from state Elevator Subcontroller Event Loop , elevator moving in direction d, fl oor f is next . The remainder of the detailed design is equally straightforward. 

```txt
FIGURE 14.12 void elevatorSubcontrollerEventLoop (void)
The detailed design of method
elevator- Subcontroller- EventLoop.
{
    while (TRUE)
    {
    if (an elevatorButton has been pressed)
    if (elevatorButton is off)
    {
    elevatorButton::turnOnButton;
    scheduler::newRequestMade;
    }
    else if (elevator is moving up)
    {
    wait for sensor message that elevator is arriving at floor;
    scheduler::checkRequests;
    if (there is no request to stop at floor f)
    elevator::moveUpOneFloor;
    else
    {
    stop elevator by not sending a message to move;
    if (elevatorButton is on)
    elevatorButton::turnOffButton;
    elevatorDoors::openDoors;
    startTimer;
    }
    }
    else if (elevator is moving down)
    [similar to up case]
    else if (elevator is stopped and request is pending)
    {
    wait for timeout;
    elevatorDoors::closeDoors;
    determine direction of next request;
    elevator::moveUp/DownOneFloor;
    wait for sensor message that elevator has left floor;
    floorSubcontroller::elevatorHasLeftFloor;
    }
    else if (elevator is at rest and not (request is pending))
    {
    wait for timeout;
    elevatorDoors::closeDoors;
    }
    else
    there are no requests, elevator is stopped with elevatorDoors closed, so do nothing;
} 
```

Now we consider the object-oriented design of the MSG Foundation case study. 

## 14.8 Object-Oriented Design: The MSG Foundation Case Study

As described in Section 14.6, object-oriented design consists of two steps. 

## Step 1. Complete the Class Diagram

The overall class diagram for the MSG Foundation case study is shown in Figure 14.13 . The user-defi ned Date Class is drawn dashed to denote that it is needed for only 

FIGURE 14.13 The overall class diagram for the MSG Foundation case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/5246369b153852d1ac3ccf890f139c54913ce730c1f769c90f373167be9c7bc4.jpg)


a C++ implementation; Java has built-in classes for handling dates, including java. text.Dateformat and java.util.Calendar. 

Next, the formats for the attributes of the classes are deduced from discussions with the client and users; examination of forms (Section 11.4.2) is also extremely useful in this regard. A portion of the result is shown in Figure 14.14. 

The methods of the product are found in the various interaction diagrams. The task of the designer is to decide to which class each method should be assigned. For example, the convention in an object-oriented software product is that associated with each attribute of a class are mutator method setAttribute, used to assign a specifi c value to that attribute , and accessor method getAttribute, which return the current value of that attribute . 

For example, consider method setAssetNumber , used to assign a number to an asset (investment or mortgage). In the classical paradigm, we would need separate functions set_investment_number and set_mortgage_number. However, the object-oriented paradigm supports inheritance. Therefore, method setAssetNumber should be assigned to Asset Class . Then, as refl ected in Figure 14.15 , the method can be applied not only to instances of Asset Class but also, as a consequence of inheritance, to instances of every subclass of Asset Class , that is, to instances of Investment Class and Mortgage Class . Similarly, method getAssetNumber should also be allocated to the superclass Asset Class. 


FIGURE 14.14 Part of the overall class diagram for the MSG Foundation case study with the attribute formats added.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/37230ed13d21d9f98cb71af81c72f1145992bd156638266a4203f011b872e06f.jpg)



FIGURE 14.15 Part of the class diagram for the MSG Foundation case study with methods setAssetNumber and getAssetNumber assigned to Asset Class.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/3e04aca5f8028674e7d769d0a768c483a44d1efd0d64547e46dc3d134aaa8f36.jpg)


Assigning the other methods to the appropriate classes is equally straightforward. The resulting design is shown in Appendix G. 

## Step 2. Perform the Detailed Design

Next, the detailed design is built by taking each method and determining what it does. Figure 14.16 shows the detailed design (in a PDL for Java) of a method computeEstimatedFunds of class EstimateFundsForWeek of the MSG Foundation case study. This method invokes method totalWeeklyNetPayments of class Mortgage shown in Figure 14.17 . 

The steps of object-oriented design are summarized in How to Perform Box 14.3 

## 14.9 The Design Workfl ow

The overall aim of the design workfl ow is to refine the artifacts of the analysis workfl ow until the material is in a form that can be implemented by the programmers. The input to the design workfl ow is therefore the analysis workfl ow artifacts ( Chapter 13 ). During the design workfl ow, these artifacts are iterated and incremented until they are in a format that can be utilized by the programmers. 

## How to Perform Object-Oriented Design

• Complete the class diagram. 

• Perform the detailed design. 

```txt
FIGURE 14.16
The detailed design of method compute- Estimated-Funds of class Estimate-FundsFor-Week of the MSG Foundation case study.
public static void computeEstimatedFunds( )
This method computes the estimated funds available for the week.
{
    float expectedWeeklyInvestmentReturn; (expected weekly investment return)
    float expectedTotalWeeklyNetPayments = (float) 0.0;
    (expected total mortgage payments less total weekly grants)
    float estimatedFunds = (float) 0.0; (total estimated funds for week)
    Create an instance of an investment record.
    Investment inv = new Investment ( );
    Create an instance of a mortgage record.
    Mortgage mort = new Mortgage ( );
    Invoke method totalWeeklyReturnOnInvestment.
    expectedWeeklyInvestmentReturn = inv.totalWeeklyReturnOnInvestment ( );
    Invoke method expectedTotalWeeklyNetPayments (see Figure 14.17)
    expectedTotalWeeklyNetPayments = mort.totalWeeklyNetPayments ( );
    Now compute the estimated funds for the week.
    estimatedFunds = (expectedWeeklyInvestmentReturn - (MSGApplication.getAnnualOperatingExpenses ( ) / (float) 52.0) + expectedTotalWeeklyNetPayments); 
```

Store this value in the appropriate location. 

MSGApplication.setEstimatedFundsForWeek (estimatedFunds); 

} // computeEstimatedFunds 

One aspect of this iteration and incrementation is the identifi cation of methods and their allocation to the appropriate classes. Another aspect is performing the detailed design. These two steps constitute the object-oriented design component of the design workfl ow. 

In addition to performing the object-oriented design, many decisions have to be made as part of the design workfl ow. One such decision is the selection of the programming language in which the software product will be implemented. This process is described in detail in Chapter 15 . Another decision is how much of existing software products to reuse in the new software product to be developed. Reuse is described in Chapter 8 . Portability is another important design decision; this topic, too, is described in Chapter 8 . Also, large software products are often implemented on a network of computers; yet another design decision is the allocation of each software component to the hardware component on which it is to run. 

The major motivation behind the development of the Unifi ed Process was to present a methodology that could be used to develop large-scale software products, typically, 500,000 lines of code or more. On the other hand, the implementations of the MSG Foundation case study in Appendices H and I are less than 5000 lines of C++ and Java, respectively. In other 

<table><tr><td colspan="2">public float totalWeeklyNetPayments ( )This method computes the net total weekly payments made by the mortgagees, that is, the expected total weekly mortgage amount less the expected total weekly grants.</td></tr><tr><td colspan="2">{</td></tr><tr><td>File mortgageFile = new File (&quot;mortgage.dat&quot;);</td><td>(file of mortgage records)</td></tr><tr><td>float expectedTotalWeeklyMortgages = (float) 0.0;</td><td>(expected total weekly mortgage payments)</td></tr><tr><td>float expectedTotalWeeklyGrants = (float) 0.0;</td><td>(expected total weekly grants)</td></tr><tr><td>float interestPayment;</td><td>(interest payment)</td></tr><tr><td>float escrowPayment;</td><td>(escrow payment)</td></tr><tr><td>float capitalRepayment;</td><td>(capital repayment)</td></tr><tr><td>float weeklyPayment;</td><td>(mortgage payment for week)</td></tr><tr><td>float maximumPermittedMortgagePayment;</td><td>(maximum amount the couple may pay)</td></tr></table>

Open the fi le of mortgages, name it inFile , and read each element in turn. 

read (inFile); 

Compute the interest payment, escrow payment, and capital repayment for this mortgage. 

interestPayment = mortgageBalance * INTEREST_RATE / WEEKS_IN_YEAR ; 

escrowPayment = (annualPropertyTax + annualInsurancePremium) / WEEKS_IN_YEAR 

capitalRepayment = weeklyPrincipalAndInterestPayment − interestPayment; 

mortgageBalance −= capitalRepayment; 

First assume that the couple can pay the mortgage in full, without a grant. 

weeklyPayment = weeklyPrincipalAndInterestPayment + escrowPayment; 

Add the weekly Principal and Interest payment to the running total of mortgage payments 

expectedTotalWeeklyMortgages += weeklyPrincipalAndInterestPayment; 

Now determine how much the couple can actually pay. 

maximumPermittedMortgagePayment = currentWeeklyIncome * 

MAXIMUM_PERC_OF_INCOME; 

If a grant is needed, add the grant amount to the running total of grant 

if (weeklyPayment > maximumPermittedMortgagePayment) 

expectedTotalWeeklyGrants += weeklyPayment − maximumPermittedMortgagePayment; 

Close the fi le of mortgages. Return the total expected net payments for the week. 

return (expectedTotalWeeklyMortgages − expectedTotalWeeklyGrants); 

} // totalWeeklyNetPayment 

words, the Unifi ed Process is intended primarily for software products at least 100 times larger than the MSG Foundation case study presented in this book. Accordingly, many aspects of the Unifi ed Process are inapplicable to this case study. For instance, an important part of the analysis workfl ow is to partition the software product into analysis packages. Each package consists of a set of related classes, usually of relevance to a small subset of the actors, that can be implemented as a single unit. For example, accounts payable, accounts receivable, and general ledger are typical analysis packages. The concept underlying analysis packages is that it is much easier to develop smaller software products than larger software products. Accordingly, a large software product is easier to develop if it can be decomposed into relatively independent packages. Decomposing a software product into packages is an example of divide-and-conquer (Section 5.3). 

This idea of decomposing a large workfl ow into relatively independent smaller workfl ows is carried forward to the design workfl ow. Here, the objective is to break up the upcoming implementation workfl ow into manageable pieces, termed subsystems . Again, it does not make sense to break up the MSG Foundation case study into subsystems; the case study is just too small. 

There are two reasons why larger workfl ows are broken into subsystems: 

1. As previously explained, it is easier to implement a number of smaller subsystems than one large system. That is, breaking up a software product into subsystems is another example of divide-and-conquer (Section 5.3). 

2. If the subsystems to be implemented are indeed relatively independent, then they can be implemented by programming teams working in parallel. This results in the software product as a whole being delivered sooner. 

Recall from Section 8.5.4 that the architecture of a software product includes the various components and how they fi t together. The allocation of components to subsystems is a major part of the architectural task. Deciding on the architecture of a software product is by no means easy and, in all but the smallest software products, is performed by a specialist, the software architect. 

In addition to being a technical expert, an architect needs to know how to make trade-offs . A software product has to satisfy the functional requirements, that is, the use cases. It also needs to satisfy the nonfunctional requirements, including portability ( Chapter 8 ), reliability (Section 6.4.2), robustness (Section 6.4.3), maintainability, and security. But it needs to do all these things within budget and time constraints. It is almost never possible to develop a software product that satisfi es all its requirements, both functional and nonfunctional, and fi nish the project within the cost and time constraints; compromises almost always have to be made. The client has to relax some of the requirements, increase the budget, or move the delivery deadline, or do more than one of these. The architect must assist the client’s decision making by clearly mapping out the trade-offs. 

In some cases the trade-offs are obvious. For example, the architect may point out that a set of security requirements that conform to a new high-security standard are going to take a further 3 months and $350,000 to incorporate in the software product. If the product is an international banking network, the issue is moot—there is no way that the client could possibly agree to compromise on security in any way. However, in other instances, the client needs to make critical determinations regarding trade-offs and has to rely on the technical expertise of the architect to assist in coming to the right business decision. For example, the architect might point out that deferring a particular requirement until the software product has been delivered and is being maintained may save $150,000 now but will cost $300,000 to incorporate later (see Figure 1.6). The decision whether or not to defer a requirement can be made only by the client, but he or she needs the technical expertise of the architect to assist in coming to the correct decision. 

The architecture of a software product is a vital factor in the delivered product’s success or a failure. And the critical decisions regarding the architecture have to be made while performing the design workfl ow. If the requirements workfl ow is badly performed, it is still possible to have a successful project, provided additional time and money are spent on the analysis workfl ow. Similarly, if the analysis workfl ow is inadequate, it is possible to recover by making an extra effort as part of the design workfl ow. But if the architecture is suboptimal, there is no way to recover; the architecture must immediately be redesigned. It is therefore essential that the development team include an architect with the necessary technical expertise and people skills. 

## 14.10 The Test Workfl ow: Design

The goal of testing the design is to verify that the specifi cations have been accurately and completely incorporated into the design as well as to ensure the correctness of the design itself. For example, the design must have no logic faults, and all interfaces must be correctly defi ned. It is important that any faults in the design be detected before coding commences; otherwise, the cost of fi xing the faults will be considerably higher, as refl ected in Figure 1.6. Design faults can be detected by means of design inspections as well as design walkthroughs. Design inspections are discussed in the remainder of this section, but the remarks apply equally to design walkthroughs. 

When the product is transaction oriented (Section 14.4), the design inspection should refl ect this [Beizer, 1990]. Inspections that include all possible transaction types should be scheduled. The reviewer should relate each transaction in the design to the specifi cations, showing how the transaction arises from the specifi cation document. For example, if the application is an automated teller machine, a transaction corresponds to each operation the customer can perform, such as deposit to or withdraw from a credit card account. In other instances, the correspondence between specifi cations and transactions is not necessarily one-to-one. In a traffi c-light control system, for example, if an automobile driving over a sensor pad results in the system deciding to change a particular light from red to green in 15 seconds, then further impulses from that sensor pad may be ignored. Conversely, to speed traffi c fl ow, a single impulse may cause a whole series of lights to be changed from red to green. 

Restricting reviews to transaction-driven inspections does not detect cases where the designers have overlooked instances of transactions required by the specifi cations. To take an extreme example, the specifi cations for the traffi c-light controller may stipulate that between 11:00 P.M. and 6:00 A.M. all lights are to fl ash yellow in one direction and red in the other direction. If the designers overlooked this stipulation, then clock-generated transactions at 11:00 P.M. and 6:00 A.M. would not be included in the design; and if these transactions were overlooked, they could not be tested in a design inspection based on transactions. Therefore, it is not adequate to schedule design inspections that are just transaction driven; specifi cation-driven inspections also are essential to ensure that no statement in the specifi cation document has been either overlooked or misinterpreted. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/61cf23bac060ef1234bb2984659141169457722fb8b60d64cb1f172c12945de1.jpg)


## 14.11 The Test Workfl ow: The MSG Foundation Case Study

Now that the design is apparently complete, all aspects of the design of the MSG Foundation case study must be checked by means of a design inspection (Section 6.2.3). In particular, each design artifact must be examined. Even if no faults are found, it is possible that the design will change again, perhaps radically, when the MSG Foundation case study is implemented. 

## 14.12 Formal Techniques for Detailed Design

One technique for detailed design has already been presented. In Section 5.1, a description of stepwise refi nement was given. It then was applied to detailed design using fl owcharts. In addition to stepwise refi nement, formal techniques can be used to advantage in detailed design. Chapter 6 suggests that implementing a complete product and then proving it correct could be counterproductive. However, developing the proof and the detailed design in parallel and carefully testing the code as well is quite a different matter. Formal techniques applied to detailed design can greatly assist in three ways: 

1. The state of the art in proving correctness is such that, although it generally cannot be applied to a product as a whole, it can be applied to module-sized pieces of a product 

2. Developing a proof together with the detailed design should lead to a design with fewer faults than if correctness proofs were not used. 

3. If the same programmer is responsible for both the detailed design and the implementation, then that programmer will feel confi dent that the detailed design is correct. This positive attitude toward the design should lead to fewer faults in the code. 

## 14.13 Real-Time Design Techniques

As explained in Section 6.4.4, real-time software is characterized by hard time constraints, that is, time constraints of such a nature that, if a constraint is not met, information is lost. In particular, each input must be processed before the next input arrives. An example of such a system is a computer-controlled nuclear reactor. Inputs such as the temperature of the core and the level of the water in the reactor chamber are continually being sent to the computer that reads the value of each input and performs the necessary processing before the next input arrives. Another example is a computer-controlled intensive care unit. There are two types of patient data: routine information such as heart rate, temperature, and blood pressure of each patient, and emergency information, when the system deduces that the condition of a patient has become critical. When such emergencies occur, the software must process both the routine inputs and the emergency-related inputs from one or more patients. 

A characteristic of many real-time systems is that they are implemented on distributed hardware. For example, software controlling a fi ghter aircraft may be implemented on fi ve computers: one to handle navigation, another the weapons system, a third for electronic countermeasures, a fourth to control the fl ight hardware such as wing fl aps and engines, and the fi fth to propose tactics in combat. Because hardware is not totally reliable, there may be additional backup computers that automatically replace a malfunctioning unit. Not only does the design of such a system have major communications implications, but timing issues, over and above those of the type just described, arise as a consequence of the distributed nature of the system. For example, under combat conditions, the tactical computer might suggest that the pilot should climb, whereas the weapons computer recommends that the pilot go into a dive so that a particular weapon may be launched under optimal conditions. However, the human pilot decides to move the stick to the right, thereby sending a signal to the fl ight hardware computer to make the necessary adjustments so that the plane banks in the indicated direction. All this information must be managed carefully in such a way that the actual motion of the plane takes precedence in every way over suggested maneuvers. Furthermore, the actual motion must be relayed to the tactical and weapons computers so that new suggestions can be formulated in the light of actual, rather than suggested, conditions. 

A further diffi culty with real-time systems is the problem of synchronization. Suppose that a real-time system is to be implemented on distributed hardware. Situations such as deadlock (or deadly embrace) can arise when two operations each have exclusive use of a data item and each requests exclusive use of the other’s data item in addition. Of course, deadlock does not occur only in real-time systems, implemented on distributed hardware. But it is particularly troublesome in real-time systems where there is no control over the order or timing of the inputs, and the situation can be complicated by the distributed nature of the hardware. In addition to deadlock, other synchronization problems are possible, including race conditions; for details, the reader may refer to [Silberschatz, Galvin, and Gagne, 2002] or other operating systems textbooks. 

From these examples it is clear that the major diffi culty with regard to the design of realtime systems is ensuring that the timing constraints are met by the design. That is, the design technique should provide a mechanism for checking that, when implemented, the design is able to read and process incoming data at the required rate. Furthermore, it should be possible to show that synchronization issues in the design also have been addressed correctly. 

Since the beginning of the computer age, advances in hardware technology have outstripped, in almost every respect, advances in software technology. Therefore, although the hardware exists to handle every aspect of the real-time systems described previously, software design technology has lagged behind considerably. In some areas of real-time software engineering, major progress has been made. For instance, many of the analysis techniques of Chapters 12 and 13 can be used to specify real-time systems. Unfortunately, software design has not yet reached the same level of sophistication. Great strides indeed are being made, but the state of the art is not yet comparable to what has been achieved with regard to analysis techniques. Because almost any design technique for real-time systems is preferable to no technique at all, a number of real-time design techniques are used in practice. But, there still is a long way to go before it will be possible to design real-time systems such as those described previously and be certain that, before the system has been implemented, every real-time constraint will be met and synchronization problems cannot arise. 

Older real-time design techniques are extensions of non-real-time techniques to the real-time domain. For example, structured development for real-time systems (SDRTS) [Ward and Mellor, 1985] essentially is an extension of structured systems analysis (Section 12.3), data fl ow analysis (Section 14.3), and transaction analysis (Section 14.4) to real-time software. The development technique includes a component for real-time design. Newer techniques are described in [Liu, 2000] and [Gomaa, 2000]. 

As stated previously, it is unfortunate that the state of the art of real-time design is not as advanced as one would wish. Nevertheless, efforts are under way to improve the situation. 

## 14.14 CASE Tools for Design

As stated in Section 14.10, a critical aspect of design is testing that the design artifacts accurately incorporate all aspects of the analysis. What is therefore needed is a CASE tool that can be used both for the analysis artifacts and the design artifacts, a so-called front-end or upperCASE tool (as opposed to a back-end or lowerCASE tool, which assists with the implementation artifacts). 

A number of upperCASE tools are on the market. Some of the more popular ones include Analyst/Designer, Software through Pictures, and System Architect. UpperCASE tools generally are built around a data dictionary. The CASE tool can check that every fi eld of every record in the dictionary is mentioned somewhere in the design or that every item in the design is refl ected in the data fl ow diagram. In addition, many upperCASE tools incorporate a consistency checker that uses the data dictionary to determine that every item in the design has been declared in the specifi cations and conversely that every item in the specifi cations appears in the design. 

Furthermore, many upperCASE tools incorporate screen and report generators. That is, the client can specify what items are to appear in a report or on an input screen and where and how each item is to appear. Because full details regarding every item are in the data dictionary, the CASE tool can easily generate the code for printing the report or displaying the input screen according to the client’s wishes. Some upperCASE products also incorporate management tools for estimating and planning. 

With regard to object-oriented design, Together, IBM Rational Rose, and Software through Pictures provide support for this workfl ow within the context of the complete object-oriented life cycle. Open-source CASE tools of this type include ArgoUML. 

## 14.15 Metrics for Design

A variety of metrics can be used to describe aspects of the design. For example, the number of code artifacts (modules or classes) is a crude measure of the size of the target product. Cohesion and coupling are measures of the quality of the design, as are fault statistics. As with all other types of inspection, it is vital to keep a record of the number and type of design faults detected during a design inspection. This information is used during code inspections of the product and in design inspections of subsequent products. 

The cyclomatic complexity M of a detailed design is the number of binary decisions (predicates) plus 1 [McCabe, 1976] or, equivalently, the number of branches in the code artifact. It has been suggested that cyclomatic complexity is a metric of design quality; the lower the value of M , the better. A strength of this metric is that it is easy to compute. However, it has an inherent problem. Cyclomatic complexity is purely a measure of the control complexity; the data complexity is ignored. That is, M does not measure the complexity of a code artifact that is data driven, such as by the values in a table. For example, suppose a designer is unaware of the C++ library function toascii and designs a code artifact from scratch that reads a character input by the user and returns the corresponding ASCII code (an integer between 0 and 127). One way of designing this is by means of a 128-way branch implemented by means of a switch statement. A second way is to have an array containing the 128 characters in ASCII code order and utilize a loop to compare the character input by the user with each element of the array of characters; the loop is exited when a match is obtained. The current value of the loop variable then is the corresponding ASCII code. The two designs are equivalent in functionality but have cyclomatic complexities of 128 and 1, respectively. 

When the classical paradigm is used, a related class of metrics for the design phase is based on representing the architectural design as a directed graph with the modules represented by nodes and the fl ows between modules (procedure and function calls) represented by arcs. The fan-in of a module can be defi ned as the number of fl ows into the module plus the number of global data structures accessed by the module. The fan-out similarly is the number of fl ows out of the module plus the number of global data structures updated by the module. A measure of complexity of the module then is given by length × ( fan-in × fan-out ) <sup>2</sup> [Henry and Kafura, 1981], where length is a measure of the size of the module (Section 9.2.1). Because the defi nitions of fan-in and fan-out incorporate global data, this metric has a data-dependent component. Nevertheless, experiments have shown that this metric is no better a measure of complexity than simpler metrics, such as cyclomatic complexity [Kitchenham, Pickard, and Linkman, 1990; Shepperd, 1990]. 

The issue of design metrics is complicated even more when the object-oriented paradigm is used. For example, the cyclomatic complexity of a class usually is low, because many classes typically include a large number of small, straightforward methods. Furthermore, as previously pointed out, cyclomatic complexity ignores data complexity. Because data and operations are equal partners within the object-oriented paradigm, cyclomatic complexity overlooks a major component that could contribute to the complexity of an object. Therefore, metrics for classes that incorporate cyclomatic complexity generally are of little use. 

A number of object-oriented design metrics have been put forward, for example, in [Chidamber and Kemerer, 1994]. These and other metrics have been questioned on both theoretical and experimental grounds [Binkley and Schach, 1996; 1997; 1998] 

## 14.16 Challenges of the Design Workfl ow

As pointed out in Sections 12.16 and 13.22, it is important not to do too much in the analysis workfl ow; that is, the analysis team must not prematurely start parts of the design workfl ow. In the design workfl ow, the design team can go wrong in two ways: by doing too much and by doing too little. 

Consider the PDL (pseudocode) detailed design of Figure 14.7 . The temptation is strong for a designer who enjoys programming to write the detailed design in C++ or Java, rather than PDL. That is, instead of sketching the detailed design in pseudocode, the designer may all but code the class. This takes longer to write than just outlining the class and longer to fi x if a fault is detected in the design (see Figure 1.6). Like the analysis team, the members of the design team must fi rmly resist the urge to do more than what is required of them. 

At the same time, the design team must be careful not to do too little. Consider the tabular detailed design of Figure 14.6 . If the design team is in a hurry, it may decide to shrink the detailed design to just the narrative box. The team may even decide that the programmers should do the detailed design by themselves. Either of these decisions would be a mistake. A primary reason for the detailed design is to ensure that all interfaces are correct. The narrative box by itself is inadequate for this purpose; no detailed design at all clearly is even less helpful. Therefore, one challenge of the design workfl ow is for the designers to do just the correct amount of work 

In addition, there is a much more signifi cant challenge. In “No Silver Bullet” (see Just in Case You Wanted to Know Box 3.4), Brooks [1986] decries the lack of what he terms great designers , that is, designers who are signifi cantly more outstanding than the other members of the design team. In Brooks’s opinion, the success of a software project depends critically on whether the design team is led by a great designer. Good design can be taught; great design is produced only by great designers, and they are “very rare.” 

The challenge, then, is to grow great designers. They should be identifi ed as early as possible (the best designers are not necessarily the most experienced), assigned a mentor, provided a formal education as well as apprenticeships to great designers, and allowed to interact with other designers. A specifi c career path should be available for these designers, and the rewards they receive should be commensurate with the contribution that only a great designer can make to a software development project. 

## Chapter Review

The design workfl ow is introduced in Section 14.1. There are three basic approaches to design: operationoriented design (Section 14.2), data-oriented design (Section 14.5), and object-oriented design (Section 14.6). Two instances of operation-oriented design are described, data fl ow analysis (Section 14.3) and transaction analysis (Section 14.4). Object-oriented design is applied to the elevator problem case study in Section 14.7 and to the MSG Foundation case study in Section 14.8. The design workfl ow is presented in Section 14.9. The design aspects of the test workfl ow are described in Section 14.10 and applied to the MSG Foundation case study in Section 14.11. Formal techniques for detailed design are discussed in Section 14.12. Real-time system design is described in Section 14.13. CASE tools and metrics for the design workfl ow are presented in Sections 14.14 and 14.15, respectively. The chapter concludes with a discussion of the challenges of the design workfl ow (Section 14.16). 

An overview of the MSG Foundation case study for Chapter 14 appears in Figure 14.18 , and for the elevator problem in Figure 14.19. 

<table><tr><td>Object-oriented design</td><td>Section 14.8</td></tr><tr><td>Overall class diagram</td><td>Figure 14.13</td></tr><tr><td>Part of overall class diagram with attribute formats added</td><td>Figure 14.14</td></tr><tr><td>Detailed design</td><td>Appendix G</td></tr></table>

<table><tr><td rowspan="8">Key Terms</td><td>abstract data type design 476</td><td>design workflow 483</td><td>low-level design 466</td></tr><tr><td>accessor 482</td><td>detailed design 466</td><td>modular design 466</td></tr><tr><td>architect 486</td><td>fan-in 491</td><td>mutator 482</td></tr><tr><td>architectural design 466</td><td>fan-out 491</td><td>object-oriented design (OOD)</td></tr><tr><td>class diagram 476</td><td>general design 466</td><td>476</td></tr><tr><td>cyclomatic complexity 491</td><td>high-level design 466</td><td>operation-oriented design 465</td></tr><tr><td>data flow analysis (DFA) 467</td><td>length 491</td><td>package 486</td></tr><tr><td>data-oriented design 465</td><td>logical design 466</td><td>physical design 466</td></tr></table>


FIGURE 14.19 Overview of the elevator problem case study for Chapter 14.


<table><tr><td>Object-oriented design</td><td>Section 14.7</td></tr><tr><td>Detailed class diagram</td><td>Figure 14.11</td></tr></table>

Data fl ow analysis and transaction analysis are described in books such as [Gane and Sarsen, 1979] and [Yourdon and Constantine, 1979]. 

The March–April 2005 issue of IEEE Software contains a number of papers on design. Designing for recovery, that is, designing software to detect, react, and recover from exceptional conditions, is described in [Wirfs-Brock, 2006]. 

Briand, Bunse, and Daly [2001] discuss the maintainability of object-oriented designs. A comparison of both object-oriented and classical design techniques appears in [Fichman and Kemerer, 1992]. The redesign of an air traffi c control system is described in [Jackson and Chapin, 2000]. Design techniques for high-performance, reliable systems are given in [Stolper, 1999]. A probabilis tic approach to estimating the change proneness of an object-oriented design appears in [Tsantalis, Chatzigeorgiou, and Stephanides, 2005]. A discussion as to whether object-oriented design is intui tive appears in [Hadar and Leron, 2008]. 

Formal design techniques are described in [Hoare, 1987]. The vital role played by the architect is described in [McBride, 2007]. Analogously to pair programming, pair design and its effectiveness are described in [Lui, Chan, and Nosek, 2008]. 

With regard to reviews during the design process, the original paper on design inspections is [Fagan, 1976]; detailed information can be obtained from that paper. Later advances in review techniques are described in [Fagan, 1986]. Architecture reviews are discussed in [Maranzano et al., 2005]. 

With regard to real-time design, specifi c techniques are to be found in [Liu, 2000] and [Gomaa, 2000]. A comparison of four real-time design techniques is found in [Kelly and Sherif, 1992]. A documentation-driven approach to the design of complex real-time systems is described in [Luqi, Zhang, Berzins, and Qiao, 2004]. The design of concurrent systems is described in [Magee and Kramer, 1999]. 

Metrics for design are described in [Henry and Kafura, 1981] and [Zage and Zage, 1993]. Metrics for object-oriented design are discussed in [Chidamber and Kemerer, 1994] and in [Binkley and Schach, 1996]. A model for object-oriented quality is presented in [Bansiya and Davis, 2002]. 

The proceedings of the International Workshops on Software Specifi cation and Design are a comprehensive source for information on design techniques. 

<table><tr><td rowspan="2">point of highest abstraction of input 467</td><td>pseudocode 471</td><td>transaction 473</td></tr><tr><td>real-time software 488</td><td>transaction analysis 475</td></tr><tr><td>point of highest abstraction of output 467</td><td>responsibility-driven design 477</td><td>transaction-driven inspections 487</td></tr><tr><td rowspan="2">program description language (PDL) 471</td><td>subsystem 486</td><td></td></tr><tr><td>trade-off 486</td><td></td></tr></table>

## Problems

14.1 Starting with your DFD for Problem 12.9, use data fl ow analysis to design a product for determining whether a bank statement is correct. 

14.2 Use transaction analysis to design the software to control an ATM (Problem 8.9). At this stage omit error-handling capabilities. 

14.3 Now take your design for Problem 14.2 and add modules to perform error handling. Carefully examine the resulting design and determine the cohesion and coupling of the modules. Be on the lookout for situations such as that depicted in Figure 14.10 . 

14.4 Two different techniques for depicting a detailed design are presented in Section 14.3.1 ( Figures 14.6 and 14.7 ). Compare and contrast the two techniques. 

14.5 Starting with your data fl ow diagram for the automated library circulation system (Problem 12.11), design the circulation system using data fl ow analysis. 

14.6 Repeat Problem 14.5 using transaction analysis. Which of the two techniques did you fi nd to be more appropriate? 

14.7 Complete the detailed class diagram for the elevator problem case study ( Figure 14.11 ) by listing the methods of the form Send message to C Class . . . that need to be included in the Elevator Subcontroller Class. 

14.8 Complete the detailed class diagram for the elevator problem case study ( Figure 14.11 ) by listing the methods of the form Send message to C Class . . . that need to be included in the Floor Subcontroller Class. 

14.9 Complete the detailed class diagram for the elevator problem case study ( Figure 14.11 ) by listing the methods of the form Send message to C Class . . . that need to be included in the Sensor Class . 

14.10 Complete the detailed class diagram for the elevator problem case study ( Figure 14.11 ) by listing the methods of the form Send message to C Class . . . that need to be included in the Floor Button Class . 

14.11 Complete the detailed class diagram for the elevator problem case study ( Figure 14.11 ) by listing the methods of the form Send message to C Class . . . that need to be included in the Elevator Button Class . 

14.12 Complete the detailed class diagram for the elevator problem case study ( Figure 14.11 ) by listing the methods of the form Send message to C Class . . . that need to be included in the Scheduler Class . 

14.13 (Analysis and Design Project) Starting with your object-oriented analysis for the automated library circulation system (Problem 13.19), design the library system using object-oriented design. 

14.14 (Analysis and Design Project) Starting with your object-oriented analysis for the product for determining whether a bank statement is correct (Problem 13.20), design the software using object-oriented design. 

14.15 (Analysis and Design Project) Starting with your object-oriented analysis for the ATM software (Problem 13.21), design the ATM software using object-oriented design. 

14.16 (Term Project) Starting with your specifi cations of Problem 12.20 or 13.22, design the Chocoholics Anonymous product (Appendix A). Use the design technique specifi ed by your instructor. 

14.17 (Case Study) Redesign the MSG Foundation product using data fl ow analysis. 

14.18 (Case Study) Redesign the MSG Foundation product using transaction analysis. 

14.19 (Case Study) The detailed design of Figures 14.16 and 14.17 is represented in PDL form. Represent the design using a tabular format. Which representation is superior? Give reasons for your answer. 

14.20 (Readings in Software Engineering) Your instructor will distribute copies of [Hadar and Leron, 2008]. To what extent do you think that object-oriented design is intuitive? 

## References



[Bansiya and Davis, 2002] J. BANSIYA AND C. G. DAVIS, “A Hierarchical Model for Object-Oriented Design Quality Assessment,” IEEE Transactions on Software Engineering 28 (January 2002), pp. 4–17. 





[Beizer, 1990] B. BEIZER, Software Testing Techniques, 2nd ed., Van Nostrand Reinhold, New York, 1990. 





[Binkley and Schach, 1996] A. B. BINKLEY AND S. R. SCHACH, “A Comparison of Sixteen Quality Metrics for Object-Oriented Design,” Information Processing Letters 57 (No. 6, June 1996), pp. 271–75. 





[Binkley and Schach, 1997] A. B. BINKLEY AND S. R. SCHACH, “Toward a Unifi ed Approach to Object-Oriented Coupling,” Proceedings of the 35th Annual ACM Southeast Conference , Murfreesboro, TN, April 2-4, 1997, IEEE, pp. 91–97. 





[Binkley and Schach, 1998] A. B. BINKLEY AND S. R. SCHACH, “Validation of the Coupling Dependency Metric as a Predictor of Run-Time Failures and Maintenance Measures,” Proceedings of the 20th International Conference on Software Engineering , Kyoto, Japan, April 1988, IEEE, pp. 542–55. 





[Briand, Bunse, and Daly, 2001] L. C. BRIAND, C. BUNSE, AND J. W. DALY, “A Controlled Experiment for Evaluating Quality Guidelines on the Maintainability of Object-Oriented Designs,” IEEE Transactions on Software Engineering 27 (June 2001), pp. 513–30. 





[Brooks, 1986] F. P. BROOKS, JR., “No Silver Bullet,” in: Information Processing ’86 , H.-J. Kugler (Editor), Elsevier North-Holland, New York, 1986; reprinted in: IEEE Computer 20 (April 1987), pp. 10–19. 





[Chidamber and Kemerer, 1994] S. R. CHIDAMBER AND C. F. KEMERER, “A Metrics Suite for Object Oriented Design,” IEEE Transactions on Software Engineering 20 (June 1994), pp. 476–93. 





[Fagan, 1976] M. E. FAGAN, “Design and Code Inspections to Reduce Errors in Program Development,” IBM Systems Journal 15 (No. 3, 1976), pp. 182–211. 





[Fagan, 1986] M. E. FAGAN, “Advances in Software Inspections,” IEEE Transactions on Software Engineering SE-12 (July 1986), pp. 744–51. 





[Fichman and Kemerer, 1992] R. G. FICHMAN AND C. F. KEMERER, “Object-Oriented and Conventional Analysis and Design Methodologies: Comparison and Critique,” IEEE Computer 25 (October 1992), pp. 22–39. 





[Flanagan, 2005] D. FLANAGAN, Java in a Nutshell: A Desktop Quick Reference , 5th ed., O’Reilly and Associates, Sebastopol, CA, 2005. 





[Gane and Sarsen, 1979] C. GANE AND T. SARSEN, Structured Systems Analysis: Tools and Techniques , Prentice Hall, Englewood Cliffs, NJ, 1979. 





[Goldberg and Robson, 1989] A. GOLDBERG AND D. ROBSON, Smalltalk-80: The Language, Addison-Wesley, Reading, MA, 1989. 





[Gomaa, 2000] H. GOMAA, Designing Concurrent, Distributed, and Real-time Applications with UML , Addison-Wesley, Reading, MA, 2000. 





[Hadar and Leron, 2008] “How Intuitive Is Object-Oriented Design?” Communications of the ACM 51 (May 2008), pp. 41–46. 





[Henry and Kafura, 1981] S. M. HENRY AND D. KAFURA, “Software Structure Metrics Based on Information Flow,” IEEE Transactions on Software Engineering SE-7 (September 1981), pp. 510–18. 





[Hoare, 1987] C. A. R. HOARE, “An Overview of Some Formal Methods for Program Design,” IEEE Computer 20 (September 1987), pp. 85–91. 





[ISO/IEC 8652, 1995] Programming Language Ada: Language and Standard Libraries , ISO/IEC 8652, International Organization for Standardization, International Electrotechnical Commission, Geneva, Switzerland, 1995. 





[Jackson, 1975] M. A. JACKSON, Principles of Program Design , Academic Press, New York, 1975. 





[Jackson and Chapin, 2000] D. JACKSON AND J. CHAPIN, “Redesigning Air Traffi c Control: An Exercise in Software Design,” IEEE Software 17 (May–June 2000), pp. 63–70. 





[Kelly and Sherif, 1992] J. C. KELLY AND J. S. SHERIF, “A Comparison of Four Design Methods for Real-Time Software Development,” Information and Software Technology 34 (February 1992), pp. 74–82. 





[Kitchenham, Pickard, and Linkman, 1990] B. A. KITCHENHAM, L. M. PICKARD, AND S. J. LINK-MAN, “An Evaluation of Some Design Metrics,” Software Engineering Journal 5 (January 1990), pp. 50–58. 





[Liu, 2000] J. W. S. LIU, Real Time Systems , Prentice Hall, Upper Saddle River, NJ, 2000. 





[Lui, Chan, and Nosek, 2008] K. M. LUI, K. C. C. CHAN, AND J. T. NOSEK, “The Effect of Pairs in Program Design Tasks,” IEEE Transactions on Software Engineering 34 (March–April 2008), pp. 197–211. 





[Luqi, Zhang, Berzins, and Qiao, 2004] LUQI, L. ZHANG, V. BERZINS, AND Y. QIAO, “Documentation Driven Development for Complex Real-Time Systems,” IEEE Transactions on Software Engineering 30 (December 2004), pp. 936–52. 





[Magee and Kramer, 1999] J. MAGEE AND J. KRAMER, Concurrency: State Models & Java Programs , John Wiley and Sons, New York, 1999. 





[Maranzano et al., 2005] J. F. MARANZANO, S. A. ROZSYPAL, G. H. ZIMMERMAN, G. W. WARNKEN, P. E. WIRTH, AND D. M. WEISS, “Architecture Reviews: Practice and Experience,” IEEE Software 22 (March–April 2005), pp. 34–43. 





[McCabe, 1976] T. J. MCCABE, “A Complexity Measure,” IEEE Transactions on Software Engineering SE-2 (December 1976), pp. 308–20. 





[McBride, 2007] M. R. MCBRIDE, “The Software Architect,” Communications of the ACM 50 (May 2007), pp. 75–81. 





[Orr, 1981] K. ORR, Structured Requirements Defi nition , Ken Orr and Associates, Topeka, KS, 1981. 





[Shepperd, 1990] M. SHEPPERD, “Design Metrics: An Empirical Analysis,” Software Engineering Journal 5 (January 1990), pp. 3–10. 





[Silberschatz, Galvin, and Gagne, 2002] A. SILBERSCHATZ, P. B. GALVIN, AND G. GAGNE, Operating System Concepts, 6th ed., Addison-Wesley, Reading, MA, 2002. 





[Stolper, 1999] S. A. STOLPER, “Streamlined Design Approach Lands Mars Pathfi nder,” IEEE Software 16 (September–October 1999), pp. 52–62. 





[Stroustrup, 2003] B. STROUSTRUP, The C++ Standard: Incorporating Technical Corrigendum No. 1 , 2nd ed., John Wiley and Sons, New York, 2003. 





[Tsantalis, Chatzigeorgiou, and Stephanides, 2005] N. TSANTALIS, A. CHATZIGEORGIOU, AND G. STEPHANIDES, “Predicting the Probability of Change in Object-Oriented Systems,” IEEE Transactions on Software Engineering 31 (July 2005), pp. 601–14. 





[Ward and Mellor, 1985] P. T. WARD AND S. MELLOR, Structured Development for Real-Time Systems, Vols. 1, 2, and 3, Yourdon Press, New York, 1985. 





[Warnier, 1976] J. D. WARNIER, Logical Construction of Programs , Van Nostrand Reinhold, New York, 1976. 





[Wirfs-Brock, 2006] R. WIRFS-BROCK, “Designing for Recovery,” IEEE Software 23 (July–August 2006), pp. 11–13. 





[Yourdon and Constantine, 1979] E. YOURDON AND L. L. CONSTANTINE, Structured Design: Fundamentals of a Discipline of Computer Program and Systems Design , Prentice Hall, Englewood Cliffs, NJ, 1979. 





[Zage and Zage, 1993] W. M. ZAGE AND D. M. ZAGE, “Evaluating Design Metrics on Large-Scale Software,” IEEE Software 10 (July 1993), pp. 75–81. 



# Implementation

Learning Objectives 

After studying this chapter, you should be able to 

• Perform the implementation workfl ow. 

• Perform black-box, glass-box, and non-execution-based unit testing. 

• Perform integration testing, product testing, and acceptance testing. 

• Appreciate the need for good programming practices and programming standards. 

Implementation is the process of translating the detailed design into code. When this is done by a single individual, the process is relatively well understood. But, most real-life products today are too large to be implemented by one programmer within the given time constraints. Instead, the product is implemented by a team, working at the same time on different components of the product; this is termed programming-in-the-many . Issues associated with programming-in-the-many are examined in this chapter. 

## 15.1 Choice of Programming Language

In most cases, the issue of which programming language to choose for the implementation simply does not arise. Suppose the client wants a product to be implemented in, say, Smalltalk. Perhaps, in the opinion of the development team, Smalltalk is entirely unsuitable for the product. Such an opinion is irrelevant to the client. Management of the development organization has only two choices: Implement the product in Smalltalk or turn down the job. 

Similarly, if the product has to be implemented on a specifi c computer and the only language available on that computer is assembler, then again there is no choice. If no other language i available, either because no compiler has yet been developed for any high-level language on that computer or management is not prepared to pay for a new C++ compiler for the stipulated computer, then again clearly the issue of choice of programming language is not relevant. 

A more interesting situation is this: A contract specifi es that the product is to be implemented in “the most-suitable” programming language. What language should be chosen? To answer this question, consider the following scenario. QQQ Corporation has been writing COBOL products for over 30 years. The entire 200-member software staff of QQQ, from the most junior programmer to the vice-president for software, has COBOL expertise. Why on earth should the most suitable programming language be anything but COBOL? The introduction of a new language, Java, for example, would mean having to hire new programmers, or, at the very least, existing staff would have to be intensively retrained. Having invested all that money and effort in Java training, management might well decide that future products also should be implemented in Java. Nevertheless, all the existing COBOL products would have to be maintained. There then would be two classes of programmers, COBOL maintenance programmers and Java programmers writing the new applications. Quite undeservedly, maintenance almost always is considered inferior to developing new applications, so there would be distinct unhappiness among the ranks of the COBOL programmers. This unhappiness would be compounded by the fact that Java programmers usually are paid more than COBOL programmers because Java programmers are in short supply. Although QQQ has excellent development tools for COBOL, a Java compiler would have to be purchased, as well as appropriate Java CASE tools. Additional hardware may have to be purchased or leased to run this new software. Perhaps most serious of all, QQQ has accumulated hundreds of person-years of COBOL expertise, the kind of expertise that can be gained only through hands-on experience, such as what to do when a certain cryptic error message appears on the screen or how to handle the quirks of the compiler. In brief, it would seem that “the most suitable” programming language could be only COBOL—any other choice would be fi nancial suicide, either from the viewpoint of the cost involved or as a consequence of plummeting staff morale leading to poor-quality code. 

And yet, the most suitable programming language for QQQ Corporation’s latest project may indeed be some language other than COBOL. Notwithstanding its position as the world’s most widely used programming language (see Just in Case You Wanted to Know Box 15.1), COBOL is suited for only one class of software products, data-processing applications. If QQQ Corporation has software needs outside this class, then COBOL rapidly loses its attractiveness. For example, if QQQ wishes to construct a knowledge-based product using artifi cial intelligence (AI) techniques, then an AI language such as Lisp could be used; COBOL is totally unsuitable for AI applications. If large-scale communications software is to be built, perhaps because QQQ requires satellite links to hundreds of branch offi ces all over the world, then a language such as Java would prove far more suitable than COBOL. If QQQ is to go into the business of writing systems software, such as operating systems, compilers, and linkers, then COBOL very defi nitely is unsuitable. And, if QQQ Corporation decides to go into defense contracting, management will soon discover that COBOL simply cannot be used for real-time embedded software. 

The issue of which programming language to use often can be decided by using cost– benefi t analysis (Section 5.2). That is, management must compute the dollar cost of an implementation in COBOL as well as the dollar benefi ts, present and future, of using COBOL. This computation must be repeated for every language under consideration. The language with the largest expected gain (that is, the difference between estimated benefi ts and estimated costs) is then the appropriate implementation language. Another way of deciding which programming language to select is to use risk analysis. For each language 

# Just in Case You Wanted to Know

Far more code has been implemented in COBOL than in all other programming languages put together. COBOL is the most widely used language primarily because COBOL is a product of the U.S. Department of Defense (DoD). Developed under the direction of the late Rear-Admiral Grace Murray Hopper, COBOL was approved by the DoD in 1960. Thereafter, the DoD would not buy hardware for running data-processing applications unless that hardware had a COBOL compiler [Sammet, 1978]. The DoD was, and still is, the world’s largest purchaser of computer hardware; and in the 1960s, a considerable proportion of DoD software was implemented for data processing. As a result, COBOL compilers were developed as a matter of urgency for virtually every computer. This widespread availability of COBOL, at a time when the only alternative language usually was assembler, resulted in COBOL becoming the world’s most popular programming language. 

Languages such as C, C--, Java, and the 4GLs undoubtedly are growing in popularity for new applications. Nevertheless, postdelivery maintenance still is the major software activity, and this maintenance is being performed on existing COBOL software. In short, the DoD put its stamp onto the world’s software via its fi rst major programming language, COBOL. 

Another reason for the popularity of COBOL is that COBOL frequently is the best language for implementing a data-processing product. In particular, COBOL generally is the language of choice when money is involved. Financial books have to balance, so rounding errors cannot be allowed to creep in. Therefore, all computations have to be performed using integer arithmetic. COBOL supports integer arithmetic on very large numbers (that is, billions of dollars). In addition, COBOL can handle very small numbers, such as fractions of a cent. Banking regulations require interest computations to be calculated to at least four decimal places of a cent, and COBOL can do this arithmetic with ease as well. Finally, COBOL probably has the best formatting, sorting, and report generation facilities of any third-generation language (or high-level language, see Section 15.2). All these reasons have made COBOL an excellent choice for implementing a data-processing product. 

As mentioned in Section 8.11.4, the current COBOL language standard is for an objectoriented language. This standard surely will further boost the popularity of COBOL. 

under consideration, a list is made of the potential risks and ways of resolving them. The language for which the overall risk is the smallest then is selected. 

Currently, software organizations are under pressure to develop new software in an object-oriented language—any object-oriented language. The question that arises is this: Which is the appropriate object-oriented language? Twenty years ago, there really was only one choice, Smalltalk. Today, however, the most widely used object-oriented programming language is C++ [Borland, 2002], with Java in second place. There are a number of reasons for the popularity of C++. One is the widespread availability of C++ compilers. In fact, some C++ compilers simply translate the source code from C++ into C, and then invoke the C compiler. Therefore, any computer with a C compiler essentially can handle C++. 

But the real explanation for the popularity of C++ is its apparent similarity to C. This is unfortunate, in that a number of managers view C++ as a superset of C and, therefore, conclude that any programmer who knows C can quickly pick up the additional pieces. Indeed, from just a syntactical viewpoint, C++ essentially is a superset of C. After all, virtually any C program can be compiled using a C++ compiler. Conceptually, however, C++ is totally different from C. C is a product of the classical paradigm, whereas C++ is for the object-oriented paradigm. Using C++ makes sense only if object-oriented techniques have been used and if the product is organized around objects and classes, not functions. 

Therefore, before an organization adopts C++, it is essential that the relevant software professionals be trained in the object-oriented paradigm. It is particularly important that the information of Chapter 7 be taught. Unless it is clear to all involved, and particularly to management, that the object-oriented paradigm is a different way of developing software and what the precise differences are, the classical paradigm will just continue to be used but with the code implemented in C++ rather than C. When organizations are disappointed with the results of switching from C to C++, a major contributory factor is a lack of education in the object-oriented paradigm. 

Suppose that an organization decides to adopt Java. In that case it is not possible to move gradually from the classical paradigm to the object-oriented paradigm. Java is a pure object-oriented programming language; it does not support the functions and procedures of the classical paradigm. Unlike a hybrid object-oriented language such as C++, Java programmers have to use the object-oriented paradigm (and only the object-oriented paradigm) from the very beginning. Because of the necessity of an abrupt transition from the one paradigm to the other, education and training are even more important when adopting Java (or another pure object-oriented language, such as Smalltalk) than if the organization were to switch to a hybrid object-oriented language like C++ or OO-COBOL. 

## 15.2 Fourth-Generation Languages

The fi rst computers had neither interpreters nor compilers. They were programmed in binary, either hardwired with plug boards or by setting switches. Such a binary machine code was a fi rst-generation language . The second-generation languages were assemblers, developed in the late 1940s and early 1950s. Instead of having to program in binary, instructions could be expressed in symbolic notation such as 

## mov $17, next

In general, each assembler instruction is translated into one machine code instruction. So, although assembler was easier to write than machine code and easier for postdelivery maintenance programmers to comprehend, the assembler source code was the same length as the machine code. 

The idea behind a third-generation language (or high-level language), such as C, C++, Pascal, or Java, is that one statement of a high-level language is compiled to as many as 5 or 10 machine code instructions (this is another example of abstraction; see Section 7.4.1). High-level language code is hence considerably shorter than the equivalent assembler code. It is also simpler to understand and, therefore, easier to maintain than assembler code. The fact that the high-level language code may not be quite as effi cient as the equivalent assembler code generally is a small price to pay for ease in postdelivery maintenance. 

This concept was taken further in the late 1970s. A major objective in the design of a fourth-generation language (4GL) is that each 4GL statement should be equivalent to 30, or even 50, machine code instructions. Products implemented in a 4GL such as Focus or Natural are shorter and hence quicker to develop and easier to maintain. 

Some years ago I hailed a cab outside Grand Central Station in New York City and said to the driver, “Please take me to Lincoln Center.” This was a nonprocedural request, because I expressed the desired result but left it to the driver to decide how to achieve that result. It turned out that the driver was an immigrant from Central Europe who had been in America less than 2 months and knew virtually nothing about the geography of New York City or the English language. As a result, I quickly replaced my nonprocedural request with a procedural request of the form, “Straight, straight. Take a right at the next light. I said right. Right, here, yes, right! Now straight. Slow down, please. I said slow down. For heaven’s sake, slow down!” and so on, until we fi nally reached Lincoln Center. 

It is diffi cult to program in machine code. It is somewhat easier to program in assembler, and easier still to use a high-level language. A second major design objective of a 4GL is ease in programming. In particular, many 4GLs are nonprocedural (see Just in Case You Wanted to Know Box 15.2 for an insight into this term). For example, consider the command 

## for every surveyor if rating is excellent add 6500 to salary

It is up to the compiler of the 4GL to translate this nonprocedural instruction into a sequence of machine code instructions that can be executed procedurally. 

Success stories abound from organizations that have switched to a 4GL. A few that previously used COBOL reported a 10-fold increase in productivity through use of a 4GL. Many organizations found that their productivity indeed increased through use of a 4GL but not spectacularly so. Other organizations tried a 4GL and were bitterly disappointed with the results. 

One reason for this inconsistency is that it is unlikely that one 4GL will be appropriate for all products. On the contrary, it is important to select the correct 4GL for the specifi c product. For example, Playtex used IBM’s Application Development Facility (ADF) and reported an 80 to 1 productivity increase over COBOL. Notwithstanding this impressive result, Playtex subsequently returned to COBOL for products deemed by management to be less well suited to ADF [Martin, 1985]. 

A second reason for these inconsistent results is that many 4GLs are supported by powerful CASE workbenches and environments (Section 5.7). CASE workbenches and environments can be both a strength and a weakness. As explained in Section 5.12, it is inadvisable to introduce large-scale CASE within an organization with a low maturity level. The reason is that the purpose of a CASE workbench or environment is to support the software process. An organization at level 1 has no software process in place. If at this point CASE is introduced as part of the transition to a 4GL, this imposes a process onto an organization not ready for any sort of process. The usual consequences at best are unsatisfactory and can be disastrous. In fact, a number of reported 4GL failures can be ascribed to the effects of the associated CASE environment rather than to the 4GL itself. 

The attitudes of 43 organizations to 4GLs are reported in [Guimaraes, 1985]. This research found that use of a 4GL reduced user frustration because the data-processing de partment could respond more quickly when a user needed information extracted from the organization’s database. However, there also were a number of problems. Some 4GLs proved to be slow and ineffi cient, with long response times. One product consumed 60 percent of the CPU cycles on an IBM 4331 mainframe, while supporting, at most, 12 concurrent users. Overall, the 28 organizations that had been using a 4GL for over 3 years felt that the benefi ts outweighed the costs. 

No one 4GL dominates the software market. Instead, there are hundreds of 4GLs; some of them, including DB2, Oracle, and PowerBuilder, have sizable user groups. This widespread proliferation of 4GLs is further evidence that care has to be taken in selecting the correct 4GL. Of course, few organizations can afford to support more than one 4GL. Once a 4GL has been chosen and used, the organization must either use that 4GL for subsequent products or fall back on the language used before the 4GL was introduced. 

Notwithstanding the potential productivity gain, there could be danger in using a 4GL the wrong way. Many organizations currently have a large backlog of products to be developed and a long list of postdelivery maintenance tasks to be performed. A design objective of many 4GLs is end-user programming , that is, programming by the person who will use the product. For example, before the advent of 4GLs, the investment manager of an insurance company would ask the data-processing manager for a product that would display certain information regarding the bond portfolio. The investment manager then would wait a year or so for the data-processing group to fi nd the time to develop the product. A 4GL was desired that would be so simple to use that the investment manager, previously untrained in programming, could implement the desired product unaided. End-user programming was intended to help reduce the development backlog, leaving the professionals to maintain existing products. 

In practice, end-user programming can be dangerous. First, consider the situation when all product development is performed by computer professionals. Computer professionals are trained to mistrust computer output. After all, probably less than 1 percent of all output during product development is correct. On the other hand, the user is told to trust all computer output, because no product should be delivered to the user until it is fault free. Now consider the situation when end-user programming is encouraged. When a user who is inexperienced in programming implements code with a user-friendly, nonprocedural 4GL, the natural tendency is for that user to believe the output. After all, for years the user has been instructed to trust computer output. As a result, many business decisions have been based on data generated by hopelessly incorrect end-user code. In some cases, the userfriendliness of certain 4GLs has led to fi nancial catastrophes. 

Another potential danger lies in the tendency, in some organizations, to allow users to implement 4GL products that update the organization’s database. A programming mistake made by a user eventually may result in the corruption of the entire database. The lesson is clear: Programming by inexperienced or inadequately trained users can be exceedingly dangerous, if not fatal, to the fi nancial health of a corporation. 

The ultimate choice of a 4GL is made by management. In making such a decision, management should be guided by the many success stories resulting from the use of a 4GL. At the same time, management should carefully analyze the failures caused by using an inappropriate 4GL, by premature introduction of a CASE environment, and by poor management of the development process. For example, a common cause of failure is neglecting to train the development team thoroughly in all aspects of the 4GL, including relational database theory [Date, 2003] where appropriate. Management should study 

In the late 1970s, a small software organization in Johannesburg, South Africa, consisted of two programming teams. Team A was made up of émigrés from Mozambique. They were of Portuguese extraction, and their native language was Portuguese. Their code was well written. Variable names were meaningful but unfortunately only to a speaker of Portuguese. Team B comprised Israeli immigrants whose native language was Hebrew. Their code was equally well written, and the names they chose for their variables were equally meaningful—but only to a speaker of Hebrew. 

One day, team A resigned en masse, together with its team leader. Team B was totally unable to maintain any of the excellent code that team A had written, because they spoke no Portuguese. The variable names, meaningful as they were to Portuguese speakers, were incomprehensible to the Israelis, whose linguistic abilities were restricted to Hebrew and English. The owner of the software organization was unable to hire enough Portuguesespeaking programmers to replace team A, and the company soon went into bankruptcy, under the weight of numerous lawsuits from disgruntled customers whose code was now essentially unmaintainable. 

The situation could have been avoided easily. The head of the company should have insisted from the start that all variable names be in English, the language understood by every South African computer professional. Variable names then would have been meaningful to any maintenance programmer. 

both the successes and failures in the specifi c application area and learn from past mistakes. Choosing the correct 4GL can mean the difference between a major success and dismal failure. 

Having decided on the implementation language, the next issue is how software engineering principles can lead to better-quality code. 

## 15.3 Good Programming Practice

Many recommendations on good coding style are language specifi c. For example, suggestions regarding use of COBOL 88-level entries or parentheses in Lisp are of little interest to programmers implementing a product in Java. In contrast, recommendations regarding language-independent good programming practice are now given. 

## 15.3.1 Use of Consistent and Meaningful Variable Names

As stated in Chapter 1 , on average at least two-thirds of a software budget is devoted to postdelivery maintenance. This implies that the programmer developing a code artifact is merely the fi rst of many who will work on that code artifact. It is counterproductive for a programmer to give names to variables that are meaningful to only that programmer; within the context of software engineering, the term meaningful variable names means “meaningful from the viewpoint of future maintenance programmers.” This point is amplifi ed in Just in Case You Wanted to Know Box 15.3. 

In addition to the use of meaningful variable names, it is equally essential that consistent variable names be chosen. For example, the following four variables are declared in a code artifact: averageFreq , frequencyMaximum , minFr , and frqncyTotl . A maintenance programmer who is trying to understand the code has to know if freq , frequency , fr , and frqncy all refer to the same thing. If yes, then the identical word should be used, 

# Just in Case You Wanted to Know

There are two explanations for the term Hungarian Naming Conventions . First, these conventions were invented by Charles Simonyi, who was born in Hungary. Second, it generally is agreed that, to the uninitiated, programs with variable names conforming to the conventions are about as easy to read as Hungarian. Nevertheless, organizations (such as Microsoft) that use them claim that they enhance code readability for those with experience in the Hungarian Naming Conventions. 

preferably frequency , although freq or frqncy is marginally acceptable; fr is not. But if one or more variable names refer to a different quantity, then a totally different name, such as rate , should be used. Conversely, do not use two different names to denote the identical concept; for example, both average and mean should not be used in the same program. 

A second aspect of consistency is the ordering of the components of variable names. For example, if one variable is named frequencyMaximum , then the name minimum-Frequency would be confusing; it should be frequencyMinimum. To make the code clear and unambiguous for future maintenance programmers, the four variables listed previously should be named frequencyAverage , frequencyMaximum , frequencyMinimum , and frequencyTotal, respectively. Alternatively, the frequency component can appear at the end of all four variable names, yielding the variable names averageFrequency , maximumFrequency, minimumFrequency , and totalFrequency. It clearly does not matter which of the two sets is chosen; what is important is that all the names be from one set or the other. 

A number of different naming conventions have been put forward that are intended to make it easier to understand the code. The idea is that the name of a variable should incorporate type information. For example, ptrChTmp might denote a temporary variable ( Tmp ) of type pointer ( ptr ) to an character ( Ch ). The best known of such schemes are the Hungarian Naming Conventions [Klunder, 1988]. (If you want to know why they are called Hungarian, see Just in Case You Wanted to Know Box 15.4.) One drawback of many such schemes is that the effectiveness of code inspections (Section 15.14) can be reduced when participants are unable to pronounce the names of variables. It is extremely frustrating to have to spell out variable names, letter by letter. 

## 15.3.2 The Issue of Self-Documenting Code

When asked why their code contains no comments whatsoever, programmers often proudly reply, “I write self-documenting code .” The implication is that their variable names are chosen so carefully and their code crafted so exquisitely that there is no need for comments. Self-documenting code does exist, but it is exceedingly rare. Instead, the usual scenario is that the programmer appreciates every nuance of the code at the time the code artifact is implemented. It is conceivable that the programmer uses the same style for every code artifact and that in 5 years’ time, the code still is crystal clear in every respect to the original programmer. Unfortunately, this is irrelevant. The important point is whether the code artifact can be understood easily and unambiguously by all the other programmers who have to read it, starting with the software quality assurance group and including a number of different postdelivery maintenance programmers. The problem becomes more acute in the light of the unfortunate practice of assigning postdelivery maintenance tasks to inexperienced programmers and not supervising them closely. The undocumented code of the artifact may be only partially comprehensible to an experi enced programmer. How much worse, then, is the situation when the maintenance programmer is inexperienced. 

To see the sorts of problems that can arise, consider the variable xCoordinateOfPosition-OfRobotArm . Such a variable name undoubtedly is self-documenting in every sense of the word, but few programmers are prepared to use a 31-character variable name, especially if that name is used frequently. Instead, a shorter name is used, xCoord , for example. The reasoning behind this is that if the entire code artifact deals with the movement of the arm of a robot, xCoord can refer only to the x coordinate of the position of the arm of the robot. Although that argument holds water within the context of the development process, it is not necessarily true for postdelivery maintenance. The maintenance programmer may not have suffi cient knowledge of the product as a whole to realize that, within this code artifact, xCoord refers to the arm of the robot or may not have the necessary documentation to understand the workings of the code artifact. The way to avoid this sort of problem is to insist that every variable name be explained at the beginning of the code artifact, in the prologue comments . If this rule is followed, the maintenance programmer quickly will understand that variable xCoord is used for the x coordinate of the position of the robot arm. 

Prologue comments are mandatory in every code artifact. The minimum information that must be provided at the top of every code artifact is listed in Figure 15.1. 

Even if a code artifact is clearly written, it is unreasonable to expect someone to have to read every line to understand what the code artifact does and how it does it. Prologue comments make it easy for others to understand the key points. Only a member of the SQA group or a maintenance programmer modifying a specifi c code artifact should be expected to have to read every line of that code artifact. 

<table><tr><td>The name of the code artifact</td></tr><tr><td>A brief description of what the code artifact does</td></tr><tr><td>The programmer&#x27;s name</td></tr><tr><td>The date the code artifact was coded</td></tr><tr><td>The date the code artifact was approved</td></tr><tr><td>The name of the person who approved the code artifact</td></tr><tr><td>The arguments of the code artifact</td></tr><tr><td>A list of the name of each variable of the code artifact, preferably in alphabetical order, and a brief description of its use</td></tr><tr><td>The names of any files accessed by this code artifact</td></tr><tr><td>The names of any files changed by this code artifact</td></tr><tr><td>Input-output, if any</td></tr><tr><td>Error-handling capabilities</td></tr><tr><td>The name of the file containing test data (to be used later for regression testing)</td></tr><tr><td>A list of each modification made to the code artifact, the date the modification was made, and who approved the modification</td></tr><tr><td>Any known faults</td></tr></table>

In addition to prologue comments, inline comments should be inserted into the code to assist maintenance programmers in understanding that code. It has been suggested that inline comments should be used only when the code is implemented in a nonobvious way or uses some subtle aspect of the language. On the contrary, confusing code should be reimplemented in a clearer way. Inline comments are a means of helping maintenance programmers and should not be used to promote or excuse poor programming practice. 

## 15.3.3 Use of Parameters

There are very few genuine constants, that is, variables whose values never change. For instance, satellite photographs have caused changes to be made in submarine navigation systems incorporating the latitude and longitude of Pearl Harbor, Hawaii, to refl ect more accurate geographic data regarding the exact location of Pearl Harbor. To take another example, sales tax is not a genuine constant; legislators tend to change the sales tax rate from time to time. Suppose that the sales tax rate currently is 6.0 percent. If the value 6.0 has been hard coded in a number of code artifacts of a product, then changing the product is a major exercise, with the likely outcome of one or two instances of the “constant” 6.0 being overlooked and, perhaps, changing an unrelated 6.0 by mistake. A better solution is a C++ declaration such as 

## const fl oat salesTaxRate = 6.0;

or, in Java, 

## public static fi nal fl oat salesTaxRate = ( fl oat ) 6.0;

Then, wherever the value of the sales tax rate is needed, the constant salesTaxRate should be used and not the number 6.0 . If the sales tax rate changes, then only the line containing the value of salesTaxRate need be altered using an editor. Better still, the value of the sales tax rate should be read in from a parameter fi le at the beginning of the run. All such apparent constants should be treated as parameters. If a value should change for any reason, this change can be implemented quickly and effectively. 

## 15.3.4 Code Layout for Increased Readability

It is relatively simple to make a code artifact easy to read. For example, no more than one statement should appear on a line, even though many programming languages permit more than one. Indentation is perhaps the most important technique for increasing readability. Just imagine how diffi cult it would be to read the code examples in Chapter 7 if indentation had not been used to assist in understanding the code. In C++ or Java, indentation can be used to connect corresponding { . . . } pairs. Indentation also shows which statements belong in a given block. In fact, correct indentation is too important to be left to humans. Instead, as described in Section 5.8, CASE tools should be used to ensure that indentation is done correctly. 

Another useful aid is blank lines. Methods should be separated by blank lines; in addition, it often is helpful to break up large blocks of code with blank lines. The extra “white space” makes the code easier to read and, hence, comprehend. 

## 15.3.5 Nested if Statements

Consider the following example. A map consists of two squares, as shown in Figure 15.2. It is required to write code to determine whether a point on the Earth’s surface lies in mapSquare1, mapSquare2 , or not on the map at all. The solution of Figure 15.3 is so badly formatted that it is incomprehensible. A properly formatted version appears in Figure 15.4 . Notwithstanding this, the combination of if - if and if - else - if constructs is so complex that it is diffi cult to check whether the code fragment is correct. This is fi xed in Figure 15.5 . When faced with complex code containing the if - if construct, one way to simplify it is to use the fact that the if - if combination 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/8ac53ca1d2d83be239baab8981360cdde4bb69e1dc79111ea77660183b6bdc0e.jpg)


```txt
if (latitude > 30 && longitude > 120) {if (latitude <= 60 && longitude <= 150)
mapSquareNo = 1; else if (latitude <= 90 && longitude <= 150) mapSquareNo = 2
else print "Not on the map";} else print "Not on the map";

if (latitude > 30 && longitude > 120)
{
    if (latitude <= 60 && longitude <= 150)
    mapSquareNo = 1;
    else
    if (latitude <= 90 && longitude <= 150)
    mapSquareNo = 2;
    else
    print "Not on the map";
}
else
    print "Not on the map";

if (longitude > 120 && longitude <= 150 && latitude > 30 && latitude <= 60)
mapSquareNo = 1;
else
    if (longitude > 120 && longitude <= 150 && latitude > 60 && latitude <= 90)
mapSquareNo = 2;
else
    print "Not on the map"; 
```

# if < condition 1>

if < condition 2> 

is equivalent to the single condition 

## if < condition 1> and < condition 2>

provided that < condition 2> is defi ned even if < condition 1> does not hold. For example, < condition 1> might check that a pointer is not null and, if so, then < condition 2> can use that pointer. (This problem does not arise in Java or C++. The && operator is defi ned such that if < condition 1> is false, then < condition 2> is not evaluated—see Problems 15.9 and 15.10.) 

Another problem with the if - if construct is that nesting if statements too deeply leads to code that can be diffi cult to read. As a rule of thumb, if statements nested to a depth greater than three is poor programming practice and should be avoided. 

## 15.4 Coding Standards

Coding standards can be both a blessing and a curse. Section 7.2.1 pointed out that modules with coincidental cohesion (that is, modules that perform multiple, completely unrelated operations) generally arise as a consequence of rules such as, “Every module will consist of between 35 and 50 executable statements.” Instead of stating a rule in such a dogmatic fashion, a better formulation is, “Programmers should consult their managers before constructing a module with fewer than 35 or more than 50 executable statements.” The point is that no coding standard can be applicable under all possible circumstances. 

Coding standards imposed from above tend to be ignored. As mentioned previously, a useful rule of thumb is that if statements should not be nested to a depth greater than three. If programmers are shown examples of unreadable code resulting from nesting if statements too deeply, then it is likely that they will conform to such a regulation. But they are unlikely to adhere to a list of coding rules imposed on them with no discussion or explanation. Furthermore, such standards are likely to lead to friction between programmers and their managers. 

In addition, unless a coding standard can be checked by machine, it is going to either waste a lot of the SQA group’s time or simply be ignored by the programmers and SQA group alike. On the other hand, consider the following rules (see Problems 15.11–15.13): 

• Nesting of if statements should not exceed a depth of three, except with prior approval from the team leader. 

• Modules should consist of between 35 and 50 statements, except with prior approval from the team leader. 

• The use of goto statements should be avoided. However, with prior approval from the team leader, a forward goto may be used for error handling. 

Such rules may be checked by machine, provided some mechanism is set up for capturing the data relating to permission to deviate from the standard. 

The aim of coding standards is to make maintenance easier. However, if the effect of a standard is to make the life of software developers diffi cult, then such a standard should be modifi ed, even in the middle of a project. Overly restrictive coding standards are counterproductive, in that the quality of software production inevitably must suffer if programmers have to develop software within such a framework. On the other hand, standards such as those just listed regarding nesting of if statements, module size, and goto statements, coupled with a mechanism for deviating from those standards, can lead to improved soft ware quality, which, after all, is a major goal of software engineering. 

## 15.5 Code Reuse

Reuse was presented in detail in Chapter 8 . In fact, the material on reuse could have appeared virtually anywhere in this book, because artifacts from all workfl ows of the software process are reused, including portions of specifi cations, contracts, plans, designs, and code artifacts. That is why the material on reuse was put into the fi rst part of the book, rather than tying it to one or another specifi c workfl ow. In particular, it was important that the material on reuse not be presented in this chapter to underline the fact that, even though reuse of code is by far the most common form of reuse, more than just code can be reused. 

## 15.6 Integration

Consider the product depicted in Figure 15.6 . One approach to integration of the product is to code and test each code artifact separately, link together all 13 code artifacts, and test the product as a whole. There are two diffi culties with this approach. First, consider artifact a . It cannot be tested on its own, because it calls artifacts b , c , and d . Therefore, to unit test artifact a , artifacts b , c , and d must be coded as stubs . In its simplest form, a stub is an empty artifact. A more effective stub prints a message such as artifact displayRadarPattern called. Best of all, a stub should return values corresponding to preplanned test cases. 

FIGURE 15.6 A typical interconnection diagram. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/787e3e5d3790400610b5326cec92ffffcd1553bf6ce1dcc5fdbaf29c09d69203.jpg)


Now consider artifact h . To test it on its own requires a driver , a code artifact that calls it one or more times, if possible checking the values returned by the artifact under test. Similarly, testing artifact d requires a driver and two stubs. Therefore, one problem that arises with separate implementation and integration is that effort has to be put into constructing stubs and drivers, all of which are thrown away after unit testing is completed. 

The second, and much more important, diffi culty that arises when implementation is completed before integration starts is lack of fault isolation. If the product as a whole is tested against a specifi c test case and the product fails, then the fault could lie in any of the 13 code artifacts or 13 interfaces. In a large product with, say, 103 code artifacts and 108 interfaces, the fault might lie in no fewer than 211 places. 

The solution to both diffi culties is to combine unit and integration testing. 

## 15.6.1 Top-down Integration

In top-down integration , if code artifact mAbove sends a message to artifact mBelow , then mAbove is implemented and integrated before mBelow . Suppose that the product shown in Figure 15.6 is implemented and integrated top down. One possible top-down ordering is a , b , c , d , e , f , g , h , i , j , k , l , and m . First, artifact a is coded and tested with b , c , and d implemented as stubs. Next stub b is expanded into artifact b , linked to artifact a, and tested with artifact e implemented as a stub. Implementation and integration proceed in this way until all the artifacts have been integrated into the product. Another possible top-down ordering is a , b , e , h , c , d , f , i , g , j , k , l , and m . With this ordering, portions of the integration can proceed in parallel in the following way. After a has been coded and tested, one programmer can use artifact a to implement and integrate b , e , and h , while another programmer can use a to work in parallel on c , d , f, and i . Once d and f are completed, a third programmer can start work on g , j , k , l , and m. 

Suppose that artifact a by itself executes correctly on a specifi c test case. However, when the same test data are submitted after b has been coded and integrated into the product, now consisting of artifacts a and b linked together, the test fails. The fault can be in one of two places, in artifact b or the interface between artifacts a and b . In general, whenever a code artifact mNew is added to what has been tested so far and a previously successful test case fails, the fault almost certainly lies either in mNew or in the interface(s) between mNew and the rest of the product. Accordingly, top-down integration supports fault isolation. 

Another strength of top-down integration is that major design fl aws show up early. The artifacts of a product can be divided into two groups, logic artifacts and operational artifacts. The logic artifacts essentially incorporate the decision-making fl ow of control aspects of the product. The logic artifacts generally are those situated close to the root in the interconnection diagram. For example, in Figure 15.6 , it is reasonable to expect artifacts a , b , c , d, and perhaps g and j to be logic artifacts. The operational artifacts , on the other hand, perform the actual operations of the product. For example, an operational artifact may be named getLineFromTerminal or measureTemperatureOfReactorCore . The operational artifacts generally are found in the lower levels, close to the leaves, of the interconnection diagram. In Figure 15.6 , artifacts e , f , h , i , k , l, and m are operational artifacts. 

It is always important to code and test the logic artifacts before coding and testing the operational artifacts. This ensures that any major design faults show up early. Suppose the whole product is completed before a major fault is detected. Large parts of the product have to be reimplemented, especially the logic artifacts that embody the fl ow of control. Many of the operational artifacts probably are reusable in the rebuilt product; for example, an artifact like getLineFromTerminal or measureTemperatureOfReactorCore is needed no matter how the product is restructured. However, the way the operational artifacts are connected to the other artifacts in the product may have to be changed, resulting in unnecessary work. Therefore, the earlier a design fault is detected, the quicker and less costly it is to correct the product and get back on the development schedule. The order in which artifacts are implemented and integrated using the top-down strategy essentially ensures that logic artifacts indeed are implemented and integrated before operational artifacts, because logic artifacts almost always are the ancestors of operational artifacts in the interconnection diagram. This is a major strength of top-down integration. 

Nevertheless, top-down integration has a weakness: Potentially reusable code artifacts may not be adequately tested, as will be explained. Reuse of an artifact that is thought, incorrectly, to have been thoroughly tested is likely to be less cost-effective than writing that artifact from scratch, because the assumption that an artifact is correct can lead to wrong conclusions when the product fails. Instead of suspecting the insuffi ciently tested, reused artifact, the tester may think that the fault lies elsewhere, resulting in a waste of effort. 

Logic artifacts are likely to be somewhat problem specifi c and hence unusable in another context. However, operational artifacts, particularly if they have informational cohesion (Section 7.2.7), probably are reusable in future products and, therefore, require thorough testing. Unfortunately, the operational artifacts generally are the lower-level code artifacts in the interconnection diagram and hence are not tested as frequently as the upper-level artifacts. For example, if there are 184 artifacts, the root artifact is tested 184 times, whereas the last artifact to be integrated into the product is tested only once. Top-down integration makes reuse a risky undertaking as a consequence of inadequate testing of operational artifacts. 

The situation is exacerbated if the product is well designed; in fact, the better the design, the less thoroughly the artifacts are likely to be tested. To see this, consider an artifact computeSquareRoot . This artifact takes two arguments, a fl oating-point number x whose square root is to be determined and an errorFlag that is set to true if x is negative. Suppose further that computeSquareRoot is invoked by artifact a3 and that a3 contains the statement 

## if (x > = 0) y = computeSquareRoot (x, errorFlag);

In other words, computeSquareRoot is never invoked unless the value of x is nonnegative; therefore, the artifact can never be tested with negative values of x to see if it behaves correctly. The type of design where the calling artifact includes a safety check of this kind is referred to as defensive programming . As a result of defensive programming, subordinate operational artifacts are unlikely to be thoroughly tested if integrated top down. An alternative to defensive programming is the use of responsibility-driven design (Section 1.9). Here, the necessary safety checks are built into the invoked artifact, rather than the invoker. Another approach is the use of assertions in the invoked artifact (Section 6.5.3). 

## 15.6.2 Bottom-up Integration

In bottom-up integration , if artifact mAbove sends a message to artifact mBelow , then mBelow is implemented and integrated before mAbove . In Figure 15.6 , one possible bottom-up ordering is l , m , h , i , j , k , e , f , g , b , c , d , and a. To have the product coded by a team, a better bottom-up ordering is as follows: h , e , and b are given to one programmer and i , f , and c to another. The third programmer starts with l , m , j , k , and g , and then implements d and integrates his or her work with the work of the second programmer. Finally, when b , c , and d have been successfully integrated, a can be implemented and integrated. 

The operational artifacts thereby are tested thoroughly when a bottom-up strategy is used. In addition, the testing is done with the aid of drivers, rather than by fault-shielding, defensively programmed artifacts. Although bottom-up integration solves the major diffi culty of top-down integration and shares with top-down integration the advantage of fault isolation, it unfortunately has a diffi culty of its own. Specifi cally, major design faults are detected late in the implementation workfl ow. The logic artifacts are integrated last; hence, if there is a major design fault, it will be picked up at the end of the implementation workfl ow with the resulting huge cost of redesigning and recoding large portions of the product. 

Therefore, both top-down and bottom-up integration have their strengths and weaknesses. The solution for product development is to combine the two strategies in such a way as to use their strengths and minimize their weaknesses. This leads to the idea of sandwich integration. 

## 15.6.3 Sandwich Integration

Consider the interconnection diagram shown in Figure 15.7 . Six of the code artifacts— a , b , c , d , g, and j —are logic artifacts and therefore should be integrated top down. Seven are 

FIGURE 15.7 The product of Figure 15.6 developed using sandwich integration. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/41ff2e293ad77bd3cfd3122c60cf834e8be727c7f726a6dc7c2f9044eb2366d8.jpg)


The term sandwich integration [Myers, 1979] comes from viewing the logic artifacts and the operational artifacts as the top and the bottom of a sandwich, and the interfaces that connect them as the sandwich fi lling. This can be seen (sort of) in Figure 15.7. 

operational artifacts— e , f , h , i , k , l , and m —and should be integrated bottom up. Because neither top-down nor bottom-up integration is suitable for all the artifacts, the solution is to partition them. The six logic artifacts are integrated top down and any major design faults can be caught early. The seven operational artifacts are integrated bottom up. They therefore receive a thorough testing, unshielded by defensively programmed artifacts that invoke them, and therefore they can be reused with confi dence in other products. When all artifacts have been appropriately integrated, the interfaces between the two groups of artifacts are tested, one by one. There is fault isolation at all times during this process, called sandwich integration (see Just in Case You Wanted to Know Box 15.5). 

Figure 15.8 summarizes the strengths and weaknesses of sandwich integration, as well as the other integration techniques previously discussed in this chapter. 

Sandwich integration is summarized in How to Perform Box 15.1. 

## 15.6.4 Integration of Object-Oriented Products

Objects can be integrated either bottom up or top down. If top-down integration is chosen, stubs are used for each method in the same way as with classical modules. 

If bottom-up integration is used, the objects that do not send messages to other objects are implemented and integrated fi rst. Then, the objects that send messages to those objects 

FIGURE 15.8 A summary of the integration approaches presented in this chapter and the section in which each is described. 

<table><tr><td>Approach</td><td>Strengths</td><td>Weaknesses</td></tr><tr><td>Implementation then integration (Section 15.6)</td><td>—</td><td>No fault isolationMajor design faults show up latePotentially reusable code artifacts are not adequately tested</td></tr><tr><td>Top-down integration (Section 15.6.1)</td><td>Fault isolationMajor design faults show up early</td><td>Potentially reusable code artifacts are not adequately tested</td></tr><tr><td>Bottom-up integration (Section 15.6.2)</td><td>Fault isolationPotentially reusable code artifacts are adequately tested</td><td>Major design faults show up late</td></tr><tr><td>Sandwich integration (Section 15.6.3)</td><td>Fault isolationMajor design faults show up earlyPotentially reusable code artifacts are adequately tested</td><td>—</td></tr></table>

## How to Perform Sandwich Integration

Box 15.1 

## • In parallel,

Implement and integrate the logic artifacts top down. 

Implement and integrate the operational artifacts bottom up. 

• Test the interfaces between the logic artifacts and the operational artifacts. 

are implemented and integrated, and so on, until all the objects in the product have been implemented and integrated. (This process must be modifi ed if there is recursion.) 

Because both top-down and bottom-up integration are supported, sandwich integration also can be used. If the product is implemented in a hybrid object-oriented language like C++, the classes generally are operational artifacts and therefore integrated bottom up. 

Many of the artifacts that are not classes are logic artifacts. These are implemented and integrated in a top-down manner. The other artifacts are operational, so they are implemented and integrated bottom up. Finally, all the nonobject artifacts are integrated with the objects. 

Even when the product is implemented using a pure object-oriented language like Java, class methods (sometimes referred to as static methods ) such as main and utility methods usually are similar in structure to logic modules of the classical paradigm. Therefore, class methods are also implemented top down and then integrated with the other objects. In other words, when implementing and integrating an object-oriented product, variants of sandwich integration are used. 

## 15.6.5 Management of Integration

A problem for management is discovering, at integration time, that the code artifacts simply do not fi t together. For example, suppose that programmer 1 coded object o1, and programmer 2 coded object o2 . In the version of the design documentation used by programmer 1, object o1 sends a message to object o2 passing four arguments, but the version of the design documentation used by programmer 2 states clearly that only three arguments are passed to o2 . A problem like this can arise when a change is made to only one copy of the design document, without informing all the members of the development group. Both programmers know that they are in the right; neither is prepared to compromise, because the programmer who gives in must recode large portions of the product. 

To solve these and similar problems of incompatibility, the entire integration process should be run by the SQA group. Furthermore, as with testing during other workfl ows, the SQA group has the most to lose if the integration testing is performed improperly. The SQA group therefore is the most likely to ensure that the testing is performed thoroughly. Hence, the manager of the SQA group should have responsibility for all aspects of integration testing. He or she must decide which artifacts are implemented and integrated top down and which bottom up and assign integration-testing tasks to the appropriate individuals. The SQA group, which will have drawn up the integration test plan in the software project management plan, is responsible for implementing that plan 

At the end of the integration process, all the code artifacts will have been tested and combined into a single product. 

## 15.7 The Implementation Workfl ow

The overall aim of the implementation workfl ow is to implement the target software product in the selected implementation language. More precisely, as explained in Section 14.9, a large software product is partitioned into smaller subsystems, which are then implemented in parallel by coding teams. The subsystems, in turn, consist of components or code artifacts. 

As soon as a code artifact has been coded, the programmer tests it; this is termed unit testing . Once the programmer is satisfied that the code artifact is correct, it is passed on to the quality assurance group for further testing. This testing by the quality assurance group is part of the test workfl ow, described in Sections 15.20 through 15.22. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/880c5f4a68c541be8e018835e8004617e6aadf888a91b3d36cbd3f2dda618bad.jpg)


Case Study 

## The Implementation Workfl ow:15.8 The MSG Foundation Case Study

Complete implementations of the MSG Foundation product in both C++ and Java can be downloaded from www.mhhe.com/schach . The programmers included a variety of comments to aid the postdelivery maintenance programmers. 

Testing during the implementation workfl ow is examined next. 

## 15.9 The Test Workfl ow: Implementation

A number of different types of testing have to be performed during the implementation workfl ow, including unit testing, integration testing, product testing, and acceptance testing. These types of testing are discussed in the following sections. 

As pointed out in Section 6.6, code artifacts (modules, classes) undergo two types of testing: informal unit testing performed by the programmer while developing the code artifact and methodical unit testing carried out by the SQA group after the programmer is satisfi ed that the artifact appears to function correctly. This methodical testing is described in Sections 15.10 through 15.14. In turn, there are two basic types of methodical testing, non-execution-based testing , in which the artifact is reviewed by a team, and execution-based testing in which the artifact is run against test cases. Techniques for selecting test cases now are described. 

# Just in Case You Wanted to Know

It is reasonable to ask why so many different names are given for the same testing concept. As so often happens in software engineering, the same concept was discovered, independently, by a number of different researchers, each of whom invented his or her own term. By the time the software engineering community realized that these were different names for the identical concept it was too late—the diverse names had crept into the software engineering vocabulary. 

In this book, I use the terms black-box testing and glass-box testing . These terms are particularly descriptive. When we test to specifi cations, we treat the code as a totally opaque black box. Conversely, when we test to code, we need to be able to see inside the box: hence the term glass-box testing . I avoid the term white-box testing because it is somewhat confusing. After all, a box painted white is just as opaque as one painted black. 

## 15.10 Test Case Selection

The worst way to test a code artifact is to use haphazard test data. The tester sits in front of the keyboard, and whenever the artifact requests input, the tester responds with arbitrary data. As will be shown, there is never time to test more than the tiniest fraction of all possible test cases, which easily can number many more than 10 <sup>100</sup> . The few test cases that can be run, perhaps, on the order of 1000, are too valuable to waste on haphazard data. Worse, there is a tendency when the machine solicits input to respond more than once with the same data, wasting even more test cases. It is clear that test cases must be constructed systematically. 

## 15.10.1 Testing to Specifi cations versus Testing to Code

Test data for unit testing can be constructed systematically in two basic ways. The fi rst is to test to specifi cations . This technique also is called black-box , behavioral , datadriven , functional , and input/output-driven testing . In this approach, the code itself is ignored; the only information used in drawing up test cases is the specifi cation document. The other extreme is to test to code and to ignore the specifi cation document when selecting test cases. Other names for this technique are glass-box , white-box , structural , logic-driven , and path-oriented testing (for an explanation of why there are so many different terms, see Just in Case You Wanted to Know Box 15.6). 

We now consider the feasibility of each of these two techniques, starting with testing to specifi cations. 

## 15.10.2 Feasibility of Testing to Specifi cations

Consider the following example. Suppose that the specifi cations for a certain dataprocessing product state that fi ve types of commission and seven types of discount must be incorporated. Testing every possible combination of just commission and discount requires 35 test cases. It is no use saying that commission and discount are computed in two entirely separate code artifacts and hence may be tested independently—in blackbox testing, the product is treated as a black box, and its internal structure therefore is completely irrelevant. 

This example contains only two factors, commission and discount, taking on fi ve and seven different values, respectively. Any realistic product has hundreds, if not thousands, of different factors. Even if there are only 20 factors, each taking on only four different values, a total of $4 ^ { 2 0 } \mathrm { o r } 1 . 1 \times 1 0 ^ { 1 2 }$ different test cases must be examined. 

To see the implications of over a trillion test cases, consider how long it would take to test them all. If a team of programmers could be found that could generate, run, and examine test cases at an average rate of one every 30 seconds, then it would take more than a million years to test the product exhaustively. 

Therefore, exhaustive testing to specifi cations is impossible in practice because of the combinatorial explosion. There simply are too many test cases to consider. Testing to code now is examined. 

## 15.10.3 Feasibility of Testing to Code

The most common form of testing to code requires that each path through the code artifact be executed at least once. 

• To see the infeasibility of this, consider the code fragment of Figure 15.9 . The corresponding fl owchart is shown in Figure 15.10 . Even though the fl owchart appears to be almost trivial, it has over $1 0 ^ { 1 2 }$ different paths. There are fi ve possible paths through the central group of six shaded boxes, and the total number of possible paths through the fl owchart therefore is 

$$
5 ^ {1} + 5 ^ {2} + 5 ^ {3} + \dots + 5 ^ {1 8} = \frac {5 \times (5 ^ {1 8} - 1)}{(5 - 1)} = 4. 7 7 \times 1 0 ^ {1 2}
$$

If there can be this many paths through a simple fl owchart containing a single loop, it is not diffi cult to imagine the total number of different paths in a code artifact of reasonable size and complexity, let alone a large artifact with many loops. In short, the huge number of possible paths renders exhaustive testing to code as infeasible as exhaustive testing to specifi cations. 

```txt
read (kmax)    // kmax is an integer between 1 and 18
for (k = 0; k < kmax; k++) do
{
    read (myChar)    // myChar is the character A, B, or C
    switch (myChar)
    {
    case 'A':
    blockA;
    if (cond1) blockC;
    break;
    case 'B':
    blockB;
    if (cond2) blockC;
    break;
    case 'C':
    blockC;
    break;
    }
    blockD;
} 
```


FIGURE 15.10 A fl owchart with over $1 0 ^ { 1 2 }$ possible paths.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/7b18158c71f9c1b8d7ddf572f4fc351679d824c534d42f4740ffad4da636dec6.jpg)


Furthermore, testing to code requires the tester to exercise every path. It is possible to exercise every path without detecting every fault in the product; that is, testing to code is not reliable. To see this, consider the code fragment shown in Figure 15.11 [Myers, 1976]. The fragment was written to test the equality of three integers, $\mathsf { x } , \mathsf { y } ,$ , and z, using the totally fallacious assumption that if the average of three numbers is equal to the fi rst number, then the three numbers are equal. Two test cases are shown in Figure 15.11 . In the fi rst test case the value of the average of the three numbers is $6 / 3$ or $^ { 2 , }$ , which is not equal to 1 . The product therefore correctly informs the tester that x , y , and z are unequal. The integers $\mathsf { x } , \mathsf { y } ,$ and z all equal 2 in the second test case, so the product computes their average as 2 , which is equal to the value of $\times ,$ and the product correctly concludes that the three numbers are equal. Accordingly, both paths through the product have been exercised without the fault being detected. Of course, the fault would come to light if test data such as $\times = 2$ , y = 1 , z = 3 are used. 

• A third diffi culty with path testing is that a path can be tested only if it is present. Consider the code fragment shown in Figure 15.12(a) . Clearly, two paths are to be tested, corresponding to the cases d = 0 and d ≠ 0 . Next, consider the single statement of Figure 15.12(b) . Now there is only one path, and this path can be tested without the fault being detected. In fact, a programmer who omits checking whether d = 0 in his or her code is likely to be unaware of the potential danger, and the case d = 0 will not be included in the programmer’s test data. This problem is an additional argument for having an independent software quality assurance group whose job includes detecting faults of this type. 

```matlab
FIGURE 15.11 if ((x + y + z)/3 == x)
    print "x, y, z are equal in value";
else
    print "x, y, z are unequal";
Test case 1:    x = 1, y = 2, z = 3
Test case 2:    x = y = z = 2

FIGURE 15.12 if (d == 0)
    zeroDivisionRoutine ();
else
    x = n/d;
    (a)

x = n/d;
    (b) 
```

These examples show conclusively that the criterion “exercise all paths in the product” is not reliable , as products exist for which some data exercising a given path detect a fault and different data exercising the same path do not. However, path-oriented testing is valid, because it does not inherently preclude selecting test data that might reveal the fault. 

Because of the combinatorial explosion, neither exhaustive testing to specifi cations nor exhaustive testing to code is feasible. A compromise is needed, using techniques that highlight as many faults as possible, while accepting that there is no way to guarantee that all faults have been detected. A reasonable way to proceed is to use black-box test cases fi rst (testing to specifi cations) and then develop additional test cases using glass-box techniques (testing to code). 

## 15.11 Black-Box Unit-Testing Techniques

Exhaustive black-box testing generally requires billions and billions of test cases. The art of testing is to devise a small, manageable set of test cases to maximize the chances of detecting a fault while minimizing the chances of wasting a test case by having the same fault detected by more than one test case. Every test case must be chosen to detect a previ ously undetected fault. One such black-box technique is equivalence testing combined with boundary value analysis. 

## 15.11.1 Equivalence Testing and Boundary Value Analysis

Suppose the specifi cations for a database product state that the product must be able to handle any number of records from 1 through $1 6 , 3 8 3 ( 2 ^ { 1 4 } - 1 )$ . If the product can handle 34 records and 14,870 records, then the chances are good that it will work fi ne for, say, 8252 records. In fact, the chances of detecting a fault, if present, are likely to be equally good if any test case from 1 through 16,383 records is selected. Conversely, if the product works correctly for any one test case in the range from 1 through 16,383, then it probably will work for any other test case in the range. The range from 1 through 16,383 constitutes an equivalence class , that is, a set of test cases such that any one member of the class is as good a test case as any other. To be more precise, the specifi ed range of numbers of records that the product must be able to handle defi nes three equivalence classes: 

Equivalence class 1. Less than 1 record. 

Equivalence class 2. From 1 through 16,383 records. 

Equivalence class 3. More than 16,383 records. 

Testing the database product using the technique of equivalence classes then requires that one test case from each equivalence class be selected. The test case from equivalence class 2 should be handled correctly, whereas error messages should be printed for the test cases from class 1 and class 3. 

A successful test case detects a previously undetected fault. To maximize the chances of fi nding such a fault, a high-payoff technique is boundary value analysis 

Experience has shown that, when a test case on or just to one side of the boundary of an equivalence class is selected, the probability of detecting a fault increases. Therefore, when testing the database product, seven test cases should be selected: 

Test case 1. 0 records: Member of equivalence class 1 and adjacent to boundary value. 

Test case 2. 1 record: Boundary value. 

Test case 3. 2 records: Adjacent to boundary value. 

Test case 4. 723 records: Member of equivalence class 2. 

Test case 5. 16,382 records: Adjacent to boundary value. 

Test case 6. 16,383 records: Boundary value. 

Test case 7. 16,384 records: Member of equivalence class 3 and adjacent to boundary value. 

This example applies to the input specifi cations. An equally powerful technique is to examine the output specifi cations. For example, in 2008, the minimum Social Security deduction or, more precisely, the minimum Old-Age, Survivors, and Disability Insurance (OASDI) deduction from any one paycheck permitted by the U.S. tax code was $0 and the maximum was $6324, the latter corresponding to gross earnings of $102,000. Therefore, when testing a payroll product, the test cases for the Social Security deduction from paychecks should include input data that are expected to result in deductions of exactly $0 and $6324. In addition, test data should be set up that might result in deductions of less than $0 or more than $6324. 

<table><tr><td>How to Perform Equivalence Testing</td><td>Box 15.2</td></tr><tr><td colspan="2">• For both the input and output specificationsFor each range (L, U)Select five test cases: less than L, equal to L, greater than L but less than U, equal to U, and greater than U.For each set SSelect two test cases: a member of S and a nonmember of S.For each precise value PSelect two cases: P and anything else.</td></tr></table>

In general, for each range $( R _ { 1 } , R _ { 2 } )$ listed in either the input or the output specifi cations, fi ve test cases should be selected, corresponding to values less than $R _ { 1 } ,$ , equal to $R _ { 1 } ,$ greater than $R _ { 1 }$ but less than $R _ { 2 } ,$ , equal to $R _ { 2 } ,$ , and greater than $R _ { 2 }$ . Where it is specifi ed that an item has to be a member of a certain set (for example, the input must be a letter), two equivalence classes must be tested, a member of the specifi ed set and a nonmember of the set. Where the specifi cations lay down a precise value (for example, the response must be followed by a # sign), then again there are two equivalence classes, the specifi ed value and anything else. 

The use of equivalence classes, together with boundary value analysis, to test both the input specifi cations and the output specifi cations is a valuable technique for generating a relatively small set of test data with the potential of uncovering a number of faults that might well remain hidden if less powerful techniques for test data selection were used. 

The process of equivalence testing is summarized in How to Perform Box 15.2. 

## 15.11.2 Functional Testing

An alternative form of black-box testing is to base the test data on the functionality of a code artifact. In functional testing [Howden, 1987], each item of functionality or function implemented in the code artifact is identifi ed. Typical functions in a classical mod ule for a computerized warehouse product might be get_next_database_record or determine_whether_quantity_on_hand_is_below_the_reorder_point . In a weapons control system, a module might include the function compute_trajectory . In a module of an operating system, one function might be determine_whether_fi le_is_empty. 

After determining all the functions of a code artifact, test data are devised to test each function separately. Now, the functional testing is taken a step further. If the code artifact consists of a hierarchy of lower-level functions, connected by the control structures of structured programming, then functional testing proceeds recursively. For example, if a higher-level function is of the form 

< higher-level function > ::= if < conditional expression > 

< lower-level function 1>; 

else 

< lower-level function 2>; 

then, because < conditional expression >, < lower-level function 1>, and < lower-level function 2> have been subjected to functional testing, < higher-level function > can be tested using branch coverage, a glass-box technique described in Section 15.13.1. Note that this form of structural testing is a hybrid technique—the lower-level functions are tested using a black-box technique, but the higher-level functions are tested using a glass-box technique. 

In practice, however, higher-level functions are not constructed in such a structured fashion from lower-level functions. Instead, the lower-level functions usually are intertwined in some way. To determine faults in this situation, functional analysis is required, a somewhat complex procedure; for details, see [Howden, 1987]. A further complicating factor is that functionality frequently does not coincide with code artifact boundaries. Therefore, the distinction between unit testing and integration testing becomes blurred; one code artifact cannot be tested without, at the same time, testing the other code artifacts whose functionality it uses. This problem also arises in the object-oriented paradigm when a method of one object sends a message to (invokes) a method of a different object. 

The random interrelationships between code artifacts from the viewpoint of functional testing may have unacceptable consequences for management. For example, milestones and deadlines can become somewhat ill defi ned, making it diffi cult to determine the status of the product with respect to the software project management plan. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/c47c982d642bbefa5183f67d23103d9d14d942c6a0ddf1875916e52ebc8a752d.jpg)


## Black-Box Test Cases: The MSG Foundation Case Study

Figures 15.13 and 15.14 contain black-box test cases for the MSG Foundation case study. First consider test cases derived from equivalence classes and boundary value analysis. The fi rst test case in Figure 15.13 tests whether the product detects an error if the itemName of an investment does not begin with an alphabetic character. The next set of fi ve test cases checks that an itemName consists of between 1 and 25 characters. Similar test cases check other statements in the specifi cations, as refl ected in Figure 15.13 . 

Turning now to functional testing, 10 functions are listed in the specifi cation doc ument, as shown in Figure 15.14 . An additional 11 test cases correspond to misuses of these functions. 

It is important to be aware that these test cases could have been developed as soon as the analysis workfl ow was complete; the only reason that they appear here is that 

<table><tr><td rowspan="7">Black-box test cases for the MSG Foundation case study derived from equivalence classes and</td><td colspan="2">Equivalence classes for identName.</td></tr><tr><td>1. First character not alphabetic</td><td>Error</td></tr><tr><td>2. &lt; 1 character</td><td>Error</td></tr><tr><td>3. 1 character</td><td>Acceptable</td></tr><tr><td>4. Between 1 and 25 characters</td><td>Acceptable</td></tr><tr><td>5. 25 characters</td><td>Acceptable</td></tr><tr><td>6. &gt; 25 characters</td><td>Error (name too long)</td></tr></table>

## FIGURE 15.13  Investment data :

1. Character instead of digi Error (not a number) 

2. < 12 digits Acceptable 

3. 12 digits Acceptable 

4. > 12 digits Error (too many digits) 

Equivalence classes for estimatedAnnualReturn and expectedAnnualOperatingExpenses. 

1. < $0.00 Error 

2. $0.00 Acceptable 

3. $0.01 Acceptable 

4. Between $0.01 and $999,999,999.97 Acceptable 

5. $999,999,999.98 Acceptable 

6. $999,999,999.99 Acceptable 

7. $1,000,000,000.00 Error 

8. > $1,000,000,000.00 Error 

9. Character instead of digi Error (not a number) 

## Mortgage information:

Equivalence classes for accountNumber are same as for itemNumber above. 

Equivalence classes for last name of mortgagees 

1. First character not alphabetic Error 

2. < 1 character Error 

3. 1 character Acceptable 

4. Between 1 and 21 characters Acceptable 

5. 21 characters Acceptable 

6. > 21 characters Acceptable (truncated to 21 characters) 

Equivalence classes for original price of home, current family income, and mortgage balance. 

1. < $0.00 Error 

2. $0.00 Acceptable 

3. $0.01 Acceptable 

4. Between $0.01 and $999,999.98 Acceptable 

5. $999,999.98 Acceptable 

6. $999,999.99 Acceptable 

7. $1,000,000.00 Error 

8. > $1,000,000.00 Error 

9. Character instead of digi Error (not a number) 

<table><tr><td rowspan="10">FIGURE 15.13 (continued)</td><td colspan="2">Equivalence classes for annual property tax and annual homeowner&#x27;s premium.</td></tr><tr><td>1. &lt; $0.00</td><td>Error</td></tr><tr><td>2. $0.00</td><td>Acceptable</td></tr><tr><td>3. $0.01</td><td>Acceptable</td></tr><tr><td>4. Between $0.01 and $99,999.98</td><td>Acceptable</td></tr><tr><td>5. $99,999.98</td><td>Acceptable</td></tr><tr><td>6. $99,999.99</td><td>Acceptable</td></tr><tr><td>7. $100,000.00</td><td>Error</td></tr><tr><td>8. &gt;$100,000.00</td><td>Error</td></tr><tr><td>9. Character instead of digit</td><td>Error (not a number)</td></tr></table>

The functions outlined in the specifi cations document are used to create test cases: 

Functional 1. Add a mortgage. 

analysis test 2. Add an investment. 

cases for 3. Modify a mortgage. 

the MSG 4. Modify an investment. 

6. Delete an investment. 

7. Update operating expenses. 

8. Compute funds to purchase houses. 

9. Print list of mortgages. 

10. Print list of investments. 

In addition to these direct tests, it is necessary to perform the following additional tests: 

11. Attempt to add a mortgage that is already on fi le. 

12. Attempt to add an investment that is already on fi le. 

13. Attempt to delete a mortgage that is not on fi le. 

14. Attempt to delete an investment that is not on fi le. 

15. Attempt to modify a mortgage that is not on fi le. 

16. Attempt to modify an investment that is not on fi le 

17. Attempt to delete twice a mortgage that is already on fi le. 

18. Attempt to delete twice an investment that is already on fi le. 

19. Attempt to update each fi eld of a mortgage twice and check that the second version is stored. 

20. Attempt to update each fi eld of an investment twice and check that the second version is stored 

21. Attempt to update operating expenses twice and check that second version is stored. 

test case selection is a topic of this chapter, rather than an earlier chapter. A majo component of every test plan should be a stipulation that black-box test cases be drawn up as soon as the analysis artifacts have been approved, for use by the SQA group during the implementation workfl ow. 

## 15.13 Glass-Box Unit-Testing Techniques

In glass-box techniques, test cases are selected on the basis of examination of the code rather than the specifi cations. There are a number of different forms of glass-box testing, including statement, branch, and path coverage. 

## 15.13.1 Structural Testing: Statement, Branch, and Path Coverage

The simplest form of glass-box unit testing is statement coverage, that is, running a series of test cases during which every statement is executed at least once. To keep track of which statements are still to be executed, a CASE tool keeps a record of how many times each statement has been executed over the series of tests; PureCoverage is an example of such a tool. 

A weakness of this approach is that there is no guarantee that all outcomes of branches are properly tested. To see this, consider the code fragment of Figure 15.15 . The programmer made a mistake; the compound conditional s > 1 && t == 0 should read s > 1 || t == 0 . The test data shown in the fi gure allow the statement x = 9 to be executed without the fault being highlighted. 

An improvement over statement coverage is branch coverage , that is, running a series of tests to ensure that all branches are tested at least once. Again, a tool usually is needed to help the tester keep track of which branches have or have not been tested; Generic Coverage Tool ( gct ) is an example of a branch coverage tool for C programs. Techniques such as statement or branch coverage are termed structural tests. 

The most powerful form of structural testing is path coverage , that is, testing all paths. As shown previously, in a product with loops, the number of paths can be very large indeed. As a result, researchers have been investigating ways of reducing the number of paths to be examined while uncovering more faults than would be possible using branch coverage. One criterion for selecting paths is to restrict test cases to linear code sequences [Woodward, Hedley, and Hennell, 1980]. To do this, fi rst identify the set of points L from which control fl ow may jump. The set L includes entry and exit points and branch statements such as an if or goto statement. The linear code sequences are those paths that begin at an element of L and end at an element of L . The technique has been successful in that it has uncovered many faults without having to test every path. 

Another way of reducing the number of paths to test is all-defi nition-use-path coverage [Rapps and Weyuker, 1985]. In this technique, each occurrence of a variable pqr, say, in the source code is labeled either as a defi nition of the variable, such as pqr = 1 or read (pqr), or a use of the variable, such as y = pqr + 3 or if (pqr < 9) errorB (). All paths between the defi nition of a variable and the use of that defi nition are identifi ed, nowadays by means of an automatic tool. Finally, a test case is set up for each such path. All-defi nition-use-path coverage is an excellent test technique in that large numbers of faults frequently are detected by relatively few test cases. However, all-defi nition-use-path coverage has the weakness that the upper bound on the number of paths is 2 <sup>d</sup> , where d is the number of decision statements (branches) in the product. Examples can be constructed exhibiting the upper bound. However, it has been shown that, for real products as opposed to artifi cial examples, this upper bound is not reached, and the actual number of paths is proportional to d [Weyuker, 1988]. In other words, the number of test cases needed for 

```txt
FIGURE 15.15 if (s > 1 && t == 0)
Code fragment x = 9;
with test data. 
```

$$
\text {   Test   case:   } \quad s = 2, t = 0.
$$

$$
\begin{array}{l} \text {if (k <   2)} \\ \{\quad \text {if (k > 3)} \\ \uparrow \\ x = x * k; \\ \} \end{array} \qquad \qquad [ s h o u l d b e k > - 3 ] \tag {a}
$$

$$
\begin{array}{c} \text { for } (j = 0; j <   0; j + +) [ s h o u l d b e j <   1 0 ] \\ \uparrow \\ \text { total } = \text { total } + \text { value } [ j ]; \\ (\text { b }) \end{array}
$$

all-defi nition-use-path coverage generally is much smaller than the theoretical upper bound. Therefore, all-defi nition-use-path coverage is a practical test case selection technique. 

When using structural testing, the tester simply might not come up with a test case that exercises a specifi c statement, branch, or path. What may have happened is that an infeasible path (“dead code”) is in the code artifact, that is, a path that cannot possibly be executed for any input data. Figure 15.16 shows two examples of infeasible paths. In Figure 15.16(a) the programmer omitted a minus sign. If k is less than 2 , then k cannot possibly be greater than 3 , so the statement $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { x } } \ { \ast }$ k cannot be reached. Similarly, in Figure 15.16(b) , j is never less than 0 , so the statement total = total + value[j] can never be reached; the programmer had intended the test to be $\mathrm { j } < 1 0$ , but made a typing mistake. A tester using statement coverage would soon realize that neither statement could be reached and the faults would be found. 

## 15.13.2 Complexity Metrics

The quality assurance viewpoint provides another approach to glass-box unit testing. Suppose a manager is told that code artifact m1 is more complex than code artifact m2. Irrespective of the precise way in which the term complex is defi ned, the manager intuitively believes that m1 is likely to have more faults than m2 . Following this idea, computer scientists have developed a number of metrics of software complexity as an aid in determining which code artifacts are most likely to have faults. If the complexity of a code artifact is found to be unreasonably high, a manager may direct that the artifact be redesigned and reimplemented on the grounds that it probably is less costly and faster to start from scratch than to attempt to debug a fault-prone code artifact. 

A simple metric for predicting numbers of faults is lines of code. The underlying assumption is that there is a constant probability, p , that a line of code contains a fault. If a tester believes that, on average, a line of code has a 2 percent chance of containing a fault, and the artifact under test is 100 lines long, then this implies that the artifact is expected to contain two faults; and an artifact that is twice as long is likely to have four faults. Basili and Hutchens [1983] as well as Takahashi and Kamayachi [1985] showed that the number of faults indeed is related to the size of the product as a whole. 

Attempts have been made to fi nd more sophisticated predictors of faults based on measures of product complexity. A typical contender is McCabe’s [1976] measure of cyclomatic complexity , the number of binary decisions (predicates) plus 1. As described in Section 14.15, the cyclomatic complexity essentially is the number of branches in the code artifact. Accordingly, cyclomatic complexity can be used as a metric for the number of test cases needed for branch coverage of a code artifact. This is the basis for so-called structured testing [Watson and McCabe, 1996]. 

McCabe’s metric can be computed almost as easily as lines of code. In some cases, it has been shown to be a good metric for predicting faults; the higher the value of M , the greater is the chance that a code artifact contains a fault. For example, Walsh [1979] analyzed 276 modules in the Aegis system, a shipboard combat system. Measuring the cyclomatic complexity, M, he found that 23 percent of the modules with M greater than or equal to 10 had 53 percent of the faults detected. In addition, the modules with M greater than or equal to 10 had 21 percent more faults per line of code than the modules with smaller M values. However, the validity of McCabe’s metric has been questioned seriously on both theoretical grounds and on the basis of the many different experiments cited in [Shepperd and Ince, 1994]. 

Musa, Iannino, and Okumoto [1987] analyzed the data available on fault densities. They concluded that most complexity metrics, including McCabe’s, show a high correlation with the number of lines of code or, more precisely, the number of deliverable, executable source instructions. In other words, when researchers measure what they believe to be the complexity of a code artifact or a product, the result they obtain may be largely a refl ection of the number of lines of code, a measure that correlates strongly with the number of faults. In addition, complexity metrics provide little improvement over lines of code for predicting fault rates. Other problems with complexity are discussed in [Shepperd and Ince, 1994]. 

## 15.14 Code Walkthroughs and Inspections

Section 6.2 made a strong case for the use of walkthroughs and inspections in general. The same arguments hold for code walkthroughs and inspections. In brief, the fault-detecting power of these two non-execution-based techniques leads to rapid, thorough, and early fault detection. The additional time required for code walkthroughs or inspections is more than repaid by increased productivity due to the presence of fewer faults when integration is performed. Furthermore, code inspections have led to a reduction of up to 95 percent in corrective maintenance costs [Crossman, 1982]. 

Another reason why code inspections should be performed is that the alternative, execution-based testing (test cases), can be extremely expensive in two ways. First, it is time consuming. Second, inspections lead to detection and correction of faults earlier in the life cycle than with execution-based testing. As refl ected in Figure 1.6, the earlier a fault is detected and corrected, the less it costs. An extreme case of the high cost of running test cases is that 80 percent of the budget for the software of the NASA Apollo program was consumed by testing [Dunn, 1984]. 

Further arguments in favor of walkthroughs and inspections are given in Section 15.15. 

## 15.15 Comparison of Unit-Testing Techniques

A number of studies have compared strategies for unit testing. Myers [1978a] compared black-box testing, a combination of black-box and glass-box testing, and three-person code walkthroughs. The experiment was performed using 59 highly experienced programmers testing the same product. All three techniques were equally effective in fi nding faults, but code walkthroughs proved to be less cost effective than the other two techniques. Hwang [1981] compared black-box testing, glass-box testing, and code reading by one person. All three techniques were found to be equally effective, with each technique having its own strengths and weaknesses. 

A major experiment was conducted by Basili and Selby [1987]. The techniques compared were the same as in Hwang’s experiment: black-box testing, glass-box testing, and one-person code reading. The subjects were 32 professional programmers and 42 advanced students. Each tested three products, using each testing technique once. Fractional factorial design [Basili and Weiss, 1984] was used to compensate for the different ways the products were tested by different participants; no participant tested the same product in more than one way. Different results were obtained from the two groups of participants. The professional programmers detected more faults with code reading than with the other two techniques, and the fault detection rate was faster. Two groups of advanced students participated. In one group, no signifi cant difference was found among the three techniques; in the other, code reading and black-box testing were equally good and both outperformed glass-box testing. However, the rate at which students detected faults was the same for all techniques. Overall, code reading led to the detection of more interface faults than the other two techniques, whereas black-box testing was most successful at fi nding control faults. 

In Basili and Selby’s experiment, code inspection was at least as successful at detecting faults as glass-box and black-box testing. Most subsequent experiments have shown that black-box testing and glass-box testing are more effi cient or more effective than inspections [Runeson et al., 2006]. However, some studies have shown that test cases and inspections tend to fi nd different kinds of faults. In other words, the two techniques are complementary, and both need to be utilized on every software product. 

A development technique that makes use of this conclusion is the Cleanroom software development technique. 

## 15.16 Cleanroom

The Cleanroom technique [Linger, 1994] is a combination of a number of different software development techniques, including an incremental life-cycle model, formal techniques for analysis and design, and non-execution-based unit-testing techniques, such as code reading [Mills, Dyer, and Linger, 1987] and code walkthroughs and inspections (Section 15.14). A critical aspect of Cleanroom is that a code artifact is not compiled until it has passed inspection. That is, a code artifact should be compiled only after non-executionbased testing has been successfully completed. 

The technique has had a number of great successes. For example, a prototype automated documentation system was developed for the U.S. Naval Underwater Systems Center using Cleanroom [Trammel, Binder, and Snyder, 1992]. Altogether 18 faults were detected while the design underwent “functional verifi cation,” a review process in which correctness-proving techniques are employed (Section 6.5). Informal proofs such as the one presented in Section 6.5.1 were used as much as possible; full mathematical proofs were developed only when participants were unsure of the correctness of the portion of the design being inspected. Another 19 faults were detected during walkthroughs of the 1820 lines of FoxBASE code; when the code was then compiled, there were no compilation errors. Furthermore, there were no failures at execution time. This is an additional indication of the power of non-execution-based testing techniques. 

This certainly is an impressive result. But, as has been pointed out, results that apply to small-scale software products cannot necessarily be scaled up to large-scale software. In the case of Cleanroom, however, results for larger products also are impressive. The relevant metric is the testing fault rate , that is, the total number of faults detected per KLOC (thousand lines of code), a relatively common metric in the software industry. Yet, there is a critical difference in the way this metric is computed when Cleanroom is used as opposed to traditional development techniques. 

As pointed out in Section 6.6, when traditional development techniques are used, a code artifact is tested informally by its programmer while it is being developed and thereafter it is tested methodically by the SQA group. Faults detected by the programmer while developing the code are not recorded. However, from the time the artifact leaves the private workspace of the programmer and is handed over to the SQA group for execution-based and non-execution-based testing, a tally is kept of the number of faults detected. In contrast, when Cleanroom is used, “testing faults” are counted from the time of compilation. Fault counting then continues through execution-based testing. In other words, when traditional development techniques are used, faults detected informally by the programmer do not count toward the testing fault rate. When Cleanroom is used, faults detected during the inspections and other non-execution-based testing procedures that precede compilation are recorded, but they do not count toward the testing fault rate. 

A report on 17 Cleanroom products appears in [Linger, 1994]. For example, Cleanroom was used to develop the 350,000-line Ericsson Telecom OS32 operating system. The product was developed in 18 months by a team of 70. The testing fault rate was only 1.0 fault per KLOC. Another product was the prototype automated documentation system described previously; the testing fault rate was 0.0 faults per KLOC for the 1820-line program. The 17 products together total nearly 1 million lines of code. The weighted average testing fault rate was 2.3 faults per KLOC, which Linger describes as a remarkable quality achievement. That praise certainly is no exaggeration. 

## 15.17 Potential Problems When Testing Objects

One of the many reasons put forward for using the object-oriented paradigm is that it reduces the need for testing. Reuse via inheritance is a major strength of the paradigm; once a class has been tested, the argument goes, there is no need to retest it. Furthermore, new methods defi ned within a subclass of such a tested class have to be tested, but inherited methods need no further testing. 

In fact, both claims are only partially true. In addition, the testing of objects poses cer tain problems that are specifi c to object orientation. These issues are discussed here. 

To begin, it is necessary to clarify an issue regarding the testing of classes and of objects. As explained in Section 7.7, a class is an abstract data type that supports inheritance, and an object is an instance of a class. That is, a class has no concrete realization, whereas an object is a physical piece of code executing within a specifi c environment. Therefore, it is impossible to perform execution-based testing on a class; only non-execution-based testing, such as an inspection, can be done. 

Information hiding and the fact that many methods consist of relatively few lines of code can have a signifi cant impact on testing. First, consider a product developed using the classical paradigm. Nowadays, such a product generally consists of modules of roughly 50 executable instructions. The interface between a module and the rest of the product is the argument list. Arguments are of two kinds, input arguments supplied to the module when it is invoked and output arguments returned by the module when it returns control to the calling module. Testing a module consists of supplying values to the input arguments and invoking the module and then comparing the values of the output arguments to the predicted results of the test. 

In contrast, a “typical” object contains perhaps 30 methods, many of which are relatively small, frequently just two or three executable statements [Wilde, Matthews, and Huitt, 1993]. These methods do not return a value to the caller but rather change the state of the object. That is, these methods modify attributes (state variables) of the object. The diffi culty here is that, to test that the change of state has been performed correctly, it is necessary to send additional messages to the object. For example, consider the bank account object described in Section 1.9. The effect of method deposit is to increase the value of state variable accountBalance . However, as a consequence of information hiding, the only way to test whether a particular deposit method has been executed correctly is to invoke method determineBalance both before and after invoking method deposit and see how the bank balance changes. 

The situation is worse if the object does not include methods that can be invoked to determine the values of all the state variables. One alternative is to include additional methods for this purpose, and then use conditional compilation to ensure that they are unavailable except for testing purposes (in C++, this can be implemented using #ifdef ). The test plan (Section 9.6) should stipulate that the value of every state variable be accessible during testing. To satisfy this requirement, additional methods that return the values of the state variables may have to be added to the relevant classes during the design workfl ow. As a result, it is possible to test the effect of invoking a specifi c method of an object by querying the value of the applicable state variable. 

Surprisingly enough, an inherited method still may have to be tested. That is, even if a method has been adequately tested, it may require thorough testing when inherited, unchanged, by a subclass. To see this latter point, consider the class hierarchy shown in Figure 15.17 . Two methods are defi ned in the base class RootedTreeClass , namely, displayNodeContents and printRoutine , where method displayNodeContents uses method printRoutine . 

Next consider subclass BinaryTreeClass. This subclass inherits method printRoutine from its base class RootedTreeClass . In addition, a new method, displayNodeContents, is defi ned that overrides the method defi ned in RootedTreeClass. This new method still uses printRoutine. In Java notation, BinaryTreeClass.displayNodeContents uses RootedTreeClass.printRoutine . 

Now consider the subclass BalancedBinaryTreeClass. This subclass inherits method displayNodeContents from its superclass BinaryTreeClass. However, a new method printRoutine is defi ned that overrides the one defi ned in RootedTreeClass. When displayNodeContents uses printRoutine within the context of Balanced BinaryTreeClass , the scope rules of C++ and Java specify that the local version of printRoutine is to be used. In Java notation, when method BinaryTreeClass.display NodeContents is invoked within the lexical scope of BalancedBinaryTreeClass, it uses method BalancedBinaryTreeClass.printRoutine. 

```dart
FIGURE 15.17 class RootedTreeClass
A Java
implementation
of a tree
hierarchy.
{
...
void displayNodeContents (Node a);
void printRoutine (Node b);
//
// method displayNodeContents uses method printRoutine
//
...
}
class BinaryTreeClass extends RootedTreeClass
{
...
void displayNodeContents (Node a);
//
// method displayNodeContents defined in this class uses
// method printRoutine inherited from ClassRootedTree
//
...
}
class BalancedBinaryTreeClass extends BinaryTreeClass
{
...
void printRoutine (Node b);
//
// method displayNodeContents (inherited from BinaryTreeClass) uses this
// local version of printRoutine within class BalancedBinaryTreeClass
//
...
} 
```

Therefore, the actual code (method printRoutine ) executed when displayNodeContents is invoked within instantiations of BinaryTreeClass is different from what is executed when displayNodeContents is invoked within instantiations of BalancedBinaryTreeClass. This holds notwithstanding that the method displayNodeContents itself is inherited, unchanged, by BalancedBinaryTreeClass from BinaryTreeClass . Therefore, even if method displayNodeContents has been thoroughly tested within a BinaryTreeClass object, it has to be retested from scratch when reused within a BalancedBinaryTreeClass environment. To make matters even more complex, there are theoretical reasons why it needs to be retested with different test cases [Perry and Kaiser, 1990]. 

It must be pointed out immediately that these complications are no reason to abandon the object-oriented paradigm. First, they arise only through the interaction of methods ( displayNodeContents and printRoutine in the example). Second, it is possible to determine when this retesting is needed [Harrold, McGregor, and Fitzpatrick, 1992]. 

Suppose an instantiation of a class has been thoroughly tested. Any new or redefi ned methods of a subclass then need to be tested, together with methods fl agged for retesting because of their interaction with other methods. In short, then, the claim that use of the object-oriented paradigm reduces the need for testing largely is true. 

Some management implications of unit testing now are considered. 

## 15.18 Management Aspects of Unit Testing

An important decision that must be made during the development of every code artifact is how much time, and therefore money, to spend on testing that artifact. As with so many other economic issues in software engineering, cost–benefi t analysis (Section 5.2) can play a useful role. For example, the decision as to whether the cost of correctness proving exceeds the benefi t of the assurance that a specifi c product satisfi es its specifi cations can be decided on the basis of cost–benefi t analysis. Cost–benefi t analysis also can be used to compare the cost of running additional test cases against the cost of failure of the delivered product caused by inadequate testing. 

There is another approach for determining whether testing of a specifi c code artifact should continue or whether it is likely that virtually all the faults have been removed. The techniques of reliability analysis can be used to provide statistical estimates of how many faults remain. A variety of different techniques have been proposed for determining statistical estimates of the number of remaining faults. The basic idea underlying these techniques is the following: Suppose a code artifact is tested for 1 week. On Monday, 23 faults are found and seven more are found on Tuesday. On Wednesday, fi ve more faults are found, two on Thursday, and none on Friday. Because the rate of fault detection decreases steadily from 23 faults per day to none, it seems likely that most faults have been found, and testing of that code artifact could be halted. Determining the probability that there are no more faults in the code requires a level of mathematical statistics beyond that required for readers of this book. Details therefore are not given here; the reader interested in reliability analysis should consult Grady [1992]. 

## 15.19 When to Reimplement Rather than Debug a Code Artifact

When a member of the SQA group detects a failure (erroneous output), as stated previously, the code artifact must be returned to the original programmer for debugging , that is, detection of the fault and correction of the code. On some occasions, it is preferable for the code artifact to be thrown away and redesigned and recoded from scratch, either by the origina programmer or by another, possibly more senior, member of the development team. 

To see why this may be necessary, consider Figure 15.18 . The graph shows the counterintuitive concept that the probability of the existence of more faults in a code artifact is proportional to the number of faults already found in that code artifact [Myers, 1979]. To see why this should be so, consider two code artifacts, a1 and a2 . Suppose that both code artifacts are approximately the same length and both have been tested for the same number of hours. Suppose further that only 2 faults were detected in a1 , but 48 faults were detected in a2 . It is likely that more faults remain to be rooted out of a2 than out of a1 . Furthermore, additional testing and debugging of a2 is likely to be a lengthy process, and the suspicion that a2 is still not perfect will remain. In both the short run and the long run, it is preferable to discard a2 , redesign it, and then recode it. 

FIGURE15.18 Graph showing that the probability that faults are still to be found is proportional to the number of faults already detected. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/2862673ac2b5f55c802a8a1ab810565d6e66c99da1c212471a274ca0875c7f93.jpg)


The distribution of faults in modules certainly is not uniform. Myers [1979] cites the example of faults found by users in OS/370. It was found that 47 percent of the faults were associated with only 4 percent of the modules. Current research shows that the nonuniform distribution of faults in modules has continued. For example, Andersson and Runeson [2007] examined three telecommunications products that were developed using the iterative-andincremental model. For the fi rst project, they found that 20 percent of the modules contained 63 percent of the faults; for the second and third projects, 20 percent of the modules contained 70 percent of the faults. 

An earlier study by Endres [1975] regarding internal tests of DOS/VS (Release 28) at IBM Laboratories, Böblingen, Germany, showed similar nonuniformity. Of the total of 512 faults detected in 202 modules, only 1 fault was detected in each of 112 of the modules. On the other hand, some modules were found to have 14, 15, 19, and 28 faults, respectively. Endres points out that the latter three modules were three of the largest modules in the product, each comprising over 3000 lines of DOS macro assembler language. However, the module with 14 faults was a relatively small module previously known to be very unstable. This type of module is a prime candidate for being discarded and recoded. 

The way for management to cope with this sort of situation is to predetermine the maximum number of faults permitted during development of a given code artifact; when that maximum is reached, the code artifact must be thrown away and then redesigned and recoded, preferably by an experienced software professional. This maximum varies from application domain to application domain and from code artifact to code artifact. After all, the maximum permitted number of faults detected in a code artifact that reads a record from a database and checks the validity of the part number should be far smaller than the number of faults in a complex code artifact from a tank weapons control system that must coordinate data from a variety of sensors and direct the aim of the main gun toward the intended target. One way to decide on the maximum fault fi gure for a specifi c code artifact is to examine fault data on similar code artifacts that have required corrective maintenance. But, whatever estimation technique is used, management must ensure that the code artifact is scrapped if that fi gure is exceeded (but see Just in Case You Wanted to Know Box 15.7). 

# Just in Case You Wanted to Know

The discussion regarding the maximum permitted number of faults detected during development of a code artifact means precisely that: the maximum number permitted during development . The maximum permitted number of faults detected after the product has been delivered to the client should be zero for all code artifacts of all products. That is, it should be the aim of every software engineer to deliver fault-free code to the client. 

## 15.20 Integration Testing

Each new code artifact must be tested when it is added to what has already been integrated; this is termed integration testing . The key point here is fi rst to test the new code artifact as described in Sections 15.10 through 15.14 (unit testing) and then to check that the rest of the partial product continues to behave as it did before the new code artifact was integrated into it. 

When the product has a graphical user interface, special issues can arise with regard to integration testing. In general, testing a product usually can be simplifi ed by storing the input data for a test case in a fi le. The product then is executed, and the relevant data submitted to it. With the aid of a CASE tool, the whole process can be automated; that is, a set of test cases is set up, together with the expected outcome of each case. The CASE tool runs each test case, compares the actual results with the expected results, and reports to the user on each case. The test cases then are stored for use in regression testing whenever the product is modifi ed. SilkTest is an example of a tool of this kind. 

However, when a product incorporates a graphical user interface, this approach does not work. Specifi cally, test data for pulling down a menu or clicking on a mouse button cannot be stored in a fi le in the same way as conventional test data. At the same time, it is time consuming and boring to test a GUI manually. The solution to this problem is to use a special CASE tool that keeps a record of mouse clicks, key presses, and so on. The GUI is tested once manually so that the CASE tool can set up the test fi le. Thereafter, this fi le is used in subsequent tests. A number of CASE tools support testing GUIs, including QARun and XRunner. 

When the integration process is complete, the product as a whole is tested; this is termed product testing . When the developers are confi dent about the correctness of every aspect of the product, it is handed over to the client for acceptance testing . These two forms of testing are now described in more detail. 

## 15.21 Product Testing

The fact that the last code artifact has been integrated successfully into the product does not mean that the task of the developers is complete. The SQA group still must perform a number of testing tasks to ascertain that the product will be successful. There are two main types of software, commercial off-the-shelf (COTS) software (Section 1.11) and custom software. The aim of COTS product testing is to ensure that the product as a whole is free of faults. When the product testing is complete, the product undergoes alpha and beta testing, as described in Section 3.7. That is, preliminary versions are shipped to selected prospective buyers of the product to get feedback, particularly regarding residual faults overlooked by the SQA team. 

Custom software, on the other hand, undergoes somewhat different product testing. The SQA group performs a number of testing tasks to be certain that the product will not fail its acceptance test, the fi nal hurdle that the custom software development team must overcome. 

The failure of a product to pass its acceptance test almost always is a poor refl ection on the management capabilities of the development organization. The client may conclude that the developers are incompetent, which all but guarantees that the client will do everything to avoid employing those developers again. Worse, the client may believe that the developers are dishonest and deliberately handed over substandard software to fi nish the contract and be paid as quickly as possible. If the client genuinely believes this and tells other potential clients, then the developers face a major public relations problem. It is up to the SQA group to make sure the product passes the acceptance test with fl ying colors. 

To ensure a successful acceptance test, the SQA group must test the product using tests that the SQA group believes closely approximate the forthcoming acceptance tests: 

• Black-box test cases for the product as a whole must be run. Up to now, test cases have been set up on an artifact-by-artifact or class-by-class basis, ensuring that each code artifact or class individually satisfi es its specifi cations. 

• The robustness of the product as a whole must be tested. Again, the robustness of individual code artifacts and classes was tested during integration; now productwide robustness is the issue for which test cases must be set up and run. In addition, the product must be subjected to stress testing , that is, making sure that it behaves correctly when operating under a peak load, such as all terminals trying to log on at the same time or customers operating all the automated teller machines simultaneously. The product also must be subjected to volume testing , for example, making sure that it can handle large input fi les. 

The SQA group must check that the product satisfi es all its constraints. For example, if the specifi cations state that the response time for 95 percent of queries when the product is working under full load must be under 3 seconds, then it is the responsibility of the SQA group to verify that this indeed is the case. There is no question that the client will check constraints during acceptance testing; and if the product fails to meet a major constraint, then the development organization will lose a considerable amount of credibility. Similarly, storage constraints and security constraints must be checked. 

• The SQA group must review all documentation to be handed over to the client together with the code. The SQA group must check that the documentation conforms to the standards laid down in the SPMP. In addition, the documentation must be checked against the product. For instance, the SQA group has to determine that the user manual indeed refl ects the correct way of using the product and that the product functions as specifi ed in the user manual. 

Once the SQA group assures management that the product can handle anything the acceptance testers can throw at it, the product (that is, the code plus all the documentation) is handed to the client organization for acceptance testing. 

## 15.22 Acceptance Testing

The purpose of acceptance testing is for the client to determine whether the product indeed satisfi es its specifi cations as claimed by the developer. Acceptance testing is done by either the client organization, the SQA group in the presence of client representatives, or an independent SQA group hired by the client for this purpose. Acceptance testing naturally includes correctness testing, but in addition, it is necessary to test performance and robustness. The four major components of acceptance testing—testing correctness, robustness, performance, and documentation—are exactly what is done by the developer during product testing; this is not surprising, because product testing is a comprehensive rehearsal for the acceptance test. 

A key aspect of acceptance testing is that it must be performed on actual data rather than on test data. No matter how well test cases are set up, by their very nature, they are artifi cial. More important, test data should be a true refl ection of the corresponding actual data, but in practice, this is not always the case. For example, the member of the specifi cation team responsible for characterizing the actual data may perform this task incorrectly. Alternatively, even if the data are specifi ed correctly, the SQA group member who uses that data specifi cation may misunderstand or misinterpret it. The resulting test cases are not a true refl ection of the actual data, leading to an inadequately tested product. For these reasons, acceptance testing must be performed on actual data. Furthermore, because the development team endeavors to ensure that the product testing duplicates every aspect of the acceptance testing, as much of the product testing as possible should also be performed on actual data. 

When a new product is to replace an existing one, the specifi cation document almost always includes a clause to the effect that the new product must be installed to run in parallel with the existing product. The reason is that there is a very real possibility that the new product may be faulty in some way. The existing product works correctly but is inadequate in some respects. If the existing product is replaced by a new product that works incorrectly, then the client is in trouble. Therefore, both products must run in parallel until the client is satisfi ed that the new product can take over the functions of the existing product. Successful parallel running concludes acceptance testing, and the existing product can be retired. 

When the product has passed its acceptance test, the task of the developers is complete. Any changes now made to that product constitute postdelivery maintenance. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/f2485ebfa67e56659d133e672ebb5265c0676855dea74cbb0ea18d157adf6758.jpg)


## The Test Workfl ow: The MSG Foundation15.23 Case Study

The C++ and Java implementations of the MSG Foundation product (available for download at www.mhhe.com/Schach ) were tested against the black-box test cases of Figure 15.13 and 15.14 , as well as the glass-box test cases of Problems 15.35 through 15.39. 

## 15.24 CASE Tools for Implementation

CASE tools to support implementation of code artifacts were described in some detail in Chapter 5 . For integration, version-control tools, build tools, and confi guration management tools are needed ( Chapter 5 ). The reason is that code artifacts under test change continually as a consequence of faults being detected and corrected, and these CASE tools are essential to ensure that the appropriate version of each artifact is compiled and linked. Commercially available confi guration-control workbenches include PVCS and SourceSafe. Popular open-source confi guration-control tools include CVS and Subversion. 

In each chapter so far, CASE tools and workbenches specifi c to that workfl ow have been described. Now that all workfl ows of the development process have been described, it is appropriate to consider CASE tools for the process as a whole. 

## 15.24.1 CASE Tools for the Complete Software Process

There is a natural progression within CASE. As described in Section 5.7, the simplest CASE device is a single tool , such as an online interface checker or a build tool. Next, tools can be combined, leading to a workbench that supports one or two activities within the software process, such as confi guration control or coding. However, such a workbench might not provide management information even for the limited portion of the software process to which it is applicable, let alone for the project as a whole. Finally, an environment provides computer-aided support for most, if not all of, the process. 

Ideally, every software development organization should utilize an environment. But the cost of an environment can be large—not just the package itself but the hardware on which to run it. For a smaller organization, a workbench, or perhaps just a set of tools, may suffi ce. But, if at all possible, an integrated environment should be utilized to support the development and maintenance effort. 

## 15.24.2 Integrated Development Environments

The most common meaning of the word integrated within the CASE context is in terms of user interface integration . That is, all the tools in the environment share a common user interface. The idea behind this is that, if all the tools have the same visual appearance, the user of one tool should have little diffi culty in learning and using another tool in the environment. This has been successfully achieved on the Macintosh, where most applications have a similar “look and feel.” Although this is the usual meaning, there are other types of integration as well. 

The term tool integration means that all the tools communicate via the same data format. For example, in the UNIX Programmer’s Workbench, the UNIX pipe formalism assumes that all data are in the form of an ASCII stream. It therefore is easy to combine two tools by directing the output stream from one tool to the input stream of the other tool. Eclipse is an open-source environment for tool integration. 

Process integration refers to an environment that supports one specifi c software process. A subset of this class of environment is the technique-based environment (but see Just in Case You Wanted to Know Box 15.8). An environment of this type supports only a specifi c technique for developing software, rather than a complete process. Environments exist for a variety of the techniques discussed in this book, such as Gane and Sarsen’s structured systems analysis (Section 12.3), Jackson system development (Section 14.5), and Petri nets (Section 12.8). The majority of these environments provide graphical support for analysis and design and incorporate a data dictionary. Some consistency checking usually is provided. Support for managing the development process frequently is incorporated into the environment. Many environments of this type are 

In the literature, technique-based environments usually are called method-based environment s. The rise of the object-oriented paradigm gave the word method a second meaning (in the software engineering context). The original meaning was a technique or an approach; this is how the word is used in the phrase method-based environment . The objectoriented meaning is an operation within an object or class. Unfortunately, it sometimes is not totally clear from the context which meaning is intended. 

Accordingly, I have used the word method exclusively within the context of the object-oriented paradigm. Otherwise, I have employed the term technique or approach . For example, that is why the term formal method never appears in Chapter 12 . Instead, I use the term formal technique . Similarly, in this chapter, I have used the term technique-based environments . 

commercially available, including Analyst/Designer and Rhapsody. Analyst/Designer is specifi c to Yourdon’s methodology [Yourdon, 1989], and Rhapsody supports Statecharts [Harel et al., 1990]. With regard to object-oriented methodologies, IBM Rational Rose supports the Unifi ed Process [Jacobson, Booch, and Rumbaugh, 1999]. In addition, some older environments have been extended to support the object-oriented paradigm; Software through Pictures is an example of this type. Almost all object-oriented environments now support UML. 

The emphasis in most technique-based environments is on the support and formalization of the manual operations for software development laid down by the technique. That is, these environments force users to utilize the technique step by step in the way intended by its author, while assisting the user by providing graphical tools, a data dictionary, and consistency checking. This computerized framework is a strength of technique-based environments in that users are forced to use a specifi c technique and use it correctly. But it can be a weakness as well. Unless the software process of the organization incorporates this specifi c technique, use of a technique-based environment can be counterproductive. 

## 15.24.3 Environments for Business Applications

An important class of environments is used for building business-oriented products. The emphasis is on ease of use, achieved in a number of ways. In particular, the environment incorporates a number of standard screens, and these can be modifi ed endlessly via a userfriendly GUI generator. One popular feature of such environments is a code generator. The lowest level of abstraction of a product then is the detailed design. The detailed design is the input to a code generator that automatically generates code in a language such as C, C++, or Java. This automatically generated code is compiled; no “programming” of any kind is performed on it. 

Languages for specifying the detailed design could well be the programming languages of the future. The level of abstraction of programming languages rose from the physical machine level of fi rst- and second-generation languages to the abstract machine level of third- and fourth-generation languages. Today, the level of abstraction of environments of this type is the detailed design level, a portable level. Section 15.2 stated that one objective in using a fourth-generation language is shorter code, and hence quicker development and easier postdelivery maintenance. The use of code generators takes these goals even further, in that the programmer has to provide fewer details to a code generator than to an interpreter or compiler for a 4GL. Therefore, it is expected that use of business-oriented environments that support code generators will increase productivity. 

A number of environments of this type are currently available, including Oracle Developer Suite. Bearing in mind the size of the market for business-oriented CASE environments, it is likely that many more environments of this type will be developed in future years. 

## 15.24.4 Public Tool Infrastructures

The European Strategic Programme for Research in Information Technology (ESPRIT) developed an infrastructure for supporting CASE tools. Despite its name, the portable common tool environment (PCTE) [Long and Morris, 1993] is not an environment. Instead, it is an infrastructure that provides the services needed by CASE tools, in much the same way that UNIX provides the operating system services needed by user products. (The word common in PCTE is in the sense of “public” or “not copyrighted.”) 

PCTE has gained widespread acceptance. For example, PCTE and the C and Ada interfaces to PCTE were adopted as ISO/IEC Standard 13719 in 1995. Implementations of PCTE include those of Emeraude and IBM. 

The hope is that, in the future, many more CASE tools will conform to the PCTE standard and that PCTE itself will be implemented on a wider variety of computers. A tool that conforms to PCTE would run on any computer that supports PCTE. Accordingly, this should result in the widespread availability of a broad range of CASE tools. This, in turn, should lead to better software processes and better-quality software. 

## 15.24.5 Potential Problems with Environments

No one environment is ideal for all products and all organizations, any more than one programming language can be considered “the best.” Every environment has its strengths and its weaknesses, and choosing an inappropriate environment can be worse than using no environment at all. For example, as explained in Section 15.24.2, a technique-based environment essentially automates a manual process. If an organization chooses to use an environment that enforces a technique inappropriate for it as a whole or for a current software product under development, then use of that CASE environment is counterproductive. 

A worse situation occurs when an organization chooses to ignore the advice of Section 5.12, that the use of a CASE environment should be fi rmly avoided until the organization has attained CMM level 3. Of course, every organization should use CASE tools, and there generally is little harm in using a workbench. However, an environment imposes an automated software process on an organization that uses it. If a good process is being used, that is, the organization is at level 3 or higher, then use of the environment assists in all aspects of software production by automating that process. But, if the organization is at the crisis-driven level 1 or even at level 2, then no process as such is in place. Automation of this nonexistent process, that is, the introduction of a CASE environment (as opposed to a CASE tool or CASE workbench), can lead only to chaos. 

## 15.25 CASE Tools for the Test Workfl ow

Numerous CASE tools are available to support the different types of testing that are performed during the implementation workfl ow. First consider unit testing. The XUnit testing frameworks, including JUnit for Java and CppUnit for C++, are a set of open-source automated tools for unit testing; that is, they are utilized to test each class in turn. A set of test cases is prepared, and the tool checks that each of the messages sent to the class results in the expected answer being returned. Commercial tools of this type are produced by many vendors, including Parasoft. 

We now turn to integration testing. Examples of commercial tools that support automated integration testing (as well as unit testing) include SilkTest and IBM Rational Functional Tester. It is common for tools of this kind to pool the unit-testing test cases and utilize the resulting set of test cases for integration testing and regression testing. 

During the test workfl ow, it is essential for management to know the status of all defects. In particular, it is vital to know which defects have been detected but have not yet been corrected. The best-known defect-tracking tool is Bugzilla, an open-source product. 

Returning to Figure 1.6 yet again, it is vital to detect coding faults as soon as possible. One way to achieve this is to use a CASE tool to analyze the code, looking for common syntactic and semantic faults, or constructs that could lead to problems later. Examples of such tools include lint (for C—see Section 8.11.4), IBM Rational Purify, Sun’s Jackpot Source Code Metrics, and three Microsoft tools: PREfi x, PREfast, and SLAM. 

The Hyades project (otherwise known as the Eclipse test and performance tools project) is an open-source integrated test, trace, and monitoring environment that currently can be used with Java and C++. It has facilities for a variety of different testing tools. As more and more tool vendors adapt their tools to work under Eclipse, users will be able to select from a wider choice of testing tools, all of which will work in conjunction with one another. 

## 15.26 Metrics for the Implementation Workfl ow

A number of different complexity metrics for the implementation workfl ow are discussed in Section 15.13.2, including lines of code and McCabe’s cyclomatic complexity. 

From a testing viewpoint, the relevant metrics include the total number of test cases and the number of test cases that resulted in a failure. The usual fault statistics must be maintained for code inspections. The total number of faults is important, because if the number of faults detected in a code artifact exceeds a predetermined maximum, then that code artifact must be redesigned and recoded, as discussed in Section 15.19. In addition, detailed statistics need to be kept regarding the types of faults detected. Typical fault types include misunderstanding the design, lack of initialization, and inconsistent use of variables. The fault data can be incorporated into the checklists to be used during code inspections of future products. 

A number of metrics specifi c to the object-oriented paradigm have been put forward, for example, the height of the inheritance tree [Chidamber and Kemerer, 1994]. Many of these metrics have been questioned on both theoretical and experimental grounds [Binkley and Schach, 1996; 1997]. Furthermore, Alshayeb and Li [2003] have shown that, whereas object-oriented metrics can relatively accurately predict the number of lines of code added, changed, and deleted in agile processes, they are of little use in predicting the same measures in a framework–based process (see Section 8.5.2). It remains to be shown that there is a need for specifi cally object-oriented metrics, as opposed to classical metrics that can be applied equally to object-oriented software. 

## 15.27 Challenges of the Implementation Workfl ow

Paradoxically, a major challenge of the implementation workfl ow has to be met in the workfl ows that precede it. As explained in Chapter 8 , code reuse is an effective way of reducing software development cost and delivery time. However, it is hard to achieve code reuse if it is attempted as late as the implementation workfl ow. 

For example, suppose the decision is made to implement a product in language L . Now, after half the code artifacts have been implemented and tested, management decides to utilize package P for the graphical user interfaces of the software product. No matter how powerful the routines of P may be, if they are implemented in a language that is hard to interface with L, then they cannot be reused in the software product. 

Even if language interoperability is not an issue, there is little point in trying to reuse an existing code artifact unless the item to be reused fi ts the design exactly. More work may be needed to modify the existing code artifact than to create a new code artifact from scratch. 

Code reuse therefore has to be built into a software product from the very beginning. Reuse has to be a user requirement as well as a constraint of the specifi cation document. The software project management plan (Section 9.4) must incorporate reuse. Also, the design document must state which code artifacts are to be implemented and which are to be reused. 

So, as stated at the beginning of this section, even though code reuse is an important challenge of implementation, code reuse has to be incorporated into the requirements, analysis, and design workfl ows. 

From a purely technical viewpoint, the implementation workfl ow is relatively straightforward. If the requirements, analysis, and design workfl ows were carried out satisfactorily, the task of implementation should pose few problems to competent programmers. However, management of integration is of critical importance; the challenges of the implementation workfl ow are to be found in this area. 

Typical make-or-break issues include use of the appropriate CASE tools (Section 15.24), test planning once the specifi cations have been signed off on by the client (Section 9.6), ensuring that changes to the design are communicated to all relevant personnel (Section 15.6.5), and deciding when to stop testing and deliver the product to the client (Section 6.1.2). 

Chapter This chapter presents various issues relating to the implementation of a product by a team. These include Review choice of programming language (Section 15.1). The issue of fourth-generation languages is discussed in some detail in Section 15.2. Good programming practice is described in Section 15.3, and the need for practical coding standards is presented in Section 15.4. Then, comments are made regarding cod reuse (Section 15.5). Implementation and integration activities must be carried out in parallel (Section 15.6). Top-down, bottom-up, and sandwich integration are described and compared (Sections 15.6.1 through 15.6.3). Integration of object-oriented products is discussed in Section 15.6.4, and management of integration in Section 15.6.5. The implementation workfl ow is presented in Section 15.7 and applied to the MSG Foundation case study in Section 15.8. Next, implementation aspects of the test workfl ow are presented (Section 15.9). Test cases must be selected systematically (Section 15.10). Various blackbox, glass-box, and non-execution-based unit-testing techniques are described (Sections 15.11, 15.13, and 15.14, respectively) and then compared (Section 15.15). Black-box testing of the MSG Foundation 

## For Further Reading

<table><tr><td>Implementation workflow</td><td>Section 15.8, Appendix H, Appendix I</td></tr><tr><td>Black-box test cases</td><td>Section 15.12</td></tr><tr><td>Test workflow</td><td>Section 15.23</td></tr></table>

case study is presented in Section 15.12. The Cleanroom technique is described in Section 15.16. Testing objects is discussed in Section 15.17, followed by a discussion of the managerial implications of unit testing (Section 15.18). Another problem is when to reimplement rather than debug a code artifact (Section 15.19). Integration testing is described in Section 15.20, product testing in Section 15.21, and acceptance testing in Section 15.22. The test workfl ow for the MSG Foundation case study is outlined in Section 15.23. CASE tools for the implementation workfl ow are described in Section 15.24. In more detail, CASE tools for the complete process are discussed in Section 15.24.1 and integrated development environments in Section 15.24.2. Environments for business applications are presented in Section 15.24.3. Section 15.24.4 is devoted to public tool infrastructures. Next, potential problems with environments are discussed (Section 15.24.5). Now CASE tools for the test workfl ow are described (Section 15.25). Metrics for the implementation workfl ow are discussed in Section 15.26. The chapter conclude with an analysis of the challenges of the implementation workfl ow (Section 15.27). 

An overview of the MSG Foundation case study for Chapter 15 appears in Figure 15.19. 

The attitudes of 43 organizations to 4GLs are reported in [Guimaraes, 1985]. Klepper and Bock [1995] describes how McDonnell Douglas obtained higher productivity with 4GLs than with 3GLs. Some of the dangers of end-user programming are presented in [Harrison, 2004]. A wide variety of papers on end-user programming appear in the November 2004 issue of the Communications of the ACM . Localization techniques to assist end users in debugging spreadsheets are described in [Ruthruff, Burnett, and Rothermel, 2006]. 

Excellent books on good programming practice include [Kernighan and Plauger, 1974] and [Mc-Connell, 1993]. 

Probably the most important early work on execution-based testing is [Myers, 1979]. A compre hensive source of information on testing in general is [Beizer, 1990]. Functional testing is described in [Howden, 1987]. Black-box testing is described in detail in [Beizer, 1995]. The design of black-box test cases is presented in [Yamaura, 1998]. The relationship between the various coverage measures of structural testing and software quality is discussed in [Horgan, London, and Lyu, 1994]. A formal approach to glass-box testing is described in [Stocks and Carrington, 1996]. Elbaum, Malishevsky, and Rothermel [2002] discuss setting test case priorities. Generation of synthetic workloads for stress testing is presented in [Krishnamurthy, Rolia, and Majumdar, 2006]. A comprehensive list of unittesting strategies appears in [Juristo, Moreno, Vegas, and Solari, 2006]. Geographically and temporally distributed code reviews are presented in [Meyer, 2008]. 

Cleanroom is described in [Linger, 1994]. The use of Cleanroom during postdelivery maintenance is presented in [Sherer, Kouchakdjian, and Arnold, 1996]. A criticism of Cleanroom is given in [Beizer, 1997]. 

A good introduction to software reliability is [Musa and Everett, 1990]. In addition, the proceedings of the annual International Symposium on Software Reliability Engineering contain a wide variety of articles on software reliability. 

The proceedings of the International Symposia on Software Testing and Analysis cover a particularly broad range of testing issues. 

A survey of different approaches to the testing of objects can be found in [Turner, 1994]. Two important papers on the subject are [Perry and Kaiser, 1990] and [Harrold, McGregor, and Fitzpatrick, 1992]. 

[Beizer, 1995], mentioned previously, also covers black-box testing of object-oriented software. With regard to the object-oriented paradigm, Jorgensen and Erickson [1994] describe the integration testing of object-oriented software. 

With regard to metrics for implementation, McCabe’s cyclomatic complexity was fi rst presented in [McCabe, 1976]. Extensions of the metric to design appear in [McCabe and Butler, 1989]. Articles questioning the validity of cyclomatic complexity include [Shepperd and Ince, 1994]. The validity of object-oriented metrics is discussed in [Alshayeb and Li, 2003]. The relative inability of objectoriented metrics to detect high-impact faults is described in [Zhou and Leung, 2006]. 

Selection of test data for integration testing appears in [Harrold and Soffa, 1991]. The generation of test cases for testing GUIs is described in [Memon, Pollack, and Soffa, 2001]. 

Every 2 or 3 years, ACM SIGSOFT and SIGPLAN sponsor a Symposium on Practical Software Development Environments. The proceedings provide information on a broad spectrum of toolkits and environments. Also useful are the proceedings of the annual International Workshops on Computer-Aided Software Engineering. 

With regard to PCTE, [Long and Morris, 1993] contains a number of information sources on that topic. 

## Key Terms

acceptance testing 535 all-defi nition-use-path coverage 526 behavioral testing 517 black-box testing 517 bottom-up integration 513 boundary value analysis 521 branch coverage 526 Cleanroom 529 code artifact 516 coding standards 509 complexity 527 component 516 consistent variable names 504 cyclomatic complexity 527 data-driven testing 517 debugging 533 defensive programming 512 driver 511 end-user programming 503 environment 538 equivalence class 521 execution-based testing 516 fi rst-generation language 501 fourth-generation language (4GL) 501 functional analysis 523 functional testing 517 glass-box testing 517 

good programming practice 504 Hungarian Naming Conventions 505 implementation workfl ow 516 input/output-driven testing 517 integrated environment 538 integration 510 integration testing 535 linear code sequences 526 logic artifact 511 logic-driven testing 517 meaningful variable names 504 method-based environment 539 non-execution-based testing 516 nonprocedural 502 operational artifact 511 path coverage 526 path-oriented testing 517 portable common tool environment (PCTE) 540 procedural 502 process integration 538 product testing 535 programming-in-the-many 498 prologue comments 506 

reliable 520 sandwich integration 514 second-generation language 501 self-documenting code 505 statement coverage 526 static method 515 stress testing 536 structural test 526 structural testing 517 structured testing 528 stub 510 technique-based environment 538 test case selection 527 testing fault rate 530 testing to code 517 testing to specifi cations 517 third-generation language 501 tool 538 tool integration 538 top-down integration 511 user interface integration 538 valid 520 unit testing 516 volume testing 536 white-box testing 517 workbench 538 

## Problems

15.1 Your instructor has asked you to implement the Chocoholics Anonymous product (Appendix A). Which language would you choose for implementing the product, and why? Of the various languages available to you, list their benefi ts and their costs. Do not attempt to attach dollar values to your answers. 

15.2 Repeat Problem 15.1 for the elevator problem (Section 12.7.1). 

15.3 Repeat Problem 15.1 for the automated library circulation system (Problem 8.7). 

15.4 Repeat Problem 15.1 for the product that determines whether a bank statement is correct (Problem 8.8). 

15.5 Repeat Problem 15.1 for the automated teller machine (Problem 8.9). 

15.6 Add prologue comments to a code artifact that you have recently implemented. 

15.7 How do coding standards for a one-person software production company differ from those in organizations with 300 software professionals? 

15.8 How do coding standards for a software company that develops and maintains software for intensive-care units differ from those in an organization that develops and maintains accounting products? 

15.9 Consider the statement 

## < condition 1> && < condition 2>

As stated at the end of Section 15.3, in Java and C++ the semantics of the && operator are such that if < condition 1> is false, then < condition 2> is not evaluated. What is the technical term for this? 

## 15.10 Consider the statement

## < condition 1> and < condition 2>

In what programming languages is < condition 2> evaluated even if < condition 1> is false? 

15.11 Why does deep nesting of if -statements frequently lead to code that can be diffi cult to read? 

15.12 Why has it been suggested that modules ideally should consist of between 35 and 50 statements? 

15.13 Why should backward goto statements be avoided, whereas a forward goto may be used for error handling? 

15.14 Set up black-box test cases for Naur’s text-processing problem (Section 6.5.2). For each test case, state what is being tested and the expected outcome of that test case. 

15.15 Using your solution to Problem 6.14 (or code distributed by your instructor), set up statement coverage test cases. For each test case, state what is being tested and the expected outcome of that test case. 

15.16 Repeat Problem 15.15 for branch coverage. 

15.17 Repeat Problem 15.15 for all-defi nition-use-path coverage. 

15.18 Repeat Problem 15.15 for path coverage. 

15.19 Repeat Problem 15.15 for linear code sequences. 

15.20 Draw a fl owchart of your solution to Problem 6.14 (or code distributed by your instructor). Determine its cyclomatic complexity. If you are unable to determine the number of branches, consider the fl owchart as a directed graph. Determine the number of edges e , nodes n , and connected components c. (Each method constitutes a connected component.) The cyclomatic complexity M is then given by the formula [McCabe, 1976] 

$$
M = e - n + 2 c
$$

15.21 You are the owner and sole employee of One-Person Software Company. You bought the programming workbench described in Section 5.8. List its fi ve capabilities in order of importance to you, giving reasons. 

15.22 You are now the vice-president for software technology of Very Big Software Company; there are 17,500 employees in your organization. How do you rank the capabilities of the programming workbench described in Section 5.8? Explain any differences between your answer to this problem and that of Problem 15.21 

15.23 As SQA manager for a software development organization, you are responsible for determining the maximum number of faults that may be found in a given code artifact during testing. If this maximum is exceeded, then the code artifact must be redesigned and recoded. What criteria would you use to determine the maximum for a given code artifact? 

15.24 Explain the difference between logic artifacts and operational artifacts. 

15.25 Defensive programming is good software engineering practice. At the same time, it can prevent operational artifacts from being tested thoroughly enough for reuse purposes. How can this apparent contradiction be resolved? 

15.26 What are the similarities between product testing and acceptance testing? What are the major differences? 

15.27 What is the role of the SQA group during implementation? 

15.28 You are the owner and sole employee of One-Person Software Company. You decide that to be competitive you must buy CASE tools. You therefore apply for a bank loan for $15,000. Your bank manager asks you for a statement no more than one page in length (preferably shorter) explaining in lay terms why you need CASE tools. Write the statement. 

15.29 The newly appointed vice-president for software development of Ye Olde Fashioned Software Corporation has hired you to help her change the way the company develops software. There are 650 employees, all writing COBOL 85 code without the assistance of any CASE tools (COBOL 85 conforms to the 1985 COBOL standard; it is not object-oriented). Write a memo to the vice-president stating what sort of CASE equipment the company should purchase. Justify your choice. 

15.30 You and a friend decide to start Personal Computer Software Programs ’R Us, developing software for personal computers on personal computers. Then a distant cousin dies, leaving you $1 million on condition that you spend the money on a business-oriented environment and the hardware needed to run it and that you keep the environment for at least 5 years. What do you do, and why? 

15.31 You are a computer science professor at an excellent small liberal arts college. Programming assignments for computer science courses are done on a network of 35 personal computers. Your dean asks you whether to use the limited software budget to buy CASE tools, bearing in mind that, unless some sort of site license can be obtained, 35 copies of every CASE tool have to be purchased. What do you advise? 

15.32 You have just been elected mayor of a major city. You discover that no CASE tools are being used to develop software for the city. What do you do? 

15.33 (Term Project) Draw up black-box test cases for the product you specifi ed in Problem 12.20 or 13.22. For each test case, state what is being tested and the expected outcome of that test case. 

15.34 (Term Project) Implement and integrate the Chocoholics Anonymous product (Appendix A). Use the programming language specifi ed by your instructor. Your instructor will tell you whether to build a Web-based user interface, a graphical user interface, or a text-based user interface. Remember to utilize the black-box test cases you developed in Problem 15.33 for testing your code. 

15.35 (Case Study) Download a copy of the implementation of the MSG Foundation product described in Section 15.8. Draw up statement coverage test cases for the product. For each test case, state what is being tested and the expected outcome of that test case. 

15.36 (Case Study) Repeat Problem 15.35 for branch coverage. 

15.37 (Case Study) Repeat Problem 15.35 for all-defi nition-use-path coverage. 

15.38 (Case Study) Repeat Problem 15.35 for path coverage. 

15.39 (Case Study) Repeat Problem 15.35 for linear code sequences. 

15.40 (Case Study) Starting with the detailed design of Problem 14.16, code the MSG Foundation case study in an object-oriented language other than C++ or Java. 

15.41 (Case Study) Recode the MSG Foundation case study (Section 15.8) in pure C, with no C++ features. Although C does not support inheritance, object-based concepts such as encapsulation and information hiding can be achieved relatively easily. How would you implement polymorphism and dynamic binding? 

15.42 (Case Study) To what extent is the documentation of the code of the implementation of Section 15.8 inadequate? Make any necessary additions. 

15.43 (Readings in Software Engineering) Your instructor will distribute copies of [Meyer, 2008]. What are your views on geographically and temporally distributed code reviews? 

## References



[Alshayeb and Li, 2003] M. ALSHAYEB, AND W. LI, “An Empirical Validation of Object-Oriented Metrics in Two Different Iterative Software Processes,” IEEE Transactions on Software Engineering 29 (November 2003), pp. 1043–49. 





[Andersson and Runeson, 2007] C. ANDERSSON AND P. RUNESON, “A Replicated Quantitative Analysis of Fault Distributions in Complex Software Systems,” IEEE Transactions on Software Engineering 33 (May 2007), pp. 273–86. 





[Basili and Hutchens, 1983] V. R. BASILI AND D. H. HUTCHENS, “An Empirical Study of a Syntactic Complexity Family,” IEEE Transactions on Software Engineering SE-9 (November 1983), pp. 664–72. 





[Basili and Selby, 1987] V. R. BASILI AND R. W. SELBY, “Comparing the Effectiveness of Software Testing Strategies,” IEEE Transactions on Software Engineering SE-13 (December 1987), pp. 1278–96. 





[Basili and Weiss, 1984] V. R. BASILI AND D. M. WEISS, “A Methodology for Collecting Valid Software Engineering Data,” IEEE Transactions on Software Engineering SE-10 (November 1984), pp. 728–38. 





[Beizer, 1990] B. BEIZER, Software Testing Techniques, 2nd ed., Van Nostrand Reinhold, New York, 1990. 





[Beizer, 1995] B. BEIZER, Black-Box Testing: Techniques for Functional Testing of Software and Systems, John Wiley and Sons, New York, 1995. 





[Beizer, 1997] B. BEIZER, “Cleanroom Process Model: A Critical Examination,” IEEE Software 14 (March–April 1997), pp. 14–16. 





[Binkley and Schach, 1996] A. B. BINKLEY AND S. R. SCHACH, “A Comparison of Sixteen Quality Metrics for Object-Oriented Design,” Information Processing Letters 57 (No. 6, June 1996), pp. 271–75. 





[Binkley and Schach, 1997] A. B. BINKLEY AND S. R. SCHACH, “Toward a Unifi ed Approach to Object-Oriented Coupling,” Proceedings of the 35th Annual ACM Southeast Conference , Murfreesboro, TN, April 2–4, ACM, 1997, pp. 91–97. 





[Borland, 2002] BORLAND, “Press Release: Borland Unveils C++ Application Development Strategy for 2002,” www.borland.com/news/press_releases/2002/01_28_02_cpp.strategy.html, January 28, 2002. 





[Chidamber and Kemerer, 1994] S. R. CHIDAMBER AND C. F. KEMERER, “A Metrics Suite for Object Oriented Design,” IEEE Transactions on Software Engineering 20 (June 1994), pp. 476–93. 





[Crossman, 1982] T. D. CROSSMAN, “Inspection Teams, Are They Worth It?” Proceedings of the Second National Symposium on EDP Quality Assurance , Chicago, ACM, November 1982. 





[Date, 2003] C. J. DATE, An Introduction to Database Systems, 8th ed., Addison-Wesley, Reading, MA, 2003. 





[Dunn, 1984] R. H. DUNN, Software Defect Removal , McGraw-Hill, New York, 1984. 





[Elbaum, Malishevsky, and Rothermel, 2002] S. ELBAUM, A. G. MALISHEVSKY, AND G. ROTHERMEL, “Test Case Prioritization: A Family of Empirical Studies,” IEEE Transactions on Software Engineering 28 (February 2002), pp. 159–82. 





[Endres, 1975] A. ENDRES, “An Analysis of Errors and Their Causes in System Programs,” IEEE Transactions on Software Engineering SE-1 (June 1975), pp. 140–49. 





[Grady, 1992] R. B. GRADY, Practical Software Metrics for Project Management and Process Improvement , Prentice Hall, Englewood Cliffs, NJ, 1992. 





[Guimaraes, 1985] T. GUIMARAES, “A Study of Application Program Development Techniques,” Communications of the ACM 28 (May 1985), pp. 494–99. 





[Harel et al., 1990] D. HAREL, H. LACHOVER, A. NAAMAD, A. PNUELI, M. POLITI, R. SHERMAN, A. SHTULL-TRAURING, AND M. TRAKHTENBROT, “STATEMATE: A Working Environment for the Development of Complex Reactive Systems,” IEEE Transactions on Software Engineering 16 (April 1990), pp. 403–14. 





[Harrison, 2004] W. HARRISON, “The Dangers of End-User Programming,” IEEE Software 21 (July– August 2004), pp. 5–7. 





[Harrold and Soffa, 1991] M. J. HARROLD AND M. L. SOFFA, “Selecting and Using Data for Integration Testing,” IEEE Software 8 (1991), pp. 58–65. 





[Harrold, McGregor, and Fitzpatrick, 1992] M. J. HARROLD, J. D. MCGREGOR, AND K. J. FITZPATRICK, “Incremental Testing of Object-Oriented Class Structures,” Proceedings of the 14th International Conference on Software Engineering , Melbourne, Australia, May 1992, IEEE, pp. 68–80. 





[Horgan, London, and Lyu, 1994] J. R. HORGAN, S. LONDON, AND M. R. LYU, “Achieving Software Quality with Testing Coverage Measures,” IEEE Computer 27 ( 1994), pp. 60–69. 





[Howden, 1987] W. E. HOWDEN, Functional Program Testing and Analysis , McGraw-Hill, New York, 1987. 





[Hwang, 1981] S.-S. V. HWANG, “An Empirical Study in Functional Testing, Structural Testing, and Code Reading Inspection,” Scholarly Paper 362, Department of Computer Science, University of Maryland, College Park, 1981. 





[Jacobson, Booch, and Rumbaugh, 1999] I. JACOBSON, G. BOOCH, AND J. RUMBAUGH, The Unifi ed Software Development Process , Addison-Wesley, Reading, MA, 1999. 





[Jorgensen and Erickson, 1994] P. C. JORGENSEN AND C. ERICKSON, “Object-Oriented Integration Testing,” Communications of the ACM 37 (September 1994), pp. 30–38. 





[Juristo, Moreno, Vegas, and Solari, 2006] N. JURISTO, A. M. MORENO, S. VEGAS, AND M. SOLARI, “In Search of What We Experimentally Know about Unit Testing,” IEEE Software 23 (November– December 2006), pp. 72–80. 





[Kernighan and Plauger, 1974] B. W. KERNIGHAN AND P. J. PLAUGER, The Elements of Programming Style, McGraw-Hill, New York, 1974. 





[Klepper and Bock, 1995] R. KLEPPER AND D. BOCK, “Third and Fourth Generation Productivity Differences,” Communications of the ACM 38 (September 1995), pp. 69–79. 





[Klunder, 1988] D. KLUNDER, “Hungarian Naming Conventions,” Technical Report, Microsoft Corporation, Redmond, WA, January 1988. 





[Krishnamurthy, Rolia, and Majumdar, 2006] D. KRISHNAMURTHY, J. A. ROLIA, AND S. MAJUMDAR, “A Synthetic Workload Generation Technique for Stress Testing Session-Based Systems,” IEEE Transactions on Software Engineering 32 (November 2006), pp. 868–82. 





[Linger, 1994] R. C. LINGER, “Cleanroom Process Model,” IEEE Software 11 (March 1994), pp. 50–58. 





[Long and Morris, 1993] F. LONG AND E. MORRIS, “An Overview of PCTE: A Basis for a Portable Common Tool Environment,” Technical Report CMU/SEI–93–TR–1, Software Engineering Institute, Carnegie Mellon University, Pittsburgh, January 1993. 





[Martin, 1985] J. MARTIN, Fourth-Generation Languages, Vols. 1, 2, and 3, Prentice Hall, Englewood Cliffs, NJ, 1985. 





[McCabe, 1976] T. J. MCCABE, “A Complexity Measure,” IEEE Transactions on Software Engineering SE-2 (December 1976), pp. 308–20. 





[McCabe and Butler, 1989] T. J. MCCABE AND C. W. BUTLER, “Design Complexity Measurement and Testing,” Communications of the ACM 32 (December 1989), pp. 1415–25. 





[McConnell, 1993] S. MCCONNELL, Code Complete: A Practical Handbook of Software Construction, Microsoft Press, Redmond, WA, 1993. 





[Memon, Pollack, and Soffa, 2001] A. M. MEMON, M. E. POLLACK, AND M. L. SOFFA, “Hierarchical GUI Test Case Generation Using Automated Planning,” IEEE Transactions on Software Engineering 27 (February 2001), pp. 144–55. 





[Meyer, 2008] B. MEYER, “Design and Code Reviews in the Age of the Internet,” Communications of the ACM 51 (September 2008), pp. 66–71. 





[Mills, Dyer, and Linger, 1987] H. D. MILLS, M. DYER, AND R. C. LINGER, “Cleanroom Software Engineering,” IEEE Software 4 (September 1987), pp. 19–25. 





[Musa and Everett, 1990] J. D. MUSA AND W. W. EVERETT, “Software-Reliability Engineering: Technology for the 1990s,” IEEE Software 7 (November 1990), pp. 36–43. 





[Musa, Iannino, and Okumoto, 1987] J. D. MUSA, A. IANNINO, AND K. OKUMOTO, Software Reliability: Measurement, Prediction, Application , McGraw-Hill, New York, 1987. 





[Myers, 1976] G. J. MYERS, Software Reliability: Principles and Practices, Wiley-Interscience, New York, 1976. 





[Myers, 1978a] G. J. MYERS, “A Controlled Experiment in Program Testing and Code Walkthroughs/ Inspections,” Communications of the ACM 21 (September 1978), pp. 760–68. 





[Myers, 1979] G. J. MYERS, The Art of Software Testing , John Wiley and Sons, New York, 1979. 





[Perry and Kaiser, 1990] D. E. PERRY AND G. E. KAISER, “Adequate Testing and Object-Oriented Programming,” Journal of Object-Oriented Programming 2 (January–February 1990), pp. 13–19. 





[Rapps and Weyuker, 1985] S. RAPPS AND E. J. WEYUKER, “Selecting Software Test Data Using Data Flow Information,” IEEE Transactions on Software Engineering SE-11 (April 1985), pp. 367–75. 





[Runeson et al., 2006] P. RUNESON, C. ANDERSSON, T. THELIN, A. ANDREWS, AND T. BERLING, “What Do We Know about Defect Detection Methods?” IEEE Software 23 (May–June 2006), pp. 82–90. 





[Ruthruff, Burnett, and Rothermel, 2006] J. R. RUTHRUFF, M. BURNETT, AND G. ROTHERMEL, “Interactive Fault Localization Techniques in a Spreadsheet Environment,” IEEE Transactions on Software Engineering 32 (April 2006), pp. 213–39. 





[Sammet, 1978] J. E. SAMMET, “The Early History of COBOL,” Proceedings of the History of Programming Languages Conference, Los Angeles, ACM, 1978, pp. 199–276. 





[Shepperd and Ince, 1994] M. SHEPPERD AND D. C. INCE, “A Critique of Three Metrics,” Journal of Systems and Software 26 (September 1994), pp. 197–210. 





[Sherer, Kouchakdjian, and Arnold, 1996] S. W. SHERER, A. KOUCHAKDJIAN, AND P. G. ARNOLD, “Experience Using Cleanroom Software Engineering,” IEEE Software 13 (May 1996), pp. 69–76. 





[Stocks and Carrington, 1996] P. STOCKS AND D. CARRINGTON, “A Framework for Specifi cation-Based Testing,” IEEE Transactions on Software Engineering 22 (November 1996), pp. 777–93. 





[Takahashi and Kamayachi, 1985] M. TAKAHASHI AND Y. KAMAYACHI, “An Empirical Study of a Model for Program Error Prediction,” Proceedings of the Eighth International Conference on Software Engineering , London, IEEE, 1985, pp. 330–36. 





[Trammel, Binder, and Snyder, 1992] C. J. TRAMMEL, L. H. BINDER, AND C. E. SNYDER, “The Automated Production Control Documentation System: A Case Study in Cleanroom Software Engineering,” ACM Transactions on Software Engineering and Methodology 1 (January 1992), pp. 81–94. 





[Turner, 1994] C. D. TURNER, “State-Based Testing: A New Method for the Testing of Object-Oriented Programs,” Ph.D. thesis, Computer Science Division, University of Durham, Durham, UK, November 1994. 





[Walsh, 1979] T. J. WALSH, “A Software Reliability Study Using a Complexity Measure,” Proceedings of the AFIPS National Computer Conference , New York, AFIPS, 1979, pp. 761–68. 





[Watson and McCabe, 1996] A. H. WATSON AND T. J. MCCABE, “Structured Testing: A Testing Methodology Using the Cyclomatic Complexity Metric,” NIST Special Publication 500–235, Computer Systems Laboratory, National Institute of Standards and Technology, Gaithersburg, MD, 1996. 





[Weyuker, 1988] E. J. WEYUKER, “An Empirical Study of the Complexity of Data Flow Testing,” Proceedings of the Second Workshop on Software Testing, Verifi cation, and Analysis , Banff, Canada, IEEE, July 1988, pp. 188–95. 





[Wilde, Matthews, and Huitt, 1993] N. WILDE, P. MATTHEWS, AND R. HUITT, “Maintaining Object-Oriented Software,” IEEE Software 10 (January 1993), pp. 75–80. 





[Woodward, Hedley, and Hennell, 1980] M. R. WOODWARD, D. HEDLEY, AND M. A. HENNELL, “Experience with Path Analysis and Testing of Programs,” IEEE Transactions on Software Engineering SE-6 (May 1980), pp. 278–86. 





[Yamaura, 1998] T. YAMAURA, “How to Design Practical Test Cases,” IEEE Software 15 (November– December 1998), pp. 30–36. 





[Yourdon, 1989] E. YOURDON, Modern Structured Analysis , Yourdon Press, Englewood Cliffs, NJ, 1989. 





[Zhou and Leung, 2006] Y. ZHOU AND H. LEUNG, “Empirical Analysis of Object-Oriented Design Metrics for Predicting High and Low Severity Faults,” IEEE Transactions on Software Engineering 32 (October 2006), pp. 771–89. 



# Postdelivery Maintenance

Learning Objectives 

After studying this chapter, you should be able to 

• Perform postdelivery maintenance. 

• Appreciate the importance of postdelivery maintenance. 

• Describe the challenges of postdelivery maintenance. 

• Describe the maintenance implications of the object-oriented paradigm. 

• Describe the skills needed for maintenance. 

A major theme of this book is the vital importance of postdelivery maintenance. Therefore, it is somewhat surprising that this is a relatively short chapter. The reason is that maintainability has to be built into a product from the very beginning and must not be compromised at any time during the development process. Accordingly, in a very real sense, all the previous chapters have been devoted to the subject of postdelivery maintenance. What is described in this chapter is how to ensure that maintainability is not compromised during postdelivery maintenance itself. 

## 16.1 Development and Maintenance

Once the product has passed its acceptance test, it is handed over to the client. The product is installed and used for the purpose for which it was constructed. Any useful product, however, is almost certain to undergo postdelivery maintenance , either to fi x faults (corrective maintenance) or extend the functionality of the product (enhancement). 

The National Gallery in London contains a masterpiece that was ruined when an additional head was added to a portrait. In 1515, the artist Lorenzo Lotto (ca. 1480–after 1556) painted a picture of Giovanni Agostino della Torre, a physician who lived in Bergamo, then in the State of Venice, Italy. Download the picture [Lotto, 1515] and examine it. It certainly appears as if the artist added della Torre’s son, Niccolò, after the original portrait had been completed, thereby irreparably marring the painting. 

Because a product consists of more than just the source code, any changes to the documentation, manuals, or any other component of the product after it has been delivered to the client are examples of postdelivery maintenance. Some computer scientists prefer to use the term evolution rather than maintenance to indicate that a product evolves over time. In fact, some view the entire software life cycle, from beginning to end, as an evolutionary process. 

This is how maintenance is viewed by the Unifi ed Process. In fact, the word maintenance hardly occurs anywhere in Jacobson, Booch, and Rumbaugh [1999]. Instead, maintenance is implicitly treated merely as another increment of the software product. However, there is a basic difference between development and maintenance, a difference that will be illustrated by means of the following example. 

Suppose that a woman has her portrait painted when she is 18. The oil painting depicts just her head and shoulders. Twenty years later she marries and now wants the portrait to be modifi ed so that it depicts both her new husband and herself. There are four diffi culties that would arise if the portrait were to be changed in this way. 

• The canvas is not large enough for her husband’s head to be added. 

• The original portrait was hung where sunlight fell on it much of the day, so the colors have faded somewhat. In addition, the brand of oil paint that was used for the original painting is no longer manufactured. For both these reasons, it will be hard to achieve consistency of color. 

• The original artist has retired, so it will be hard to achieve consistency of style. 

• The woman’s face has aged 20 years since the original portrait was painted, so considerable work will have to be done to ensure that the modifi ed painting is an accurate likeness. 

For all these reasons, it would be laughable even to think about modifying the original portrait. Instead, a new artist will paint a new portrait of the couple from scratch (but see Just in Case You Wanted to Know Box 16.1). 

Now consider the maintenance of a software product that originally cost $2 million to develop. There are four diffi culties that have to be solved: 

• Unfortunately, the disk on which the database is stored is all but full—the current disk is not large enough for more data to be added. 

• The company that manufactured the original disk is no longer in business, so a larger disk will have to be bought from a different manufacturer. However, there are hardware incompatibilities between the new disk and the existing software product (Section 8.11.1), and it will cost about $100,000 to make all the changes needed to use the new disk. 

• The original developers left the company some years ago, so the changes to the software product will have to be made by a team of maintainers who have never seen the software product before. 

• The original software product was developed using the classical paradigm. Nowadays, the object-oriented paradigm (and specifi cally the Unifi ed Process) is commonly used. 

There is a clear correspondence between each portrait bullet point and the correspond ing software product bullet point. The inescapable conclusion regarding the oil painting is to paint a new portrait from scratch. Does that mean that, instead of performing a $100,000 maintenance task, we should develop a totally new software product at a cost of $2 million? 

The answer is that analogies should never be taken too far. Just as it is obvious that a new portrait should be painted, it is equally obvious that the existing software product should undergo maintenance at 5 percent of the cost of a new software product. 

Nevertheless, there is an important lesson to be learned from this otherwise poor analogy. Whether we are dealing with portraits or software products, it is easier to create a new version than to modify an existing version. In the case of the portrait, not only was it all but impossible to modify the existing portrait, but the cost of doing so would surely have been more than the cost of painting a new portrait from scratch. In the case of the software product, not only were the changes feasible, but the cost of doing them would be a fraction of the cost of developing a new software product from scratch. In other words, even though it is harder to make changes to existing artifacts than to construct new artifacts from scratch, economic considerations make maintenance far preferable to redevelopment. 

## 16.2 Why Postdelivery Maintenance Is Necessary

There are three main reasons for making changes to a product: 

1. A fault needs correcting, whether an analysis fault, design fault, coding fault, documentation fault, or any other type of fault. This is termed corrective maintenance. 

2. In perfective maintenance , a change is made to the code to improve the effectiveness of the product. For instance, the client may wish additional functionality or request that the product be modifi ed so that it runs faster. Improving the maintainability of a product is another example of perfective maintenance. 

3. In adaptive maintenance , a change is made to the product to react to a change in the environment in which the product operates. For example, a product almost certainly has to be modifi ed if it is ported to a new compiler, operating system, or hardware. With each change to the tax code, a product that prepares tax returns has to be modifi ed accordingly. When the U.S. Postal Service introduced nine-digit ZIP codes in 1981, products that had allowed for only fi ve-digit ZIP codes had to be changed. Adaptive maintenance is not requested by a client; instead, it is externally imposed on the client. 

## 16.3 What Is Required of Postdelivery Maintenance Programmers?

During the software life cycle, more time is spent on postdelivery maintenance than on any other activity. In fact, on average, at least 67 percent of the total cost of a product can be attributed to postdelivery maintenance, as shown in Figure 1.3 . But many organizations, even today, assign the task of postdelivery maintenance to beginners and less competent programmers, leaving the “glamorous” job of product development to better or more experienced programmers. 

In fact, postdelivery maintenance is the most diffi cult of all aspects of software production. A major reason is that postdelivery maintenance incorporates aspects of all the other workfl ows of the software process. Consider what happens when a defect report is handed to a maintenance programmer (recall from Section 1.11 that a defect is a generic term for a fault, failure, or error). A defect report is fi led if, in the opinion of the user, the product is not working as specifi ed in the user manual. A number of causes are possible. First, nothing at all could be wrong; perhaps the user has misunderstood the user manual or is using the product incorrectly. Alternatively, if there is a fault in the product, it simply might be that the user manual has been badly worded and nothing is wrong with the code itself. Usually, however, there is a fault in the code. But, before making any changes, the maintenance programmer has to determine exactly where the fault lies, using the defect report fi led by the user, the source code, and often nothing else. Therefore, the maintenance programmer needs to have far above average debugging skills, because the fault could lie anywhere within the product. And the original cause of the defect might lie in the by now nonexistent analysis or design artifacts. 

Suppose that the maintenance programmer has located a fault and must fi x it without inadvertently introducing another fault elsewhere in the product, that is, a regression fault. If regression faults are to be minimized, detailed documentation for the product as a whole and each individual code artifact must be available. However, software professionals are notorious for their dislike of paperwork of all kinds, especially documentation; and it is quite common for the documentation to be incomplete, erroneous, or totally missing. In these cases, the maintenance programmer has to deduce from the source code itself, the only valid form of documentation available, all the information needed to avoid introducing a regression fault. 

Having determined the probable fault and tried to correct it, the maintenance programmer now must test that the modifi cation works correctly and no regression faults have been introduced. To check the modifi cation itself, the maintenance programmer must construct special test cases; checking for regression faults is done using the set of test data stored precisely for performing regression testing (Section 3.8). Then the test cases constructed for checking the modifi cation must be added to the set of stored test cases to be used for future regression testing of the modifi ed product. In addition, if changes to the analysis or design had to be made to correct the fault, then these changes also must be checked. Expertise in testing therefore is an additional prerequisite for postdelivery maintenance. Finally, it is essential that the maintenance programmer document every change. The preceding discussion relates to corrective maintenance. For that task, the maintenance programmer primarily must be a superb diagnostician to determine if there is a fault and, if so, an expert technician to fi x it. 

The other major maintenance tasks are adaptive and perfective maintenance. To perform these, the maintenance programmer must perform the requirements, analysis, design, and implementation workfl ows, taking the existing product as the starting point. For some types of changes, additional code artifacts have to be designed and implemented. In other cases, changes to the design and implementation of existing code artifacts are needed. Therefore, whereas specifi cations frequently are produced by analysis experts, designs by design experts, and code by programming experts, a maintenance programmer has to be an expert in all three areas. Perfective and adaptive maintenance are adversely affected by a lack of adequate documentation, just like corrective maintenance. Furthermore, the ability to design suitable test cases and write good documentation is needed for perfective and adaptive maintenance, just as in corrective maintenance. Therefore, none of the forms of maintenance is a task for a less experienced programmer unless a top-rank computer professional supervises the process. 

From the preceding discussion, it is clear that maintenance programmers have to possess almost every technical skill that a software professional could have. But what does he or she get in return? 

• Postdelivery maintenance is a thankless task in every way. Maintainers deal with dissatisfi ed users; if the user were happy with the product, it would not need maintenance. 

• The user’s problems have frequently been caused by the individuals who developed the product, not the maintainer. 

• The code itself may be badly written, adding to the frustrations of the maintainer. 

• Postdelivery maintenance is looked down on by many software developers, who consider development to be a glamorous job and maintenance to be drudge work fi t only for junior programmers or incompetents. 

Postdelivery maintenance can be likened to after-sales service. The product has been delivered to the client. But the client is dissatisfi ed, because the product does not work correctly, it does not do everything that the client currently wants, or the circumstances for which the product was built have changed in some way. Unless the software organization provides good maintenance service, the client will take all future product development business elsewhere. When the client and software group are part of the same organization, and hence inextricably tied from the viewpoint of future work, a dissatisfi ed client may use every means, fair or foul, to discredit the software group. This, in turn, leads to an erosion of confi dence, from both outside and inside the software group, and resignations and dismissals. It is important for every software organization to keep its clients happy by providing excellent postdelivery maintenance service. So, for product after product, postdelivery maintenance is the most challenging aspect of software production—and frequently the most thankless. 

How can this situation be changed? Managers must restrict postdelivery maintenance tasks to programmers with all the skills needed to perform maintenance. They must make it known that only top computer professionals merit maintenance assignments in their organization and pay them accordingly. If management believes that postdelivery maintenance is a challenge and good maintenance is critical for the success of the organization, attitudes toward postdelivery maintenance will slowly improve (but see Just in Case You Wanted to Know Box 16.2). 

Some of the problems that maintenance programmers face are now highlighted in a mini case study. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/a00d3cde39de18ebdb1eb2acbef7a5ca9c85cfc576f6e4885e83e13761b61537.jpg)


## 16.4

## Postdelivery Maintenance Mini Case Study

In countries with centralized economies, the government controls the distribution and marketing of agricultural products. In one such country, temperate fruits, such as peaches, apples, and pears, were the responsibility of the Temperate Fruit Committee (TFC). One day, the chairman of the TFC asked a government computer consultant 

# Just in Case You Wanted to Know

In Practical Software Maintenance , Tom Pigoski [1996] describes how he set up a U.S. Navy postdelivery maintenance organization in Pensacola, Florida. His idea was that, if prospective employees were told in advance that they were to work as maintainers, they would have a positive attitude toward postdelivery maintenance. In addition, he tried to keep morale high by ensuring that all employees received plenty of training and had the opportunity to travel all over the world in the course of their work. The beautiful nearby beaches certainly helped, as did the brand-new building they occupied. 

Nevertheless, within 6 months of starting work at the postdelivery maintenance organization, every employee asked when he or she could do some development work. It seems that it is extremely hard to change the attitudes of individuals toward postdelivery maintenance. 

to computerize the operations of the TFC. The chairman informed the consultant that there are exactly seven temperate fruits: apples, apricots, cherries, nectarines, peaches, pears, and plums. The database was to be designed for those seven fruits, no more and no less. After all, that was the way that the world was, and the consultant was not to waste time and money allowing for any sort of expandability. 

The product was duly delivered to the TFC. About a year later, the chairman summoned the maintenance programmer responsible for the product. “What do you know about kiwi fruit?” asked the chairman. “Nothing,” replied the mystifi ed programmer. “Well,” said the chairman, “it seems that kiwi fruit is a temperate fruit that has just started to be grown in our country, and the TFC is responsible for it. Please change the product accordingly.” 

The maintenance programmer discovered that the consultant fortunately had not carried out the chairman’s original instructions to the letter. The good practice of allowing for some sort of future expansion was too ingrained, and the consultant had provided a number of unused fi elds in the relevant database records. By slightly rearranging certain items, the maintenance programmer was able to incorporate kiwi fruit, the eighth temperate fruit, into the product. 

Another year went by, and the product functioned well. Then the maintenance programmer again was called to the chairman’s offi ce. The chairman was in a good mood. He jovially informed the programmer that the government had reorganized the distribution and marketing of agricultural products. His committee was now responsible for all fruit produced in that country, not just temperate fruit, and so the product now had to be modifi ed to incorporate the 26 additional kinds of fruit on the list he handed to the maintenance programmer. The programmer protested, pointing out that this change would take almost as long as rewriting the product from scratch. “Nonsense,” replied the chairman. “You had no trouble adding kiwi fruit. Just do the same thing another 26 times!” 

A number of important lessons are to be learned from this: 

The problem with the product, no provision for expansion, was caused by the developer, not the maintainer. The developer made the mistake of obeying the chairman’s instruction regarding future expandability of the product, but the maintenance programmer suffered the consequences. In fact, unless she reads this book, the consultant who developed the original product may never realize that her product was anything but a success. One of the more annoying aspects of postdelivery maintenance is that the maintainer is responsible for fi xing other people’s mistakes. The person who caused the problem either has other duties or has left the organization, but the maintenance programmer is left holding the baby. 

The client frequently does not understand that postdelivery maintenance can be difficult or, in some instances, all but impossible. The problem is exacerbated when the maintenance programmer has successfully carried out previous perfective and adaptive maintenance tasks but suddenly protests that a new assignment cannot be done, even though superfi cially it seems no different from what has been done before with little diffi culty. 

• All software development must be carried out with an eye on future postdelivery maintenance. If the consultant had designed the product for an arbitrary number of different kinds of fruit, there would have been no diffi culty in incorporating fi rst the kiwi fruit and then the 26 other kinds of fruit. 

As stated many times, postdelivery maintenance is a vital aspect of software pro duction, and the one that consumes the most resources. During product development, it is essential that the development team never forget the maintenance programmer, who will be responsible for the product once it has been installed. 

## 16.5 Management of Postdelivery Maintenance

Issues regarding management of postdelivery maintenance are now considered. 

## 16.5.1 Defect Reports

The fi rst thing needed when maintaining a product is a mechanism for changing the product. With regard to corrective maintenance, that is, removing residual faults, if the product appears to be functioning incorrectly, then a defect report should be fi led by the user. This must include enough information to enable the maintenance programmer to re-create the problem, which usually is some sort of software failure. In addition, the maintenance programmer must indicate the severity of the defect; typical severity categories include critical, major, normal, minor, and trivial. 

Ideally, every defect reported by a user should be fi xed immediately. In practice, programming organizations usually are understaffed, with a backlog of work, both development and maintenance. If the defect is critical, such as if a payroll product crashes the day before payday or overpays or underpays employees, immediate corrective action must be taken. Otherwise, each defect report must at least receive an immediate preliminary investigation. 

The maintenance programmer should fi rst consult the defect report fi le. This contains all reported defects that have not yet been fi xed, together with suggestions for working around them, that is, ways for the user to bypass the portion of the product that apparently is responsible for the failure, until such time as the defect can be fi xed. If the defect has been reported previously, any information in the defect report fi le should be given to the user. But, if what the user reports appears to be a new defect, then the maintenance programmer should study the problem and attempt to fi nd the cause and a way to fi x it. In addition, an attempt should be made to fi nd a way to work around the problem, because it may take 6 or 9 months before someone can be assigned to make the necessary changes to the software. 

In the light of the serious shortage of programmers and in particular programmers good enough to perform maintenance, suggesting a way to live with the defect until it can be solved often is the only way to deal with defect reports that are not true emergencies. 

The maintenance programmer’s conclusions should be added to the defect report fi le, together with any supporting documentation, such as listings, designs, and manuals used to arrive at those conclusions. The manager in charge of postdelivery maintenance should consult the fi le regularly, setting priorities for the various fi xes. The fi le also should contain the client’s requests for perfective and adaptive maintenance. The next modifi cation made to the product then will be the one with the highest priority. 

When copies of a product have been distributed to a variety of sites, copies of defect reports must be circulated to all users of the product, together with an estimate of when each defect can be fi xed. Then, if the same failure occurs at another site, the user can consult the relevant defect report to determine if it is possible to work around the defect and when it will be fi xed. It would be preferable to fi x every defect immediately and distribute a new version of the product to all sites, of course. Given the current worldwide shortage of good programmers and the realities of postdelivery software maintenance, distributing defect reports probably is the best that can be done. 

There is another reason why defects usually are not fi xed immediately. It almost always is cheaper to make a number of changes, test them all, change the documentation, and install the new version than it is to perform each change separately, test it, document it, install the new version, and then repeat the entire cycle for the next change. This is particularly true if every new version has to be installed on a signifi cant number of computers (such as a large number of clients in a client–server network) or when the software is running at different sites. As a result, organizations prefer to accumulate noncritical maintenance tasks, and then implement the changes as a group. 

## 16.5.2 Authorizing Changes to the Product

Once a decision has been made to perform corrective maintenance, a maintenance programmer is assigned the task of determining the fault that caused the failure and repairing it. After the code has been changed, the repair must be tested, as must the product as a whole (regression testing). Then, the documentation must be updated to refl ect the changes. In particular, a detailed description of what was changed, why it was changed, by whom, and when must be added to the prologue comments of any changed code artifact ( Figure 15.1 ). If necessary, analysis or design artifacts also are changed. A similar set of steps is followed when performing perfective or adaptive maintenance; the only real difference is that perfective and adaptive maintenance are initiated by a change in requirements rather than by a defect report. 

At this point all that would seem to be needed would be to distribute the new version to the users. But, what if the maintenance programmer has not tested the repair adequately? Before the product is distributed, it must be subjected to software quality assurance performed by an independent group; that is, the members of the maintenance SQA group must not report to the same manager as the maintenance programmer. It is important that the SQA group remain managerially independent (Section 6.1.2). 

Reasons were given previously as to why postdelivery maintenance is diffi cult. For those same reasons, maintenance also is fault prone. Testing during postdelivery maintenance is diffi cult and time consuming, and the SQA group should not underestimate the implications of software maintenance with regard to testing. Once the new version has been approved by the SQA group, it can be distributed. 

Another area in which management must ensure that procedures are followed carefully is when the technique of baselines and private copies (Section 5.10.2) is used. Suppose a programmer wishes to change Tax Provision Class . The programmer makes copies of Tax Provision Class and all the other code artifacts needed to perform the required maintenance task; often this includes all the other classes in the product. The programmer makes the necessary changes to Tax Provision Class and tests them. Now, the previous version of Tax Provision Class is frozen, and the modifi ed version of Tax Provision Class incorporating the changes is installed in the baseline. But, when the modifi ed product is delivered to the user, it immediately crashes. What went wrong is that the maintenance programmer tested the modifi ed version of Tax Provision Class using his or her private workspace copies, that is, the copies of the other code artifacts that were in the baseline at the time that maintenance of Tax Provision Class was started. In the meantime, certain other code artifacts were updated by other maintenance programmers working on the same product. The lesson is clear: Before installing a code artifact, it must be tested using the current baseline versions of all the other code artifacts and not the programmer’s private versions. This is a further reason for stipulating an independent SQA group—members of the SQA group simply have no access to programmers’ private workspaces. A third reason is that it has been estimated that the initial correction of a fault is itself incorrect some 70 percent of the time [Parnas, 1999]. 

## 16.5.3 Ensuring Maintainability

Postdelivery maintenance is not a one-time effort. A well-written product goes through a series of versions over its lifetime. As a result, it is necessary to plan for postdelivery maintenance during the entire software process. During the design workfl ow, for example, information-hiding techniques (Section 7.6) should be employed; during implementation, variable names should be selected that will be meaningful to future maintenance programmers (Section 15.3). Documentation should be complete, correct, and refl ect the current version of every component code artifact of the product. 

During postdelivery maintenance, it is important not to compromise the maintainability that has been built into the product from the very beginning. In other words, just as software development personnel always should be conscious of the inevitable postdelivery maintenance, so software maintenance personnel always should be conscious of the equally inevitable further future postdelivery maintenance. The principles established for maintain ability during development apply equally to postdelivery maintenance. 

## 16.5.4 Problem of Repeated Maintenance

One of the more frustrating diffi culties of software development is the moving-target problem (Section 2.4). As fast as the developer constructs the product, the client can change the requirements. Not only is this frustrating to the development team, frequent changes can result in a poorly constructed product. In addition, such changes add to the cost of the product. 

The problem is exacerbated during postdelivery maintenance. The more a completed product is changed, the more it deviates from its original design, and the more diffi cult further changes become. Under repeated maintenance, the documentation is likely to become even less reliable than usual, and the regression testing fi les may not be up to date. If still more maintenance is done, the product as a whole may fi rst have to be completely reimplemented. 

The problem of the moving target clearly is a management problem. In theory, if management is suffi ciently fi rm with the client and explains the problem at the beginning of the project, then the requirements can be frozen from the time the specifi cations are signed off on until the product is delivered. Again, after each request for perfective maintenance, the requirements can be frozen for, say, 3 months or 1 year. In practice, it does not work that way. For example, if the client happens to be the president of the corporation and the development organization is the software division of that corporation, then the president can order changes every Monday and Thursday and they will be implemented. The old proverb, “He who pays the piper calls the tune,” unfortunately is all too relevant in this situation. Perhaps, the best that the vice-president for software can do is to try to explain to the president the effect on the product of repeated maintenance, and then simply have the complete product reimplemented whenever further maintenance would be hazardous to the integrity of the product. 

Trying to discourage additional maintenance by ensuring that the requested changes are implemented slowly may mean that the relevant personnel are replaced by others prepared to do the job faster. In short, if the person who requests repeated changes has suffi cient clout, there is no solution to the problem of the moving target. 

## 16.6 Maintenance of Object-Oriented Software

One reason put forward for using the object-oriented paradigm is that it promotes maintainability. After all, an object is an independent unit of a program. More specifi cally, a well-designed object exhibits conceptual independence, otherwise known as encapsulation (Section 7.4). Every aspect of the product that relates to the portion of the real world modeled by that object is localized to the object itself. In addition, objects exhibit physical independence; information hiding is employed to ensure that implementation details are not visible outside that object (Section 7.6). The only form of communication permitted is sending a message to the object to invoke a specifi c method. 

As a consequence, the argument goes, it is easy to maintain an object for two reasons. First, conceptual independence means it is easy to determine which part of a product must be changed to achieve a specifi c maintenance goal, be it enhancement or corrective maintenance. Second, information hiding ensures that a change made to an object has no impact outside that object, and hence the number of regression faults is reduced greatly. 

In practice, however, the situation is not quite this idyllic. In fact, three obstacles are specifi c to the maintenance of object-oriented software. One of the problems can be solved through use of appropriate CASE tools, but the others are less tractable: 

1. Consider the C-- class hierarchy shown in Figure 16.1 . Method displayNode is defi ned in UndirectedTreeClass , inherited by DirectedTreeClass , and then redefi ned in RootedTreeClass . This redefi ned version is inherited by BinaryTreeClass and BalancedBinaryTreeClass and utilized in BalancedBinaryTreeClass . Therefore, a maintenance programmer has to study the complete inheritance hierarchy to understand BalancedBinaryTreeClass . Worse, the hierarchy may not be displayed in the linear fashion of Figure 16.1 but generally is spread over the entire product. So, to understand what displayNode does in BalancedBinaryTreeClass , the maintenance programmer may have to peruse a major proportion of the product. This is a far class UndirectedTreeClass { void displayNode (Node a); }// class UndirectedTreeClass class DirectedTreeClass : public UndirectedTreeClass { }// class DirectedTreeClass class RootedTreeClass : public DirectedTreeClass { void displayNode (Node a); }// class RootedTreeClass class BinaryTreeClass : public RootedTreeClass { }// class BinaryTreeClass class BalancedBinaryTreeClass : public BinaryTreeClass { Node hhh; displayNode (hhh); }// class BalancedBinaryTreeClass 

cry from the “independent” object described at the beginning of this section. The solution to this problem is straightforward: use the appropriate CASE tool. Just as a C++ compiler can resolve precisely the version of displayNode within instances of the class BalancedBinaryTreeClass , so a programming workbench can provide a “fl attened” version of a class, that is, a defi nition of the class with all features inherited directly or indirectly appearing explicitly, with any renaming or redefi nition incorporated. The fl attened form of BalancedBinaryTreeClass of Figure 16.1 includes the defi nition of displayNode from RootedTreeClass. 

2. Another obstacle to the maintenance of a product implemented using an objectoriented language is less easy to solve. It arises as a consequence of polymorphism and dynamic binding, concepts explained in Section 7.8. An example was given in that section, a base class named File Class , together with three subclasses: Disk File Class , Tape File Class , and Diskette File Class . This is shown in Figure 7.33(b) , reproduced here for convenience as Figure 16.2 . In base class File Class , a dummy ( abstract or virtual ) method open is declared. Then, a specifi c implementation of the method appears in each of the three subclasses; each method is given the identical name, open, as shown in Figure 16.2 . Suppose that myFile is declared to be an object, an instance of File Class , and the code to be maintained contains the message myFile.open ( ). As a consequence of polymorphism and dynamic binding, at run time, myFile could be a member of any of the three derived classes of File Class , that 

FIGURE 16.2 Defi nition of base class File Class with derived classes Disk File Class, Tape File Class, and Diskette File Class . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/340c10078040eadf168408e04f2348c6b430cbd927f5e213546fe4c66934708d.jpg)


is, a disk fi le, a tape fi le, or a diskette fi le. Once the run-time system has determined in which derived class it is, the appropriate version of open is invoked. This can have adverse consequences for maintenance. If a maintenance programmer encounters the call myFile.open ( ) in the code, then, to understand that part of the product, he or she has to consider what would happen if myFile were an instance of each of the three subclasses. A CASE tool cannot help here because, in general, there is no way to resolve dynamic binding issues using static methods. The only way to determine which of a number of dynamic bindings actually occurs in a particular set of circumstances is to trace through the code, either by running it on a computer or tracing through it manually. Polymorphism and dynamic binding indeed are extremely powerful aspects of object-oriented technology that promote the development of an object-oriented product. However, they can have a deleterious impact on maintenance, by forcing the maintenance programmer to investigate a wide variety of possible bindings that might occur at run time and hence determine which of a number of different methods could be invoked at that point in the code. 

3. The fi nal problem arises as a consequence of inheritance . Suppose a particular base class does most, but not all, of what is required for the design of a new product. A derived class now is defi ned, that is, a class identical to the base class in many ways, but new features may be added and existing features renamed, reimplemented, suppressed, or changed in other ways. Furthermore, these changes may be made without having an effect on the base class or any other derived classes. However, suppose now that the base class itself is changed. If this happens, all derived classes are changed in the same way. In other words, the strength of inheritance is that new leaves can be added to the inheritance tree (or graph, if the implementation language supports multiple inheritance, as C-- does) without altering any other class in the tree. But, if an interior node of the tree is changed in any way, then this change is propagated to all its descendants (the fragile base class problem ). 

Consequently, inheritance is another feature of object-oriented technology that can have a major positive infl uence on development but a negative impact on maintenance. 

## 16.7 Postdelivery Maintenance Skills versus Development Skills

Earlier in this chapter, much was said about the skills needed for postdelivery maintenance. 

• For corrective maintenance, the ability to determine the cause of a failure of a large product was deemed essential. But this skill is not needed exclusively for postdelivery maintenance. It is used throughout integration and product testing. 

• Another vital skill is the ability to function effectively without adequate documentation. Again, the documentation rarely is complete while integration and product testing are under way. 

• Also stressed was that skills with regard to analysis, design, implementation, and testing are essential for adaptive and perfective maintenance. These activities also are carried out during the development process, and each requires specialized skills if it is to be performed correctly. 

In other words, the skills a postdelivery maintenance programmer needs are in no way different from those needed by software professionals specializing in other aspects of software production. The key point is that a maintenance programmer must not be merely skilled in a broad variety of areas but highly skilled in all those areas. Although the average software developer can specialize in one area of software development, such as design or testing, the software maintainer must be a specialist in virtually every area of software production. After all, postdelivery maintenance is the same as development, only more so. 

## 16.8 Reverse Engineering

As has been pointed out, sometimes the only documentation available for postdelivery maintenance is the source code itself. (This happens all too frequently when maintaining legacy systems , that is, software in current use but developed some 15 or 20 years ago, if not earlier.) Under these circumstances, maintaining the code can be extremely diffi cult. One way of handling this problem is to start with the source code and attempt to re-create the design documents or even the specifi cations. This process is called reverse engineering. 

CASE tools can assist with this process. One of the simplest is a pretty printer (Section 5.8), which may help display the code more clearly. Other tools construct diagrams, such as fl owcharts or UML diagrams, directly from the source code; these visual aids can help in the process of design recovery. 

Once the maintenance team has reconstructed the design, there are two possibilities. One alternative is to attempt to reconstruct the specifi cations, modify the reconstructed specifi cations to refl ect the necessary changes, and reimplement the product the usual way. (Within the context of reverse engineering, the usual development process that proceeds from analysis through design to implementation is called forward engineering. The process of reverse engineering followed by forward engineering sometimes is called reengineering .) In practice, reconstruction of the specifi cations is an extremely hard task. More frequently the reconstructed design is modifi ed and the modifi ed design then is forward engineered. 

A related activity often performed during maintenance is restructuring. Reverse engineering takes the product from a lower level of abstraction to a higher level of abstraction, for example, from code to design. Forward engineering takes the product from a higher level of abstraction to a lower level. Restructuring , however, takes place at the same level. It is the process of improving the product without changing its functionality. Pretty printing is one form of restructuring, and so is converting code from unstructured to structured form. In general, restructuring is performed to make the source code (or design or even the database) easier to maintain. When an agile process (Section 2.9.5) is used, the design modifi cation known as refactoring is another example of restructuring. 

A worse situation occurs if the source code is lost and the executable version of the prod uct is all that is available. At fi rst sight, it might seem that the only possible way to re-create the source code is to use a disassembler to create assembler code and then to build a tool (that might be termed a reverse compiler ) to try to re-create the original high-level language code. A number of virtually insurmountable problems accompany this approach: 

• The names of the variables will have been lost as a consequence of the original compilation. 

• Many compilers optimize the code in some way, making it extremely diffi cult to attempt to re-create the source code. 

• A construct such as a loop in the assembler could correspond to a number of different possible constructs in the source code. 

In practice, therefore, the existing product is treated as a black box and reverse engineering is used to deduce the specifi cations from the behavior of the current product. The reconstructed specifi cations are modifi ed as required, and a new version of the product is forward engineered from those specifi cations. 

## 16.9 Testing during Postdelivery Maintenance

While the product is being developed, many members of the development team have a broad overview of the product as a whole, but as a result of the rapid personnel turnover in the computer industry, it is unlikely that members of the postdelivery maintenance team have been involved in the original development. Therefore, the maintainer tends to see the product as a set of loosely related components and generally is not aware that a change to one code artifact may seriously affect one or more other artifacts and hence the product as a whole. Even if the maintainer wished to understand every aspect of the product, the pressures to fi x or to extend the product generally are such that no time is allowed for the detailed study needed to achieve this. Furthermore, in many cases, little or no documentation is available to assist in gaining that understanding. One way of trying to minimize this diffi culty is to use regression testing, that is, testing the changed product against previous test cases to ensure that it still works correctly. 

For this reason, it is vital to store all test cases, together with their expected outcomes, in machine-readable form. As a result of changes made to the product, certain stored test cases may have to be modifi ed. For example, if the percentages of salary to be withheld change as a consequence of tax legislation, then the correct output from a payroll product for each test case involving withholding changes, too. Similarly, if satellite observations lead to corrections in the latitude and longitude of an island, then the correct output from a product that calculates the position of an aircraft using the coordinates of the island must correspondingly change. Depending on the maintenance performed, some valid test cases become invalid. But the computations that need to be made to correct the stored test cases are essentially the same as would have to be made to set up new test data for checking that the maintenance has been correctly performed. No additional work therefore is involved in maintaining the fi le of test cases and their expected outcomes. 

It can be argued that regression testing is a waste of time because regression testing requires the complete product to be retested against a host of test cases, most of which apparently have nothing to do with the code artifacts modifi ed in the course of product maintenance. The word apparently in the previous sentence is critical. The dangers of unwitting side effects of maintenance (that is, the introduction of regression faults) are too great for that argument to hold water; regression testing is an essential aspect of maintenance in all situations. 

## 16.10 CASE Tools for Postdelivery Maintenance

It is unreasonable to expect maintenance programmers to keep track manually of the various revision numbers and assign the next revision number each time a code artifact is updated. Unless the operating system incorporates version control, a version-control tool such as the UNIX tools sccs (source code control system) [Rochkind, 1975] and rcs (revision control system) [Tichy, 1985] is needed. It is equally unreasonable to expect manual control of the freezing technique described in Chapter 5 or any other manual way of ensuring that revisions are updated appropriately. A confi guration-control tool is needed. Popular opensource confi guration-control tools include CVS (concurrent versions system) [Loukides and Oram, 1997] and Subversion. Typical examples of commercial tools are CCC (change and confi guration control) and IBM Rational ClearCase. Even if the software organization does not wish to purchase a complete confi guration-control tool, at the very least a build tool must be used in conjunction with a version-control tool. Another category of CASE tool virtually essential during postdelivery maintenance is a defect-tracking tool that keeps a record of reported defects not yet fi xed. 

Section 16.8 described some categories of CASE tools that can assist in reverse engineering and reengineering. Examples of such tools that assist by creating visual displays of the structure of the product include IBM Rational Rose and Together. Doxygen is an opensource tool of this kind. 

Defect tracking is an important aspect of postdelivery maintenance. It is vital to be able to determine the current status of every reported defect. IBM Rational ClearQuest is a commercial defect-tracking tool , and Bugzilla is a popular open-source tool. Such tools can be used to record the severity of a defect (Section 16.5.1) and its status (essentially, whether or not the defect has been fi xed). In addition, some defect-tracking tools can link a defect report to the confi guration management tool so that, when a new version is built, the maintenance programmer can select specifi c defect report fi xes to be included in the build. 

Postdelivery maintenance is diffi cult and frustrating. The very least that management can do is to provide the maintenance team the tools needed for effi cient and effective product maintenance. 

## 16.11 Metrics for Postdelivery Maintenance

The activities of postdelivery maintenance essentially are analysis, design, implementation, testing, and documentation. Therefore, the metrics that measure these activities are equally applicable to maintenance. For example, the complexity metrics of Section 15.13.2 are relevant to postdelivery maintenance, in that a code artifact with high complexity is a likely candidate for inducing a regression fault. Particular care must be taken in modifying such a code artifact. 

In addition, metrics specifi c to postdelivery maintenance include measures relating to software defect reports, such as the total number of defects reported and classifi cation of those defects by severity and type. In addition, information regarding the current status of the defect reports is needed. For example, there is a considerable difference between having 13 critical defects reported and fi xed during 2006 and having only 2 critical defects reported during that year but neither of them fi xed. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/e179d31a6c84946fc4ad8fbc26aaf7473856fc9804540acb493c77cea78d27be.jpg)


## 16.12 Postdelivery Maintenance: The MSG Foundation Case Study

A number of faults have been seeded in the source code of the MSG Foundation case study. In addition, perfective maintenance must be performed. These maintenance tasks are left as exercises (Problems 16.16 through 16.21). 

## 16.13 Challenges of Postdelivery Maintenance

This chapter describes numerous challenges of postdelivery maintenance. The toughest one to change is that maintenance is generally harder than development, yet maintenance programmers are often looked down on by developers and all too frequently are paid less than developers. 

## Chapter apter Review view

The chapter begins with a comparison of development and maintenance (Section 16.1). Postdelivery maintenance is an important and challenging software activity (Sections 16.2 and 16.3). This is illustrated by means of the mini case study of Section 16.4. Issues relating to the management of postdelivery maintenance are described (Section 16.5), including the problem of repeated maintenance (Section 16.5.4). Postdelivery maintenance of object-oriented software is discussed in Section 16.6. The skills that a maintenance programmer needs are the same as those of a developer; the difference is that a developer can specialize in one aspect of the software process, whereas the maintainer mus be an expert in all aspects of software production (Section 16.7). A description of reverse engineering is given in Section 16.8. Next follows a description of testing during postdelivery maintenance (Section 16.9) and CASE tools for postdelivery maintenance (Section 16.10). Metrics for postdelivery maintenance are described in Section 16.11. Postdelivery maintenance of the MSG Foundation case study, discussed in Section 16.12. is left as an exercise. The chapter concludes with a discussion of the challenges of postdelivery maintenance (Section 16.13) 

A classic source of information on postdelivery maintenance is [Lientz, Swanson, and Tompkins, 1978], although some of the results are now being questioned (see Just in Case You Wanted to Know Box 1.3). Regression test case selection is discussed in [Harrold, Rosenblum, Rothermel, and Weyuker, 2001] and setting priorities of regression test cases in [Rothermel, Untch, Chu, and Harrold, 2001]. A method for estimating staffi ng needs during postdelivery maintenance is described in [Antoniol, Cimitile, Di Lucca, and Di Penta, 2004]. 

The September 2005 issue of Journal of Systems and Software contains a number of papers on reverse engineering. Fioravanti and Nesi [2001] present metrics for estimating adaptive maintenance effort. Problems of comprehension of legacy systems are discussed in [Rajlich, Wilde, Buckellew, and Page, 2001]. The importance of traceability within the context of reengineering is the subject of [Ebner and Kaindl, 2002]. The use of metrics within the context of maintainability is discussed in [Bandi, Vaishnavi, and Turk, 2003]. Problems that can arise in the maintenance of open-source software are presented in [Samoladas, Stamelos, Angelis, and Oikonomou, 2005]. Extracting the architecture of a software product from run-time observations is described in [Schmerl et al., 2006]. How developers gain an understand ing of unfamiliar code is presented in [Ko, Myers, Coblenz, and Aung, 2006] and [Sillito, Murphy, and De Volder, 2008]. During maintenance, the size of the test suite can grow signifi cantly. Culling of test cases, however, can reduce the fault detection effectiveness. This issue is addressed in [Jeffrey and Gupta, 2007]. 

Briand, Bunse, and Daly [2001] discuss the maintainability of object-oriented designs. Experiments to assess the impact of design pattern documentation on postdelivery maintenance are described in [Prechelt, Unger-Lamprecht, Philippsen, and Tichy, 2002]. The maintainability of object-oriented software is discussed in [Lim, Jeong, and Schach, 2005] and [Freeman and Schach, 2005]. The impact of UML diagrams on maintenance is described in [Arisholm, Briand, Hove, and Labiche, 2006]; the costs and benefi ts in [Dzidek, Arisholm, and Briand, 2008]. A tool that supports incremental software maintenance while ensuring consistency between the artifacts is described in [Reiss, 2006]. Automated refactoring to reduce the cost of maintaining object-oriented software is proposed in [O’Keeffe and Ó Cinnéide, 2008]. Lack of effectiveness of software metrics in identifying fault-prone classes in postdelivery maintenance (as opposed to during development) is discussed in [Shatnawi and Li, 2008]. 

Papers on software maintenance appear in the September 2006 issue of IEEE Transactions on Software Engineering ; [Briand, Labiche, and Leduc, 2006] is of particular interest. The proceedings of the annual Conference on Software Maintenance and Reengineering, as well as the International Conference on Software Maintenance and Evolution, are broadly based sources of information on all aspects of maintenance. 

<table><tr><td>Key Terms</td><td>adaptive maintenance 553corrective maintenance 553defect 554defect report 557defect-tracking tool 565encapsulation 560evolution 552</td><td>forward engineering 563fragile base class problem 562inheritance 562legacy system 563moving-target problem 559perfective maintenance 553postdelivery maintenance 551</td><td>reengineering 563refactoring 564regression fault 554regression testing 554restructuring 564reverse engineering 563</td></tr></table>

## Problems

16.1 Why do you think that the mistake is frequently made of considering postdelivery software maintenance to be inferior to software development? 

16.2 Consider a product that determines whether a computer is virus free. Describe why such a product is likely to have multiple variations of many of its code artifacts. What are the implications for postdelivery maintenance? How can the resulting problems be solved? 

16.3 Repeat Problem 16.2 for the automated library circulation system of Problem 8.7. 

16.4 Repeat Problem 16.2 for the product of Problem 8.8 that checks whether a bank statement is correct. 

16.5 Repeat Problem 16.2 for the automated teller machine of Problem 8.9. 

16.6 You are the manager in charge of postdelivery maintenance in a large software organization. What qualities do you look for when hiring new employees? 

16.7 What are the implications of postdelivery maintenance for a one-person software production organization? 

16.8 You have been asked to build a computerized defect report fi le. What sort of data would you store in the fi le? What sorts of queries could be answered by your tool? What sorts of queries could not be answered by your tool? 

16.9 You receive a memo from the vice-president for software maintenance of Ye Olde Fashioned Software Corporation (Problem 15.29), pointing out that, for the foreseeable future, Olde Fashioned will have to maintain tens of millions of lines of COBOL 85 code and asking your advice with regard to CASE tools for such postdelivery maintenance. What do you reply? 

16.10 Now you are told that the tens of millions of lines of COBOL 85 code (Problem 16.9) have to be reimplemented in an object-oriented language, either in COBOL 2002 or in C++/Java. Which of the two would you choose: COBOL 2002 or C++/Java? Justify your answer. 

16.11 If Ye Olde Fashioned Software Corporation decides to reimplement their code in COBOL 2002 (see Problem 16.10), what strategy would you follow? 

16.12 If Ye Olde Fashioned Software Corporation decides to reimplement their code in C++/Java (see Problem 16.10), what strategy would you follow? 

16.13 What role does reuse play in your answers to Problems 16.11 and 16.12? 

16.14 What role does portability play in your answers to Problems 16.11 and 16.12? 

16.15 (Term Project) Suppose that the product for Chocoholics Anonymous in Appendix A has been implemented exactly as described. Now the product has to be modifi ed to include endocrinologists as providers. In what ways will the existing product have to be changed? Would it be better to discard everything and start again from scratch? Compare your answer to the answer you gave to Problem 1.19. 

16.16 (Case Study) Improve the aesthetic appearance of the reports in the implementation of Section 15.8 by adjusting the horizontal alignment of the various components. 

16.17 (Case Study) Suppose that the requirements of the MSG Foundation are changed so that a couple will never have to pay more than 26 percent of their gross income each week to the MSG Foundation (rather than the 28 percent as currently stipulated). In how many places does the implementation of Section 15.8 have to be changed? 

16.18 (Case Study) The MSG Foundation has decided that it will now operate on a monthly basis, rather than a weekly basis. Modify the implementation of Section 15.8 accordingly. 

16.19 (Case Study) Replace the menu-driven input routines in the implementation of Section 15.8 with a graphical user interface (GUI). 

16.20 (Case Study) Modify the implementation of Section 15.8 so that it runs under Linux. 

16.21 (Case Study) Modify the implementation of Section 15.8 to make it Web-based. 

16.22 (Readings in Software Engineering) Your instructor will distribute copies of [Freeman and Schach, 2005]. Do you feel that the paper resolves the question of whether object orientation promotes maintainability? Justify your answer. 

## References



[Antoniol, Cimitile, Di Lucca, and Di Penta, 2004] G. ANTONIOL , A. CIMITILE , G. A. DI LUCCA, AND M. DI PENTA , “Assessing Staffi ng Needs for a Software Maintenance Project through Queuing Simulation,” IEEE Transactions on Software Engineering 30 (January 2004), pp. 43–58. 





[Arisholm, Briand, Hove, and Labiche, 2006] E. ARISHOLM , L. C. BRIAND , S. E. HOVE, AND Y. LABICHE , “The Impact of UML Documentation on Software Maintenance: An Experimental Evaluation,” IEEE Transactions on Software Engineering 32 (June 2006), pp. 365–81. 





[Bandi, Vaishnavi, and Turk, 2003] R. K. BANDI , V. K. VAISHNAVI, AND D. E. TURK , “Predicting Maintenance Performance Using Object-Oriented Design Complexity Metrics,” IEEE Transactions on Software Engineering 29 (January 2003), pp. 77–87. 





[Briand, Bunse, and Daly, 2001] L. C. BRIAND , C. BUNSE, AND J. W. DALY , “A Controlled Experiment for Evaluating Quality Guidelines on the Maintainability of Object-Oriented Designs,” IEEE Transactions on Software Engineering 27 (June 2001), pp. 513–30. 





[Briand, Labiche, and Leduc, 2006] L. C. BRIAND , Y. LABICHE, AND J. LEDUC , “Toward the Reverse Engineering of UML Sequence Diagrams for Distributed Java Software,” IEEE Transactions on Software Engineering 32 (September 2006), pp. 642–63. 





[Dzidek, Arisholm, and Briand, 2008] W. J. DZIDEK , E. ARISHOLM, AND L. C. BRIAND , “A Realistic Empirical Evaluation of the Costs and Benefi ts of UML in Software Maintenance,” IEEE Transactions on Software Engineering 34 (May–June 2008), pp. 407–32. 





[Ebner and Kaindl, 2002] G. EBNER AND H. KAINDL , “Tracing All Around in Reengineering,” IEEE Software 19 (May–June 2002), pp. 70–77. 





[Fioravanti and Nesi, 2001] F. FIORAVANTI AND P. NESI , “Estimation and Prediction Metrics for Adaptive Maintenance Effort of Object-Oriented Systems,” IEEE Transactions on Software Engineering 27 (December 2001), pp. 1062–84. 





[Freeman and Schach, 2005] G. L. FREEMAN , JR. AND S. R. SCHACH , “The Task-Dependent Nature of the Maintenance of Object-Oriented Programs,” Journal of Systems and Software 76 (May 2005), pp. 195–206. 





[Harrold, Rosenblum, Rothermel and Weyuker, 2001] M. J. HARROLD , D. ROSENBLUM , G. ROTHER-MEL, AND E. WEYUKER , “Empirical Studies of a Prediction Model for Regression Test Selection,” IEEE Transactions on Software Engineering 27 (March 2001), pp. 248–63. 





[Jacobson, Booch, and Rumbaugh, 1999] I. JACOBSON , G. BOOCH, AND J. RUMBAUGH , The Unifi ed Software Development Process, Addison-Wesley, Reading, MA, 1999. 





[Jeffrey and Gupta, 2007] D. JEFFREY AND N. GUPTA , “Improving Fault Detection Capability by Selectively Retaining Test Cases during Test Suite Reduction,” IEEE Transactions on Software Engineering 33 (February 2007), pp. 108–23. 





[Ko, Myers, Coblenz, and Aung, 2006] A. J. KO, B. A. MYERS , M. J. COBLENZ, AND H. H. AUNG , “An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks,” IEEE Transactions on Software Engineering 32 (December 2006), pp. 971–87. 





[Lientz, Swanson, and Tompkins, 1978] B. P. LIENTZ , E. B. SWANSON, AND G. E. TOMPKINS , “Characteristics of Application Software Maintenance,” Communications of the ACM 21 (June 1978), pp. 466–71. 





[Lim, Jeong, and Schach, 2005] J. S. LIM , S. R. JEONG, AND S. R. SCHACH , “An Empirical Investigation of the Impact of the Object-Oriented Paradigm on the Maintainability of Real-World Mission-Critical Software,” Journal of Systems and Software 77 (August 2005), pp. 131–38. 





[Lotto, 1515] L. LOTTO , Giovanni Agostino della Torre and his Son, Niccolò , oil on canvas, 1515, www.nationalgallery.org.uk/cgi-bin/WebObjects.dll/CollectionPublisher.woa/wa/largeI mage?workNumber=NG699. 





[Loukides and Oram, 1997] M. K. LOUKIDES AND A. ORAM , Programming with GNU Software, O’Reilly and Associates, Sebastopol, CA, 1997. 





[O’Keeffe and Ó Cinnéide, 2008] M. O’ KEEFFE AND M. Ó CINNÉIDE, “Software Reliability Prediction by Soft Computing Techniques,” Journal of Systems and Software 81 (April 2008), pp. 502–16. 





[Parnas, 1999] D. L. PARNAS , “Ten Myths about Y2K Inspections,” Communications of the ACM 42 (May 1999), p. 128. 





[Pigoski, 1996] T. M. PIGOSKI , Practical Software Maintenance: Best Practices for Managing Your Software Investment , John Wiley and Sons, New York, 1996. 





[Prechelt, Unger-Lamprecht, Philippsen, and Tichy, 2002] L. PRECHELT , B. UNGER - LAMPRECHT , M. PHILIPPSEN, AND W. F. TICHY , “Two Controlled Experiments in Assessing the Usefulness of Design Pattern Documentation in Program Maintenance,” IEEE Transactions on Software Engineering 28 (June 2002), pp. 595–606. 





[Rajlich, Wilde, Buckellew, and Page, 2001] V. RAJLICH , N. WILDE , M. BUCKELLEW, AND H. PAGE , “Software Cultures and Evolution,” IEEE Computer 34 (September 2001), pp. 24–28. 





[Reiss, 2006] S. P. REISS , “Incremental Maintenance of Software Artifacts,” IEEE Transactions on Software Engineering 32 (September 2006), pp. 682–97. 





[Rochkind, 1975] M. J. ROCHKIND , “The Source Code Control System,” IEEE Transactions on Software Engineering SE-1 (October 1975), pp. 255–65. 





[Rothermel, Untch, Chu, and Harrold, 2001] G. ROTHERMEL , R. H. UNTCH , C. CHU, AND M. J. HAR-ROLD , “Prioritizing Test Cases for Regression Test Cases,” IEEE Transactions on Software Engineering 27 (October 2001), pp. 929–48. 





[Samoladas, Stamelos, Angelis, and Oikonomou, 2005] I. SAMOLADAS , I. STAMELOS , L. ANGELIS, AND A. OIKONOMOU , “Open Source Software Development Should Strive for Even Greater Code Maintainability,” Communications of the ACM 47 (October 2004), pp. 83–87. 





[Schmerl et al., 2006] B. SCHMERL , J. ALDRICH , D. GARLAN , R. KAZMAN, AND H. YAN , “Discovering Architectures from Running Systems,” IEEE Transactions on Software Engineering 32 (July 2006), pp. 454–66. 





[Shatnawi and Li, 2008] R. SHATNAWI AND W. LI , “The Effectiveness of Software Metrics in Identifying Error-Prone Classes in Post-Release Software Evolution Process,” Journal of Systems and Software 81 (November 2008), pp. 1868–82. 





[Sillito, Murphy, and De Volder, 2008] J. SILLITO , G. C. MURPHY, AND K. DE VOLDER , “Asking and Answering Questions during a Programming Change Task,” IEEE Transactions on Software Engineering 34 (July–August 2008), pp. 434–51. 





[Tichy, 1985] W. F. TICHY , “RCS—A System for Version Control,” Software—Practice and Experience 15 (July 1985), pp. 637–54. 



# More on UML

Learning Objectives 

After studying this chapter, you should be able to 

• Model software using UML use cases, class diagrams, notes, use-case diagrams, interaction diagrams, statecharts, activity diagrams, packages, component diagrams, and deployment diagrams. 

• Appreciate that UML is a language, not a methodology. 

During the course of this book, various elements of UML [Booch, Rumbaugh, and Jacobson, 1999] have been introduced. Specifi cally, the notation for class diagrams, inheritance, aggregation, and association was described in Chapter 7 . In Chapter 11 , use cases, use-case diagrams, and notes were introduced; in Chapter 13 , statecharts, interaction diagrams, and sequence diagrams were added. 

This subset of UML is adequate for understanding this book and for doing all the exercises, as well as the term project of Appendix A. However, real-world software products are, unfortunately, much larger and considerably more complex than the MSG Foundation case study or the term project of Appendix A. Accordingly, in this chapter more material on UML is presented, as preparation for entering the real world. 

Before reading this chapter, it is necessary to be aware that UML, like all state-of-the-art computer languages, is constantly changing. When this book was written, the latest version of UML was Version 2.0. By this time, however, some aspects of UML may have changed. As explained in Just in Case You Wanted to Know Box 3.2, UML is now under the control of the Object Management Group. Before proceeding, it would probably be a good idea to check for updates to UML at the OMG website, www.omg.org . 

## 17.1 UML Is Not a Methodology

Before looking at UML in more detail, it is essential to clarify what UML is and, more importantly, what UML is not. UML is an acronym for Unifi ed Modeling Language. That is, UML is a language . Consider a language like English. English can be used to write novels, encyclopedias, poems, prayers, news reports, and even textbooks on software engineering. That is, a language is simply a tool for expressing ideas. A specifi c language does not constrain the types of ideas that can be described by that language or the way that they can be described. 

As a language, UML can be used to describe software developed using the traditional paradigm or any of the many versions of the object-oriented paradigm, including the Unifi ed Process. In other words, UML is a notation, not a methodology. It is a notation that can be used in conjunction with any methodology. 

In fact, UML is not merely a notation; it is the notation. It is hard to imagine a modern book on software engineering that does not use UML to describe software. UML has become a world standard, so much so that someone unfamiliar with UML would have diffi culty functioning today as a software professional. 

The title of this chapter is “More on UML.“ Bearing in mind the central role played by UML, it would seem essential for all of UML to be presented here. However, the manual for Version 2.0 of UML is over 1200 pages long, so complete coverage would probably not be a good idea. But is it possible to be a competent software professional without knowing every single aspect of UML? 

The key point is that UML is a language. The English language has over 100,000 words, but almost all speakers of English seem to manage perfectly well with just a subset of the complete English vocabulary. In the same way, in this chapter all the types of UML diagrams are described, together with many (but by no means all) of the various options for each of those diagrams. The small subset of UML presented in Chapters 7 , 11 , and 13 is adequate for the purposes of this book. In the same way, the larger subset of UML presented in this chapter is adequate for the development and maintenance of most software products. 

## 17.2 Class Diagrams

The simplest possible class diagram is shown in Figure 17.1 . It depicts the Bank Account Class. More details of Bank Account Class are shown in the class diagram of Figure 17.2 . A key aspect of UML is that both Figures 17.1 and 17.2 are valid class diagrams. In other words, in UML as many or as few details may be added as are judged appropriate for the current iteration and incrementation. 


FIGURE 17.1 The simplest possible class diagram.


<table><tr><td>Bank Account Class</td></tr><tr><td></td></tr></table>


FIGURE 17.2 The class diagram of Figure 17.1 with an attribute and two operations added.


<table><tr><td>Bank Account Class</td></tr><tr><td>accountBalance</td></tr><tr><td>deposit ( ) withdraw ( )</td></tr></table>

This freedom of notation extends to objects. The notation bank account may be informally used for one specifi c object of this class. The full UML notation is 

## bank account : Bank Account Class

That is, bank account is an object, an instance of a class Bank Account Class. In more detail, the underlining denotes an object, the colon denotes “an instance of,” and the boldface and initial uppercase letters in Bank Account Class denote this is a class. However, UML allows us to use a shorter notation bank account when there is no ambiguity. 

Now suppose we wish to model the concept of an arbitrary bank account. That is, we do not wish to refer to one specifi c object of Bank Account Class. The UML notation for this is 

## : Bank Account Class

As just pointed out, the colon means “an instance of,” so : Bank Account Class means “an instance of class Bank Account Class ,” which is precisely what we wanted to model. This notation is widely used in Chapter 13 . Conversely, in Figure 13.51, a communication diagram for the realization of a scenario of the use case Update Estimated Annual Operating Expenses of the MSG Foundation software product, the actor is labeled MSG Staff Member and not : MSG Staff Member (the labeling of other items in that diagram) precisely because MSG Staff Member denotes that MSG Staff Member is an actor, whereas : MSG Staff Member would denote “an instance of the [nonexistent] MSG Staff Member Class .” 

Section 7.6 introduced the concept of information hiding. In UML, the prefi x + indicates that an attribute or operation is public , and similarly the prefi x – denotes that the attribute or operation is private. This notation is used in Figure 17.3 . The attribute of Bank Account Class is declared to be private (so that we can achieve information hiding), whereas both the operations are public so that they can be invoked from anywhere in the software product. A third standard type of visibility, protected , uses the prefi x #. If an attribute is public, it is visible everywhere; if it is private, it is visible only in the class in which it is defi ned, and if it is protected, it is visible both within the class in which it is defi ned and within subclasses of that class. 

Up to now in this chapter, class diagrams containing only one class have been presented. Section 17.2.1 considers class diagrams with more than one class. 

## 17.2.1 Aggregation

Consider Figure 17.4 , which models the statement: “A car consists of a chassis, an engine, wheels, and seats.” Recall that the open diamonds denote aggregation. Aggregation is the UML term for the part–whole relationship ; the parts of a car are the chassis, engine, wheels, and seats. The diamond is placed at the “whole” (car) end, not the “part” (chassis, engine, wheels, or seats) end of the line connecting a part to the whole 

<table><tr><td>Bank Account</td></tr><tr><td>- accountBalance</td></tr><tr><td>+ deposit ( ) + withdraw ( )</td></tr></table>


FIGURE 17.4 An aggregation example.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/44348035c14b3af594125c77f858fddf09374165be7b37dcc6c5bd48c0be85fc.jpg)



FIGURE 17.5 Aggregation example with multiplicities.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/63fef49ca8832dc154f78296977ee0a60d3d6aa96c06460dff0f9c6742326fd8.jpg)


## 17.2.2 Multiplicity

Now suppose that we want to use UML to model the statement: “A car consists of one chassis, one engine, four or fi ve wheels, an optional sunroof, zero or more fuzzy dice hanging from the rearview mirror, and two or more seats.” This is shown in Figure 17.5 . The numbers next to the ends of the lines denote multiplicity , the number of times that the one class is associated with the other class. 

First consider the line connecting Chassis Class to Car Class . The 1 at the “part” end of the line denotes that one chassis is involved in this relationship, and the 1 at the “whole” end denotes that one car is involved; that is, each car has one chassis. Similar observations hold for the line connecting Engine Class to Car Class. 

Stephen Kleene laid the foundations of recursive function theory, a branch of mathematical logic that has had a major infl uence on computer science. The Kleene star (the asterisk that denotes “zero or more” in diagrams like Figure 17.5 ) is named after him. 

The Kleene star is well known among mathematicians and computer scientists. What is considerably less well known is that Kleene pronounced his last name as if it were written “Clay knee” (with the accent on the fi rst syllable), and not “Clean knee.” 

Now consider the line connecting Wheels Class to Car Class . The 4..5 at the “part” end together with the 1 at the “whole” end denotes that each car has from four to fi ve wheels (the fi fth wheel is the spare). Because instances of classes come in whole numbers only, this means that the UML diagram models the statement that a car has four or fi ve wheels, as required. 

In general, the two dots .. denote a range. Consequently, 0..1 means zero or one, which is the UML way of denoting “optional.” That is why there is the 0..1 next to the line connecting Sun Roof Class to Car Class. 

Now look at the line connecting Fuzzy Dice Class to Car Class . At the “part” end, the label is *. An asterisk by itself denotes “zero or more.” Accordingly, the * in Figure 17.5 means that a car has zero or more fuzzy dice hanging from the rearview mirror. (If you want to know more about that asterisk, see Just in Case You Wanted to Know Box 17.1.) 

Now look at the line connecting Seats Class to Car Class . At the “part” end, the label is 2..*. An asterisk by itself denotes “zero or more”; an asterisk in a range denotes “or more.” Consequently, the 2..* in Figure 17.5 means that a car has two or more seats. 

Therefore, in UML if the exact multiplicity is known, that number is used. An example is the 1 that appears in eight places in Figure 17.5 . If the range is known, the range notation is used, as with the 0..1 or 4..5 in Figure 17.5 . And if the number is unspecifi ed, the asterisk is used. If the upper limit in a range is unspecifi ed, the range notation is combined with the asterisk notation, as with the 2..* in Figure 17.5 . In passing, the multiplicity notation of UML is based on the entity–relationship diagrams of traditional database theory (see Section 12.6). 

## 17.2.3 Composition

Another example of aggregation is shown in Figure 17.6 , which models the relationship between a chessboard and its squares; every chessboard consists of 64 squares. In fact, this relationship goes further; it is an example of composition , a stronger form of aggregation. As previously stated, association models the part–whole relationship. When there is composition, then, in addition, every part may belong to only one whole, and if the whole is deleted, so are the parts. In the example, if there are a number of different chessboards, each square belongs to only one board, and if a chessboard is thrown away, all 64 squares 

Another aggregation example (but see Figure 17.7 ). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/32d780631f80b160d94ca5f8d684454919afb84df179925e668b3accdb944a87.jpg)


FIGURE 17.7 Composition example. 

FIGURE 17.8 Generalization (inheritance) example with an explicit discriminator. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/d1ef5ff474827da6fcd081fa41cf516f2b7af4e7c9ed27ca0232c2ae67028f78.jpg)



FIGURE 17.9 An association.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/be0e24eae47c2338b11a67478160b354b847606c9f3b2508b8f456fe7d135ea0.jpg)


on that board go as well. Composition, an extension of aggregation, is depicted with a solid diamond, as in Figure 17.7 . 

## 17.2.4 Generalization

Inheritance is a required feature of object orientation. It is a special case of generalization . The UML notation for generalization is an open triangle. Sometimes we choose to label that open triangle with a discriminator . Consider Figure 17.8 , which models two types of investments, bonds and stocks. The notation investmentType next to the open triangle means that every instance of Investment Class or its two subclasses has an attribute investmentType , and this attribute can be used to distinguish between instances of bonds and instances of stocks. 

## 17.2.5 Association

In Section 7.7, an example of association involving two classes was presented in which the direction of the association had to be clarified by means of a navigation arrow in the form of a solid triangle. Figure 7.32 is reproduced here as Figure 17.9. 


FIGURE 17.10 An association class.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/7e25b365c7a47ff2b0aa48d8fe214d72c29daee74ee19ea45b67b76a767ea8ff.jpg)


In some cases, the association between the two classes may itself need to be modeled as a class. For example, suppose the radiologist in Figure 17.9 consults the lawyer on a number of different occasions, on each occasion for a different length of time. To enable the lawyer to bill the radiologist correctly, a class diagram such as that depicted in Figure 17.10 is needed. Now consults has become a class, Consults Class , called an association class (because it is both an association and a class). 

## 17.3 Notes

When we want to include a comment in a UML diagram, we put it in a note (a rectangle with the top right-hand corner bent over). A dashed line is then drawn from the note to the item to which the note refers. Figure 13.41 shows a note. 

## 17.4 Use-Case Diagrams

As described in Section 11.4.3, a use case is a model of the interaction between external users of a software product ( actors ) and the software product itself. More precisely, an actor is a user playing a specifi c role. A use-case diagram is a set of use cases. 

In Section 11.4.3, generalization within the context of actors was described, as depicted in Figure 11.2. Figure 17.11 is another example; it shows that a Manager is a special case of an Employee . As with classes, the open triangle points toward the more general case. 

## 17.5 Stereotypes

The three primary tax forms for U.S. personal income tax are Forms 1040, 1040A, and 1040EZ. Figure 17.12 shows that use cases Prepare Form 1040, Prepare Form 

FIGURE 17.12 The use cases Prepare Form 1040, Prepare Form 1040A, and Prepare Form 1040EZ incorporate the use case Print Tax Form. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/2993e30f2a63bc21b98de86e438e34718f1f6fa6e6bd99607a39e75129d34c14.jpg)



FIGURE 17.13 Use case Order a Burger showing the variation when the customer turns down the fries.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/f8c9d2d15d538a2ec9f28d1c529d648d69a9bf918302e28e433bad0c13b1aae3.jpg)


1040A, and Prepare Form 1040EZ all incorporate the use case Print Tax Form , as indicated by the include relationship, represented by a stereotype. 

A stereotype in UML is a way of extending UML. That is, if we need to defi ne a construct that is not in UML, we can do it. Three stereotypes were presented in Chapter 12 : boundary, control, and entity classes. In general, the names of stereotypes appear between guillemets [Wikipedia, 2010], for example, «this is my own construct» . Accordingly, instead of using the special symbol for a boundary class, the standard rectangular symbol for a class could have been used with the notation «boundary class» inside the rectangle and similarly for control and entity classes. 

The include relationship shown in Figure 17.12 is treated in UML as a stereotype; hence the notation «include» in that fi gure to denote common functionality, in this instance the use case Print Tax Form (Figure 11.41). Another relationship is the extend relationship , where one use case is a variation of the standard use case. For example, we may wish to have a separate use case to model the situation of a diner ordering a burger but turning down the fries. The notation «extend» is similarly used for this purpose, as shown in Figure 17.13 . However, for this relationship, the open-headed arrow goes in the other direction. 

## 17.6 Interaction Diagrams

Interaction diagrams show the way that the objects in the software product interact with one another. In Chapter 13 , both types of interaction diagram supported by UML were presented: sequence diagrams and communication diagrams. 

First, consider sequence diagrams . Suppose that someone interactively orders an item over the Internet, but when the overall total, including sales tax and delivery charges, is displayed, the buyer decides that the price is too high and cancels the order. Figure 17.14 depicts the dynamic creation and subsequent dynamic destruction of the order. 

1. Consider the lifelines in Figure 17.14 . When an object is active, this is denoted by a thin rectangle ( activation box ) in place of the dashed line. For example, the : Price Class 

FIGURE 17.14 A sequence diagram showing dynamic creation and destruction of an object, return, and explicit activation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-28/1d39870d-6b34-4267-a3b5-fc99e11720cc/d8bdba5ca3d5720ba743131bec3e2535c83a5db3cd186427cbaa0ef9cacbbb54.jpg)
