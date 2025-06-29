# Define attributes (must already exist in WooCommerce or be created via API)
from categories import Categories

image_url = "https://cranky.cranky.gr/wp-content/uploads/2025/06"
attributes = [
    {
        "name": "Size",
        "variation": True,
        "options": ["S", "M", "L"]
    },
    {
        "name": "Color",
        "variation": True,
        "options": ["Black", "White"]
    }
]
org_tee_description = f"""
<ul>
<li>185 g/m²</li>
<li>100% οργανικό βαμβάκι</li>
<li>Όλες οι αποχρώσεις είναι κατασκευασμένες από βαμβάκι σε μεταβατικό στάδιο προς τη βιολογική καλλιέργεια</li>
<li>Σωληνωτή πλέξη (χωρίς πλαϊνές ραφές)</li>
<li>Ίσια γραμμή</li>
<li>Στρογγυλή λαιμόκοψη με ριμπ ύφανση και διπλή ραφή</li>
<li>Επένδυση λαιμού με ταιριαστή ταινία</li>
<li>Διπλή ραφή στα μανίκια και στο στρίφωμα</li>
"""
# Sample products
products = [
    {
        "name": "Insufficient facts always invite danger",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "“Logic is only the beginning.” Inspired by Spock’s timeless wisdom, this eco-conscious tee is a salute to intellect, calm under pressure, and boldly going with style.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},  
            {"id": Categories.MOVIES},  
        ],
        "images": [{"src": f"{image_url}/81.jpg"}],
        "attributes": attributes
    },
    {
        "name": "You Have No Real Power",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Δεν έχεις καμία πραγματική δύναμη… μόνο αυτό που πιστεύουν οι άλλοι. Μια οικολογική μπλούζα εμπνευσμένη από το Wicked, για όσους ξέρουν ότι η αλήθεια πίσω από τη μαγεία δεν είναι πάντα αυτό που φαίνεται.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},  
            {"id": Categories.MOVIES},  
        ],
        "images": [
            {"src": f"{image_url}/1.jpg"},
            {"src": f"{image_url}/2.jpg"},
                   ],
        "attributes": attributes
    },
    {
        "name": "Fly you fools",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Αν ο Γκάνταλφ είχε T-shirt, θα φορούσε αυτό. Για ήρωες που τρέχουν από τον Μπαλρόγκ και δεν ξεχνούν να σώσουν τον πλανήτη με βιώσιμο στυλ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},  
            {"id": Categories.MOVIES},  
        ],
        "images": [
            {"src": f"{image_url}/8.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "I know what kind of God I Need to be",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Αυτή η μπλούζα είναι το χάος με στιλ — για θεούς που ξέρουν τι θέλουν.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},  
            {"id": Categories.MOVIES},  
        ],
        "images": [
            {"src": f"{image_url}/9.jpg"},
            {"src": f"{image_url}/90.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The flying donut",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Ο Homer πετάει ψηλά — χωρίς φανέλα, με ντόνατ στο χέρι και στυλ θρύλου. Μια μπλούζα για όσους αγαπούν το ακραίο και το αστείο, φτιαγμένη με 100% οργανικό βαμβάκι.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},  
            {"id": Categories.SERIES},  
        ],
        "images": [
            {"src": f"{image_url}/82.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "I can do this all day!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους δεν κουράζονται ποτέ… εκτός από όταν λείπει ο καφές. Και η μπλούζα; 100% οργανική, για ατελείωτο στυλ χωρίς ενοχές.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},  
            {"id": Categories.MOVIES},  
        ],
        "images": [
            {"src": f"{image_url}/3.jpg"},
            {"src": f"{image_url}/4.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The only crime in a war is to lose",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Το μόνο έγκλημα στον πόλεμο είναι να χάσεις — οπότε φρόντισε να φοράς σωστή πανοπλία (ή μπλούζα). Για όσους παίζουν σκληρά, αλλά ξέρουν και να το κάνουν με στιλ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},  
            {"id": Categories.SERIES},  
        ],
        "images": [
            {"src": f"{image_url}/5.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Do not be sorry, be better!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Μην ζητάς συγγνώμη, γίνε καλύτερος! Μπλούζα για όσους προτιμούν τις πράξεις αντί για λόγια — με στιλ και οικολογική συνείδηση.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.GAMES},
        ],
        "images": [
            {"src": f"{image_url}/91.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Bro Mitzva Requirements",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Bro Mitzvah: η ιερή μετάβαση από bro... σε legendary bro. Μπλούζα για σοβαρές τελετές, επικές φάρσες και όσους παίρνουν το bromance με στιλ — και οργανικό βαμβάκι.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/89.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "You Are A Loser, Eddie!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Είσαι ένας χαμένος… αλλά με φοβερό T-shirt! Για φωνές μέσα στο κεφάλι σου που έχουν άποψη — και οικολογική συνείδηση.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/36.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Tomorrow, HYDRA will stand as master of the world!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Αύριο κατακτούμε τον κόσμο. Σήμερα κάνουμε πρόβα με μπλούζα. Ιδανική για μυστικά σχέδια, κακές προθέσεις και καλές οικολογικές επιλογές.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/24.jpg"},
            {"src": f"{image_url}/25.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "You…You… Complete Me.",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Εσύ… εσύ… με ολοκληρώνεις. Και η μπλούζα επίσης. Για χαοτικούς ρομαντικούς, θεότρελες ισορροπίες και 100% οργανικό χάος με στιλ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/88.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "…and in the darkness bind them!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "…και στο σκοτάδι θα τους δέσει. Ή απλώς θα τραβήξει όλα τα βλέμματα. Μπλούζα για μυστηριώδεις ψυχές, σκοτεινή αισθητική και βιώσιμο στιλ που λάμπει από μόνο του.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/77.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Red man walking",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Red Man Walking: Όταν ο θυμός βγαίνει βόλτα. Μπλούζα για ήρεμους ανθρώπους… μέχρι να μην είναι. 100% οργανικό βαμβάκι για εκρήξεις με οικολογική συνείδηση.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/83.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Assemble!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όχι γιατί έχεις υπερδυνάμεις, αλλά γιατί κάποιος πρέπει να φέρει τους καφέδες. Μπλούζα για ηρωικές εμφανίσεις στο γραφείο ή το περίπτερο.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/84.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Call me Red!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν οι καλές προθέσεις δεν φτάνουν, η παρουσία σου μιλάει πιο δυνατά από λόγια — και η μπλούζα είναι 100% οργανική για να μην έχεις δικαιολογίες.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/34.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Welcome to the dark cloud",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Εκεί όπου οι σκέψεις γίνονται βαριές, το στυλ σκοτεινό και το οργανικό βαμβάκι... φωτεινό (για να μη σε πιάσουν στον ύπνο).",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/80.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Skeleton Brew",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους πίνουν σαν αθάνατοι — ή τουλάχιστον προσπαθούν. Μπλούζα για χαλαρές βραδιές και οργανικό στυλ χωρίς expiry date.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/13.jpg"},
            {"src": f"{image_url}/92.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "4 Touchdowns in 1 Game",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η μπλούζα για όσους ζουν μεγάλες στιγμές — στο μυαλό τους. Ιδανική για όσους ξέρουν να πουλάνε καλά τα παραμύθια τους.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/63.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Just Tails",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Δύο ουρές, διπλή φασαρία. Για όσους δεν φοβούνται να ξεχωρίσουν — ή να μπερδέψουν τα πάντα γύρω τους.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/55.jpg"},
            {"src": f"{image_url}/56.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "When life gives you lemons…",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Πάρε δύο ουρές, φτιάξε λεμονάδα και κάνε τους άλλους να αναρωτιούνται τι ακριβώς συμβαίνει. (Και να ζηλεύουν λίγο.)",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/53.jpg"},
            {"src": f"{image_url}/54.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The Dude",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους κινούνται με τη δική τους ταχύτητα — και προτιμούν να το κάνουν με στιλ και 100% οργανικό βαμβάκι.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/52.jpg"},
            {"src": f"{image_url}/51.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The Shadow",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Γιατί μερικές φορές το να είσαι ο κακός είναι απλώς πιο διασκεδαστικό — και τουλάχιστον η μπλούζα σου είναι 100% οργανική.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/59.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Now I am pissed",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν η υπομονή τελειώνει αλλά το στυλ δεν εγκαταλείπει ποτέ. Ιδανική μπλούζα για μέρες που θέλεις να το δείξεις... με οργανικό τρόπο.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/49.jpg"},
            {"src": f"{image_url}/50.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Leave me Alone",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν θες χώρο, αλλά όχι τόσο πολύ ώστε να χάσεις το στιλ σου. Ιδανική για ντροπαλούς με… οικολογική συνείδηση.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/47.jpg"},
            {"src": f"{image_url}/48.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "You fool…Away!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για τις στιγμές που η υπομονή τελειώνει, αλλά το στιλ παραμένει – κι ας φύγουν όλοι μακριά.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/61.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Morning, Losers!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η ιδανική μπλούζα για όσους ξυπνούν με διάθεση... να βάλουν τα πράγματα στη θέση τους — με χιούμορ και στυλ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/45.jpg"},
            {"src": f"{image_url}/46.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Nakatomi Towers",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν το γραφείο γίνεται πεδίο μάχης και εσύ απλώς προσπαθείς να βγεις ζωντανός — με στιλ που αντέχει κάθε έκρηξη.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/26.jpg"},
            {"src": f"{image_url}/27.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "There is a devil in this world, and I have met him.",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους γνωρίζουν πως το σκοτάδι δεν είναι απλώς μια λέξη — είναι εμπειρία.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/68.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Dimi, why you do this to me?",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν το χάος μπαίνει στο σπίτι και πρέπει να βρεις τον ένοχο — ακόμα κι αν είναι ο ίδιος σου ο εαυτός.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/28.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The Ghosts of our Children’s Future",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Μια υπενθύμιση ότι το μέλλον κουβαλάει τις σκιές του παρελθόντος — για όσους σκέφτονται πέρα από το τώρα.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/29.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Tribal",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν η αρχαία σοφία συναντά το μοντέρνο στιλ — ιδανική για ταξιδιώτες μεταξύ κόσμων.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.GAMES},
        ],
        "images": [
            {"src": f"{image_url}/72.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The Warrior",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους δεν υποχωρούν ποτέ — μαχητές με καρδιά και στιλ που ξεχωρίζει.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.GAMES},
        ],
        "images": [
            {"src": f"{image_url}/73.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Ocarina",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η μελωδία που ταξιδεύει μέσα στο χρόνο — για όσους αγαπούν να γράφουν τη δική τους ιστορία με κάθε νότα.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.GAMES},
        ],
        "images": [
            {"src": f"{image_url}/71.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Elements",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Φωτιά, νερό, γη και… λίγο χάος. Για όσους ξέρουν να παίζουν με τις δυνάμεις της φύσης χωρίς να καίνε το σπίτι.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.GAMES},
        ],
        "images": [
            {"src": f"{image_url}/21.jpg"},
            {"src": f"{image_url}/22.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Damage +2",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Γιατί λίγο παραπάνω πόνος δεν έβλαψε ποτέ κανέναν — ιδανικό για παίκτες που ξέρουν να χτυπάνε με στιλ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.GAMES},
        ],
        "images": [
            {"src": f"{image_url}/7.jpg"},
            {"src": f"{image_url}/86.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Health +1",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Μια μικρή δόση ζωής — για όσους ξέρουν ότι κάθε καρδιά μετράει… ακόμα και η πιο μικρή.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.GAMES},
        ],
        "images": [
            {"src": f"{image_url}/6.jpg"},
            {"src": f"{image_url}/93.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Blood is Life",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η παλιά αλήθεια που δεν ξεχνιέται — γιατί μερικές φορές η ζωή χτυπά με κόκκινο χρώμα.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/37.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Go Isotopes",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η ιδανική φανέλα για όσους στηρίζουν την πιο... ραδιενεργή ομάδα της πόλης.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/94.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The way of the spider",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους ζουν τη ζωή κρεμασμένοι ανάποδα — και πάντα τυλίγουν τα πράγματα σε… μπελάδες.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/74.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Super Someone",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για εκείνους που δεν ξέρουν τι κάνουν, αλλά το κάνουν με απίστευτο στυλ — ο ήρωας που όλοι χρειαζόμαστε (ή φοβόμαστε).",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/75.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "One batch, two batch, Penny, and Dime.",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν κάθε λεπτομέρεια μετράει και το παρελθόν δεν ξεχνιέται εύκολα.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/5.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Aaaaarggg!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η φωνή που βγαίνει όταν ακόμα και οι πιο δυνατοί δεν μπορούν να κρύψουν την απογοήτευσή τους.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/16.jpg"},
            {"src": f"{image_url}/17.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "I am but a Humble Servant",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν κάνεις ό,τι σου λένε… αλλά μέσα σου ξέρεις ότι έχεις ήδη κάνει όλη τη δουλειά.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/95.jpg"},
            {"src": f"{image_url}/96.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Suit-Up!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν ο σκοτεινός άρχοντας αποφασίζει ότι η ισχύς χρειάζεται και στυλ — επίσημος τρόπος καταστροφής.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/18.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Keep Calm",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για εκείνες τις στιγμές που προσπαθείς να λύσεις τα ίδια προβλήματα ξανά και ξανά — αλλά τουλάχιστον το κάνεις με στυλ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/97.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Trig is easy!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους ξέρουν ότι η μόνη γωνία που μετράει είναι αυτή που σε κάνει να πετύχεις.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SCIENCE},
        ],
        "images": [
            {"src": f"{image_url}/10.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Science mumbo jumbo",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους αγαπούν να πετούν δύσκολες λέξεις, χωρίς να καταλαβαίνουν και πολλά — αλλά πάντα με στυλ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SCIENCE},
        ],
        "images": [
            {"src": f"{image_url}/11.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Physics is hard",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους ξέρουν ότι μερικές φορές οι νόμοι της φύσης απλά δεν κάνουν διακρίσεις.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SCIENCE},
        ],
        "images": [
            {"src": f"{image_url}/12.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "I’ve got a bad feeling about this.",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους ξέρουν ότι μερικές φορές οι νόμοι της φύσης απλά δεν κάνουν διακρίσεις.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/14.jpg"},
            {"src": f"{image_url}/15.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Engineer’s Manual",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Οδηγός χρήσης για όσους πιστεύουν ότι ένα μικρό σφάλμα δεν καταστρέφει το σύμπαν... μέχρι να το κάνει.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/19.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "I am not Kitten",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όχι απλό γατάκι — η φωτιά που καίει... μέχρι να την πνίξεις με νερό.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/98.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The Little One",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Μικρός στο μέγεθος, αλλά έτοιμος να ταράξει τα νερά… ή τουλάχιστον να προσπαθήσει.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/38.jpg"},
            {"src": f"{image_url}/39.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Turtle Sage",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η σοφία που κινείται με αργούς ρυθμούς — γιατί οι καλύτερες απαντήσεις έρχονται στο χρόνο τους.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/60.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Enlightenment",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η διαδρομή προς τη γνώση και την εσωτερική γαλήνη — ένα βήμα τη φορά.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/67.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Ultra Mode",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν ξυπνάς και αποφασίζεις να αφήσεις τους άλλους να προσπαθούν... από μακριά.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/99.jpg"},
            {"src": f"{image_url}/100.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "So I Hate To Say It…",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν πρέπει να πεις την αλήθεια, ακόμα κι αν κανείς δεν θέλει να την ακούσει.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/62.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The Path to Enlightenment",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Μια διαδρομή γεμάτη προκλήσεις, όπου κάθε βήμα φωτίζει την επόμενη στροφή.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/101.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "KA-ME-HA-ME-HAAA !!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η κραυγή που ξυπνάει ήρωες… ή απλά ξεσηκώνει τον καναπέ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/69.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "The Way of the Sword",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η τέχνη που απαιτεί υπομονή, αποφασιστικότητα και λίγο... χάος.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/103.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Dream Pagoda",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Ένα ταξίδι σε κόσμους ονείρων όπου η παράδοση συναντά τη φαντασία.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/102.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "RIP C3PO",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν το πιο πολύγλωσσο ρομπότ αποφασίζει να κάνει διακοπές... για πάντα.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/79.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "C3P what?!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν δεν είσαι σίγουρος αν είσαι ρομπότ ή απλά μπερδεύεσαι με τις οδηγίες.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/78.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Dragon's balls",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν ψάχνεις την τύχη, αλλά βρίσκεις απλώς πολλές… εκπλήξεις.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/40.jpg"},
            {"src": f"{image_url}/41.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Never quit gaming",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Για όσους ξέρουν ότι το παιχνίδι συνεχίζεται… ακόμα κι όταν όλα πάνε στραβά.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
        ],
        "images": [
            {"src": f"{image_url}/57.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "F**k the avengers",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν η “τελική ελπίδα της ανθρωπότητας” μοιάζει περισσότερο με ομαδική σύγχυση.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/31.jpg"},
            {"src": f"{image_url}/32.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Little grootie pie",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Μικρό, πράσινο και με attitude — το φυτό που δεν θέλει πότισμα, μόνο χειροκρότημα.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/30.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Han wanted, dead or alive",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Καταζητείται για υπερβολικό αυτοπεποίθηση, κακή στάθμευση και ατάκες που δεν τελειώνουν ποτέ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/23.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Juan Cholo",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Όταν ρίχνεις ατάκες στο διάστημα… αλλά κανείς δεν γελάει.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/20.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "Private!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Ο πιο γλυκός της ομάδας, μέχρι να του πει κάποιος ότι δεν είναι στρατός εδώ.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/35.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "I am the Iron dude!",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Μισός μέταλλο, μισός εγωισμός, 100% άποψη. Μην του πεις να φορτίσει… το ξέρει ήδη.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/70.jpg"},
        ],
        "attributes": attributes
    },
    {
        "name": "I will catch them all",
        "type": "simple",
        "regular_price": "18.00",
        "description": org_tee_description,
        "short_description": "Η μπάλα που υπόσχεται περιπέτεια, αλλά κυλάει κάτω από τον καναπέ όταν τη χρειάζεσαι περισσότερο.",
        "status": "publish",
        "categories": [
            {"id": Categories.T_SHIRTS},
            {"id": Categories.SERIES},
            {"id": Categories.MOVIES},
        ],
        "images": [
            {"src": f"{image_url}/64.jpg"},
        ],
        "attributes": attributes
    }
]
