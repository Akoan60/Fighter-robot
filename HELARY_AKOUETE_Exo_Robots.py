#Exercice 5 : Robots

#Cette fonction permet de commencer la simulation, de décrire un peu le fonctionnement de celle_ci
def presentation_programme():
    print("Salut ! Je me présente, je suis CynoBot ! Je suis là pour te guider dans cette simulation de monde habité par des robots.")
    print("Pour cette simulation je te propose de te glisser dans la peau de l'un d'entre nous.")
    print("Choisis ton nom de robot :")
    nom = input()
    print("Waw ! Très bon choix, j'aime beaucoup. Alors bienvenu parmi nous {} !".format(nom))
    print("Maintenant tu vas devoir choisir ta fonction. Il y a les médecins, les soldats ou les hybrides qui sont à la fois soldats et médecins.")
    return choix_fonction(nom)
    
#Cette fonction gère le choix de la focntion/competence souhaité par le joueur        
def choix_fonction(nom_choisi):
    print("Tape 1 pour être médecin, 2 pour être soldat et 3 pour être hybride :")
    fonction = input()
    if (fonction == "1"):
        personnage = Medecin(nom_choisi)
    elif (fonction == "2"):
        personnage = Soldat(nom_choisi)
    elif (fonction == "3"):
        personnage = Hybride(nom_choisi)
    else:
        print("Il semble que ton choix ne soit pas correct ...")
        choix_fonction(nom_choisi)
    if type(personnage) is Hybride :
        print("Super te voilà maintenant dans la peau d'un robot {} equipé d'un(e) {} et d'un(e) {} !".format(personnage.competence, personnage.arme.nom, personnage.soin.nom))
        return personnage
    elif type(personnage) is Medecin :
        print("Super te voilà maintenant dans la peau d'un robot {} equipé d'un(e) {} !".format(personnage.competence, personnage.soin.nom))
        return personnage
    elif type(personnage) is Soldat :
        print("Super te voilà maintenant dans la peau d'un robot {} equipé d'un(e) {} !".format(personnage.competence, personnage.arme.nom))
        return personnage

#Cette classe permet de créer des Objets         
class Objet():
    #Constructeur de la classe Objet
    def __init__(self, nom, puissance):
        self. nom = nom
        self.puissance = puissance
        
#Cette classe permet de créer des Armes (elle hérite de la classe Objet)
class Arme(Objet):
    #Constructeur de la classe Arme
    def __init__(self, nom = "bâton", puissance = 2):
        Objet.__init__(self, nom, puissance)

#Cette classe permet de créer des Soins (elle hérite de la classe Objet)
class Soin(Objet):
    #Constructeur de la classe Soin
    def __init__(self, nom  = "pansement", puissance  = 2):
        Objet.__init__(self, nom, puissance)
    
#Cette classe permet de créer des Robots
class Robot():
    seuil_critique_vie = 30
    #Constructeur de la classe Robot
    def __init__(self, nom, competence, niv_vie = 100):
        self.nom = nom
        self.competence = competence
        self._niv_vie = niv_vie
    #Getter pour l'attribut niv_vie    
    def get_niv_vie(self):
        return self._niv_vie
    #Setter pour l'attribut niv_vie
    def set_niv_vie(self, valeur):
        if valeur > 100 :
            print("Impossible, votre niveau de vie doit être compris être 0 et 100 inclus")
        elif valeur < 0 :
            self._niv_vie = 0
        else :
            self._niv_vie = valeur
    niv_vie = property(get_niv_vie, set_niv_vie)
    #Cette méthode permet à un robot de se présenter
    def se_presenter(self):
        print("Salut ! Je suis {} et je suis un {} !".format(self.nom, self.competence))
            
#Cette classe permet de créer des robots soldats (elle hérite de la classe Robot)
class Soldat(Robot):
    #Constructeur de la classe Soldat
    def __init__(self, nom, arme = Arme(), force = 20, niv_vie = 100, competence = "soldat"):
        Robot.__init__(self, nom, competence, niv_vie)
        self._force = force
        self.arme = arme
    #Getter pour l'attribut force     
    def get_force(self):
        return self._force 
    #Setter pour l'attribut force
    def set_force(self, valeur):
        if valeur >=80 :
            print("Impossible la force est trop élevée.")
        else:
            self._force = valeur      
    force = property(get_force,set_force)
    #Cette méthode permet à un robot soldat d'attaquer un autre robot    
    def attaquer(self, robot_attaque):
        print("{} : Aaaaaaaa l'attaaaaaaaque !".format(self.nom))
        robot_attaque.niv_vie = robot_attaque.niv_vie - (self._force + self.arme.puissance)
        print("{} : Aie !".format(robot_attaque.nom))
        if robot_attaque.niv_vie <= 0 :
            print("{} : Je me meurs ...".format(robot_attaque.nom))
    #Cette méthode permet à un robot soldat d'échanger son arme avec un autre robot possédant aussi une arme        
    def echangerArme(self, robot):
        if (type(robot) is Soldat or type(robot) is Hybride):
            temp = self.arme
            self.arme = robot.arme
            robot.arme = temp
            print("{} : Je possède maintenant {}.".format(self.nom, self.arme.nom))
        else :
            print("Impossible d'échanger une arme avec ce robot car il n'en possède pas ...")
    #Cette méthode permet à un robot soldat de se présenter
    def se_presenter(self):
        super(Soldat, self).se_presenter()
        print("{} : Fais attention à toi ! Je peux te botter les fesses avec mon(ma) {} !".format(self.nom,self.arme.nom))     

#Cette classe permet de créer des robots médecins (elle hérite de la classe Robot)
class Medecin(Robot):
    #Constructeur de la classe Medecin
    def __init__(self, nom, soin = Soin(), guerison = 10, niv_vie = 100, competence = "medecin"):
        Robot.__init__(self, nom, competence, niv_vie)
        self._guerison = guerison
        self.soin = soin
    #Getter pour l'attribut guerison    
    def get_guerison(self):
        return self._force 
    #Setter pour l'attribut guerison
    def set_guerison(self, valeur):
        if valeur >=80 :
            print("Impossible la puissance de guérison est trop élevée.")
        else:
            self._guerison = valeur          
    guerison = property(get_guerison,set_guerison)
    #Cette méthode permet à un robot médecin de soigner un autre robot étant dans le besoin   
    def soigner(self, robot_soigne):
        if robot_soigne.niv_vie <= Robot.seuil_critique_vie :
            print("{} : Je crois que tu as besoin d'aide je vais t'aider ;)".format(self.nom))
            robot_soigne.niv_vie = robot_soigne.niv_vie + self.guerison
            print("{} : Merci beaucoup {} !".format(robot_soigne.nom, self.nom))
        else:
            print("{} : Tu n'as pas encore besoin de mon aide, courage !".format(self.nom))
    #Cette méthode permet à un robot médecin d'échanger son soin avec un robot possédant lui aussi un soin       
    def echangerSoin(self, robot):
        if (type(robot) is Medecin or type(robot) is Hybride):
            temp = self.soin
            self.soin = robot.soin
            robot.soin = temp
            print("{} : Je possède maintenant {}.".format(self.nom, self.soin.nom))
        else :
            print("Impossible d'échanger un soin avec ce robot car il n'en possède pas ...")
    #Cette méthode permet çà un robot médecin de se présenter
    def se_presenter(self):
        super(Medecin, self).se_presenter()
        print("{} : Si tu as besoin de soins je suis là, n'hésite pas surtout ! Je peux t'aider avec mon(ma) {}".format(self.nom, self.soin.nom))    
        
        
#Cette classe permet de créer des robots hybrides (à la fois soldat et médecin)
class Hybride(Soldat, Medecin):
    #Constructeur de la classe Hybride
    def __init__(self, nom, arme = Arme(), soin = Soin(), force = 10, guerison = 5, competence = "hybride", niv_vie = 100):
        Soldat.__init__(self, nom, arme, force, niv_vie, competence)
        Medecin.__init__(self, nom, soin, guerison, niv_vie, competence)
    #Cette méthode permet à un robot hybride de se présenter    
    def se_presenter(self):
        super(Hybride, self).se_presenter()
        print("{} : Je suis un peu bipolaire ... donc fais attention tout de même à ce que tu risques ...".format(self.nom))

#Cette méthode permet de vérifier si un robot est mort ou vivant
def check_statut(robot):
    if (robot.niv_vie == 0):
        print("{} est mort :(".format(robot.nom))
    else:
        print("{} est toujours vivant! Il a {:d} hp".format(robot.nom,robot.niv_vie))
               
#Création d'une base d'objets et de robots
arme_epee = Arme("epee",5)
arme_hache = Arme("hache", 10)
arme_poignard = Arme("poignard", 3)
soin_bandage = Soin("bandage", 5)
soin_antibiotique = Soin("antibiotique", 10)
soin_miracle = Soin("miracle", 30)
robot_soldat_1 = Soldat("Wally",arme_epee, 30)
robot_soldat_2 = Soldat("Jarvis",arme_hache,20)
robot_soldat_3 = Soldat("Friday",arme_poignard,15)
robot_medecin_1 = Medecin("Xeno", soin_bandage, 25)
robot_medecin_2 = Medecin("Eric")
robot_hybride_1 = Hybride("Miko", arme_hache, soin_antibiotique)


#Lancement de la simulation
personnage = presentation_programme()

if type(personnage) is Soldat:
    robot_soldat_1.se_presenter()
    personnage.attaquer(robot_soldat_1)
    check_statut(robot_soldat_1)
    if (robot_soldat_1.niv_vie > 0):
        robot_medecin_2.soigner(robot_soldat_1)
        print("{} : Prepare toi à ma contre-attaque".format(robot_soldat_1.nom))
        robot_soldat_1.attaquer(personnage)
    else:
        print("Le meilleur c'est moi ! {} !".format(personnage.nom))
elif type(personnage) is Medecin:
    print("Un combat se prépare !")
    robot_soldat_1.se_presenter()
    robot_soldat_2.se_presenter()
    robot_soldat_1.echangerArme(robot_soldat_2)
    robot_soldat_1.attaquer(robot_soldat_2)
    check_statut(robot_soldat_2)
    if robot_soldat_2.niv_vie > 0:
        robot_soldat_2.attaquer(robot_soldat_1)
        check_statut(robot_soldat_1)
        if robot_soldat_2.niv_vie >= robot_soldat_1.niv_vie:
            personnage.soigner(robot_soldat_1)
elif type(personnage) is Hybride:
    robot_soldat_2.se_presenter()
    robot_soldat_2.attaquer(personnage)
    check_statut(personnage)
    if robot_soldat_2.niv_vie > 0:
        personnage.soigner(robot_soldat_2)