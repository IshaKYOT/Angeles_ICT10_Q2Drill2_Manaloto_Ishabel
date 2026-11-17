
from pyscript import document

grade7 = {
    "Taiga Naguit",
    "Mark Herringbonia",
    "Sean Espiritu",
    "Montano Mercado"
}

grade8 = {
    "Tipany Wilson",
    "Garcia Cristobal",
    "Ethan Beranes",
    "Taylor Swift"
}

grade9 = {
    "Hans Lee",
    "Martina Louise",
    "Paula Sabrina",
    "Aubrey Cabrera"
}

grade10 = {
    "Fabon Dumandan",
    "Majuko Hashimo",
    "Ishakyot Manaloto",
    "Punay Punlas"
}

new_members = set()


def add_member(event):

    first = document.getElementById("first_name").value.strip().title()
    last = document.getElementById("last_name").value.strip().title()

    full_name = first + " " + last

    new_members.add(full_name)

    all_members = grade7 | grade8 | grade9 | grade10 | new_members

    member_list = "<br>".join(sorted(all_members))

    total = len(all_members)
    document.getElementById("output").innerHTML = f"""
        <div class="pink-box">
            <strong>All Members:</strong>
            <br><br>
            {member_list}
            <hr>
            <strong>Total Members: {total}</strong>
        </div>
    """
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
