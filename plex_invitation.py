import argparse
from plexapi.server import PlexServer
from send_mail import send_email
from config import PLEX_TOKEN, PLEX_SERVER_URL, SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT, EMAIL_SENDER

def send_plex_invitation(user_email):
    try:
        # Authenticate with Plex using the token
        plex = PlexServer(PLEX_SERVER_URL, PLEX_TOKEN)

        # Invite the user
        invite = plex.myPlexAccount().inviteFriend(user_email, server=plex, allowSync=False)
        invite_token = invite.get("token")
        print(f"Invite sent successfully to {user_email}")
      
        send_email(user_email)

    except Exception as e:
        print(f"Failed to send invite: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send Plex invitation and email to a user.")
    parser.add_argument("user_email", type=str, help="Email address of the user to invite")
    args = parser.parse_args()

    send_plex_invitation(args.user_email)
