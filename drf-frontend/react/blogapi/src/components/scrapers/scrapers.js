import React,{useEffect,useState} from 'react';
import axiosInstance from '../../axios';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '56.25%', // 16:9
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},
	postTitle: {
		fontSize: '16px',
		textAlign: 'left',
	},
	postText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));

const Scrapers = () => {
	const classes = useStyles();
    const [scrapers,setScrapers] = useState();

    useEffect(()=> {
        axiosInstance.get(`scraper/`).then((res)=> {
            const allScrapers = res.data;
            setScrapers(allScrapers)
            console.log(res.data);
        },[setScrapers])
    });

    

	if (!scrapers || scrapers.length === 0) return <p>Can not find any Scrapers, sorry</p>;
	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Grid container spacing={5} alignItems="flex-end">
					{scrapers.map((scraper) => {
						return (
							// Enterprise card is full width at sm breakpoint
							<Grid item key={scraper.id} xs={12} md={4}>
								<Card className={classes.card}>
									<CardMedia
										className={classes.cardMedia}
										image="https://source.unsplash.com/random"
										title="Image title"
									/>
									<CardContent className={classes.cardContent}>
										<Typography
											gutterBottom
											variant="h6"
											component="h2"
											className={classes.postTitle}
										>
											{scraper.name}...
										</Typography>
										<div className={classes.postText}>
											<Typography color="textSecondary">
												{scraper.website}
											</Typography>
										</div>
                                        <div className={classes.postText}>
											<Typography color="textSecondary">
												{scraper.key_words}
											</Typography>
										</div>
                                        <div className={classes.postText}>
											<Typography color="textSecondary">
												{scraper.years}
											</Typography>
										</div>
									</CardContent>
								</Card>
							</Grid>
						);
					})}
				</Grid>
			</Container>
		</React.Fragment>
	);
};
export default Scrapers;
