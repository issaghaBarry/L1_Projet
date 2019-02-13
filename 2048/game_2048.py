
DIRECTIONS = { "right" : (1,0), "left" : (-1,0), "up" : (0,-1), "down" : (0,1) }
l=[[1,3,2,4],[8,1,2,9],[5,2,6,8],[5,8,10,4]]
from random import *



##########################FONCTION INTERMEDIAIRE################################
def get_new_position (grid):
    """
    Paramètre: (list) representant une grille
    Valeur renvoyé: (tuple) representant une case vide
    """
    list_vid=[]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='':
                list_vid.append((i,j))
    if len(list_vid)!=0:
        return list_vid[randint(0,len(list_vid)-1)]


def get_new_tile ():
    """
    Paramètre: aucun
    Valeur renvoyé: (int) un deux ou un quatre d'après que les deux sont plus frequent que les quatres
    """
    k=randint(0,100)
    if 0<=k<=85:
        return '2'
    else:
        return '4'
    


def grid_get_value(grid,i,j):
    """
    Paramètre: (list) representant une grille
    Paramètre: (int) i representant la colonne et j (int) representant la ligne
    Valeur renvoyé: (int) representant la valeur de la cellule de coordonnée i ,j
    """
    if grid[i][j]=='':
        return 0
    else:
        return int(grid[i][j])




def grid_get_next(grid, i, j, d):
    """
    """
    if j+DIRECTIONS[d][0]>3 or j+DIRECTIONS[d][0]<0 or i+DIRECTIONS[d][1]<0 or i+DIRECTIONS[d][1]>3:
        return None
    else:
        return (i+DIRECTIONS[d][1],j+DIRECTIONS[d][0])
    
def carre(k):
    """
    """
    cpt=1
    aux=k
    while aux//2!=1:
        aux= aux//2
        cpt+=1
    return cpt


################################FONCTION PRINCIPALE#################################        

var= { 2:'H', 4:'He', 8:'Li', 16:'Be', 32:'B', 64:'C', 128:'N', 256:'O', 512:'F', 1024:'Ne', 2048:'Na'}




def grid_init():
    """
    Paramètre: aucun
    Valeur renvoyé: (list) généré chaque fois avec deux nombres a l'interieur dans des positions differentes soit des 2 ou des 4
    """
    l=[['','','',''],['','','',''],['','','',''],['','','','']]
    for k in range(2):
        casevide=get_new_position(l)
        i, j= casevide
        l[i][j]= get_new_tile()
    return l
    
def grid_print(grid, theme= 'entier'):
    """
    Paramètre: (list) une liste de liste representant les grilles du tableau
    valeur renvoyé: une grille contenant tout les elements de la liste mise en parametre
    """
    grid1=[e.copy() for e in grid]
    size=0
    if theme== 'entier':
        size= int(grid_get_max_value(grid1))
        len_str_size= len(str(size))
    elif theme== 'chimie':
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid1[i][j]!= '':
                    grid1[i][j]= var[int(grid1[i][j])]
                if grid1[i][j]!='' and len(grid1[i][j])>size:
                    size= len(grid1[i][j])
        len_str_size= size                  
    s="{:^"+str(len_str_size)+"}"
    print(('-'*(len_str_size+1))*4+'-')           #
    for line in grid1:
        print((("|"+s)*4).format(*line)+"|")
        print(('-'*(len_str_size+1))*4+'-')
        

def grid_get_max_value(grid):
    """
    Paramètre: (list) liste de liste representant une grille
    valeur renvoyé: (int) la valeur maximal de cette liste de liste

    Exemple:grid=[[2,2,'',4],[8,16,2,''],[2,2,'',4],[2,2,'',4]]
    
    """
    grid1=[i.copy() for i in grid]
    aux=0
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if grid1[i][j]!='' and int(grid1[i][j])>aux:
                aux=int(grid[i][j])
    return aux
        

def grid_move(grid, order):
    """
    paramètre: (list) une liste de liste
    paramètre: (str) une chaine representant un ordre
    Valeur renvoyé: (list) liste de liste avec la direction et la sommation demande
    """
    DIRECTION = { "right" : [(0,4,1),(2,-1,-1)], "left" : [(0,4,1),(1,4,1)], "up" : [(1,4,1),(0,4,1)], "down" : [(2,-1,-1),(0,4,1)] }
    d = True
    grid1=[i.copy() for i in grid]
    i1, i2, pas1=DIRECTION[order][0]                     #les differentes initialisation et arret des lignes selon l'ordre croissant ou decroissant
    j1, j2, pas2=DIRECTION[order][1]                     #les differentes initialisation et arret des colonne selon l'ordre coissant ou decroissant
    while d:
        d=False
        for i in range(i1,i2,pas1):
            i_d=i+DIRECTIONS[order][1]                                 # pour connaitre si on doit ajouté ou echanger avec celui d'avant ou d'apres
            for j in range(j1, j2, pas2):
                j_d=j+DIRECTIONS[order][0]
                if grid1[i][j]!='' and grid1[i_d][j_d]=='':
                    grid1[i_d][j_d], grid1[i][j]=grid1[i][j], grid1[i_d][j_d]      #echanger celui d'avant ou d'apres 
                    d=True
    for i in range(i1,i2,pas1):
        i_d=i+DIRECTIONS[order][1]                                 # pour connaitre si on doit ajouté ou echanger avec celui d'avant ou d'apres
        for j in range(j1, j2, pas2):
            j_d=j+DIRECTIONS[order][0]
            if grid1[i][j]!='' and grid1[i_d][j_d]!='':
                if grid1[i][j]==grid1[i_d][j_d]:
                    grid1[i_d][j_d], grid1[i][j]=str(int(grid1[i][j])+int(grid1[i_d][j_d])), ''
    c=True
    while c:
        c=False
        for i in range(i1,i2,pas1):
            i_d=i+DIRECTIONS[order][1]                                 # pour connaitre si on doit ajouté ou echanger avec celui d'avant ou d'apres
            for j in range(j1, j2, pas2):
                j_d=j+DIRECTIONS[order][0]
                if grid1[i][j]!='' and grid1[i_d][j_d]=='':
                    grid1[i_d][j_d], grid1[i][j]=grid1[i][j], grid1[i_d][j_d]      #echanger celui d'avant ou d'apres 
                    c=True
    return grid1   
        


def grid_add_new_tile(grid):
    """
    Paramètre: (list) liste de liste representant une grille
    valeur renvoyé: (list) liste de liste juste il ajoute 
    """
    try:                                              #On essaye de voir si on peut ajouté une valeur 
        ligne, colonne= get_new_position(grid)
        grid[ligne][colonne] = str(get_new_tile())
    except TypeError:                                #dans le cas ou on ne peut pas ajouté une valeur alors on nous renvoie l'ancienne grille
        grid=grid


def is_grid_over(grid):
    """
    Paramètre: (list) representant une grille
    Valeur renvoyé: booléen d'apres lequel si oui ou non le jeu est fini
    """
    grid1=[i.copy() for i in grid]
    if grid_get_max_value(grid1)>= 2048:
        return True
    elif grid_get_max_value(grid1)< 2048 and get_new_position(grid1)!=None:
        return False
    elif get_new_position(grid1)==None:
        return all([grid_move(grid1, e)==grid for e in DIRECTIONS])

        
        
################################CALCUL DE SCORE###############################

def grid_score(grid):
    """
    Paramètre: (list) une liste de liste representant une grille
    Valeur renvoyé: (int) representant la somme de toute les tuiles presente dans la grille 
    """
    som=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            som+=grid_get_value(grid,i,j)
    return som





#######################ENREGISTREMENT D'UNE PARTIE EN COURS####################

def grid_save(grid, fname):
    """
    Paramètre: grid (list) representant une grille
    Paramètre: (str) representant un nom de fichier
    """
    with open (fname, 'w', encoding='utf_8') as sortie:
        sortie.writelines([str(e)+'\n' for l in grid for e in l])


def grid_load(fname):
    """
    """
    with open(fname, 'r', encoding= 'utf_8') as entre:
        contenue= entre.readlines()
    l1=[]
    l2=[]
    for e in contenue:
        e1=e.rstrip('\n')
        l1.append(e1)
        if len(l1)==4:
            l2.append(l1)
            l1=[]
    return l2


#########################FAIRE JOUER L'ORDINATEUR###############################


    









