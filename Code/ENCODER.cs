u s i n g   S y s t e m ; 
 
 u s i n g   S y s t e m . I O ; 
 
 u s i n g   S y s t e m . C o l l e c t i o n s . G e n e r i c ; 
 
 n a m e s p a c e   T e s t O f C i p h e r F o r E P 
 
 { 
 
 	 c l a s s   M a i n C l a s s 
 
 	 { 
 
 	 	 p u b l i c   s t a t i c   L i s t < s t r i n g >   t o N u m b e r s ( s t r i n g   i ) 
 
 	 	 { 
 
 	 	 	 L i s t < s t r i n g >   f i n a l   =   n e w   L i s t < s t r i n g > ( ) ; 
 
 	 	 	 f o r   ( i n t   j   =   0 ;   j   <   i . L e n g t h ;   j + + ) 
 
 	 	 	 { 
 
 	 	 	 	 i f   ( i   [ j ]   = =   ' \ 0 ' )   { 
 
 	 	 	 	 	 f i n a l . A d d   ( C o n v e r t . T o S t r i n g ( i   [ j ] ) ) ; 
 
 	 	 	 	 }   e l s e   { 
 
 	 	 	 	 	 f i n a l . A d d   ( C o n v e r t . T o S t r i n g   ( C o n v e r t . T o I n t 3 2   ( i   [ j ] ) ) ) ; 
 
 	 	 	 	 } 
 
 	 	 	 } 
 
 	 	 	 r e t u r n   f i n a l ; 
 
 	 	 } 
 
 	 	 p u b l i c   s t a t i c   v o i d   M a i n   ( s t r i n g [ ]   a r g s ) 
 
 	 	 { 
 
 / / 	 	 	 # d e f i n e   p r o d u c t N u m b e r   1 0 1 1 
 
 / / 	 	 	 u s i n g   ( S t r e a m W r i t e r   w r i t e r   =   n e w   S t r e a m W r i t e r   ( " i . t x t " ) )   { 
 
 / / 	 	 	 	 f o r   ( i n t   i   =   3 3 ;   i   <   1 0 0 0 0 ;   i + + )   { 
 
 / / 	 	 	 	 	 i f   ( i   >   1 2 6   & &   i   <   1 6 0 )   { 
 
 / / 	 	 	 	 	 	 i   =   1 6 1 ; 
 
 / / 	 	 	 	 	 } 
 
 / / 	 	 	 	 	 C o n s o l e . W r i t e L i n e   ( " I :   "   +   i   +   " \ t "   +   ( c h a r ) i ) ; 
 
 / / 	 	 	 	 	 w r i t e r . W r i t e L i n e   ( " I :   "   +   i   +   " \ t "   +   ( c h a r ) i ) ; 	 	 	 
 
 / / 	 	 	 	 } 
 
 / / 	 	 	 } 
 
 / / / / 	 	 	 C o n s o l e . R e a d L i n e   ( ) ; 
 
 / / / / 	 	 	 	 w h i l e   ( C o n v e r t . T o I n t 3 2   ( C o n s o l e . R e a d L i n e   ( ) )   ! =   0 )   { 
 
 / / / / 	 	 	 	 	 C o n s o l e . W r i t e L i n e   ( " H e l l o   W o r l d ! " ) ; 
 
 / / / / 	 	 	 	 	 c h a r   i n p u t   =   C o n s o l e . R e a d L i n e   ( )   [ 0 ] ; 
 
 / / / / 	 	 	 	 	 i n t   i n p u t O f C i p h e r D i s t a n c e   =   C o n v e r t . T o I n t 3 2   ( C o n s o l e . R e a d L i n e   ( ) ) ; 
 
 / / / / 	 	 	 	 	 i n t   i n p u t C o m v e r t e d   =   C o n v e r t . T o I n t 3 2   ( i n p u t ) ; 
 
 / / / / 	 	 	 	 	 C o n s o l e . W r i t e L i n e   ( " \ t "   +   i n p u t C o m v e r t e d ) ; 
 
 / / / / 	 	 	 	 	 i n t   f i n a l   =   i n p u t C o m v e r t e d   +   i n p u t O f C i p h e r D i s t a n c e ; 
 
 / / / / 	 	 	 	 	 C o n s o l e . W r i t e L i n e   ( ( c h a r ) f i n a l ) ; 
 
 / / / / 	 	 	 	 } 
 
 	 	 	 u s i n g   ( S t r e a m W r i t e r   w r i t e r   =   n e w   S t r e a m W r i t e r   ( " i . t x t " ) )   { 
 
 	 	 	 	 C o n s o l e . W r i t e L i n e   ( " E n t e r   S e r i a l   N u m b e r " ) ; 
 
 	 	 	 	 s t r i n g   i n p u t   =   C o n s o l e . R e a d L i n e   ( ) ; 
 
 	 	 	 	 	 C o n s o l e . W r i t e L i n e   ( " E n t e r   n a m e   o f   t h e   a c c o u n t " ) ; 
 
 	 	 	 	 	 s t r i n g   a c c o u n t   =   C o n s o l e . R e a d L i n e   ( ) ; 
 
 	 	 	 	 	 C o n s o l e . W r i t e L i n e   ( " E n t e r   u s e r n a m e " ) ; 
 
 	 	 	 	 	 s t r i n g   u s e r n a m e   =   C o n s o l e . R e a d L i n e   ( ) ; 
 
 	 	 	 	 	 C o n s o l e . W r i t e L i n e   ( " E n t e r   p a s s w o r d " ) ; 
 
 	 	 	 	 	 s t r i n g   p a s s w o r d   =   C o n s o l e . R e a d L i n e   ( ) ; 
 
 	 	 	 	 	 s t r i n g   c o m b i n e d   =   a c c o u n t   +   C o n v e r t . T o C h a r   ( 0 )   +   u s e r n a m e   +   C o n v e r t . T o C h a r   ( 0 )   +   p a s s w o r d ; 
 
 	 	 	 	 	 L i s t < s t r i n g >   c o m b i n e d T o N u m b e r s   =   t o N u m b e r s   ( c o m b i n e d ) ; 
 
 	 	 	 	 	 L i s t < s t r i n g >   d u p l i c a t e d   =   c o m b i n e d T o N u m b e r s ; 
 
 	 	 	 	 	 L i s t < s t r i n g >   o u t p u t N u m b e r   =   n e w   L i s t < s t r i n g >   ( ) ; 
 
 	 	 	 	 	 i n t   p l a c e T o   =   i n p u t . L e n g t h   -   1 ; 
 
 	 	 	 	 	 i n t   c o u n t e r 2   =   0 ; 
 
 	 	 	 	 	 i n t   c o u n t e r   =   0 ; 
 
 	 	 	 	 	 w h i l e   ( c o u n t e r   <   c o m b i n e d T o N u m b e r s . C o u n t )   { 
 
 	 	 	 	 	 	 i f   ( c o u n t e r 2   >   p l a c e T o )   { 
 
 	 	 	 	 	 	 	 c o u n t e r 2   =   0 ; 
 
 	 	 	 	 	 	 	 p l a c e T o - - ; 
 
 	 	 	 	 	 	 } 
 
 	 	 	 	 	 	 / / d e a l i n g   w i t h   c o m b i n e d [ c o u n t e r ] 
 
 	 	 	 	 	 	 / / w i t h s e r i a l c o u n t e r 2 
 
 	 	 	 	 	 	 i f   ( c o m b i n e d T o N u m b e r s [ c o u n t e r ] [ 0 ]   = =   ' \ 0 ' )   { 
 
 	 	 	 	 	 	 	 o u t p u t N u m b e r . A d d   ( C o n v e r t . T o S t r i n g ( c o m b i n e d T o N u m b e r s   [ c o u n t e r ] ) ) ; 
 
 	 	 	 	 	 	 }   e l s e   { 
 
 	 	 	 	 	 	 	 i n t   f i n a l   =   ( i n t ) i n p u t   [ c o u n t e r 2 ]   +   C o n v e r t . T o I n t 3 2 ( c o m b i n e d T o N u m b e r s   [ c o u n t e r ] ) ; 
 
 	 	 	 	 	 	 	 i f   ( f i n a l   > =   1 2 7 )   { 
 
 	 	 	 	 	 	 	 	 f i n a l   =   f i n a l   +   3 4 ; 
 
 	 	 	 	 	 	 	 } 
 
 	 	 	 	 	 	 	 o u t p u t N u m b e r . A d d   ( C o n v e r t . T o S t r i n g   ( f i n a l ) ) ; 
 
 	 	 	 	 	 	 } 
 
 	 	 	 	 	 	 c o u n t e r 2 + + ; 
 
 	 	 	 	 	 	 c o u n t e r + + ; 
 
 	 	 	 	 	 } 
 
 	 	 	 	 	 s t r i n g   C o n v e r t i n g T o R e a l   =   " " ; 
 
 	 	 	 	 	 f o r   ( i n t   k   =   0 ;   k   <   o u t p u t N u m b e r . C o u n t ;   k + + )   { 
 
 	 	 	 	 	 	 i f   ( o u t p u t N u m b e r [ k ] [ 0 ]   = =   ' \ 0 ' )   { 
 
 	 	 	 	 	 	 	 C o n v e r t i n g T o R e a l   =   C o n v e r t i n g T o R e a l   +   C o n v e r t . T o S t r i n g   ( C o n v e r t . T o C h a r   ( 0 ) ) ; 
 
 	 	 	 	 	 	 }   e l s e   { 
 
 	 	 	 	 	 	 	 i n t   t e m p   =   C o n v e r t . T o I n t 3 2   ( o u t p u t N u m b e r   [ k ] ) ; 
 
 	 	 	 	 	 	 	 C o n v e r t i n g T o R e a l   =   C o n v e r t i n g T o R e a l   +   C o n v e r t . T o C h a r   ( t e m p ) ; 
 
 	 	 	 	 	 	 } 
 
 	 	 	 	 	 } 
 
 	 	 	 	 	 C o n s o l e . W r i t e L i n e   ( C o n v e r t i n g T o R e a l   +   "   L e n g t h   =   "   +   C o n v e r t i n g T o R e a l . L e n g t h ) ; 
 
 	 	 	 	 	 i n p u t   =   C o n s o l e . R e a d L i n e   ( ) ; 
 
 	 	 	 	 	 w r i t e r . W r i t e   ( C o n v e r t i n g T o R e a l ) ; 
 
 
 
 	 	 	 } 
 
 	 	 } 
 
 
 
 	 } 
 
 } 
 
 